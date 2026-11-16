#!/bin/bash
# uso: espera.sh log1 log2 ... ; espera até algum ter "exit" (máx ~9,5 min)
G=$HOME/trilha-neuro-computacional/docs/gestao/ordens/G5
for i in $(seq 1 57); do for l in "$@"; do grep -q "^exit" $G/$l.log 2>/dev/null && { grep -H "^exit\|RESOURCE" $G/$l.log | cut -c1-200; done_=1; }; done; [ -n "$done_" ] && exit 0; sleep 10; done; echo "nenhum terminou ainda"
