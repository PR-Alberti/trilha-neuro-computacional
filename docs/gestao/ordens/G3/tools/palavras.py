"""Conta palavras de prosa de um .dlt (sem código, sem tags, sem matemática). uso: python palavras.py arq.dlt"""
import re, sys
t = open(sys.argv[1], encoding="utf-8").read()
t = re.sub(r"<code[^>]*>.*?</code>", " ", t, flags=re.S)
t = re.sub(r"\$\$.*?\$\$", " ", t, flags=re.S)
t = re.sub(r"\$[^$]*\$", " M ", t)
t = re.sub(r"<[^>]+>", " ", t)
print(len(re.findall(r"\w+", t)))
