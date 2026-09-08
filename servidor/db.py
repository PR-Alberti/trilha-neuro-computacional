"""Camada de acesso ao banco de dados (SQLite).

SQLite guarda tudo num único arquivo (guia.db) — perfeito para pequena
escala e para aprender: dá para abrir o banco com `sqlite3 dados/guia.db` no
terminal e inspecionar as tabelas com SQL puro.
"""
import pathlib
import sqlite3
from contextlib import contextmanager

# fora da árvore publicada pelo servidor (ver RAIZ_SITE em app.py): um
# arquivo com e-mails e tokens de sessão não pode ser baixável pela web
CAMINHO_BANCO = pathlib.Path(__file__).resolve().parent / "dados" / "guia.db"
CAMINHO_BANCO.parent.mkdir(exist_ok=True)


@contextmanager
def conectar():
    """Abre uma conexão que faz commit no sucesso e sempre fecha no final.

    Uso:
        with conectar() as con:
            con.execute(...)
    """
    con = sqlite3.connect(CAMINHO_BANCO)
    con.row_factory = sqlite3.Row  # linhas acessíveis por nome: linha["email"]
    con.execute("PRAGMA foreign_keys = ON")
    try:
        yield con
        con.commit()
    finally:
        con.close()


def criar_tabelas():
    with conectar() as con:
        con.executescript("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id         INTEGER PRIMARY KEY,
            email      TEXT    NOT NULL UNIQUE,
            criado_em  INTEGER NOT NULL
        );

        CREATE TABLE IF NOT EXISTS sessoes (
            token      TEXT    PRIMARY KEY,
            usuario_id INTEGER NOT NULL REFERENCES usuarios(id) ON DELETE CASCADE,
            expira_em  INTEGER NOT NULL
        );

        CREATE TABLE IF NOT EXISTS progresso (
            usuario_id INTEGER NOT NULL REFERENCES usuarios(id) ON DELETE CASCADE,
            tema       TEXT    NOT NULL,
            marcado_em INTEGER NOT NULL,
            PRIMARY KEY (usuario_id, tema)
        );
        """)
        # bancos criados na versão com senha ainda têm a coluna senha_hash
        # (NOT NULL), que quebraria os INSERTs de agora — some com ela.
        colunas = {linha["name"] for linha in con.execute("PRAGMA table_info(usuarios)")}
        if "senha_hash" in colunas:
            con.execute("ALTER TABLE usuarios DROP COLUMN senha_hash")
