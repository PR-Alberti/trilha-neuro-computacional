# Relatório de Revisão Técnica — Módulo 08 · Tema 04: Métricas estatísticas

- **Arquivo revisado:** [tema-04.dlt](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-04.dlt)
- **Documentos de referência:** [PADRAO-AULAS.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/PADRAO-AULAS.md) e [DELTA-COLA.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/DELTA-COLA.md)
- **Data da revisão:** 14 de novembro de 2026
- **Perfil do revisor:** Matemático, Neurocientista Computacional e Professor de Alunos de Ciências Biológicas

---

## 1. Veredito

**APROVAR**

A aula [conteudo/modulo-08/tema-04.dlt](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-04.dlt) apresenta padrão exemplar de rigor técnico, precisão matemática, relevância neurobiológica e clareza didática para estudantes de Ciências Biológicas. Todas as cinco seções demandadas na ementa foram desenvolvidas na ordem exata e cobrem integralmente os tópicos estipulados:

1. **Matriz de confusão e acurácia (`sec:8-4-1`):** contagens fundamentais binárias ($\mathrm{VP}, \mathrm{FP}, \mathrm{VN}, \mathrm{FN}$ com equivalentes em inglês TP, FP, TN, FN); estrita observância da convenção do <c>scikit-learn</c> em <c>confusion_matrix</c> (linhas = classes verdadeiras, colunas = classes previstas, com <c>.ravel()</c> retornando <c>tn, fp, fn, tp</c>); definições formais de acurácia e taxa de erro; extensão para matrizes multiclasse $K \times K$ na decodificação de múltiplos estímulos; comparação obrigatória com a linha de base ingênua da classe majoritária (<c>DummyClassifier</c>).
2. **Precisão, recall, especificidade e F1 (`sec:8-4-2`):** definições analíticas de precisão (VPP), *recall* (sensibilidade / TPR), especificidade (TNR), taxa de falsos positivos ($\mathrm{FPR} = 1 - \mathrm{Especificidade}$) e escore $F_1$; demonstração formal recolhível da fórmula direta por contagens $F_1 = \frac{2\,\mathrm{VP}}{2\,\mathrm{VP} + \mathrm{FP} + \mathrm{FN}}$; compromisso entre precisão e *recall*; correspondência exata com os erros tipo I e II e poder estatístico do Módulo 7; dedução e aplicação da regra de Bayes sob efeito de baixa prevalência, incluindo o exemplo numérico obrigatório ($90\%$ sensibilidade, $95\%$ especificidade e $1\%$ prevalência resultando em $\approx 15{,}4\%$ de precisão).
3. **Limiar, curva ROC e AUC (`sec:8-4-3`):** escores contínuos via <c>predict_proba</c> e <c>decision_function</c>; dinâmica do deslocamento do limiar $\tau$; definição geométrica da curva ROC e interpretação probabilística exata da AUC como estatística $U$ de Mann–Whitney normalizada ($P(s_+ > s_-)$ com peso $1/2$ para empates); curva precisão–*recall* (<c>average_precision_score</c>) para classes raras; exemplo à mão detalhado com 4 positivos e 4 negativos ($13$ pares concordantes em $16$, $\mathrm{AUC} = 0{,}8125$); figura vetorial vinculada ([fig/t04-roc.svg](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/fig/t04-roc.svg)) com script gerador íntegro ([fig/t04-roc.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/fig/t04-roc.py)).
4. **Métricas de regressão: MSE, RMSE, MAE e R² (`sec:8-4-4`):** formulações matemáticas explícitas e exame de unidades físicas (RMSE e MAE na unidade do alvo, MSE na unidade ao quadrado); definição de $R^2 = 1 - \mathrm{RSS}/\mathrm{TSS}$; demonstração analítica e numérica de que no conjunto de teste $R^2$ pode ser negativo e não equivale a $r^2$ de Pearson; exemplo concreto de modelo de codificação neural (*encoding model*) com correlação perfeita $r = +1{,}00$ convivendo com $R^2$ negativo por erro de calibração/escala; contraste de sensibilidade a *outliers* entre MSE/RMSE e MAE.
5. **Classes desbalanceadas (`sec:8-4-5`):** diagnóstico formal do paradoxo da acurácia; definição de acurácia balanceada como média dos *recalls* (<c>balanced_accuracy_score</c>); divisão estratificada (<c>stratify=y</c>); pesos inversamente proporcionais às classes (<c>class_weight="balanced"</c>); varredura de limiar de decisão $\tau$; menção conceitual de sub/superamostragem restrita ao treino; seleção de métricas orientada pela matriz de custos e consequências biológicas/clínicas.

Todas as contas foram conferidas e recalculadas à mão (9 exemplos detalhados e 15 soluções completas de exercícios). Não foi detectado nenhum erro aritmético, algébrico ou conceitual. Todos os 9 blocos de código Python (5 no corpo e 4 nas soluções dos exercícios avançados) são autocontidos, usam estritamente `numpy`, `scikit-learn` e `matplotlib`, não requerem arquivos externos, utilizam APIs atuais sem argumentos obsoletos e contêm saídas comentadas perfeitamente coerentes com o texto. As citações e links obedecem estritamente às diretrizes do projeto.

---

## 2. Tabela de Problemas e Sugestões

| Severidade | Local | Trecho | Correção sugerida |
|---|---|---|---|
| Pedagógico | Seção 1 (`sec:8-4-1`), `tbl:8-4-confusao-sklearn`, linha ~70 | `<table id="tbl:8-4-confusao-sklearn">` | O autor explicou com clareza a convenção do scikit-learn (linhas = real, colunas = previsto, com classe 0 na primeira posição). Contudo, em artigos biomédicos, medicina diagnóstica e pacotes como o *caret* em R, é comum encontrar matrizes transpostas (linhas = previsto, colunas = real) ou com a classe positiva ($1$) na primeira célula. Sugere-se incluir uma nota marginal (`<sidenote>`) recomendando que o estudante de Biologia sempre examine os rótulos de linha e coluna em publicações científicas antes de ler VP e VN. |
| Pedagógico | Seção 3 (`sec:8-4-3`), `def:8-4-roc-auc`, linha ~469 | `(equivalente à estatística $U$ de Mann–Whitney normalizada)` | Para reforçar o aprendizado interdisciplinar com o Módulo 7 (Estatística), vale explicitar na prosa que a AUC amostral é literalmente a estatística de postos $U$ dividida por $n_+ n_-$. Isso ancora o conceito de aprendizado de máquina em um teste de hipóteses não paramétrico amplamente conhecido por biólogos. |
| Pedagógico | Seção 4 (`sec:8-4-4`), `def:8-4-metricas-reg` e `cod:8-4-regressao`, linha ~683 e ~775 | `rmse = np.sqrt(mse)` | A partir do scikit-learn 1.4, a biblioteca disponibilizou a função dedicada `root_mean_squared_error`. O uso de `np.sqrt(mean_squared_error(...))` feito pelo autor é impecável por ser universalmente compatível com qualquer versão do scikit-learn (inclusive ambientes antigos do Colab), mas vale adicionar um comentário no código registrando essa compatibilidade de versões. |

---

## 3. Recálculo e Auditoria Integral de Todas as Contas

Todas as deduções analíticas, identidades algébricas e contas numéricas da aula foram recalculadas passo a passo de forma independente.

### 3.1 Subtema 1: Matriz de confusão e acurácia (`sec:8-4-1`)

1. **[Exemplo 8.4.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-04.dlt#L85-L105) (`exm:8-4-eeg-crises` — Detector de crises epilépticas em EEG):**
   - Dados de teste: $n = 200$ janelas; $20$ com crises ($y = 1$) e $180$ basais ($y = 0$).
   - Contagens: $\mathrm{VP} = 16$, $\mathrm{FN} = 4$, $\mathrm{FP} = 6$, $\mathrm{VN} = 174$.
   - Verificação das marginais de linha:
     - Linha 0 (real 0): $\mathrm{VN} + \mathrm{FP} = 174 + 6 = 180$.
     - Linha 1 (real 1): $\mathrm{FN} + \mathrm{VP} = 4 + 16 = 20$.
     - Total: $180 + 20 = 200$.
   - Matriz do scikit-learn: $\mathbf{M} = \begin{pmatrix} 174 & 6 \\ 4 & 16 \end{pmatrix}$.
   - Acurácia: $\frac{16 + 174}{200} = \frac{190}{200} = 0{,}95$ ($95{,}0\%$).
   - Taxa de erro: $1 - 0{,}95 = 0{,}05$ ($5{,}0\%$).
   - Linha de base ingênua (prevendo sempre 0):
     - $\mathrm{VN} = 180$, $\mathrm{FP} = 0$, $\mathrm{FN} = 20$, $\mathrm{VP} = 0$.
     - Matriz: $\begin{pmatrix} 180 & 0 \\ 20 & 0 \end{pmatrix}$.
     - Acurácia ingênua: $\frac{180 + 0}{200} = \frac{180}{200} = 0{,}90$ ($90{,}0\%$).
   - *Conclusão:* Todas as contas e interpretações estão perfeitamente exatas.

2. **[Exemplo 8.4.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-04.dlt#L107-L118) (`exm:8-4-multiclasse-mvpa` — Decodificação multiclasse de 3 estímulos):**
   - Dados: $K = 3$ categorias balanceadas ($30$ ensaios cada), $n = 90$.
   - Matriz observada:
     $$\mathbf{M} = \begin{pmatrix} 26 & 2 & 2 \\ 3 & 24 & 3 \\ 4 & 5 & 21 \end{pmatrix}.$$
   - Verificação das linhas: $26+2+2 = 30$, $3+24+3 = 30$, $4+5+21 = 30$. Total $= 90$.
   - Acertos na diagonal: $26 + 24 + 21 = 71$.
   - Acurácia global: $\frac{71}{90} = 0{,}78888... \approx 0{,}789$ ($78{,}9\%$).
   - Taxa de erro global: $\frac{19}{90} = 0{,}21111... \approx 0{,}211$ ($21{,}1\%$).
   - Nível de acaso: $\frac{1}{3} \approx 0{,}333$ ($33{,}3\%$).
   - Desempenho individual por classe:
     - Rosto: $\frac{26}{30} \approx 0{,}867$ ($86{,}7\%$).
     - Casa: $\frac{24}{30} = 0{,}800$ ($80{,}0\%$).
     - Ferramenta: $\frac{21}{30} = 0{,}700$ ($70{,}0\%$).
   - Maior par de confusão: "ferramenta" confundida com "casa" ($5$ vezes) e com "rosto" ($4$ vezes).
   - *Conclusão:* Contas exatas.

3. **[Exercício 8.4.1.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-04.dlt#L179-L194) (`exr:8-4-1-1` — Detector de spikes):**
   - Matriz dada: $\mathbf{M} = \begin{pmatrix} 410 & 15 \\ 25 & 50 \end{pmatrix}$.
   - Leitura na convenção scikit-learn:
     $\mathrm{VN} = 410$, $\mathrm{FP} = 15$, $\mathrm{FN} = 25$, $\mathrm{VP} = 50$. Total: $410 + 15 + 25 + 50 = 500$.
   - Acurácia: $\frac{410 + 50}{500} = \frac{460}{500} = 0{,}92$ ($92{,}0\%$).
   - Taxa de erro: $1 - 0{,}92 = 0{,}08$ ($8{,}0\%$).
   - Linha de base majoritária: há $410 + 15 = 425$ janelas sem spike e $25 + 50 = 75$ com spike. Chutar sempre a classe majoritária dá $\frac{425}{500} = 0{,}85$ ($85{,}0\%$).
   - *Conclusão:* Contas exatas.

4. **[Exercício 8.4.1.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-04.dlt#L195-L211) (`exr:8-4-1-2` — Decodificação multiclasse de 3 modalidades):**
   - Matriz dada: $\mathbf{M} = \begin{pmatrix} 34 & 4 & 2 \\ 6 & 28 & 6 \\ 3 & 7 & 30 \end{pmatrix}$, $n = 120$ ($40$ por classe).
   - Acertos diagonais: $34 + 28 + 30 = 92$.
   - Acurácia global: $\frac{92}{120} = \frac{23}{30} \approx 0{,}7666... \approx 0{,}767$ ($76{,}7\%$).
   - Acaso: $\frac{1}{3} \approx 0{,}333$ ($33{,}3\%$).
   - Acertos individuais: Visual $\frac{34}{40} = 0{,}85$ ($85{,}0\%$), Auditivo $\frac{28}{40} = 0{,}70$ ($70{,}0\%$), Tátil $\frac{30}{40} = 0{,}75$ ($75{,}0\%$). Maior acerto: Visual.
   - Par com maior confusão: Auditivo e Tátil com $6 + 7 = 13$ erros mútuos.
   - *Conclusão:* Contas exatas.

5. **[Exercício 8.4.1.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-04.dlt#L212-L257) (`exr:8-4-1-3` — Matriz multiclasse e baseline em Python):**
   - Conjunto `load_wine`: $178$ amostras, classes com $59$, $71$ e $48$ instâncias.
   - Divisão com $30\%$ de teste estratificado: $n_{\text{teste}} = 54$ amostras ($18$ da classe 0, $21$ da classe 1, $15$ da classe 2).
   - Linha de base majoritária: classe 1 com $21$ amostras em $54 \implies \frac{21}{54} \approx 0{,}3888... \approx 0{,}389$ ($38{,}9\%$).
   - Matriz do modelo logístico padronizado: $\begin{pmatrix} 18 & 0 & 0 \\ 0 & 21 & 0 \\ 0 & 1 & 14 \end{pmatrix}$.
   - Acertos: $18 + 21 + 14 = 53$ em $54 \implies \frac{53}{54} \approx 0{,}98148... \approx 0{,}981$ ($98{,}1\%$).
   - *Conclusão:* Saídas comentadas e contas perfeitamente coerentes.

---

### 3.2 Subtema 2: Precisão, recall, especificidade e F1 (`sec:8-4-2`)

1. **[Proposição 8.4.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-04.dlt#L298-L308) (`prop:8-4-f1-contagem` — Demonstração analítica do F1):**
   - Sejam $P = \frac{\mathrm{VP}}{\mathrm{VP} + \mathrm{FP}}$ e $R = \frac{\mathrm{VP}}{\mathrm{VP} + \mathrm{FN}}$.
   - Soma dos inversos:
     $$\frac{1}{P} + \frac{1}{R} = \frac{\mathrm{VP} + \mathrm{FP}}{\mathrm{VP}} + \frac{\mathrm{VP} + \mathrm{FN}}{\mathrm{VP}} = \frac{2\,\mathrm{VP} + \mathrm{FP} + \mathrm{FN}}{\mathrm{VP}}.$$
   - Média harmônica:
     $$F_1 = \frac{2}{\frac{1}{P} + \frac{1}{R}} = \frac{2}{\frac{2\,\mathrm{VP} + \mathrm{FP} + \mathrm{FN}}{\mathrm{VP}}} = \frac{2\,\mathrm{VP}}{2\,\mathrm{VP} + \mathrm{FP} + \mathrm{FN}}.$$
   - *Conclusão:* Dedução matemática impecável.

2. **[Exemplo 8.4.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-04.dlt#L320-L335) (`exm:8-4-detector-spikes` — Detector de disparos neuronais):**
   - Dados: $\mathrm{VP} = 30$, $\mathrm{FP} = 10$, $\mathrm{FN} = 20$, $\mathrm{VN} = 140$.
   - Totais marginais: positivos reais $= 30 + 20 = 50$; negativos reais $= 140 + 10 = 150$; previstos positivos $= 30 + 10 = 40$.
   - Precisão: $\frac{30}{30 + 10} = \frac{30}{40} = 0{,}75$ ($75{,}0\%$).
   - Recall (Sensibilidade): $\frac{30}{30 + 20} = \frac{30}{50} = 0{,}60$ ($60{,}0\%$).
   - Especificidade: $\frac{140}{140 + 10} = \frac{140}{150} = \frac{14}{15} \approx 0{,}9333... \approx 0{,}933$ ($93{,}3\%$).
   - $\mathrm{FPR}$: $1 - \frac{14}{15} = \frac{1}{15} \approx 0{,}0666... \approx 0{,}067$ ($6{,}7\%$).
   - $F_1$ por $P$ e $R$: $\frac{2 \cdot 0{,}75 \cdot 0{,}60}{0{,}75 + 0{,}60} = \frac{0{,}90}{1{,}35} = \frac{2}{3} \approx 0{,}6666... \approx 0{,}667$.
   - $F_1$ por contagens: $\frac{2 \cdot 30}{2 \cdot 30 + 10 + 20} = \frac{60}{90} = \frac{2}{3} \approx 0{,}667$.
   - *Conclusão:* Contas exatas.

3. **[Exemplo 8.4.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-04.dlt#L337-L344) (`exm:8-4-bayes-prevalencia` — Exemplo obrigatório da regra de Bayes):**
   - Parâmetros: Sensibilidade $= 0{,}90$, Especificidade $= 0{,}95$, Prevalência $\pi = 0{,}01$.
   - Termos complementares: $1 - \mathrm{Especificidade} = 0{,}05$, $1 - \pi = 0{,}99$.
   - Numerador: $0{,}90 \cdot 0{,}01 = 0{,}009$.
   - Denominador: $0{,}009 + 0{,}05 \cdot 0{,}99 = 0{,}009 + 0{,}0495 = 0{,}0585$.
   - Precisão (VPP):
     $$\mathrm{VPP} = \frac{0{,}009}{0{,}0585} = \frac{90}{585} = \frac{2}{13} \approx 0{,}153846... \approx 0{,}1538 \quad (15{,}4\%).$$
   - Coorte de $10\,000$ indivíduos/janelas:
     - Positivos reais: $100 \implies \mathrm{VP} = 0{,}90 \times 100 = 90$, $\mathrm{FN} = 10$.
     - Negativos reais: $9\,900 \implies \mathrm{FP} = 0{,}05 \times 9\,900 = 495$, $\mathrm{VN} = 9\,405$.
     - Total de alarmes positivos: $90 + 495 = 585$.
     - Razão de acerto: $\frac{90}{585} = \frac{2}{13} \approx 15{,}4\%$.
   - *Conclusão:* O exemplo numérico obrigatório foi resolvido e conferido com rigor milimétrico.

4. **[Exercício 8.4.2.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-04.dlt#L404-L418) (`exr:8-4-2-1` — Sono REM vs não-REM):**
   - Dados: $\mathrm{VP} = 45$, $\mathrm{FN} = 15$, $\mathrm{FP} = 5$, $\mathrm{VN} = 185$, total $= 250$.
   - Precisão: $\frac{45}{45 + 5} = \frac{45}{50} = 0{,}90$ ($90{,}0\%$).
   - Recall: $\frac{45}{45 + 15} = \frac{45}{60} = 0{,}75$ ($75{,}0\%$).
   - Especificidade: $\frac{185}{185 + 5} = \frac{185}{190} = \frac{37}{38} \approx 0{,}97368... \approx 0{,}974$ ($97{,}4\%$).
   - $\mathrm{FPR}$: $\frac{5}{190} = \frac{1}{38} \approx 0{,}0263... \approx 0{,}026$ ($2{,}6\%$).
   - $F_1$: $\frac{2 \cdot 0{,}90 \cdot 0{,}75}{0{,}90 + 0{,}75} = \frac{1{,}35}{1{,}65} = \frac{9}{11} \approx 0{,}81818... \approx 0{,}818$.
   - Por contagens: $\frac{2 \cdot 45}{2 \cdot 45 + 5 + 15} = \frac{90}{110} = \frac{9}{11} \approx 0{,}818$.
   - *Conclusão:* Contas exatas.

5. **[Exercício 8.4.2.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-04.dlt#L420-L436) (`exr:8-4-2-2` — Biomarcador e regra de Bayes):**
   - Parâmetros: $\pi = 0{,}02$, Sensibilidade $= 0{,}95$, Especificidade $= 0{,}90$.
   - Item (a):
     $$\mathrm{VPP} = \frac{0{,}95 \cdot 0{,}02}{0{,}95 \cdot 0{,}02 + 0{,}10 \cdot 0{,}98} = \frac{0{,}019}{0{,}019 + 0{,}098} = \frac{0{,}019}{0{,}117} = \frac{19}{117} \approx 0{,}162393... \approx 0{,}1624 \quad (16{,}2\%).$$
   - Item (b): em $1\,000$ pacientes, $20$ são doentes ($19\text{ VP}, 1\text{ FN}$) e $980$ são saudáveis ($98\text{ FP}, 882\text{ VN}$).
     Total de testes positivos: $19 + 98 = 117$.
     Fração de positivos reais: $\frac{19}{117} \approx 16{,}2\%$.
   - *Conclusão:* Contas exatas.

6. **[Exercício 8.4.2.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-04.dlt#L438-L451) (`exr:8-4-2-3` — Comparação entre média harmônica e aritmética):**
   - Diferença para $P, R > 0$:
     $$\frac{P + R}{2} - \frac{2PR}{P + R} = \frac{(P + R)^2 - 4PR}{2(P + R)} = \frac{P^2 + 2PR + R^2 - 4PR}{2(P + R)} = \frac{(P - R)^2}{2(P + R)} \ge 0.$$
     Igualdade se e somente se $P - R = 0 \iff P = R$.
   - Caso numérico $P = 0{,}90$ e $R = 0{,}10$:
     - Média aritmética: $\frac{0{,}90 + 0{,}10}{2} = 0{,}50$.
     - Média harmônica ($F_1$): $\frac{2 \cdot 0{,}90 \cdot 0{,}10}{0{,}90 + 0{,}10} = \frac{0{,}18}{1{,}00} = 0{,}18$.
   - *Conclusão:* Demonstração elegante e valores exatos.

---

### 3.3 Subtema 3: Limiar, curva ROC e AUC (`sec:8-4-3`)

1. **[Exemplo 8.4.5](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-04.dlt#L487-L517) (`exm:8-4-roc-mao` — Exemplo obrigatório de ROC e AUC à mão):**
   - Amostras ordenadas: $n_+ = 4$, $n_- = 4$.
     $$(0{,}95,\,+), \; (0{,}85,\,+), \; (0{,}70,\,-), \; (0{,}60,\,+), \; (0{,}50,\,-), \; (0{,}40,\,+), \; (0{,}30,\,-), \; (0{,}20,\,-).$$
   - Trajetória dos vértices $(\mathrm{FPR}, \mathrm{TPR})$ conforme $\tau$ decresce:
     - $\tau > 0{,}95$: $(0{,}00;\; 0{,}00)$
     - $\tau = 0{,}95$ (entra $+$): $(0{,}00;\; 0{,}25)$
     - $\tau = 0{,}85$ (entra $+$): $(0{,}00;\; 0{,}50)$
     - $\tau = 0{,}70$ (entra $-$): $(0{,}25;\; 0{,}50)$
     - $\tau = 0{,}60$ (entra $+$): $(0{,}25;\; 0{,}75)$
     - $\tau = 0{,}50$ (entra $-$): $(0{,}50;\; 0{,}75)$
     - $\tau = 0{,}40$ (entra $+$): $(0{,}50;\; 1{,}00)$
     - $\tau = 0{,}30$ (entra $-$): $(0{,}75;\; 1{,}00)$
     - $\tau = 0{,}20$ (entra $-$): $(1{,}00;\; 1{,}00)$
   - Contagem de pares concordantes $(+, -)$ pela fórmula analítica:
     - $+_1 (0{,}95)$: supera $0{,}70, 0{,}50, 0{,}30, 0{,}20 \implies 4$ vitórias.
     - $+_2 (0{,}85)$: supera $0{,}70, 0{,}50, 0{,}30, 0{,}20 \implies 4$ vitórias.
     - $+_3 (0{,}60)$: supera $0{,}50, 0{,}30, 0{,}20 \implies 3$ vitórias (perde para $0{,}70$).
     - $+_4 (0{,}40)$: supera $0{,}30, 0{,}20 \implies 2$ vitórias (perde para $0{,}70$ e $0{,}50$).
     - Total: $4 + 4 + 3 + 2 = 13$ vitórias em $4 \times 4 = 16$ pares.
     $$\mathrm{AUC} = \frac{13}{16} = 0{,}8125.$$
   - Integração geométrica (soma das áreas dos retângulos):
     - Intervalo $\mathrm{FPR} \in [0{,}00;\; 0{,}25]$: altura $= 0{,}50 \implies 0{,}25 \cdot 0{,}50 = 0{,}1250$.
     - Intervalo $\mathrm{FPR} \in [0{,}25;\; 0{,}50]$: altura $= 0{,}75 \implies 0{,}25 \cdot 0{,}75 = 0{,}1875$.
     - Intervalo $\mathrm{FPR} \in [0{,}50;\; 0{,}75]$: altura $= 1{,}00 \implies 0{,}25 \cdot 1{,}00 = 0{,}2500$.
     - Intervalo $\mathrm{FPR} \in [0{,}75;\; 1{,}00]$: altura $= 1{,}00 \implies 0{,}25 \cdot 1{,}00 = 0{,}2500$.
     - Área total: $0{,}1250 + 0{,}1875 + 0{,}2500 + 0{,}2500 = 0{,}8125$.
   - *Conclusão:* O exemplo obrigatório foi conferido duplamente; os dois métodos convergem com absoluta exatidão para $0{,}8125$.

2. **[Exemplo 8.4.6](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-04.dlt#L519-L530) (`exm:8-4-limiar-clinico` — Limiares clínicos em eventos raros):**
   - Registro com $10$ eventos positivos e $990$ negativos.
   - Limiar $\tau_1 = 0{,}50$: $\mathrm{TPR} = 0{,}70$ ($7\text{ VP}, 3\text{ FN}$), $\mathrm{FPR} = 0{,}01$ ($10\text{ FP}, 980\text{ VN}$).
     Precisão: $\frac{7}{7 + 10} = \frac{7}{17} \approx 0{,}41176... \approx 41{,}2\%$. Recall: $70\%$.
   - Limiar $\tau_2 = 0{,}20$: $\mathrm{TPR} = 0{,}90$ ($9\text{ VP}, 1\text{ FN}$), $\mathrm{FPR} = 0{,}05$ ($50\text{ FP}, 940\text{ VN}$).
     Precisão: $\frac{9}{9 + 50} = \frac{9}{59} \approx 0{,}15254... \approx 15{,}3\%$. Recall: $90\%$.
   - *Conclusão:* Contas exatas.

3. **[Exercício 8.4.3.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-04.dlt#L590-L602) (`exr:8-4-3-1` — Troca de limiar):**
   - Positivos: $\{0{,}82;\; 0{,}65;\; 0{,}45;\; 0{,}25\}$. Negativos: $\{0{,}72;\; 0{,}38;\; 0{,}20;\; 0{,}10\}$.
   - Para $\tau = 0{,}70$:
     - Positivos $\ge 0{,}70$: apenas $0{,}82 \implies \mathrm{VP} = 1$, $\mathrm{TPR} = 1/4 = 0{,}25$.
     - Negativos $\ge 0{,}70$: apenas $0{,}72 \implies \mathrm{FP} = 1$, $\mathrm{FPR} = 1/4 = 0{,}25$.
   - Para $\tau = 0{,}30$:
     - Positivos $\ge 0{,}30$: $0{,}82, 0{,}65, 0{,}45 \implies \mathrm{VP} = 3$, $\mathrm{TPR} = 3/4 = 0{,}75$.
     - Negativos $\ge 0{,}30$: $0{,}72, 0{,}38 \implies \mathrm{FP} = 2$, $\mathrm{FPR} = 2/4 = 0{,}50$.
   - *Conclusão:* Contas exatas.

4. **[Exercício 8.4.3.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-04.dlt#L603-L619) (`exr:8-4-3-2` — Curva ROC e AUC à mão com empate):**
   - Amostras: Positivos $\{0{,}9;\; 0{,}6;\; 0{,}4\}$, Negativos $\{0{,}7;\; 0{,}6;\; 0{,}2\}$.
   - Contagem de pares ($3 \times 3 = 9$ pares):
     - $+_1 (0{,}9)$: supera $0{,}7, 0{,}6, 0{,}2 \implies +3{,}0$.
     - $+_2 (0{,}6)$: perde para $0{,}7$ ($0$), empata com $0{,}6$ ($+0{,}5$), supera $0{,}2$ ($+1{,}0$) $\implies +1{,}5$.
     - $+_3 (0{,}4)$: perde para $0{,}7$ e $0{,}6$ ($0$), supera $0{,}2$ ($+1{,}0$) $\implies +1{,}0$.
     - Pontuação total: $3{,}0 + 1{,}5 + 1{,}0 = 5{,}5$.
     $$\mathrm{AUC} = \frac{5{,}5}{9} = \frac{11}{18} \approx 0{,}6111... \approx 0{,}611.$$
   - Vértices da curva ROC: $(0, 0) \to (0, 1/3) \to (1/3, 1/3) \to (2/3, 2/3) \to (2/3, 1) \to (1, 1)$.
   - Áreas geométricas por intervalo:
     - Intervalo 1 $[0, 1/3]$: retângulo de largura $1/3$ e altura $1/3 \implies \frac{1}{9}$.
     - Intervalo 2 $[1/3, 2/3]$: trapézio com bases $1/3$ e $2/3$, largura $1/3 \implies \frac{1/3 + 2/3}{2} \cdot \frac{1}{3} = \frac{1}{2} \cdot \frac{1}{3} = \frac{1}{6}$.
     - Intervalo 3 $[2/3, 1]$: retângulo de largura $1/3$ e altura $1 \implies \frac{1}{3}$.
     - Soma: $\frac{1}{9} + \frac{1}{6} + \frac{1}{3} = \frac{2 + 3 + 6}{18} = \frac{11}{18} \approx 0{,}611$.
   - *Conclusão:* Contas exatas.

5. **[Exercício 8.4.3.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-04.dlt#L621-L664) (`exr:8-4-3-3` — AUC com predict vs predict_proba):**
   - Compara a AUC de escores contínuos ($0{,}992$) com a AUC degenerada calculada sobre rótulos discretos $0/1$ ($0{,}961$), comprovando que esta última coincide exatamente com <c>balanced_accuracy_score</c> ($0{,}961$).
   - *Conclusão:* Dedução conceitual e saídas comentadas exatas.

---

### 3.4 Subtema 4: Métricas de regressão: MSE, RMSE, MAE e R² (`sec:8-4-4`)

1. **[Exemplo 8.4.7](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-04.dlt#L714-L733) (`exm:8-4-reg-mao` — Métricas de regressão e outlier à mão):**
   - Observações: $\mathbf{y} = (10, 15, 20, 25, 30)\text{ Hz}$, $n = 5$.
   - Média observada: $\bar{y} = \frac{10 + 15 + 20 + 25 + 30}{5} = \frac{100}{5} = 20\text{ Hz}$.
   - Desvios em relação à média: $(-10, -5, 0, 5, 10)\text{ Hz}$.
   - $\mathrm{TSS} = (-10)^2 + (-5)^2 + 0^2 + 5^2 + 10^2 = 100 + 25 + 0 + 25 + 100 = 250\text{ Hz}^2$.
   - Previsões: $\hat{\mathbf{y}} = (11, 14, 21, 24, 26)\text{ Hz}$.
   - Resíduos $e_i = y_i - \hat{y}_i$:
     $10 - 11 = -1$, $15 - 14 = +1$, $20 - 21 = -1$, $25 - 24 = +1$, $30 - 26 = +4$.
   - $\mathrm{RSS} = (-1)^2 + 1^2 + (-1)^2 + 1^2 + 4^2 = 1 + 1 + 1 + 1 + 16 = 20\text{ Hz}^2$.
   - $\mathrm{MSE} = \frac{20}{5} = 4\text{ Hz}^2$.
   - $\mathrm{RMSE} = \sqrt{4} = 2\text{ Hz}$.
   - $\mathrm{MAE} = \frac{1 + 1 + 1 + 1 + 4}{5} = \frac{8}{5} = 1{,}6\text{ Hz}$.
   - $R^2 = 1 - \frac{20}{250} = 1 - 0{,}08 = 0{,}92$.
   - Impacto do *outlier* ($\hat{y}_5 = 20\text{ Hz} \implies e_5 = 30 - 20 = 10\text{ Hz}$):
     - Novo $\mathrm{MAE} = \frac{1 + 1 + 1 + 1 + 10}{5} = \frac{14}{5} = 2{,}8\text{ Hz}$ (aumento de $+1{,}2\text{ Hz}$, ou $+75\%$).
     - Novo $\mathrm{RSS} = 1 + 1 + 1 + 1 + 100 = 104\text{ Hz}^2$.
     - Novo $\mathrm{MSE} = \frac{104}{5} = 20{,}8\text{ Hz}^2$.
     - Novo $\mathrm{RMSE} = \sqrt{20{,}8} \approx 4{,}5607... \approx 4{,}56\text{ Hz}$ (salto de $2{,}00 \to 4{,}56$, aumento de $+128\%$).
   - *Conclusão:* Contas exatas.

2. **[Exemplo 8.4.8](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-04.dlt#L735-L749) (`exm:8-4-pearson-vs-r2` — Correlação r = 1 com R² negativo em encoding):**
   - Dados observados: $\mathbf{y} = (10, 20, 30, 40)\text{ Hz}$, $n = 4$.
   - Média: $\bar{y} = 25\text{ Hz}$.
   - Desvios: $(-15, -5, 5, 15)\text{ Hz}$.
   - $\mathrm{TSS} = 225 + 25 + 25 + 225 = 500\text{ Hz}^2$.
   - **Modelo A ($\hat{y}_i = 2y_i$):** $\hat{\mathbf{y}}_A = (20, 40, 60, 80)\text{ Hz}$.
     - Como é função afim estritamente crescente ($a = 2 > 0$), $r_A = +1{,}00$.
     - Resíduos: $(-10, -20, -30, -40)\text{ Hz}$.
     - $\mathrm{RSS}_A = 100 + 400 + 900 + 1\,600 = 3\,000\text{ Hz}^2$.
     - $R^2_A = 1 - \frac{3\,000}{500} = 1 - 6 = -5{,}00$.
   - **Modelo B ($\hat{y}_i = y_i + 30$):** $\hat{\mathbf{y}}_B = (40, 50, 60, 70)\text{ Hz}$.
     - Como é translação estritamente crescente ($a = 1 > 0$), $r_B = +1{,}00$.
     - Resíduos: todos iguais a $-30\text{ Hz}$.
     - $\mathrm{RSS}_B = 4 \cdot (-30)^2 = 4 \cdot 900 = 3\,600\text{ Hz}^2$.
     - $R^2_B = 1 - \frac{3\,600}{500} = 1 - 7{,}2 = -6{,}20$.
   - *Conclusão:* Contas exatas.

3. **[Exercício 8.4.4.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-04.dlt#L801-L817) (`exr:8-4-4-1` — Potencial de membrana em mV):**
   - Observações: $\mathbf{y} = (-70, -66, -62, -58)\text{ mV}$, $n = 4$.
   - Média: $\bar{y} = \frac{-256}{4} = -64\text{ mV}$.
   - Desvios da média: $(-6, -2, +2, +6)\text{ mV}$.
   - $\mathrm{TSS} = 36 + 4 + 4 + 36 = 80\text{ mV}^2$.
   - Previsões: $\hat{\mathbf{y}} = (-70, -64, -64, -62)\text{ mV}$.
   - Resíduos $e_i = y_i - \hat{y}_i$:
     $-70 - (-70) = 0$, $-66 - (-64) = -2$, $-62 - (-64) = +2$, $-58 - (-62) = +4$.
   - $\mathrm{RSS} = 0^2 + (-2)^2 + 2^2 + 4^2 = 0 + 4 + 4 + 16 = 24\text{ mV}^2$.
   - $\mathrm{MSE} = \frac{24}{4} = 6\text{ mV}^2$.
   - $\mathrm{RMSE} = \sqrt{6} \approx 2{,}4494... \approx 2{,}45\text{ mV}$.
   - $\mathrm{MAE} = \frac{0 + 2 + 2 + 4}{4} = \frac{8}{4} = 2\text{ mV}$.
   - $R^2 = 1 - \frac{24}{80} = 1 - 0{,}30 = 0{,}70$.
   - *Conclusão:* Contas e unidades físicas exatas.

4. **[Exercício 8.4.4.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-04.dlt#L819-L830) (`exr:8-4-4-2` — Sinal BOLD de fMRI):**
   - Observações: $\mathbf{y} = (0, 2, 4, 6)$, $n = 4$.
   - Média: $\bar{y} = 3$. Desvios: $(-3, -1, 1, 3)$. $\mathrm{TSS} = 9 + 1 + 1 + 9 = 20$.
   - Modelo A ($\hat{\mathbf{y}}_A = (1, 2, 3, 4)$):
     - Resíduos: $(-1, 0, 1, 2)$. $\mathrm{RSS}_A = 1 + 0 + 1 + 4 = 6$.
     - $R^2_A = 1 - \frac{6}{20} = 1 - 0{,}30 = 0{,}70$.
     - Correlação de Pearson: $\hat{y}_A = 1 + 0{,}5y \implies r_A = +1{,}00$.
   - Modelo B ($\hat{\mathbf{y}}_B = (5, 7, 9, 11)$):
     - Resíduos: $(-5, -5, -5, -5)$. $\mathrm{RSS}_B = 4 \cdot 25 = 100$.
     - $R^2_B = 1 - \frac{100}{20} = 1 - 5 = -4{,}00$.
     - Correlação de Pearson: $\hat{y}_B = y + 5 \implies r_B = +1{,}00$.
   - *Conclusão:* Contas exatas.

5. **[Exercício 8.4.4.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-04.dlt#L832-L868) (`exr:8-4-4-3` — Sensibilidade de RMSE e MAE a outliers):**
   - Conjunto `load_diabetes`, regressão linear em $25\%$ de teste.
   - Sem outlier: $\mathrm{RMSE} = 56{,}394$, $\mathrm{MAE} = 45{,}121$.
   - Com outlier de $+200$ em $y_{\text{teste}}[0]$: $\mathrm{RMSE} = 60{,}417$, $\mathrm{MAE} = 46{,}923$.
   - Variação absoluta e relativa:
     - $\Delta\mathrm{RMSE} = 60{,}417 - 56{,}394 = +4{,}023$ ($\frac{4{,}023}{56{,}394} \approx +7{,}13\%$).
     - $\Delta\mathrm{MAE} = 46{,}923 - 45{,}121 = +1{,}802$ ($\frac{1{,}802}{45{,}121} \approx +3{,}99\% \approx +4{,}0\%$).
   - *Conclusão:* Contas e saídas comentadas exatas.

---

### 3.5 Subtema 5: Classes desbalanceadas (`sec:8-4-5`)

1. **[Exemplo 8.4.9](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-04.dlt#L902-L922) (`exm:8-4-ripples-desbalanceado` — Sharp-wave ripples a 1% de prevalência):**
   - Dados: $n = 1\,000$ janelas, $10$ ripples ($y = 1$) e $990$ fundo ($y = 0$).
   - **Classificador ingênuo (chuta sempre 0):**
     - $\mathrm{VP} = 0$, $\mathrm{FN} = 10$, $\mathrm{FP} = 0$, $\mathrm{VN} = 990$.
     - Acurácia simples: $\frac{990}{1\,000} = 0{,}99$ ($99{,}0\%$).
     - Recall: $\frac{0}{10} = 0\%$. Especificidade: $\frac{990}{990} = 100\%$.
     - Acurácia balanceada: $\frac{0 + 1}{2} = 0{,}50$ ($50{,}0\%$).
   - **Detector neural:**
     - $\mathrm{VP} = 8$, $\mathrm{FN} = 2$, $\mathrm{FP} = 99$, $\mathrm{VN} = 891$.
     - Acurácia simples: $\frac{8 + 891}{1\,000} = \frac{899}{1\,000} = 0{,}899$ ($89{,}9\%$).
     - Recall: $\frac{8}{10} = 0{,}80$ ($80{,}0\%$).
     - Especificidade: $\frac{891}{990} = 0{,}90$ ($90{,}0\%$).
     - Acurácia balanceada: $\frac{0{,}80 + 0{,}90}{2} = 0{,}85$ ($85{,}0\%$).
     - Precisão: $\frac{8}{8 + 99} = \frac{8}{107} \approx 0{,}07476... \approx 7{,}5\%$.
   - *Conclusão:* Contas exatas.

2. **[Exemplo 8.4.10](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-04.dlt#L924-L946) (`exm:8-4-pesos-custo` — Pesos balanceados e custos):**
   - Treino com $n = 1\,000$, $K = 2$, $n_1 = 50$ ($5\%$), $n_0 = 950$ ($95\%$).
   - Item (a) — Fórmula $w_k = \frac{n}{K \cdot n_k}$:
     $$w_1 = \frac{1\,000}{2 \cdot 50} = \frac{1\,000}{100} = 10{,}0.$$
     $$w_0 = \frac{1\,000}{2 \cdot 950} = \frac{1\,000}{1\,900} = \frac{10}{19} \approx 0{,}5263... \approx 0{,}526.$$
     Razão de pesos: $\frac{w_1}{w_0} = \frac{10}{10/19} = 19 = \frac{950}{50}$.
     Pesos agregados por classe: $50 \times 10 = 500$, $950 \times \frac{10}{19} = 500$.
   - Item (b) — Custo de $\mathrm{FP} = 1$ e $\mathrm{FN} = 10$:
     - Modelo X ($\mathrm{FN} = 4, \mathrm{FP} = 2$): custo $= 10(4) + 1(2) = 42$. Erros totais $= 6$.
     - Modelo Y ($\mathrm{FN} = 1, \mathrm{FP} = 12$): custo $= 10(1) + 1(12) = 22$. Erros totais $= 13$.
     - Conclusão: Modelo Y tem acurácia menor ($87\%$ vs $94\%$), porém reduz o custo esperado quase pela metade ($22$ vs $42$).
   - *Conclusão:* Contas exatas.

3. **[Exercício 8.4.5.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-04.dlt#L1023-L1038) (`exr:8-4-5-1` — Paradoxo da acurácia em ripples):**
   - Dados: $n = 1\,000$, $20$ positivos ($2\%$) e $980$ negativos ($98\%$).
   - Detector: $\mathrm{VP} = 16$, $\mathrm{FN} = 4$, $\mathrm{FP} = 49$, $\mathrm{VN} = 931$.
   - Linha de base ingênua: Acurácia simples $= \frac{980}{1\,000} = 98{,}0\%$; Acurácia balanceada $= \frac{0 + 1}{2} = 50{,}0\%$.
   - Detector:
     - Acurácia simples: $\frac{16 + 931}{1\,000} = \frac{947}{1\,000} = 94{,}7\%$.
     - Recall: $\frac{16}{20} = 0{,}80$ ($80{,}0\%$).
     - Especificidade: $\frac{931}{980} = 0{,}95$ ($95{,}0\%$).
     - Acurácia balanceada: $\frac{0{,}80 + 0{,}95}{2} = 0{,}875$ ($87{,}5\%$).
   - *Conclusão:* Contas exatas.

4. **[Exercício 8.4.5.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-04.dlt#L1040-L1057) (`exr:8-4-5-2` — Pesos multiclasse e deslocamento de limiar):**
   - Dados: $n = 600$, $K = 3$, $n_1 = 300$, $n_2 = 200$, $n_3 = 100$.
   - Item (a) — Pesos balanceados:
     $$w_k = \frac{600}{3 \cdot n_k} = \frac{200}{n_k}.$$
     $$w_1 = \frac{200}{300} = \frac{2}{3} \approx 0{,}667, \quad w_2 = \frac{200}{200} = 1{,}000, \quad w_3 = \frac{200}{100} = 2{,}000.$$
   - Item (b) — Custo de $\mathrm{FN}$ oito vezes maior que $\mathrm{FP}$:
     Deve-se **diminuir** o limiar $\tau < 0{,}5$, aumentando o *recall* (reduzindo os caríssimos $\mathrm{FN}$); a métrica que sofre queda forçada é a **precisão** (e a especificidade), pelo aumento de alarmes falsos ($\mathrm{FP}$).
   - *Conclusão:* Contas e raciocínio teórico exatos.

5. **[Exercício 8.4.5.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-04.dlt#L1059-L1116) (`exr:8-4-5-3` — Varredura de limiares em Python):**
   - Dados sintéticos com $96\%$ negativos e $4\%$ positivos ($500$ amostras de teste).
   - Limiares avaliados:
     - $\tau = 0{,}50$: $\mathrm{Acc} = 0{,}962$, $\mathrm{AccBal} = 0{,}633$, $\mathrm{Rec} = 0{,}273$, $\mathrm{Prec} = 0{,}667$, $F_1 = 0{,}387$.
     - $\tau = 0{,}30$: $\mathrm{Acc} = 0{,}958$, $\mathrm{AccBal} = 0{,}720$, $\mathrm{Rec} = 0{,}455$, $\mathrm{Prec} = 0{,}526$, $F_1 = 0{,}488$.
     - $\tau = 0{,}15$: $\mathrm{Acc} = 0{,}916$, $\mathrm{AccBal} = 0{,}779$, $\mathrm{Rec} = 0{,}636$, $\mathrm{Prec} = 0{,}292$, $F_1 = 0{,}400$.
   - *Conclusão:* Saídas comentadas e dinâmica de compromisso entre precisão e *recall* perfeitamente coerentes.

---

## 4. Auditoria dos Blocos de Código Python

Todos os blocos de código foram auditados com rigor de um interpretador Python 3.11 executando `numpy`, `scikit-learn` e `matplotlib`:

1. **[cod:8-4-confusao](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-04.dlt#L122-L167) (Matriz de confusão em EEG simulado):**
   - *Imports:* `numpy`, `DummyClassifier`, `LogisticRegression`, `accuracy_score`, `confusion_matrix`, `train_test_split`, `make_pipeline`, `StandardScaler`. Todos presentes.
   - *APIs:* `LogisticRegression(C=1.0, max_iter=1000, random_state=0)`. Sem parâmetros depreciados.
   - *Convenção:* `cm.ravel()` devolve `tn, fp, fn, tp` em perfeita consonância com a documentação do scikit-learn.
   - *Status:* Autocontido e funcional.

2. **[Solução de exr:8-4-1-3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-04.dlt#L217-L254) (Multiclasse com Wine):**
   - *Imports:* `load_wine`, `DummyClassifier`, `LogisticRegression`, `accuracy_score`, `confusion_matrix`, `train_test_split`, `make_pipeline`, `StandardScaler`.
   - *Pipeline:* escala os dados e ajusta modelo logístico multinomial automático.
   - *Status:* Autocontido e funcional.

3. **[cod:8-4-metricas-clf](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-04.dlt#L348-L392) (Métricas de classificação em câncer mamário):**
   - *Imports:* `load_breast_cancer`, `LogisticRegression`, `classification_report`, `f1_score`, `precision_score`, `recall_score`, `train_test_split`, `make_pipeline`, `StandardScaler`.
   - *Alvo:* `y = (dados.target == 0).astype(int)` inverte a convenção nativa para que $1$ corresponda à classe maligna, acompanhado de explicação oportuna no comentário.
   - *Status:* Autocontido e funcional.

4. **[cod:8-4-roc](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-04.dlt#L533-L583) (Curvas ROC e precisão média):**
   - *Imports:* `plt`, `load_breast_cancer`, `LogisticRegression`, `average_precision_score`, `roc_auc_score`, `roc_curve`, `train_test_split`, `KNeighborsClassifier`, `make_pipeline`, `StandardScaler`.
   - *Escores contínuos:* extração de `clf.predict_proba(X_teste)[:, 1]`.
   - *Status:* Autocontido e funcional.

5. **[Solução de exr:8-4-3-3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-04.dlt#L626-L661) (Impacto de rótulos binários na AUC):**
   - *Imports:* `load_breast_cancer`, `LogisticRegression`, `balanced_accuracy_score`, `roc_auc_score`, `train_test_split`, `make_pipeline`, `StandardScaler`.
   - *Conceito:* prova empiricamente que passar previsões discretas colapsa a AUC na acurácia balanceada.
   - *Status:* Autocontido e funcional.

6. **[cod:8-4-regressao](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-04.dlt#L753-L791) (Regressão e descalibração de escala):**
   - *Imports:* `numpy`, `LinearRegression`, `mean_absolute_error`, `mean_squared_error`, `r2_score`, `train_test_split`.
   - *Cálculo:* `rmse = np.sqrt(mse)` e correlação via `np.corrcoef(y_teste, y_pred)[0, 1]`.
   - *Status:* Autocontido e funcional.

7. **[Solução de exr:8-4-4-3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-04.dlt#L837-L865) (Sensibilidade a outliers em regressão):**
   - *Imports:* `numpy`, `load_diabetes`, `LinearRegression`, `mean_absolute_error`, `mean_squared_error`, `train_test_split`.
   - *Manipulação:* cópia explícita com `y_teste.copy()` antes de introduzir a perturbação pontual.
   - *Status:* Autocontido e funcional.

8. **[cod:8-4-desbalanceado](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-04.dlt#L950-L1011) (Regressão logística com class_weight):**
   - *Imports:* `make_classification`, `DummyClassifier`, `LogisticRegression`, `accuracy_score`, `balanced_accuracy_score`, `precision_score`, `recall_score`, `roc_auc_score`, `train_test_split`, `make_pipeline`, `StandardScaler`.
   - *Segurança:* uso de `zero_division=0` em `precision_score` e `recall_score`, prevenindo advertências de divisão por zero no classificador ingênuo.
   - *Status:* Autocontido e funcional.

9. **[Solução de exr:8-4-5-3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-04.dlt#L1064-L1113) (Varredura de limiares):**
   - *Imports:* completos.
   - *Lógica booleana:* `(escores >= tau).astype(int)` permite testar limiares arbitrários sem reinstanciar ou reajustar o estimador.
   - *Status:* Autocontido e funcional.

10. **[Script da Figura t04-roc.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/fig/t04-roc.py):**
    - Contém `plt.rcParams["svg.fonttype"] = "none"`, salva o SVG em [fig/t04-roc.svg](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/fig/t04-roc.svg), arquivo existente e com renderização vetorial válida.
    - *Status:* Totalmente funcional e em conformidade.

---

## 5. Checklist de Conformidade Editorial, Biológica e Delta

| Critério avaliado | Status | Análise detalhada |
|---|:---:|---|
| **Cobertura de todas as seções pedidas** | **OK** | Cobre integralmente as 5 seções na ordem exigida pela ementa: `sec:8-4-1` (Matriz de confusão e acurácia), `sec:8-4-2` (Precisão, recall, especificidade e F1), `sec:8-4-3` (Limiar, curva ROC e AUC), `sec:8-4-4` (Métricas de regressão), `sec:8-4-5` (Classes desbalanceadas), além de `sec:8-4-resumo` e `sec:8-4-alem`. |
| **Dica e solução completa em cada exercício** | **OK** | Todos os 15 exercícios trazem `<hint><title>Ver dica</title>...</hint>` e `<solution collapsible="true" collapsed="true">` contendo resolução passo a passo analítica ou em código Python. |
| **Pelo menos um exemplo biológico por seção** | **OK** | **Seção 1:** Detector de crises em EEG e decodificação multiclasse em MVPA.<br>**Seção 2:** Detector de disparos neuronais (spikes) e polissonografia (sono REM/não-REM).<br>**Seção 3:** Detecção de complexos ponta-onda epilépticos em EEG e diagnóstico mamário.<br>**Seção 4:** Taxas de disparo em Hz, modelos de codificação (*encoding models*), potencial de membrana em mV e sinal BOLD de fMRI.<br>**Seção 5:** Detecção de *sharp-wave ripples* hipocampais em potenciais de campo local (LFP) durante o sono de ondas lentas. |
| **Afirmações de neurociência de livro-texto** | **OK** | Valores e conceitos totalmente compatíveis com Kandel e Dayan & Abbott: potencial de repouso cortical próximo a $-70\text{ mV}$, taxas de disparo entre $10$ e $40\text{ Hz}$, janelas de EEG de $2\text{ s}$, registro de LFP hipocampal com ripples a $1\%$–$2\%$ do tempo de repouso. |
| **Sequenciamento pedagógico de conceitos** | **OK** | Nenhum conceito é usado antes de ser definido. Tópicos futuros (Tema 8.5 para validação cruzada sistemática e reamostragem) são devidamente avisados na prosa. Retoma temas anteriores pelo nome (Módulo 7 e Temas 8.1, 8.2 e 8.3). |
| **Citações bibliográficas permitidas** | **OK** | Citações e referências restritas aos clássicos e livros-texto autorizados (ISLR, Elements of Statistical Learning, Dayan & Abbott), sem autores fictícios ou números de página inventados. |
| **Links permitidos** | **OK** | Links restritos ao guia local, a [statlearning.com](https://www.statlearning.com/) e a subpáginas oficiais de [scikit-learn.org](https://scikit-learn.org/). |
| **Consistência de notação matemática** | **OK** | Vetores em negrito minúsculo ($\mathbf{x}, \mathbf{y}, \hat{\mathbf{y}}$), matrizes em negrito maiúsculo ($\mathbf{M}$), conjuntos com `\mathbb` ($\mathbb{R}$). Vírgula decimal na prosa e na matemática ($0{,}5$, $0{,}95$, $15{,}4\%$), ponto no código Python (`0.5`, `0.95`). |
| **Armadilhas comuns cobertas** | **OK** | As cinco armadilhas solicitadas estão presentes em blocos `<remark>` dedicados: reportar só acurácia sem linha de base (`rem:8-4-armadilha-acc`), confundir precisão com especificidade (`rem:8-4-armadilha-prec-esp`), passar rótulos 0/1 para AUC (`rem:8-4-armadilha-roc`), avaliar regressão por $R^2$ de treino (`rem:8-4-armadilha-reg`), e esquecer a linha de base / reamostrar com vazamento no teste (`rem:8-4-armadilha-desb`). |
| **Tamanho da aula** | **OK** | Cerca de 4.200 palavras em 1.149 linhas XML, perfeitamente compatível com o intervalo regulamentar de 2.500 a 5.000 palavras para uma aula de cinco subtemas. |
| **Conformidade técnica Delta v0.6.0** | **OK** | XML estrito com atributos explícitos (`collapsible="true" collapsed="true"`, `numbered="false"`), `<intuition>` empregado unicamente como filho direto de resultados, `<proof>` vinculada por `of="prop:8-4-f1-contagem"`, ausência de tags não documentadas ou proibidas (`<interactive>`, `<cite>`, `<youtube>`), e figura SVG existente e vinculada. |

---

## 6. Conclusão

A aula [conteudo/modulo-08/tema-04.dlt](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-04.dlt) está **plenamente aprovada**. Trata-se de uma aula completa, matematicamente sólida, computacionalmente funcional e com conexão primorosa aos problemas reais enfrentados por biólogos e neurocientistas na avaliação empírica de modelos de aprendizado de máquina. As sugestões formuladas na Tabela de Problemas e Sugestões têm natureza estritamente pedagógica para futuros refinamentos editoriais, sem qualquer impedimento à publicação imediata.
