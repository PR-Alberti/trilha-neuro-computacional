"""Roda cada bloco python e mostra SÓ divergências: erros de execução, comentários exatos ausentes da saída,
e pares (aprox. esperado | linha real). uso: conferir.py arq.dlt"""
import re, sys, subprocess, tempfile, os, textwrap
from pathlib import Path
t=open(sys.argv[1],encoding="utf-8").read()
py=Path.home()/".local/share/venv-aulas/bin/python"
nb=0
for i,m in enumerate(re.finditer(r'<code lang="(?:python|py)"[^>]*>(.*?)</code>',t,re.S),1):
    nb+=1
    c=textwrap.dedent(m.group(1).strip("\n")); linha=t.count("\n",0,m.start())+1
    if c.lstrip().startswith("%%writefile"):
        p,resto=c.lstrip().split("\n",1); nome=p.split()[1]; c=f"open({nome!r},'w',encoding='utf-8').write({resto!r})"
    c="\n".join(("pass  # "+l) if l.lstrip().startswith(("!","%")) else l for l in c.split("\n"))
    with tempfile.TemporaryDirectory() as d:
        try:
            r=subprocess.run([str(py),"-c",c],cwd=d,capture_output=True,text=True,timeout=240,env=dict(os.environ,MPLBACKEND="Agg"))
        except subprocess.TimeoutExpired:
            print(f"[{i} l.{linha}] TIMEOUT"); continue
    out=r.stdout; outl=[l.strip() for l in out.split("\n") if l.strip()]
    if r.returncode:
        print(f"[{i} l.{linha}] ERRO: {r.stderr.strip().splitlines()[-1][:300]}"); continue
    lines=c.split("\n"); k=0; prob=[]
    for j,l in enumerate(lines):
        mm=re.search(r'#\s*(.*)$',l)
        if 'print(' in l and mm:
            exp=mm.group(1).strip()
            real=outl[k] if k<len(outl) else "<sem saída>"
            if re.match(r'(?i)(aprox|~|≈|por exemplo|varia|exemplo|saída varia|na ordem)',exp) or "aprox" in exp.lower():
                prob.append(f"  ~ esp: {exp[:110]} | real: {real[:110]}")
            elif exp not in out and exp.replace("Saída: ","") not in out:
                prob.append(f"  ! esp: {exp[:110]} | real: {real[:110]}")
            k+=1
        elif 'print(' in l:
            k+=1
    if prob: print(f"[{i} l.{linha}]"); print("\n".join(prob))
print(f"blocos: {nb}")
