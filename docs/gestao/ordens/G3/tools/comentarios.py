"""Para cada bloco python: saída real x comentários de saída esperada. uso: comentarios.py arq.dlt"""
import re, sys, subprocess, tempfile, os, textwrap
from pathlib import Path
t=open(sys.argv[1],encoding="utf-8").read()
py = Path.home() / ".local/share/venv-aulas/bin/python"
for i,m in enumerate(re.finditer(r'<code lang="(?:python|py)"[^>]*>(.*?)</code>',t,re.S),1):
    c=textwrap.dedent(m.group(1).strip("\n"))
    linha=t.count("\n",0,m.start())+1
    if c.lstrip().startswith("%%writefile"):
        p,resto=c.lstrip().split("\n",1); nome=p.split()[1]
        c=f"open({nome!r},'w',encoding='utf-8').write({resto!r})"
    c="\n".join(("pass  # "+l) if l.lstrip().startswith(("!","%")) else l for l in c.split("\n"))
    exp=[re.sub(r'^.*?#\s*','',l).strip() for l in c.split("\n") if re.search(r'(print\(|^\s*[A-Za-z_][\w\.\[\]"\']*\s*$|\)\s*$).*#|^\s*#\s*(Saída|saída|Sa[ií]da)',l) or re.match(r'^\s*#\s',l) and False]
    with tempfile.TemporaryDirectory() as d:
        try:
            r=subprocess.run([str(py),"-c",c],cwd=d,capture_output=True,text=True,timeout=180,env=dict(os.environ,MPLBACKEND="Agg"))
            out=r.stdout.rstrip()+("\n[ERRO] "+r.stderr.strip().split("\n")[-1] if r.returncode else "")
        except subprocess.TimeoutExpired: out="[TIMEOUT]"
    print(f"===== {i} (l.{linha})\n--- real:\n{out[:1500]}\n--- coment.:\n"+"\n".join(exp)[:1500])
