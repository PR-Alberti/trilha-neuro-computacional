"""Camada de acesso ao banco de dados (SQLite).

SQLite guarda tudo num único arquivo (guia.db) — perfeito para pequena
escala e para aprender: dá para abrir o banco com `sqlite3 guia.db` no
terminal e inspecionar as tabelas com SQL puro.
"""
import pathlib
import sqlite3
from contextlib import contextmanager

CAMINHO_BANCO = pathlib.Path(__file__).resolve().parent / "guia.db"


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
            senha_hash TEXT    NOT NULL,
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
