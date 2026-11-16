#!/bin/bash
# uso: inputs.sh NN -> põe em inputs todos os tema-*.dlt existentes, em ordem
cd ~/trilha-neuro-computacional/conteudo/modulo-$1 || exit 1
L=$(ls tema-*.dlt 2>/dev/null | sort | sed 's/.*/"&"/' | paste -sd, | sed 's/,/, /g')
sed -i "s/^inputs = .*/inputs = [$L]/" project.toml; grep ^inputs project.toml
