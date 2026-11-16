"""Conta palavras de prosa (sem código), exemplos e exercícios por seção de um .dlt.

Uso: python contar.py arquivo.dlt
"""
import re
import sys

texto = open(sys.argv[1], encoding="utf-8").read()
sem_codigo = re.sub(r"<code\b.*?</code>", " ", texto, flags=re.S)
prosa = re.sub(r"<[^>]+>", " ", sem_codigo)
prosa = re.sub(r"\$\$[^$]*\$\$", " M ", prosa)
prosa = re.sub(r"\$[^$\n]*\$", " M ", prosa)
prosa = re.sub(r"<equations?\b.*?</equations?>", " ", prosa, flags=re.S)
palavras = len(re.findall(r"[A-Za-zÀ-ÿ]{2,}", prosa))
print(f"palavras de prosa (aprox.): {palavras}")
print(f"blocos de código: {len(re.findall(r'<code ', texto))} · figuras: {re.findall(r'<figure src=\"([^\"]+)\"', texto)}")
secoes = re.split(r'(?=<section id=")', texto)
for s in secoes[1:]:
    sid = re.match(r'<section id="([^"]+)"', s).group(1)
    tit = re.search(r"<title>(.*?)</title>", s)
    nex = len(re.findall(r"<example\b", s))
    ner = len(re.findall(r"<exercise\b", s))
    nsol = len(re.findall(r"<solution\b", s))
    nh = len(re.findall(r"<hint>", s))
    ncod = len(re.findall(r"<code ", s))
    print(f"  {sid:16} ex={nex} exr={ner} sol={nsol} hint={nh} code={ncod}  {tit.group(1) if tit else ''}")
titulos = re.findall(r'<exercise id="([^"]+)">\s*<title>([^<]*)', texto)
ruins = [t for t in titulos if not re.match(r"(Básico|Intermediário|Avançado) —", t[1])]
if ruins:
    print("títulos de exercício fora do padrão:", ruins)
