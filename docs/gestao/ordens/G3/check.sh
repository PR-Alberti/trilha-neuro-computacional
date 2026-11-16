#!/bin/bash
# uso: check.sh NN TT  -> build + lint do módulo (resumido) e estrutura do tema
cd ~/trilha-neuro-computacional/conteudo/modulo-$1 || exit 1
B=$(delta build project.toml 2>&1); be=$?
L=$(delta lint 2>&1); le=$?
echo "BUILD exit=$be LINT exit=$le"
echo "$B" | grep -v "^→" | grep -o "tema-[0-9]*\.dlt" | sort | uniq -c | sed 's/^/  msgs build: /'
echo "$B" | grep -v "^→" | grep "tema-$2.dlt" | head -6 | cut -c1-220
echo "$L" | grep -v "^no problems" | grep "tema-$2" | head -6 | cut -c1-220
G=$HOME/trilha-neuro-computacional/docs/gestao/ordens/G3
~/.local/share/venv-aulas/bin/python $G/tools/estrutura.py tema-$2.dlt | grep -v "^sec:.*resumo\|^sec:.*alem"
echo "palavras: $(~/.local/share/venv-aulas/bin/python $G/tools/palavras.py tema-$2.dlt)"
