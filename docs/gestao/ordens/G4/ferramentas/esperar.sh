#!/bin/bash
# Uso: esperar.sh log1 log2 ... — espera até algum dos logs (nomes sem .log) ganhar a linha "exit".
G=$HOME/trilha-neuro-computacional/docs/gestao/ordens/G4
while true; do
  for f in "$@"; do
    if grep -q "^exit" $G/$f.log 2>/dev/null; then
      echo "$f: $(grep '^exit' $G/$f.log) quota=$(grep -c RESOURCE_EXHAUSTED $G/$f.log)"; exit 0
    fi
  done
  sleep 10
done
