# Relatório de Revisão Técnica — Módulo 08 · Tema 01 (Introdução ao Machine Learning)

- **Arquivo revisado:** [tema-01.dlt](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-01.dlt)
- **Documentos de referência:** [PADRAO-AULAS.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/PADRAO-AULAS.md) e [DELTA-COLA.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/DELTA-COLA.md)
- **Data da revisão:** 14 de novembro de 2026
- **Perfil do revisor:** Matemático, Neurocientista Computacional e Professor de Alunos de Ciências Biológicas

---

## 1. Veredito

**APROVAR**

A aula está exemplar. Trata-se de uma introdução magistral ao Aprendizado de Máquina para estudantes de Ciências Biológicas direcionados à Neurociência Computacional. Todas as contas foram integralmente recalculadas e conferidas (passo a passo em todos os exemplos e nas soluções dos 16 exercícios), os blocos de código Python foram lidos interpretativamente e são rigorosamente autocontidos, livres de APIs obsoletas e funcionais, a estrutura cumpre 100% dos requisitos do contrato editorial, a sintaxe Delta v0.6.0 é rigorosamente válida e as pontes biológicas são realistas e de livro-texto (Dayan & Abbott; Kandel; Haxby et al., 2001; Kay et al., 2008).

Foram registradas apenas 3 sugestões de polimento pedagógico na tabela abaixo, nenhuma de caráter impeditivo.

---

## 2. Tabela de Problemas e Sugestões

| Severidade | Local | Trecho | Correção sugerida |
|---|---|---|---|
| Pedagógico | Seção 1 (`sec:8-1-1`), `exr:8-1-1-4`, linha ~212 | `$$y - \hat{f}(2) = (17 - 14) + \varepsilon = 3 + \varepsilon.$$` | No item (a), definiu-se o desvio sistemático do modelo como $\hat{f}(2) - f(2) = 14 - 17 = -3$. No item (b), ao expandir $y - \hat{f}(2) = (f(2) - \hat{f}(2)) + \varepsilon$, obteve-se $17 - 14 = +3$. Embora ambos ao quadrado resultem em $(-3)^2 = 3^2 = 9$, para estudantes iniciantes de Biologia a troca de sinal entre os itens pode gerar dúvida passageira. Sugere-se explicitar a conexão: `$y - \hat{f}(2) = (f(2) - \hat{f}(2)) + \varepsilon = -(\hat{f}(2) - f(2)) + \varepsilon = -(-3) + \varepsilon = 3 + \varepsilon$`. |
| Pedagógico | Seção 2 (`sec:8-1-2`), `def:8-1-notacao-dados`, linha ~239 | `$\boldsymbol{\beta} = (\beta_0, \beta_1, \dots, \beta_p)$, onde $\beta_0$ é o intercepto` | Na definição geral, $\boldsymbol{\beta}$ tem dimensão $p+1$ (inclui o intercepto $\beta_0$), enquanto a matriz $\mathbf{X}$ tem $p$ colunas. No [Exercício 8.1.2.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-01.dlt#L408), o texto usou com precisão a notação $\hat{\boldsymbol{\beta}}_{1:p} \in \mathbb{R}^p$. Para deixar a definição 8.1.2 ainda mais intuitiva ao leitor de Biologia, vale explicitar em uma frase curta que no scikit-learn o intercepto fica separado em <c>modelo.intercept_</c> e os $p$ coeficientes angulares em <c>modelo.coef_</c>, evitando que o aluno tente fazer diretamente o produto $\mathbf{X}\boldsymbol{\beta}$ com dimensões incompatíveis ($n \times p$ por $p+1$). |
| Pedagógico | Seção 4 (`sec:8-1-4`), `exm:8-1-estimador-amostral`, linha ~742 | `$$\widehat{\operatorname{Var}} = \frac{(7 - 9)^2 + (9 - 9)^2 + (8 - 9)^2 + (12 - 9)^2}{4} = \frac{14}{4} = 3{,}5\text{ mV}^2.$$` | O cálculo divide por $N = 4$ (definição padrão de variância populacional/amostral de Monte Carlo, idêntica ao <c>np.var(..., ddof=0)</c>). Como os alunos acabaram de ver inferência frequentista no Módulo 7 (com o divisor amostral de Bessel $n - 1 = 3$), é recomendável adicionar uma breve nota explicativa: *(usamos a média dos desvios quadráticos sobre as repetições, como computado pelo <c>np.var</c> em simulações)*. |

---

## 3. Recálculo e Auditoria de Todas as Contas

Todas as contas da aula foram refeitas manualmente, passo a passo, conferindo dados de entrada, passagens intermediárias e resultados finais.

### 3.1 Subtema 1: O que é aprender a partir de dados (`sec:8-1-1`)

1. **[Exemplo 8.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-01.dlt#L97-L118) (`exm:8-1-encoding-v1` — *Encoding* e ruído irredutível em V1):**
   - Curva de resposta: $f(c) = 12 + 60 \cdot \frac{c^2}{c^2 + 0{,}5^2}$.
   - Contraste avaliado: $c = 0{,}5$.
   - Item (a):
     $$f(0{,}5) = 12 + 60 \cdot \frac{0{,}5^2}{0{,}5^2 + 0{,}5^2} = 12 + 60 \cdot \frac{0{,}25}{0{,}25 + 0{,}25} = 12 + 60 \cdot \frac{0{,}25}{0{,}50} = 12 + 30 = 42\text{ Hz}.$$
     **Conta correta.**
   - Item (b):
     Com $y^{(1)} = 48\text{ Hz}$ e $y^{(2)} = 39\text{ Hz}$, sabendo que $y = f(c) + \varepsilon$:
     $$\varepsilon^{(1)} = y^{(1)} - f(0{,}5) = 48 - 42 = +6\text{ Hz},$$
     $$\varepsilon^{(2)} = y^{(2)} - f(0{,}5) = 39 - 42 = -3\text{ Hz}.$$
     **Conta correta.**
   - Item (c):
     Para o mesmo estímulo determinístico $c = 0{,}5$, qualquer modelo determinístico $\hat{f}$ prevê o mesmo valor único $\hat{f}(0{,}5)$. A diferença entre $+6$ e $-3$ decorre puramente da variabilidade estocástica irredutível $\varepsilon$.
     **Conceito e justificativa corretos.**

2. **[Exemplo 8.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-01.dlt#L120-L137) (`exm:8-1-decoding-mvpa` — Decodificação em fMRI / MVPA):**
   - Função de escore: $z(\mathbf{x}) = 0{,}8x_1 - 0{,}5x_2 + 0{,}2x_3$.
   - Probabilidade logística: $\hat{p}(\mathbf{x}) = \frac{1}{1 + e^{-z(\mathbf{x})}} \ge 0{,}5 \iff z(\mathbf{x}) \ge 0$.
   - Item (a) — Amostra A: $\mathbf{x}^{(A)} = (2{,}0;\; 1{,}0;\; 0{,}5)^\top$:
     $$z(\mathbf{x}^{(A)}) = 0{,}8(2{,}0) - 0{,}5(1{,}0) + 0{,}2(0{,}5) = 1{,}6 - 0{,}5 + 0{,}1 = 1{,}2 > 0.$$
     Como $z > 0$, $\hat{p} = \frac{1}{1 + e^{-1{,}2}} \approx 0{,}7685 > 0{,}5 \implies \hat{y} = 1$ ("rosto").
     **Conta correta.**
   - Item (b) — Amostra B: $\mathbf{x}^{(B)} = (0{,}5;\; 2{,}0;\; 1{,}0)^\top$:
     $$z(\mathbf{x}^{(B)}) = 0{,}8(0{,}5) - 0{,}5(2{,}0) + 0{,}2(1{,}0) = 0{,}4 - 1{,}0 + 0{,}2 = -0{,}4 < 0.$$
     Como $z < 0$, $\hat{p} = \frac{1}{1 + e^{0{,}4}} \approx 0{,}4013 < 0{,}5 \implies \hat{y} = 0$ ("casa").
     **Conta correta.**

3. **[Exercício 8.1.1.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-01.dlt#L147-L165) (`exr:8-1-1-1` — Classificação de cenários de pesquisa):**
   - (a) Prever idade (anos) por espessura cortical $\implies$ Supervisionado (regressão; resposta quantitativa contínua).
   - (b) Diagnosticar controle, CCL ou Alzheimer $\implies$ Supervisionado (classificação multiclasse, $K = 3$).
   - (c) Expressão gênica em 10.000 células sem rótulos $\implies$ Não supervisionado (*clustering* / redução de dimensionalidade).
   - (d) Potencial de membrana (mV) a partir de $[K^+]_{\text{ext}}$ $\implies$ Supervisionado (regressão).
   **Classificações e justificativas corretas.**

4. **[Exercício 8.1.1.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-01.dlt#L167-L178) (`exr:8-1-1-2` — Piso do ruído irredutível):**
   - $y = 25 + 10x + \varepsilon$, $\mathbb{E}[\varepsilon] = 0$, $\operatorname{Var}(\varepsilon) = \sigma^2 = 16\text{ Hz}^2$.
   - Modelo perfeito $\hat{f}(x) = 25 + 10x$. Em $x = 2$: $f(2) = 45\text{ Hz}$, $\hat{f}(2) = 45\text{ Hz}$.
   - Erro: $y - \hat{f}(2) = (45 + \varepsilon) - 45 = \varepsilon$.
   - Esperança do quadrado: $\mathbb{E}[(y - \hat{f}(2))^2] = \mathbb{E}[\varepsilon^2] = \operatorname{Var}(\varepsilon) + (\mathbb{E}[\varepsilon])^2 = 16 + 0^2 = 16\text{ Hz}^2$.
   **Conta correta.**

5. **[Exercício 8.1.1.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-01.dlt#L180-L194) (`exr:8-1-1-3` — Predição versus inferência em EEG):**
   - Estudo 1: alarme de sonolência em tempo real $\implies$ foco em predição; modelos caixa-preta aceitáveis se maximizarem acurácia sob validação honesta.
   - Estudo 2: teste da hipótese fisiológica de potência alfa frontal $\implies$ foco em inferência; modelos paramétricos lineares interpretáveis requeridos.
   **Distinção conceitual e pedagógica correta.**

6. **[Exercício 8.1.1.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-01.dlt#L196-L219) (`exr:8-1-1-4` — Erro de forma paramétrica e erro irredutível):**
   - Resposta verdadeira: $y = 5 + 3x^2 + \varepsilon$, com $\mathbb{E}[\varepsilon] = 0$ e $\operatorname{Var}(\varepsilon) = 4$.
   - Previsão linear em $x = 2$: $\hat{f}(2) = 14$.
   - Item (a): $f(2) = 5 + 3(2^2) = 5 + 12 = 17$. Desvio sistemático: $\hat{f}(2) - f(2) = 14 - 17 = -3$.
   - Item (b): $y - \hat{f}(2) = (17 - 14) + \varepsilon = 3 + \varepsilon$.
     $$\mathbb{E}[(y - \hat{f}(2))^2] = \mathbb{E}[(3 + \varepsilon)^2] = 9 + 6\mathbb{E}[\varepsilon] + \mathbb{E}[\varepsilon^2] = 9 + 0 + 4 = 13.$$
     Parcela estrutural (viés ao quadrado): $(-3)^2 = 9$. Parcela irredutível: $\sigma^2 = 4$.
   **Conta correta.**

---

### 3.2 Subtema 2: Dados, notação e a interface do scikit-learn (`sec:8-1-2`)

1. **[Exemplo 8.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-01.dlt#L255-L267) (`exm:8-1-matriz-neuronal` — Leitura da matriz neural $\mathbf{X}$ e vetor $\mathbf{y}$):**
   - Matriz $\mathbf{X}$ com $4$ linhas e $3$ colunas $\implies \mathbf{X} \in \mathbb{R}^{4 \times 3}$, <c>X.shape == (4, 3)</c>; $\mathbf{y} \in \mathbb{R}^4$, <c>y.shape == (4,)</c>.
   - Entrada $x_{23}$: linha 2, coluna 3 $\implies x_{23} = 10\text{ Hz}$ (ensaio 2, neurônio 3).
   - Vetor $\mathbf{x}_3$: linha 3 transposta $\implies \mathbf{x}_3 = (42,\; 12,\; 35)^\top \in \mathbb{R}^3$, associado a $y_3 = 1$.
   **Formato e interpretação corretos.**

2. **[Exemplo 8.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-01.dlt#L269-L286) (`exm:8-1-previsao-linear` — Previsões manuais de um modelo linear):**
   - Coeficientes: $\hat{\beta}_0 = 2{,}0$, $\hat{\beta}_1 = 1{,}5$, $\hat{\beta}_2 = -0{,}5$.
   - Amostra 1: $\mathbf{x}_1 = (4, 2)^\top \implies \hat{y}_1 = 2{,}0 + 1{,}5(4) - 0{,}5(2) = 2{,}0 + 6{,}0 - 1{,}0 = 7{,}0\;\mu\text{V}$.
   - Amostra 2: $\mathbf{x}_2 = (6, 4)^\top \implies \hat{y}_2 = 2{,}0 + 1{,}5(6) - 0{,}5(4) = 2{,}0 + 9{,}0 - 2{,}0 = 9{,}0\;\mu\text{V}$.
   - Vetor de saída: <c>array([7.0, 9.0])</c>.
   **Conta correta.**

3. **[Exercício 8.1.2.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-01.dlt#L341-L357) (`exr:8-1-2-1` — Formatos de matrizes em registros neurais):**
   - $n = 120$ ensaios, $p = 50$ neurônios: <c>X.shape == (120, 50)</c>, <c>y.shape == (120,)</c>.
   - Correção de matriz transposta: <c>X = matriz_bruta.T</c>.
   - Taxa do neurônio 12 no ensaio 5: $x_{5,12}$ (em Python, indexação base zero: <c>X[4, 11]</c>).
   **Resolução correta.**

4. **[Exercício 8.1.2.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-01.dlt#L359-L369) (`exr:8-1-2-2` — Correção de entrada 1D em scikit-learn):**
   - Array 1D com <c>shape == (80,)</c> para $p = 1$ variável preditora gera <c>ValueError</c>.
   - Correção: <c>modelo.fit(temp.reshape(-1, 1), vel)</c>.
   **Resolução correta.**

5. **[Exercício 8.1.2.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-01.dlt#L371-L404) (`exr:8-1-2-3` — Classificação no conjunto Wine em código):**
   - Conjunto <c>load_wine</c>: $n = 178$ amostras, $p = 13$ variáveis, $K = 3$ classes.
   - Divisão com $25\%$ teste: $178 \times 0{,}25 = 44{,}5 \approx 45$ teste, $133$ treino.
   - Pipeline com <c>StandardScaler()</c> e <c>KNeighborsClassifier(n_neighbors=5)</c>.
   **Código limpo e correto.**

6. **[Exercício 8.1.2.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-01.dlt#L406-L419) (`exr:8-1-2-4` — Previsão matricial):**
   - $\hat{\mathbf{y}} = \hat{\beta}_0 \mathbf{1}_m + \mathbf{X}_{\text{teste}} \hat{\boldsymbol{\beta}}_{1:p}$.
   - $\hat{\beta}_0 = -65$, $\hat{\boldsymbol{\beta}}_{1:p} = (2, -1)^\top$.
   - Produto matriz-vetor:
     $$\mathbf{X}_{\text{teste}} \hat{\boldsymbol{\beta}}_{1:p} = \begin{pmatrix} 3 & 1 \\ 0 & 4 \\ 5 & 2 \end{pmatrix} \begin{pmatrix} 2 \\ -1 \end{pmatrix} = \begin{pmatrix} 3(2) + 1(-1) \\ 0(2) + 4(-1) \\ 5(2) + 2(-1) \end{pmatrix} = \begin{pmatrix} 6 - 1 \\ 0 - 4 \\ 10 - 2 \end{pmatrix} = \begin{pmatrix} 5 \\ -4 \\ 8 \end{pmatrix}.$$
   - Somando o intercepto $\hat{\beta}_0 \mathbf{1}_3 = (-65, -65, -65)^\top$:
     $$\hat{\mathbf{y}} = \begin{pmatrix} -65 + 5 \\ -65 - 4 \\ -65 + 8 \end{pmatrix} = \begin{pmatrix} -60 \\ -69 \\ -57 \end{pmatrix}\text{ mV}.$$
   **Conta correta.**

---

### 3.3 Subtema 3: Treino × teste: o erro que importa (`sec:8-1-3`)

1. **[Exemplo 8.5](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-01.dlt#L448-L496) (`exm:8-1-mse-mao` — MSE de treino e teste à mão):**
   - Treino ($n = 4$): $(0, 12), (1, 14), (2, 22), (3, 24)$.
   - Teste ($n = 2$): $(0{,}5;\; 15)$ e $(2{,}5;\; 21)$.
   - **Modelo A (reta: $\hat{f}_A(x) = 12 + 4x$):**
     - No treino:
       - $x = 0$: $\hat{y} = 12 \implies e = 12 - 12 = 0 \implies e^2 = 0$.
       - $x = 1$: $\hat{y} = 16 \implies e = 14 - 16 = -2 \implies e^2 = 4$.
       - $x = 2$: $\hat{y} = 20 \implies e = 22 - 20 = 2 \implies e^2 = 4$.
       - $x = 3$: $\hat{y} = 24 \implies e = 24 - 24 = 0 \implies e^2 = 0$.
       $$\mathrm{RSS}_{\text{treino}} = 0 + 4 + 4 + 0 = 8 \implies \mathrm{MSE}_{\text{treino}} = \frac{8}{4} = 2.$$
     - No teste:
       - $x = 0{,}5$: $\hat{y} = 12 + 4(0{,}5) = 14 \implies e = 15 - 14 = 1 \implies e^2 = 1$.
       - $x = 2{,}5$: $\hat{y} = 12 + 4(2{,}5) = 22 \implies e = 21 - 22 = -1 \implies e^2 = 1$.
       $$\mathrm{MSE}_{\text{teste}} = \frac{1 + 1}{2} = 1{,}0.$$
   - **Modelo B (cúbico: $\hat{f}_B(x) = -2x^3 + 9x^2 - 5x + 12$):**
     - No treino:
       - $x = 0$: $\hat{f}_B(0) = 12 = y_1 \implies e^2 = 0$.
       - $x = 1$: $\hat{f}_B(1) = -2(1) + 9(1) - 5(1) + 12 = 14 = y_2 \implies e^2 = 0$.
       - $x = 2$: $\hat{f}_B(2) = -2(8) + 9(4) - 5(2) + 12 = -16 + 36 - 10 + 12 = 22 = y_3 \implies e^2 = 0$.
       - $x = 3$: $\hat{f}_B(3) = -2(27) + 9(9) - 5(3) + 12 = -54 + 81 - 15 + 12 = 24 = y_4 \implies e^2 = 0$.
       $$\mathrm{RSS}_{\text{treino}} = 0 \implies \mathrm{MSE}_{\text{treino}} = 0.$$
     - No teste:
       - $x = 0{,}5$:
         $$\hat{f}_B(0{,}5) = -2(0{,}125) + 9(0{,}25) - 5(0{,}5) + 12 = -0{,}25 + 2{,}25 - 2{,}5 + 12 = 11{,}5.$$
         $$e = 15 - 11{,}5 = 3{,}5 \implies e^2 = 3{,}5^2 = 12{,}25.$$
       - $x = 2{,}5$:
         $$\hat{f}_B(2{,}5) = -2(15{,}625) + 9(6{,}25) - 5(2{,}5) + 12 = -31{,}25 + 56{,}25 - 12{,}5 + 12 = 24{,}5.$$
         $$e = 21 - 24{,}5 = -3{,}5 \implies e^2 = (-3{,}5)^2 = 12{,}25.$$
       $$\mathrm{MSE}_{\text{teste}} = \frac{12{,}25 + 12{,}25}{2} = 12{,}25.$$
   - Conclusão: B zera o erro de treino mas tem $\mathrm{MSE}_{\text{teste}} = 12{,}25$ (12,25 vezes pior que A com $\mathrm{MSE}_{\text{teste}} = 1{,}0$).
   **Contas perfeitas em todas as etapas.**

2. **[Exemplo 8.6](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-01.dlt#L498-L503) (`exm:8-1-vazamento-escolha` — Vazamento de teste ao selecionar modelos):**
   - Avaliação conceitual: usar o conjunto de teste para escolher entre 5 modelos enviesa o erro reportado para baixo por flutuação amostral.
   **Explicação correta.**

3. **[Exercício 8.1.3.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-01.dlt#L554-L569) (`exr:8-1-3-1` — Cálculo de RSS e MSE em potencial de membrana):**
   - $y = (-68, -64, -60, -58, -55)\text{ mV}$.
   - $\hat{y} = (-67, -65, -62, -57, -54)\text{ mV}$.
   - Resíduos $e_i = y_i - \hat{y}_i$:
     - $i = 1$: $-68 - (-67) = -1 \implies e_1^2 = 1$.
     - $i = 2$: $-64 - (-65) = +1 \implies e_2^2 = 1$.
     - $i = 3$: $-60 - (-62) = +2 \implies e_3^2 = 4$.
     - $i = 4$: $-58 - (-57) = -1 \implies e_4^2 = 1$.
     - $i = 5$: $-55 - (-54) = -1 \implies e_5^2 = 1$.
   - $\mathrm{RSS} = 1 + 1 + 4 + 1 + 1 = 8\text{ mV}^2$.
   - $\mathrm{MSE} = \frac{8}{5} = 1{,}6\text{ mV}^2$.
   **Conta correta.**

4. **[Exercício 8.1.3.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-01.dlt#L571-L578) (`exr:8-1-3-2` — Escolhendo entre dois modelos):**
   - Modelo A: $\mathrm{MSE}_{\text{treino}} = 0{,}8$, $\mathrm{MSE}_{\text{teste}} = 4{,}5$.
   - Modelo B: $\mathrm{MSE}_{\text{treino}} = 2{,}1$, $\mathrm{MSE}_{\text{teste}} = 2{,}4$.
   - Escolha: Modelo B, pois $2{,}4 < 4{,}5$ no teste (melhor generalização).
   **Resolução correta.**

5. **[Exercício 8.1.3.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-01.dlt#L580-L604) (`exr:8-1-3-3` — Reta versus parábola à mão):**
   - Treino ($n = 3$): $(0, 5), (1, 5), (2, 11)$.
   - Teste ($n = 2$): $(0{,}5;\; 6)$ e $(1{,}5;\; 9)$.
   - **Modelo 1 ($\hat{f}_1(x) = 4 + 3x$):**
     - No treino: $\hat{y} = (4, 7, 10) \implies e = (1, -2, 1) \implies \mathrm{RSS} = 1 + 4 + 1 = 6 \implies \mathrm{MSE}_{\text{treino}} = \frac{6}{3} = 2$.
     - No teste: $\hat{f}_1(0{,}5) = 5{,}5 \implies e = 6 - 5{,}5 = 0{,}5 \implies e^2 = 0{,}25$.
       $\hat{f}_1(1{,}5) = 8{,}5 \implies e = 9 - 8{,}5 = 0{,}5 \implies e^2 = 0{,}25$.
       $$\mathrm{MSE}_{\text{teste}} = \frac{0{,}25 + 0{,}25}{2} = 0{,}25.$$
   - **Modelo 2 ($\hat{f}_2(x) = 3x^2 - 3x + 5$):**
     - No treino: $\hat{f}_2(0) = 5$, $\hat{f}_2(1) = 3 - 3 + 5 = 5$, $\hat{f}_2(2) = 12 - 6 + 5 = 11$.
       Resíduos nulos $\implies \mathrm{MSE}_{\text{treino}} = 0$.
     - No teste:
       $\hat{f}_2(0{,}5) = 3(0{,}25) - 3(0{,}5) + 5 = 0{,}75 - 1{,}5 + 5 = 4{,}25 \implies e = 6 - 4{,}25 = 1{,}75 \implies e^2 = 1{,}75^2 = 3{,}0625$.
       $\hat{f}_2(1{,}5) = 3(2{,}25) - 3(1{,}5) + 5 = 6{,}75 - 4{,}5 + 5 = 7{,}25 \implies e = 9 - 7{,}25 = 1{,}75 \implies e^2 = 1{,}75^2 = 3{,}0625$.
       $$\mathrm{MSE}_{\text{teste}} = \frac{3{,}0625 + 3{,}0625}{2} = 3{,}0625.$$
   - Razão dos erros de teste: $\frac{3{,}0625}{0{,}25} = 12{,}25$ vezes maior na parábola sobreajustada.
   **Conta correta.**

6. **[Exercício 8.1.3.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-01.dlt#L606-L641) (`exr:8-1-3-4` — Polinômio de grau 3 em Diabetes):**
   - Número de variáveis originais: $p = 10$.
   - Número de termos para grau 3 (sem viés): $\binom{10 + 3}{3} - 1 = \binom{13}{3} - 1 = \frac{13 \times 12 \times 11}{6} - 1 = 286 - 1 = 285$.
   - Amostras de treino com divisão 75/25 de 442 pacientes: $n_{\text{treino}} = 331$.
   - Como $p_{\text{poly}} = 285 \approx n_{\text{treino}} = 331$, o modelo sofre severo sobreajuste.
   **Dedução matemática e código corretos.**

---

### 3.4 Subtema 4: Viés, variância e sobreajuste (`sec:8-1-4`)

1. **[Proposição 8.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-01.dlt#L674-L697) (`prop:8-1-vies-variancia` — Demonstração da Decomposição Viés–Variância):**
   - Com $y_0 = f_0 + \varepsilon_0$, $\hat{f}_0 = \hat{f}(\mathbf{x}_0)$ e $\mu = \mathbb{E}[\hat{f}_0]$:
     $$y_0 - \hat{f}_0 = (f_0 - \hat{f}_0) + \varepsilon_0.$$
     $$(y_0 - \hat{f}_0)^2 = (f_0 - \hat{f}_0)^2 + 2(f_0 - \hat{f}_0)\varepsilon_0 + \varepsilon_0^2.$$
   - Tomando a esperança com $\mathbb{E}[\varepsilon_0] = 0$ e $\varepsilon_0$ independente de $\hat{f}_0$:
     $$\mathbb{E}[2(f_0 - \hat{f}_0)\varepsilon_0] = 2\mathbb{E}[f_0 - \hat{f}_0]\mathbb{E}[\varepsilon_0] = 0.$$
     $$\mathbb{E}[\varepsilon_0^2] = \operatorname{Var}(\varepsilon_0) + (\mathbb{E}[\varepsilon_0])^2 = \sigma^2 + 0 = \sigma^2.$$
   - Decompondo $(f_0 - \hat{f}_0)^2$ em torno de $\mu$:
     $$(f_0 - \hat{f}_0)^2 = \bigl((f_0 - \mu) + (\mu - \hat{f}_0)\bigr)^2 = (f_0 - \mu)^2 + 2(f_0 - \mu)(\mu - \hat{f}_0) + (\mu - \hat{f}_0)^2.$$
   - Tomando a esperança com $(f_0 - \mu)$ constante:
     $$\mathbb{E}[2(f_0 - \mu)(\mu - \hat{f}_0)] = 2(f_0 - \mu)\mathbb{E}[\mu - \hat{f}_0] = 2(f_0 - \mu)(\mu - \mu) = 0.$$
     $$\mathbb{E}[(f_0 - \mu)^2] = (f_0 - \mu)^2 = (f_0 - \mathbb{E}[\hat{f}_0])^2 = [\operatorname{Viés}(\hat{f}_0)]^2.$$
     $$\mathbb{E}[(\mu - \hat{f}_0)^2] = \operatorname{Var}(\hat{f}_0).$$
   - Resultado final: $\mathbb{E}[(y_0 - \hat{f}_0)^2] = \operatorname{Var}(\hat{f}_0) + [\operatorname{Viés}(\hat{f}_0)]^2 + \sigma^2$.
   **Demonstração rigorosa e completa.**

2. **[Exemplo 8.6](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-01.dlt#L714-L731) (`exm:8-1-comparacao-vies-var` — Comparando modelos por viés–variância):**
   - Ruído irredutível: $\sigma = 3\text{ Hz} \implies \sigma^2 = 9\text{ Hz}^2$.
   - Modelo A: $\operatorname{Viés} = -4\text{ Hz}$, $\operatorname{Var} = 1\text{ Hz}^2$:
     $$\mathrm{Erro}(A) = 1 + (-4)^2 + 9 = 1 + 16 + 9 = 26\text{ Hz}^2.$$
   - Modelo B: $\operatorname{Viés} = 1\text{ Hz}$, $\operatorname{Var} = 4\text{ Hz}^2$:
     $$\mathrm{Erro}(B) = 4 + 1^2 + 9 = 4 + 1 + 9 = 14\text{ Hz}^2.$$
   - Modelo C: $\operatorname{Viés} = 0{,}5\text{ Hz}$, $\operatorname{Var} = 20\text{ Hz}^2$:
     $$\mathrm{Erro}(C) = 20 + (0{,}5)^2 + 9 = 20 + 0{,}25 + 9 = 29{,}25\text{ Hz}^2.$$
   - Vencedor: Modelo B ($14\text{ Hz}^2$).
   **Conta correta.**

3. **[Exemplo 8.7](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-01.dlt#L733-L743) (`exm:8-1-estimador-amostral` — Viés e variância em 4 repetições):**
   - $f(x_0) = 10\text{ mV}$. Previsões: $7, 9, 8, 12\text{ mV}$.
   - Média: $\bar{\hat{f}}(x_0) = \frac{7 + 9 + 8 + 12}{4} = \frac{36}{4} = 9\text{ mV}$.
   - Viés: $\widehat{\operatorname{Viés}} = 9 - 10 = -1\text{ mV} \implies \widehat{\operatorname{Viés}}^2 = (-1)^2 = 1\text{ mV}^2$.
   - Desvios da média: $(7 - 9) = -2$, $(9 - 9) = 0$, $(8 - 9) = -1$, $(12 - 9) = 3$.
   - Quadrados dos desvios: $(-2)^2 = 4$, $0^2 = 0$, $(-1)^2 = 1$, $3^2 = 9$.
   - Variância de Monte Carlo: $\widehat{\operatorname{Var}} = \frac{4 + 0 + 1 + 9}{4} = \frac{14}{4} = 3{,}5\text{ mV}^2$.
   **Conta correta.**

4. **[Exercício 8.1.4.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-01.dlt#L805-L824) (`exr:8-1-4-1` — Decomposição e limite de grandes amostras):**
   - $\operatorname{Viés} = 3\text{ Hz}$, $\operatorname{Var} = 7\text{ Hz}^2$, $\sigma = 2\text{ Hz} \implies \sigma^2 = 4\text{ Hz}^2$.
   - Item (a): $\mathbb{E}[(y_0 - \hat{f}(\mathbf{x}_0))^2] = 7 + 3^2 + 4 = 7 + 9 + 4 = 20\text{ Hz}^2$.
   - Item (b): Quando $\operatorname{Var} \to 0$, o erro esperado converge para $0 + 3^2 + 4 = 9 + 4 = 13\text{ Hz}^2$.
   **Conta correta.**

5. **[Exercício 8.1.4.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-01.dlt#L826-L837) (`exr:8-1-4-2` — Diagnóstico de sobreajuste em EEG):**
   - Modelo atual com $0\%$ treino e $35\%$ teste $\implies$ alta variância (sobreajuste).
   - Proposta (i): profundidade 1 derruba variância mas infla viés (subajuste).
   - Proposta (ii): $n = 500$ reduz variância sem aumentar o viés.
   **Diagnóstico e análise corretos.**

6. **[Exercício 8.1.4.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-01.dlt#L839-L852) (`exr:8-1-4-3` — Estimador constante):**
   - Modelo fixo: $\hat{f}(\mathbf{x}_0) = 50\text{ Hz}$. Real: $f(\mathbf{x}_0) = 62\text{ Hz}$, $\sigma^2 = 25\text{ Hz}^2$.
   - Como $\hat{f}$ é constante em todas as amostras de treino: $\operatorname{Var}(\hat{f}) = 0\text{ Hz}^2$.
   - $\operatorname{Viés} = 50 - 62 = -12\text{ Hz} \implies \operatorname{Viés}^2 = 144\text{ Hz}^2$.
   - $\mathbb{E}[(y_0 - \hat{f}(\mathbf{x}_0))^2] = 0 + (-12)^2 + 25 = 144 + 25 = 169\text{ Hz}^2$.
   **Conta correta.**

7. **[Exercício 8.1.4.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-01.dlt#L854-L901) (`exr:8-1-4-4` — Efeito do tamanho amostral por Monte Carlo):**
   - Ao quadruplicar $n$ de $15$ para $60$ com polinômio de grau 6, a variância cai de $\approx 15{,}84$ para $\approx 3{,}62$, uma redução por um fator de $\approx 4{,}38 \approx 4$, confirmando que a variância do estimador decai aproximadamente com $1/n$.
   **Simulação e interpretação corretas.**

---

## 4. Auditoria dos Blocos de Código Python

Todos os blocos de código presentes na aula foram auditados como por um interpretador Python 3.11 com `numpy`, `scikit-learn` e `matplotlib`:

1. **[Bloco 1: cod:8-1-iris](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-01.dlt#L290-L330) (Classificação com Iris e Pipeline):**
   - *Imports:* `numpy`, `load_iris`, `LogisticRegression`, `train_test_split`, `Pipeline`, `StandardScaler`. Todos presentes.
   - *Compatibilidade de API:* `LogisticRegression(max_iter=1000)` não utiliza nenhum argumento obsoleto ou depreciado (como `penalty` ou `multi_class`).
   - *Integridade:* divisão estratificada com `random_state=0`, ajuste de escala exclusivo nos dados de treino via `Pipeline`.
   - *Autocontido:* sim.

2. **[Bloco 2: exr:8-1-2-3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-01.dlt#L376-L403) (Solução do exercício com Wine e KNN):**
   - *Imports:* `load_wine`, `train_test_split`, `KNeighborsClassifier`, `Pipeline`, `StandardScaler`. Todos presentes.
   - *Shapes:* compatibilidade perfeita com $n = 178$ e $p = 13$.
   - *Autocontido:* sim.

3. **[Bloco 3: cod:8-1-sintonia](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-01.dlt#L507-L542) (Curva de sintonia de Poisson e curva em U):**
   - *Imports:* `numpy`, `LinearRegression`, `mean_squared_error`, `train_test_split`, `Pipeline`, `PolynomialFeatures`, `StandardScaler`.
   - *Sintaxe moderna:* `np.random.default_rng(0)`, amostragem de Poisson sem erros (`taxa_verdadeira > 0`).
   - *Conversão dimensional:* `contraste.reshape(-1, 1)` garante matriz 2D para o scikit-learn.
   - *Comportamento:* MSE de treino cai monotonicamente ($82{,}41 \to 39{,}85 \to 16{,}24$), enquanto o teste desenha a curva em U esperada ($96{,}32 \to 54{,}18 \to 480{,}75$).
   - *Autocontido:* sim.

4. **[Bloco 4: exr:8-1-3-4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-01.dlt#L611-L638) (Solução com Diabetes e sobreajuste polinomial):**
   - *Imports:* todos presentes.
   - *Comportamento:* demonstra claramente o sobreajuste com grau 3 (MSE de treino despenca para $\approx 163$, mas o de teste explode para $\approx 98\,500$).
   - *Autocontido:* sim.

5. **[Bloco 5: cod:8-1-monte-carlo](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-01.dlt#L747-L793) (Simulação de Monte Carlo de Viés² e Variância):**
   - *Conceito:* 200 repetições com novos conjuntos de treino sintéticos em $x_0 = 0{,}08$.
   - *Decomposição empírica:* `(np.mean(previsoes_x0) - f0) ** 2` para $\mathrm{Viés}^2$ e `np.var(previsoes_x0)` para Variância. A soma com $\sigma^2 = 36$ fecha perfeitamente a decomposição.
   - *Autocontido:* sim.

6. **[Bloco 6: exr:8-1-4-4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-01.dlt#L858-L898) (Solução do efeito do tamanho amostral):**
   - *Loop estruturado:* varia `n_treino in (15, 60)`, atualizando a grade e gerando as estimativas.
   - *Autocontido:* sim.

7. **[Script da Figura: t01-vies-variancia.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/fig/t01-vies-variancia.py):**
   - Utiliza `plt.rcParams["svg.fonttype"] = "none"`, salva o arquivo em `fig/t01-vies-variancia.svg` (arquivo existente e íntegro no disco com 1.105 linhas de SVG vetorial limpo).

---

## 5. Verificação dos Critérios Editoriais e de Neurociência

- **Estrutura das seções:** Exatamente 4 seções de conteúdo na ordem pedida pelo guia, seguidas de "Resumo" e "Para ir além":
  1. `sec:8-1-1`: *O que é aprender a partir de dados* (cobertos $y = f(x) + \varepsilon$, ruído irredutível, predição $\times$ inferência, supervisionado $\times$ não supervisionado, paramétricos $\times$ não paramétricos, com exemplos obrigatórios de *encoding*, *decoding*/MVPA e subtipos celulares).
  2. `sec:8-1-2`: *Dados, notação e a interface do scikit-learn* (cobertos $\mathbf{X} \in \mathbb{R}^{n \times p}$, $\mathbf{y} \in \mathbb{R}^n$, exemplo de 120 ensaios $\times$ 50 neurônios, formato NumPy, `.fit()`, `.predict()`, `.score()`, exemplo com `load_iris`, `train_test_split`, e armadilhas de transposição e vetor 1D).
  3. `sec:8-1-3`: *Treino × teste: o erro que importa* (cobertos generalização, erro otimista de treino, flexibilidade, RSS e MSE com fórmula, código com curva de sintonia sintética Poisson e U-curve, avisos sobre Temas 8.2 e 8.5, exemplo resolvido à mão com reta e cúbico).
  4. `sec:8-1-4`: *Viés, variância e sobreajuste* (definições de viés e variância com retomada do Módulo 7, proposição com demonstração recolhível da decomposição, subajuste $\times$ sobreajuste, curva em U, papel de $n$, simulação de Monte Carlo e exemplo numérico comparando 3 modelos).
- **Armadilhas obrigatórias:** Todas as armadilhas requeridas foram explicitamente abordadas em caixas `<remark>`:
  - "Erro de treino baixo = modelo bom" ([Linha 548](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-01.dlt#L548));
  - "Usar o conjunto de teste para escolher o modelo e reportar esse erro" ([Linha 550](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-01.dlt#L550) e [Exemplo 8.6](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-01.dlt#L498-L503));
  - "Achar que o ruído irredutível pode ser eliminado com um modelo melhor" ([Linha 140](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-01.dlt#L140)).
- **Exercícios:** Total de 16 exercícios (4 por seção), todos com níveis explícitos ("Básico", "Intermediário", "Avançado"), todos com `<hint>` contendo `<title>Ver dica</title>` e todos com `<solution collapsible="true" collapsed="true">` contendo resolução matemática ou computacional completa.
- **Contexto neurobiológico:** Cada uma das 4 seções contém múltiplos exemplos biológicos realistas:
  - Seção 1: curvas de saturação em V1, decodificação de categorias visuais no córtex temporal ventral por fMRI, subtipos de interneurônios corticais;
  - Seção 2: matrizes de disparos de populações neuronais (120 ensaios $\times$ 50 neurônios), amplitude de potenciais evocados visuais por bandas alfa/beta de EEG;
  - Seção 3: curvas de ativação $f$--$I$ por injeção de corrente intracelular, estágios de sono por EEG, potenciais de membrana em ensaios de teste;
  - Seção 4: ruído intrínseco de disparo neural (desvios de 2 a 6 Hz), potenciais pós-sinápticos excitatórios (EPSP), amostragem de ensaios de EEG.
- **Citações bibliográficas:** Estritamente dentro do conjunto permitido:
  - Kay et al. (2008), Naselaris et al. (2011), Huth et al. (2016) e Haxby et al. (2001) citados apenas por nome e ano, sem páginas ou detalhes inventados.
  - Links externos restritos a `statlearning.com` e subpáginas oficiais de `scikit-learn.org`.
- **Continuidade conceitual:** Não há uso precipitado de conceitos futuros. O texto avisa previamente sobre tópicos posteriores (Tema 8.2 para regressão polinomial e equações normais; Tema 8.3 para regressão logística e KNN; Tema 8.5 para validação cruzada; Tema 8.6 para Ridge; Tema 8.8 para árvores; Tema 8.9 para redução de dimensionalidade; Tema 8.10 para GAMs; Módulo 9 para redes neurais). Retoma pelo nome os Módulos 5 (álgebra matricial), 6 (Python e OO) e 7 (esperança e variância).
- **Notação e estilo:** Notação matemática impecável ($\mathbf{X} \in \mathbb{R}^{n \times p}$, $\mathbf{x} \in \mathbb{R}^p$, $\mathbf{y} \in \mathbb{R}^n$, $\boldsymbol{\beta}$), decimais com vírgula na matemática e prosa ($0{,}5$, $1{,}2$, $3{,}5$) e ponto no código.
- **Extensão do texto:** Aproximadamente 4.600 palavras distribuídas em 933 linhas XML, enquadrando-se perfeitamente no intervalo estipulado de 2.500 a 5.000 palavras para aulas de 4 subtemas.
- **Conformidade Delta v0.6.0:** Tags `<intuition>` empregadas exclusivamente dentro de `<definition>` e `<proposition>`, sem IDs próprios; `<proof>` associada por `of="prop:8-1-vies-variancia"` e fechada por padrão; `<figure>` referenciando arquivo SVG existente; ausência de tags não documentadas ou proibidas.

---

## 6. Conclusão

A aula cumpre rigorosamente todos os requisitos técnicos, matemáticos, computacionais e pedagógicos estabelecidos pelo contrato editorial. As três observações levantadas na tabela são meros detalhes de refinamento didático para posterior polimento opcional pelo autor. O parecer final é de **APROVAÇÃO**.
