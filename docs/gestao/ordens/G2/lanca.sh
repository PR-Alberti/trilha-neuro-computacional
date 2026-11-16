#!/bin/bash
# uso: lanca.sh <arquivo-ordem> <nome-log> [modelo]
G2=$HOME/trilha-neuro-computacional/docs/gestao/ordens/G2
ORDEM="$1"; LOG="$G2/$2.log"; MODELO="${3:-gemini-4-hydrogen-high}"
cd ~/trilha-neuro-computacional && agy -p "$(cat "$ORDEM")" --model "$MODELO" --mode accept-edits > "$LOG" 2>&1; echo "exit $?" >> "$LOG"
