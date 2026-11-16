#!/bin/bash
# uso: agy.sh <arquivo-ordem> <arquivo-log> [modelo]
ORDEM="$1"; LOG="$2"; MODELO="${3:-gemini-4-hydrogen-high}"
cd ~/trilha-neuro-computacional && agy -p "$(cat "$ORDEM")" --model "$MODELO" --mode accept-edits > "$LOG" 2>&1; echo "exit $?" >> "$LOG"
