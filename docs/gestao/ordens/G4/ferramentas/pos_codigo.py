"""Mostra, para cada bloco <code lang="python">, as primeiras linhas de prosa após </code> que contêm números."""
import re, sys
t = open(sys.argv[1], encoding="utf-8").read()
for k, m in enumerate(re.finditer(r'<code\b[^>]*lang="python"[^>]*>.*?</code>', t, flags=re.S), 1):
    resto = t[m.end():m.end() + 3000]
    linhas = [l.strip() for l in resto.split("\n") if l.strip() and not l.strip().startswith("<")][:3]
    linha = t.count("\n", 0, m.end()) + 1
    print(f"BLOCO {k} (fim na linha {linha}):")
    for l in linhas:
        if re.search(r"\d", l):
            print("   ", l[:400])
