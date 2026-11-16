#!/bin/bash
# Roda as ordens de correção pendentes do G1 (3 em paralelo) quando a cota Gemini voltar.
G=$HOME/trilha-neuro-computacional/docs/gestao/ordens/G1
cd ~/trilha-neuro-computacional || exit 1
for t in 1-4 2-3 1-5; do
  agy -p "$(cat $G/correcao-$t.txt)" --model gemini-4-hydrogen-high --mode accept-edits > $G/pend-$t.log 2>&1; echo "exit $?" >> $G/pend-$t.log &
done
wait
agy -p "$(cat $G/correcao-1-3b.txt)" --model gemini-4-hydrogen-high --mode accept-edits > $G/pend-1-3b.log 2>&1; echo "exit $?" >> $G/pend-1-3b.log
for m in 01 02; do (cd conteudo/modulo-$m && (cd fig && for f in *.py; do MPLBACKEND=Agg ~/.local/share/venv-aulas/bin/python $f; done) && delta build project.toml && delta lint); done
