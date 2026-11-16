"""Extrai os blocos <code lang="python"> de um .dlt, executa cada um isolado e
mostra, para cada print, o comentário esperado ao lado da saída real.

Uso: python rodar_codigo.py arquivo.dlt [--so N] [--timeout S]
"""
import os
import re
import subprocess
import sys
import tempfile

PY = os.path.expanduser("~/.local/share/venv-aulas/bin/python")


def blocos(texto):
    padrao = re.compile(r'<code\b([^>]*)>(.*?)</code>', re.S)
    for m in padrao.finditer(texto):
        attrs, corpo = m.group(1), m.group(2)
        lang = re.search(r'lang="([^"]+)"', attrs)
        if not lang or lang.group(1) not in ("python", "py"):
            continue
        linha = texto.count("\n", 0, m.start()) + 1
        yield linha, corpo


def main():
    arq = sys.argv[1]
    so = None
    timeout = 120
    if "--so" in sys.argv:
        so = int(sys.argv[sys.argv.index("--so") + 1])
    if "--timeout" in sys.argv:
        timeout = int(sys.argv[sys.argv.index("--timeout") + 1])
    texto = open(arq, encoding="utf-8").read()
    env = dict(os.environ, MPLBACKEND="Agg", PYTHONWARNINGS="default")
    todos = list(blocos(texto))
    print(f"{arq}: {len(todos)} blocos python")
    for k, (linha, corpo) in enumerate(todos, 1):
        if so is not None and k != so:
            continue
        with tempfile.TemporaryDirectory() as d:
            caminho = os.path.join(d, "bloco.py")
            with open(caminho, "w", encoding="utf-8") as f:
                f.write(corpo)
            try:
                r = subprocess.run([PY, "-I", caminho], cwd=d, env=env,
                                   capture_output=True, text=True, timeout=timeout)
                out, err, rc = r.stdout, r.stderr, r.returncode
            except subprocess.TimeoutExpired:
                out, err, rc = "", "TIMEOUT", -1
        esperados = []
        linhas = corpo.split("\n")
        for i, l in enumerate(linhas):
            if "print(" in l:
                coment = []
                j = i + 1
                while j < len(linhas) and linhas[j].strip().startswith("#"):
                    coment.append(linhas[j].strip())
                    j += 1
                inline = l.split("#", 1)[1].strip() if "#" in l and not l.strip().startswith("#") and l.count('"') % 2 == 0 else ""
                esperados.append((l.strip(), (["# " + inline] if inline else []) + coment))
        print("=" * 70)
        print(f"BLOCO {k} (linha {linha} do .dlt) — código de saída {rc}")
        print("--- comentários esperados:")
        for p, c in esperados:
            print("   ", p[:90])
            for cc in c:
                print("        ", cc[:110])
        print("--- saída real:")
        print(out.rstrip()[:4000])
        err_util = "\n".join(l for l in err.splitlines() if l.strip())
        if err_util:
            print("--- stderr:")
            print(err_util[-2500:])


if __name__ == "__main__":
    main()
