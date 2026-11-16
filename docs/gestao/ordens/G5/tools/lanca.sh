#!/bin/bash
# uso: lanca.sh <ordem.txt> <modelo> <nome-log>
G=$HOME/trilha-neuro-computacional/docs/gestao/ordens/G5
cd ~/trilha-neuro-computacional && agy -p "$(cat $G/$1)" --model $2 --mode accept-edits > $G/$3.log 2>&1; echo "exit $?" >> $G/$3.log
