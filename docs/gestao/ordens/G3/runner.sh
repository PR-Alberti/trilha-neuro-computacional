#!/bin/bash
# Fila de chamadas agy (máx. 3 simultâneas). Linhas da fila: ordem|log|modelo
# Flags: ESGOTADO-<modelo> contém o epoch do reset; enquanto valer, jobs desse modelo esperam na fila.
G=$HOME/trilha-neuro-computacional/docs/gestao/ordens/G3
Q=$G/fila.txt; R=$G/rodando.txt; E=$G/eventos.log
touch $Q $R $E
esgotado() { local f=$G/ESGOTADO-$1; [ -f $f ] || return 1; [ $(date +%s) -lt $(cat $f) ] && return 0; rm -f $f; echo "RESET $1 $(date +%H:%M)" >> $E; return 1; }
while true; do
  while IFS='|' read -r log modelo; do
    [ -z "$log" ] && continue
    if grep -q "^exit" "$log" 2>/dev/null; then
      ex=$(grep -c RESOURCE_EXHAUSTED "$log")
      grep -v "^$log|" $R > $R.tmp; mv $R.tmp $R
      if [ "$ex" -gt 0 ]; then
        r=$(grep -o "Resets in [0-9hms]*" "$log" | head -1 | sed 's/Resets in //')
        h=$(echo $r | grep -o "[0-9]*h" | tr -d h); m=$(echo $r | grep -o "[0-9]*m" | tr -d m)
        echo $(( $(date +%s) + ${h:-0}*3600 + ${m:-0}*60 + 120 )) > $G/ESGOTADO-$modelo
      fi
      echo "FIM $(basename $log .log) [$modelo] $(tail -1 $log) esgotado=$ex" >> $E
    fi
  done < <(cat $R)
  n=$(grep -c . $R)
  [ -f $G/PARAR ] && { sleep 20; continue; }
  while [ "$n" -lt 3 ]; do
    pick=""; ln=0
    while IFS= read -r linha; do
      ln=$((ln+1)); [ -z "$linha" ] && continue
      modelo=${linha##*|}
      esgotado $modelo && continue
      pick=$linha; break
    done < $Q
    [ -z "$pick" ] && break
    sed -i "${ln}d" $Q
    ordem=${pick%%|*}; resto=${pick#*|}; log=${resto%%|*}; modelo=${resto#*|}
    [ -f "$log" ] && mv "$log" "$log.ant"
    nohup $G/agy.sh "$ordem" "$log" "$modelo" >/dev/null 2>&1 &
    echo "$log|$modelo" >> $R; echo "INICIO $(basename $log .log) [$modelo] $(date +%H:%M)" >> $E
    n=$((n+1))
  done
  sleep 15
done
