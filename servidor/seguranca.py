"""Sessões.

PILOTO: não há senha. A pessoa se identifica pelo e-mail e o servidor
guarda apenas quais temas ela marcou como estudados — nada além disso.
Isso significa que *qualquer um* que digite o e-mail de outra pessoa vê o
progresso dela. É uma escolha consciente para esta fase; antes de abrir o
piloto para além de quem você conhece, troque por autenticação de verdade
(link mágico por e-mail, ou e-mail + senha com hash).

Sessões são "server-side": o navegador guarda só um token opaco num
cookie; quem manda é a linha correspondente na tabela `sessoes` — apagar
a linha encerra a sessão na hora.
"""
import secrets
import time

DURACAO_SESSAO = 30 * 24 * 3600  # 30 dias, em segundos


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
