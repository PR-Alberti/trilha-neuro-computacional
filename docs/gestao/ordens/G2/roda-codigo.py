# uso: python -I roda-codigo.py arquivo.dlt  -> extrai blocos <code lang="python"> e roda cada um
import re, sys, subprocess, os, tempfile
fn = sys.argv[1]
s = open(fn, encoding='utf-8').read()
blocos = [(m.start(), m.group(1)) for m in re.finditer(r'<code lang="python"[^>]*>(.*?)</code>', s, flags=re.S)]
py = os.path.expanduser('~/.local/share/venv-aulas/bin/python')
for k, (pos, cod) in enumerate(blocos, 1):
    linha = s.count('\n', 0, pos) + 1
    with tempfile.NamedTemporaryFile('w', suffix='.py', delete=False) as f:
        f.write(cod); nome = f.name
    r = subprocess.run([py, nome], capture_output=True, text=True, timeout=120, env={**os.environ, 'MPLBACKEND': 'Agg'})
    print(f"===== bloco {k} (linha {linha}) exit={r.returncode}")
    esperadas = re.findall(r'#\s*sa[ií]da[^:]*:\s*(.*)', cod)
    print("--- saída real:"); print(r.stdout.rstrip()[:3000])
    if r.stderr.strip(): print("--- stderr:"); print(r.stderr.strip()[-1500:])
    print("--- comentários de saída:"); print("\n".join(esperadas)[:2000])
