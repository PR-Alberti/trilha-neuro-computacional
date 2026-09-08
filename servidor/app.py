"""API do Guia — FastAPI + SQLite.

Arquitetura (um processo só, sem CORS):

    navegador ──── fetch /api/... ────> esta API ────> SQLite (dados/guia.db)
        └───── GET /, /testes/... ────> arquivos estáticos do repositório

PILOTO: a identificação é só por e-mail, sem senha (ver seguranca.py).

Para rodar (a partir da pasta servidor/):

    uvicorn app:app --reload

Depois abra http://localhost:8000 — e http://localhost:8000/api/docs
para a documentação interativa da API (gerada automaticamente).
"""
import pathlib
import re
import time

from fastapi import Depends, FastAPI, HTTPException, Request, Response
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

import db
import seguranca

RAIZ_SITE = pathlib.Path(__file__).resolve().parent.parent
RE_EMAIL = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
RE_TEMA = re.compile(r"^\d{1,2}-\d{1,2}$")  # ex.: "3-2" = módulo 3, tema 2
NOME_COOKIE = "sessao"

app = FastAPI(title="API do Guia", docs_url="/api/docs", openapi_url="/api/openapi.json")

db.criar_tabelas()


# ---------- modelos de entrada (validados pelo FastAPI/Pydantic) ----------

class Identificacao(BaseModel):
    email: str


class PedidoSincronizacao(BaseModel):
    temas: list[str]


# ---------- infraestrutura ----------

def usuario_atual(request: Request):
    """Lê o cookie de sessão e devolve o usuário logado, ou None."""
    token = request.cookies.get(NOME_COOKIE)
    if not token:
        return None
    with db.conectar() as con:
        return seguranca.usuario_da_sessao(con, token)


def exigir_usuario(request: Request):
    usuario = usuario_atual(request)
    if usuario is None:
        raise HTTPException(401, "Identifique-se com seu e-mail para continuar.")
    return usuario


def abrir_sessao(resposta: Response, usuario_id: int):
    with db.conectar() as con:
        token = seguranca.criar_sessao(con, usuario_id)
    # HttpOnly: o JavaScript da página não consegue ler o cookie (anti-XSS)
    # SameSite=Lax: outros sites não conseguem disparar requisições logadas (anti-CSRF)
    resposta.set_cookie(NOME_COOKIE, token, httponly=True, samesite="lax",
                        max_age=seguranca.DURACAO_SESSAO, path="/")


# ---------- identificação ----------

@app.post("/api/entrar")
def entrar(ident: Identificacao, resposta: Response):
    """Identifica pelo e-mail — cria o registro na primeira vez.

    Sem senha: não há "entrar" e "registrar" separados, e nunca há erro de
    credencial. Ver a nota do piloto em seguranca.py.
    """
    email = ident.email.strip().lower()
    if not RE_EMAIL.match(email):
        raise HTTPException(400, "E-mail inválido.")
    with db.conectar() as con:
        con.execute(
            "INSERT OR IGNORE INTO usuarios (email, criado_em) VALUES (?, ?)",
            (email, int(time.time())),
        )
        linha = con.execute("SELECT id FROM usuarios WHERE email = ?", (email,)).fetchone()
        seguranca.limpar_sessoes_vencidas(con)  # faxina oportunista
    abrir_sessao(resposta, linha["id"])
    return {"email": email}


@app.post("/api/sair", status_code=204)
def sair(request: Request, resposta: Response):
    token = request.cookies.get(NOME_COOKIE)
    if token:
        with db.conectar() as con:
            seguranca.encerrar_sessao(con, token)
    resposta.delete_cookie(NOME_COOKIE, path="/")


@app.get("/api/eu")
def eu(usuario=Depends(exigir_usuario)):
    return {"email": usuario["email"]}


# ---------- progresso ----------

def validar_tema(tema: str):
    if not RE_TEMA.match(tema):
        raise HTTPException(400, "Identificador de tema inválido (esperado M-T, ex.: 3-2).")


@app.get("/api/progresso")
def ver_progresso(usuario=Depends(exigir_usuario)):
    with db.conectar() as con:
        linhas = con.execute(
            "SELECT tema FROM progresso WHERE usuario_id = ? ORDER BY tema",
            (usuario["id"],),
        ).fetchall()
    return {"temas": [linha["tema"] for linha in linhas]}


@app.put("/api/progresso/{tema}", status_code=204)
def marcar(tema: str, usuario=Depends(exigir_usuario)):
    validar_tema(tema)
    with db.conectar() as con:
        con.execute(
            "INSERT OR IGNORE INTO progresso (usuario_id, tema, marcado_em) VALUES (?, ?, ?)",
            (usuario["id"], tema, int(time.time())),
        )


@app.delete("/api/progresso/{tema}", status_code=204)
def desmarcar(tema: str, usuario=Depends(exigir_usuario)):
    validar_tema(tema)
    with db.conectar() as con:
        con.execute(
            "DELETE FROM progresso WHERE usuario_id = ? AND tema = ?",
            (usuario["id"], tema),
        )


@app.post("/api/progresso/sincronizar")
def sincronizar(pedido: PedidoSincronizacao, usuario=Depends(exigir_usuario)):
    """União do progresso local (enviado) com o da conta — ninguém perde nada."""
    agora = int(time.time())
    with db.conectar() as con:
        for tema in pedido.temas:
            validar_tema(tema)
            con.execute(
                "INSERT OR IGNORE INTO progresso (usuario_id, tema, marcado_em) VALUES (?, ?, ?)",
                (usuario["id"], tema, agora),
            )
        linhas = con.execute(
            "SELECT tema FROM progresso WHERE usuario_id = ?", (usuario["id"],)
        ).fetchall()
    return {"temas": sorted(linha["tema"] for linha in linhas)}


# ---------- site estático ----------
# Lista do que pode ser baixado, em vez de publicar a raiz do repositório
# inteira: assim servidor/ (que guarda o banco), .git/ e qualquer arquivo
# novo na raiz ficam de fora por padrão, sem depender de a gente lembrar
# de bloqueá-los. Para publicar um arquivo novo, acrescente-o aqui.

@app.get("/", include_in_schema=False)
def pagina():
    return FileResponse(RAIZ_SITE / "index.html")


@app.get("/Guia.pdf", include_in_schema=False)
def guia_pdf():
    return FileResponse(RAIZ_SITE / "Guia.pdf")


app.mount("/testes", StaticFiles(directory=RAIZ_SITE / "testes"), name="testes")
