"""Lista trechos de matemática com letras acentuadas fora de \\text{...}.

Percorre o texto (sem <code> e <c>) alternando dentro/fora da matemática a cada $ ou $$
não escapado, e também olha <equation>, <equations> e <m>.
Uso: python acentos_math.py arquivo.dlt
"""
import re
import sys

texto = open(sys.argv[1], encoding="utf-8").read()
t = re.sub(r"<code\b.*?</code>", lambda m: "\n" * m.group(0).count("\n"), texto, flags=re.S)
t = re.sub(r"<c>.*?</c>", "", t)


def ruim(trecho):
    limpo = re.sub(r"\\text\{(?:[^{}]|\{[^{}]*\})*\}", "", trecho)
    return re.search(r"[À-ÿ]", limpo)


achados = []
for m in re.finditer(r"<(equations?|m)\b[^>]*>(.*?)</\1>", t, flags=re.S):
    if ruim(m.group(2)):
        achados.append((t.count("\n", 0, m.start()) + 1, m.group(2).strip()[:140]))
t2 = re.sub(r"<(equations?|m)\b[^>]*>.*?</\1>", lambda m: "\n" * m.group(0).count("\n"), t, flags=re.S)
i, dentro, ini, n = 0, False, 0, len(t2)
while i < n:
    if t2[i] == "\\" and i + 1 < n and t2[i + 1] == "$":
        i += 2
        continue
    if t2[i] == "$":
        passo = 2 if t2[i:i + 2] == "$$" else 1
        if dentro:
            trecho = t2[ini:i]
            if ruim(trecho):
                achados.append((t2.count("\n", 0, ini) + 1, trecho.strip()[:140]))
            dentro = False
        else:
            dentro, ini = True, i + passo
        i += passo
        continue
    i += 1
for linha, tr in sorted(set(achados)):
    print(f"linha {linha}: {tr}")
print(f"total: {len(set(achados))}")
