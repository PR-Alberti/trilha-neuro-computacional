"""Roda vários blocos python de um .dlt na MESMA pasta temporária, em sequência (para blocos que dependem de arquivos criados antes).
uso: python rodar_seq.py arquivo.dlt i j k"""
import re, subprocess, sys, tempfile, os, textwrap
from pathlib import Path
arq = Path(sys.argv[1]).resolve(); sel = [int(x) for x in sys.argv[2:]]
txt = arq.read_text(encoding="utf-8")
blocos = [textwrap.dedent(m.group(1).strip("\n")) for m in re.finditer(r'<code lang="(?:python|py)"[^>]*>(.*?)</code>', txt, re.S)]
py = Path.home() / ".local/share/venv-aulas/bin/python"
with tempfile.TemporaryDirectory() as d:
    for i in sel:
        c = blocos[i-1]
        if c.lstrip().startswith("%%writefile"):
            p, resto = c.lstrip().split("\n", 1); nome = p.split()[1]
            Path(d, nome).write_text(resto + "\n", encoding="utf-8"); print(f"== {i}: wrote {nome}"); continue
        c = "\n".join(("pass  # " + l) if l.lstrip().startswith(("!", "%")) else l for l in c.split("\n"))
        r = subprocess.run([str(py), "-c", c], cwd=d, capture_output=True, text=True, timeout=180, env=dict(os.environ, MPLBACKEND="Agg"))
        print(f"== {i}:\n{r.stdout.rstrip()}" + (f"\n[STDERR]\n{r.stderr[-2000:]}" if r.returncode else ""))
