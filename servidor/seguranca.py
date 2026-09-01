"""Senhas e sessões.

Senhas nunca são guardadas em texto: guardamos apenas scrypt(senha, sal).
O scrypt vem na biblioteca padrão do Python e é caro de calcular de
propósito — é isso que torna força bruta impraticável mesmo se o banco
vazar. O sal (aleatório por usuário) impede tabelas pré-computadas.

Sessões são "server-side": o navegador guarda só um token opaco num
cookie; quem manda é a linha correspondente na tabela `sessoes` — apagar
a linha encerra a sessão na hora.
"""
import hashlib
import hmac
import secrets
import time

DURACAO_SESSAO = 30 * 24 * 3600  # 30 dias, em segundos

# custo do scrypt (n = iterações; dobrar n dobra o trabalho do atacante)
_PARAMETROS = dict(n=2**14, r=8, p=1, dklen=32)


def gerar_hash_senha(senha: str) -> str:
    sal = secrets.token_bytes(16)
    resumo = hashlib.scrypt(senha.encode(), salt=sal, **_PARAMETROS)
    return f"scrypt${sal.hex()}${resumo.hex()}"


def verificar_senha(senha: str, guardado: str) -> bool:
    try:
        _, sal_hex, resumo_hex = guardado.split("$")
    except ValueError:
        return False
    resumo = hashlib.scrypt(senha.encode(), salt=bytes.fromhex(sal_hex), **_PARAMETROS)
    # compare_digest evita "timing attacks" (medir o tempo da comparação)
    return hmac.compare_digest(resumo.hex(), resumo_hex)


def criar_sessao(con, usuario_id: int) -> str:
    token = secrets.token_urlsafe(32)
    con.execute(
        "INSERT INTO sessoes (token, usuario_id, expira_em) VALUES (?, ?, ?)",
        (token, usuario_id, int(time.time()) + DURACAO_SESSAO),
    )
    return token


def usuario_da_sessao(con, token: str):
    """Devolve a linha do usuário dono do token, ou None se inválido/vencido."""
    return con.execute(
        """SELECT u.* FROM sessoes s
           JOIN usuarios u ON u.id = s.usuario_id
           WHERE s.token = ? AND s.expira_em > ?""",
        (token, int(time.time())),
    ).fetchone()


def encerrar_sessao(con, token: str):
    con.execute("DELETE FROM sessoes WHERE token = ?", (token,))


def limpar_sessoes_vencidas(con):
    con.execute("DELETE FROM sessoes WHERE expira_em <= ?", (int(time.time()),))
