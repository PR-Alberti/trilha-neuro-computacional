import re, sys
for p in sys.argv[1:]:
    s = open(p, encoding="utf-8").read()
    s = re.sub(r'<code\b.*?</code>', ' ', s, flags=re.S)
    s = re.sub(r'\$\$.*?\$\$', ' M ', s, flags=re.S)
    s = re.sub(r'\$[^$]*\$', ' M ', s)
    s = re.sub(r'<[^>]+>', ' ', s)
    w = re.findall(r'\w+', s)
    print(p, len(w), "palavras de prosa (fórmulas contam como 1)")
