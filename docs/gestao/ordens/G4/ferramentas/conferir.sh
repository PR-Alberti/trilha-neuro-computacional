#!/bin/bash
# Uso: conferir.sh TT — compila o tema sozinho, conta avisos, acentos na matemática, palavras e compara saídas de código.
G=$HOME/trilha-neuro-computacional/docs/gestao/ordens/G4
PY=~/.local/share/venv-aulas/bin/python
cd ~/trilha-neuro-computacional/conteudo/modulo-08
echo "== build tema-$1"; delta build tema-$1.dlt -o $G/b$1.html 2>&1 | grep -v "→" | sort | uniq -c
$PY $G/ferramentas/acentos_math.py tema-$1.dlt | tail -3
$PY $G/ferramentas/contar.py tema-$1.dlt | head -2
$PY $G/ferramentas/rodar_codigo.py tema-$1.dlt 2>&1 | $PY -c "
import sys
txt=sys.stdin.read()
src=open('tema-$1.dlt').read()
for b in txt.split('='*70)[1:]:
    head=b.strip().split('\n')[0]
    real=[l.rstrip() for l in b.split('--- saída real:')[1].split('--- stderr')[0].strip().split('\n') if l.strip()]
    err=b.split('--- stderr:')[1].strip() if '--- stderr:' in b else ''
    falt=[r for r in real if ('# '+r.strip()) not in src and ('#'+r.strip()) not in src]
    ok = (not falt) and 'código de saída 0' in head
    print(head[:55], 'OK' if ok else 'DIVERGE')
    for r in falt: print('   sem comentário igual:', r[:150])
    if 'código de saída 0' not in head: print('   ERRO:', err[-400:])
"
