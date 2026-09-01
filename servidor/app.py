"""API do Guia — FastAPI + SQLite.

Arquitetura (um processo só, sem CORS):

    navegador ──── fetch /api/... ────> esta API ────> SQLite (guia.db)
        └───── GET /, /testes/... ────> arquivos estáticos do repositório

Para rodar (a partir da pasta servidor/):

    uvicorn app:app --reload

Depois abra http://localhost:8000 — e http://localhost:8000/api/docs
para a documentação interativa da API (gerada automaticamente).
"""
import pathlib
import re
import sqlite3
import time

from fastapi import Depends, FastAPI, HTTPException, Request, Response
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

class Credenciais(BaseModel):
    email: str
    senha: str


class PedidoSincronizacao(BaseModel):
    temas: list[str]


# ---------- infraestrutura ----------

@app.middleware("http")
async def bloquear_arquivos_ocultos(request: Request, chamar_proximo):
    # o servidor estático serve a raiz do repositório; nunca exponha
    # pastas "escondidas" como .git/ ou .venv/
    if any(parte.startswith(".") for parte in request.url.path.split("/") if parte):
        return Response(status_code=404)
    return await chamar_proximo(request)


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
        raise HTTPException(401, "Faça login para continuar.")
    return usuario


def abrir_sessao(resposta: Response, usuario_id: int):
    with db.conectar() as con:
        token = seguranca.criar_sessao(con, usuario_id)
    # HttpOnly: o JavaScript da página não consegue ler o cookie (anti-XSS)
    # SameSite=Lax: outros sites não conseguem disparar requisições logadas (anti-CSRF)
    resposta.set_cookie(NOME_COOKIE, token, httponly=True, samesite="lax",
                        max_age=seguranca.DURACAO_SESSAO, path="/")


# ---------- conta ----------

@app.post("/api/registrar", status_code=201)
def registrar(cred: Credenciais, resposta: Response):
    email = cred.email.strip().lower()
    if not RE_EMAIL.match(email):
        raise HTTPException(400, "E-mail inválido.")
    if len(cred.senha) < 8:
        raise HTTPException(400, "A senha precisa de pelo menos 8 caracteres.")
    with db.conectar() as con:
        try:
            cursor = con.execute(
                "INSERT INTO usuarios (email, senha_hash, criado_em) VALUES (?, ?, ?)",
                (email, seguranca.gerar_hash_senha(cred.senha), int(time.time())),
            )
        except sqlite3.IntegrityError:
            raise HTTPException(409, "Já existe uma conta com esse e-mail.")
        usuario_id = cursor.lastrowid
    abrir_sessao(resposta, usuario_id)
    return {"email": email}


@app.post("/api/entrar")
def entrar(cred: Credenciais, resposta: Response):
    email = cred.email.strip().lower()
    with db.conectar() as con:
        linha = con.execute("SELECT * FROM usuarios WHERE email = ?", (email,)).fetchone()
        seguranca.limpar_sessoes_vencidas(con)  # faxina oportunista
    # mensagem única de propósito: não revele se o e-mail existe ou não
    if linha is None or not seguranca.verificar_senha(cred.senha, linha["senha_hash"]):
        raise HTTPException(401, "E-mail ou senha incorretos.")
    abrir_sessao(resposta, linha["id"])
    return {"email": linha["email"]}


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


# ---------- site estático (montado por último: /api/* tem prioridade) ----------

app.mount("/", StaticFiles(directory=RAIZ_SITE, html=True), name="site")
