"""Extrai os blocos <code lang="python"> de um .dlt e executa cada um isoladamente.
Uso: python rodar_codigo.py <arquivo.dlt> <pasta_saida> [indices...]"""
import re, sys, subprocess, time, html, os
from pathlib import Path

PY = os.path.expanduser("~/.local/share/venv-aulas/bin/python")
src = Path(sys.argv[1]).read_text(encoding="utf-8")
out = Path(sys.argv[2]); out.mkdir(parents=True, exist_ok=True)
sel = set(int(i) for i in sys.argv[3:])
pat = re.compile(r'<code\s+([^>]*lang="(?:python|py)"[^>]*)>(.*?)</code>', re.S)
for i, m in enumerate(pat.finditer(src), 1):
    if sel and i not in sel:
        continue
    attrs, body = m.group(1), m.group(2)
    idm = re.search(r'id="([^"]+)"', attrs)
    line = src[:m.start()].count("\n") + 1
    f = out / f"bloco{i:02d}.py"
    f.write_text(body, encoding="utf-8")
    t0 = time.time()
    try:
        r = subprocess.run([PY, str(f)], capture_output=True, text=True, timeout=240,
                           env={**os.environ, "MPLBACKEND": "Agg", "OMP_NUM_THREADS": "2", "MKL_NUM_THREADS": "2"}, cwd=str(out))
        rc, so, se = r.returncode, r.stdout, r.stderr
    except subprocess.TimeoutExpired:
        rc, so, se = "TIMEOUT", "", ""
    dt = time.time() - t0
    print(f"===== bloco {i} ({idm.group(1) if idm else 'sem id'}, linha {line}) rc={rc} t={dt:.1f}s")
    print(so[-2500:])
    if se.strip():
        print("--- stderr:", se[-1500:])
