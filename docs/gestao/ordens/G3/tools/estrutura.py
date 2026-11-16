"""Resumo estrutural de um .dlt: por seção, nº de exemplos, exercícios, hints, soluções, armadilhas, códigos, figuras."""
import re, sys
t = open(sys.argv[1], encoding="utf-8").read()
semcod = re.sub(r"(<code[^>]*>)(.*?)(</code>)", lambda m: m.group(1) + "X" * 0 + m.group(3), t, flags=re.S)
secs = [(m.start(), m.group(1)) for m in re.finditer(r'<section id="([^"]+)"', semcod)]
secs.append((len(semcod), "FIM"))
print("titulo cap:", re.search(r"<chapter[^>]*>\s*<title>(.*?)</title>", semcod).group(1))
for (a, sid), (b, _) in zip(secs, secs[1:]):
    s = semcod[a:b]
    tit = re.search(r"<title>(.*?)</title>", s).group(1)
    exs = re.findall(r"<exercise id=\"([^\"]+)\">\s*<title>(.*?)</title>", s)
    bad = []
    for m in re.finditer(r"<exercise id=\"([^\"]+)\">(.*?)</exercise>", s, re.S):
        if "<hint" not in m.group(2) or "<solution" not in m.group(2):
            bad.append(m.group(1))
    print(f"{sid:16s} {tit[:45]:45s} ex={s.count('<example')} exr={len(exs)} arm={len(re.findall('Armadilha comum', s))} def={s.count('<definition')} prop={s.count('<proposition')+s.count('<theorem')} code={s.count('<code')} fig={s.count('<figure')} semHS={bad}")
    for i, tt in exs:
        if not re.match(r"(Básico|Intermediário|Avançado) —", tt):
            print("   título fora do padrão:", i, tt)
ids = re.findall(r'\bid="([^"]+)"', semcod)
dup = {i for i in ids if ids.count(i) > 1}
print("ids duplicados:", dup or "nenhum")
refs = set(re.findall(r'<ref to="([^"]+)"', semcod))
print("refs sem alvo:", (refs - set(ids)) or "nenhuma")
print("figuras:", re.findall(r'<figure src="([^"]+)"', semcod))
print("links:", sorted(set(re.findall(r'<link to="([^"]+)"', semcod))))
print("proibidos:", [x for x in ("<interactive", "<cite", "<bibliography", "<youtube") if x in semcod] or "nenhum")
