"""Conta palavras de prosa (sem matemática nem código) de aulas .dlt."""
import re
import sys

for f in sys.argv[1:]:
    s = open(f, encoding="utf-8").read()
    s = re.sub(r"<code[^>]*>.*?</code>", " ", s, flags=re.S)
    s = re.sub(r"\$\$.*?\$\$", " ", s, flags=re.S)
    s = re.sub(r"<equations?[^>]*>.*?</equations?>", " ", s, flags=re.S)
    s = re.sub(r"\$[^$]*\$", " X ", s)
    s = re.sub(r"<[^>]+>", " ", s)
    print(f, len(s.split()))
