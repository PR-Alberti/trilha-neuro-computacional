"""Extrai os blocos <code lang="python"> de um .dlt e roda cada um isolado.
uso: python rodar_codigo.py arquivo.dlt [indices...]
Mostra, para cada bloco, a linha inicial, o stdout/stderr e os comentários '# ' finais de linha."""
import re, subprocess, sys, tempfile, os
from pathlib import Path

arq = Path(sys.argv[1]).resolve()
sel = set(int(x) for x in sys.argv[2:])
txt = arq.read_text(encoding="utf-8")
padrao = re.compile(r'<code lang="(?:python|py)"[^>]*>(.*?)</code>', re.S)
py = Path.home() / ".local/share/venv-aulas/bin/python"
for i, m in enumerate(padrao.finditer(txt), 1):
    if sel and i not in sel:
        continue
    linha = txt.count("\n", 0, m.start()) + 1
    codigo = m.group(1)
    # remove indentação comum
    import textwrap
    codigo = textwrap.dedent(codigo.strip("\n"))
    print(f"===== BLOCO {i} (linha {linha}) =====")
    if "%%writefile" in codigo or codigo.lstrip().startswith("!") or "\n!" in codigo or "%timeit" in codigo or "%cd" in codigo:
        print("[contém mágica de notebook; adaptado]")
    # adapta %%writefile
    if codigo.lstrip().startswith("%%writefile"):
        primeira, resto = codigo.lstrip().split("\n", 1)
        nome = primeira.split()[1]
        codigo = f"open({nome!r}, 'w', encoding='utf-8').write({resto!r})\nprint('Writing {nome}')"
    codigo = "\n".join(("pass  # " + l) if l.lstrip().startswith(("!", "%")) else l for l in codigo.split("\n"))
    with tempfile.TemporaryDirectory() as d:
        env = dict(os.environ, MPLBACKEND="Agg", PYTHONHASHSEED="0")
        try:
            r = subprocess.run([str(py), "-c", codigo], cwd=d, capture_output=True, text=True, timeout=180, env=env)
            out = r.stdout + (("\n[STDERR]\n" + r.stderr[-2500:]) if r.returncode else "")
        except subprocess.TimeoutExpired:
            out = "[TIMEOUT]"
    print(out.rstrip())
