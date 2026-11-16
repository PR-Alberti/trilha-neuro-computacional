#!/bin/bash
# uso: mkrev.sh NN TT  -> cria ordem-revisao-mN-tTT.txt com a lista de seções da spec
G=$HOME/trilha-neuro-computacional/docs/gestao/ordens/G3
N=${1#0}; O=$G/ordem-revisao-m$N-t$2.txt
sed "s/modulo-NN/modulo-$1/g; s/tema-TT/tema-$2/g" $G/revisor-modelo.txt > $O
printf '\nSeções que a aula deveria cobrir (definidas pelo gestor), com o conteúdo esperado:\n' >> $O
grep -E '^[0-9]\. sec:' $G/spec/m$N-t$2.txt >> $O
echo $O
