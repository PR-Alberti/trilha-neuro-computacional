import re, sys
def conta(s):
    s = re.sub(r'<code\b.*?</code>', ' ', s, flags=re.S)
    s = re.sub(r'\$\$.*?\$\$', ' M ', s, flags=re.S)
    s = re.sub(r'\$[^$]*\$', ' M ', s)
    s = re.sub(r'<[^>]+>', ' ', s)
    return len(re.findall(r'\w+', s))
for p in sys.argv[1:]:
    s = open(p, encoding="utf-8").read()
    partes = re.split(r'(?=<section id=")', s)
    tot = 0
    print(p)
    for parte in partes:
        m = re.match(r'<section id="([^"]+)"', parte)
        nome = m.group(1) if m else "abertura"
        n = conta(parte); tot += n
        ex = len(re.findall(r'<exercise', parte)); em = len(re.findall(r'<example', parte))
        print(f"  {nome:18s} {n:5d} palavras | {em} exemplos | {ex} exercícios")
    print(f"  TOTAL {tot}")
