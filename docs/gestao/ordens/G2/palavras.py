import re, sys
for fn in sys.argv[1:]:
    s = open(fn, encoding='utf-8').read()
    s = re.sub(r'<code[^>]*>.*?</code>', ' ', s, flags=re.S)
    s = re.sub(r'\$\$.*?\$\$', ' ', s, flags=re.S)
    s = re.sub(r'<equations?[^>]*>.*?</equations?>', ' ', s, flags=re.S)
    s = re.sub(r'\$[^$]*\$', '  ', s)
    s = re.sub(r'<[^>]+>', ' ', s)
    w = [x for x in s.split() if re.search(r'[A-Za-zÀ-ú]', x)]
    print(f"{fn}: {len(w)} palavras de prosa")
