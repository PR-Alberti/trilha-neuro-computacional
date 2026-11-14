# Relatório do Gestor G3 (Ferramentas): Módulos 6 e 7

**Estado em 14/11/2026, 18:15.** O trabalho está **interrompido** porque as duas cotas
acabaram: o `gemini-4-hydrogen-high` e o `gemini-3.8-flash-high` voltam por volta das 22:53.
Das 17 aulas, 9 estão escritas e compilam: 6.1–6.5, 7.1 e 7.2, mais 7.3 e 7.4, que ainda não compilam.
Quatro já estão aprovadas: 6.2, 7.1, 7.2 e, na prática, 6.1.

Ordens, logs e a fila pronta para retomar estão em
`/tmp/claude-336166952/-home-al-pedro-alberti/50153656-da93-42f3-9736-b244dac32ddb/scratchpad/trilha/gestores/G3/`:

- `fila.txt` guarda as próximas chamadas, na ordem;
- `runner.sh` executa a fila, com no máximo 3 chamadas ao mesmo tempo, e espera sozinho o reset de cada cota;
- `notas.txt` registra a minha conferência de cada aula.

Para retomar, apague `PARAR` e rode `runner.sh` em background.

## Decisões técnicas

- **Seções definidas pelo gestor.** Fiz isso em todos os temas sem subtemas no guia: de 4 a 5
  seções por tema, seguindo as orientações do maestro. Cada ordem tem a spec completa, em
  `spec/mN-tTT.txt` na pasta acima.
- **`conteudo/modulo-07/project.toml`.** Por ora, `inputs` lista só `tema-01` e `tema-02`.
  Os arquivos `tema-03.dlt` e `tema-04.dlt` existem, mas têm erros de KaTeX e quebrariam o
  build do módulo inteiro. Volte a incluí-los depois da correção que já está na fila.
- **Regra nova nas ordens dos autores.** O erro mais frequente do Hydrogen é escrever
  `&lt;`, `&gt;` e `&amp;` dentro da matemática, o que faz o KaTeX falhar. As ordens dos temas
  ainda não iniciados já trazem essa regra em destaque.
- **Conferência de código.** Rodo todos os blocos Python de cada aula no venv com
  `tools/conferir.py`, que compara a saída real com os comentários, e `tools/rodar_seq.py`
  para os blocos que dependem de `%%writefile`.

## Tabela por tema

| Tema | Estado | Seções (definidas pelo G3) | Principais correções | Pendências |
|---|---|---|---|---|
| 6.1 Ambientes | Compila, revisor: APROVAR | Colab; Jupyter e notebooks locais; VS Code e scripts .py; pip, venv e Anaconda; terminal | — | 4 ajustes pedagógicos do parecer: `exit()` × shell, `pip --version`, `Activate.ps1` no PowerShell, bloco da ordem de execução |
| 6.2 Comandos iniciais e lógica básica | **Aprovado** | Variáveis, tipos e operadores; strings e f-strings; if/elif/else; for e while | 4 refinamentos do parecer, incluindo a convenção N·Δt na duração. Os 31 blocos conferem | — |
| 6.3 Informática básica | Compila, revisor: APROVAR | Arquivos, pastas e caminhos; extensões e formatos (CSV/TSV/JSON, BIDS); terminal; codificação de texto | Os 20 blocos conferem | 4 ajustes pedagógicos do parecer: `is_absolute` no Windows, `.suffixes` para `.nii.gz`, máximo iniciado em `-inf`, `ensure_ascii` |
| 6.4 Estruturas de dados básicas | Compila; correção na fila | Listas e tuplas; dicionários e conjuntos; arrays NumPy; como escolher a estrutura | **Erro de código** em `cod:6-4-aliasing-listas`: o comentário diz `Cópia: [-99.0, …]`, mas a saída real é `[-70.0, 0.0, -65.0]` | Corrigir (ordem `correcao-lote2`) e consultar o revisor |
| 6.5 Códigos funcionais | Compila | Definir e chamar funções; parâmetros, escopo e efeitos colaterais; compreensões; módulos | Os 40 blocos conferem: 2 erros são intencionais e os módulos foram testados em sequência | Consultar o revisor |
| 6.6 Bibliotecas | Não escrito | NumPy; pandas; Matplotlib; SciPy, MNE e nilearn (MNE e nilearn só em texto) | — | Na fila |
| 6.7 Visualizações | Não escrito | Gráficos básicos; imshow e mapas de calor; raster plot e PSTH; boas práticas. 2 figuras | — | Na fila |
| 6.8 Orientação a objetos | Não escrito | Classes e objetos; classe NeuronioLIF (T ≈ 16,1 ms, ≈ 62 Hz com 2 nA); herança com período refratário; API fit/predict | — | Na fila |
| 6.9 Complexidade | Não escrito | Contar passos e O(·); classes de complexidade; medir tempo e vetorizar; memória. 1 figura | — | Na fila |
| 6.10 Prática | Não escrito | Pipelines extensas; Git e GitHub (subtemas do guia) | — | Na fila |
| 7.1 Combinatória | **Aprovado** | Princípios multiplicativo e aditivo; permutações e arranjos; combinações e o triângulo de Pascal; da contagem à probabilidade | **Erro de código** apontado pelo revisor: GAATTC estava codificado com G no fim, `[2,0,0,1,1,2]`, e passou a `[…,3]`. Também: texto do box igual ao `d`, uso de `itertools.combinations`, notação. Refiz a seção 3 (201 376 e 5/32) e conferi o Resumo e os 11 blocos | — |
| 7.2 Variável aleatória | **Aprovado** | Espaço amostral e VA; esperança e variância; Bernoulli, binomial e Poisson; uniforme, exponencial e normal. 1 figura | 32 erros de KaTeX (entidades na matemática) corrigidos; demonstração do item 3; `<proof>` tirado de `<definition>`. Conferi o Resumo e os 8 blocos | — |
| 7.3 Introdução à inferência | **Não compila** (3 erros de KaTeX) | População e amostra; estimadores e viés (ddof); erro padrão; intervalo de confiança. 1 figura | Os 8 blocos conferem | Correção na fila (`correcao-lote2`) e consulta ao revisor |
| 7.4 Testes de hipóteses | **Não compila** (38 erros de KaTeX) | Lógica do teste e p-valor; teste t; erros I e II e poder; Bonferroni e FDR (BH) em voxels. 1 figura | Encontrei um erro de código no exercício de permutação: o comentário diz "≈ −25 ms, p &lt; 0,10", mas a saída real é −16,42 ms e p = 0,188. A correção, que reinterpreta o resultado como baixo poder, está na fila | Correção e revisor |
| 7.5 Convergências | Não escrito (a chamada caiu por falta de cota) | Markov e Chebyshev; LGN; TCL; aproximação normal e quando falha. 2 figuras | — | Na fila |
| 7.6 Inferência Bayesiana | Não escrito | Bayes e taxa de base; priori, verossimilhança e posteriori em grade; beta-binomial; combinação ótima de pistas. 2 figuras | — | Na fila |
| 7.7 Inferência não-Bayesiana | Não escrito | Verossimilhança; EMV de Poisson; EMV da normal; frequentista × Bayesiano. 1 figura | — | Na fila |

## Próximos passos (fila, na ordem)

1. `correcao-lote2`: entidades na matemática de 7.3 e 7.4, permutação de 7.4, aliasing de 6.4.
2. Autor de 7.5.
3. Revisores de 7.4, 7.3, 6.4 e 6.5.
4. Autores de 6.6, 7.6, 6.7, 7.7, 6.8, 6.9 e 6.10.
5. Ainda por enfileirar:
   - um lote pequeno para 6.1 e 6.3, com os ajustes pedagógicos dos pareceres;
   - os revisores e as correções dos temas novos;
   - devolver `tema-03` e `tema-04` aos `inputs` do Módulo 7.
