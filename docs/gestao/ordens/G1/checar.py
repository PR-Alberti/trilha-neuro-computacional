"""Checagens estruturais rápidas de uma aula .dlt (complementa o delta lint).

Uso: python checar.py caminho/tema-TT.dlt
"""
import re
import sys
from pathlib import Path

src = Path(sys.argv[1]).read_text(encoding="utf-8")
print(f"bytes: {len(src.encode('utf-8'))}")
prosa = re.sub(r"<code[^>]*>.*?</code>", " ", src, flags=re.S)
prosa = re.sub(r"<[^>]+>", " ", prosa)
print(f"palavras (aprox., inclui LaTeX): {len(prosa.split())}")

secs = re.findall(r'<section id="([^"]+)"', src)
print("seções:", secs)

# exercícios: dica e solução
for m in re.finditer(r'<exercise id="([^"]+)">(.*?)</exercise>', src, flags=re.S):
    eid, body = m.group(1), m.group(2)
    t = re.search(r"<title>(.*?)</title>", body)
    titulo = t.group(1) if t else "(sem título)"
    falta = []
    if "<hint" not in body:
        falta.append("hint")
    if "<solution" not in body:
        falta.append("solution")
    if not re.match(r"(Básico|Intermediário|Avançado) —", titulo):
        falta.append("título fora do padrão")
    if falta:
        print(f"  EXERCÍCIO {eid}: falta {falta} | {titulo}")

# contagem por seção
for i, m in enumerate(re.finditer(r'<section id="([^"]+)">(.*?)</section>', src, flags=re.S)):
    sid, body = m.group(1), m.group(2)
    ne = body.count("<example ")
    nx = body.count("<exercise ")
    nr = body.count("Armadilha comum")
    print(f"  {sid}: exemplos={ne} exercícios={nx} armadilhas={nr}")

ids = re.findall(r'\bid="([^"]+)"', src)
dup = {i for i in ids if ids.count(i) > 1}
if dup:
    print("IDS DUPLICADOS:", dup)
refs = set(re.findall(r'<ref to="([^"]+)"', src))
print("refs:", sorted(refs))
print("figuras:", re.findall(r'<figure src="([^"]+)"', src))
print("links:", sorted(set(re.findall(r'<link to="([^"]+)"', src))))
proib = [t for t in ("<interactive", "<cite", "<bibliography", "<youtube", "<p>") if t in src]
if proib:
    print("PROIBIDOS:", proib)
print("blocos de código python:", len(re.findall(r'<code lang="python"', src)))
