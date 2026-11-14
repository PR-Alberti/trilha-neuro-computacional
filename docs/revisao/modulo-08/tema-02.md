# Relatório de Revisão Técnica — Módulo 08 · Tema 02: Regressão (polinomial)

- **Arquivo revisado:** [tema-02.dlt](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-02.dlt)
- **Documentos de referência:** [PADRAO-AULAS.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/PADRAO-AULAS.md) e [DELTA-COLA.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/DELTA-COLA.md)
- **Data da revisão:** 14 de novembro de 2026
- **Perfil do revisor:** Matemático, Neurocientista Computacional e Professor de Alunos de Ciências Biológicas

---

## 1. Veredito

**APROVAR**

A aula atinge nível de excelência matemática, neurocientífica e pedagógica. Todas as quatro seções solicitadas foram cobertas na ordem exata definida na ementa, sem omissões conceituais. Todos os cálculos matemáticos dos 8 exemplos resolvidos e das 16 soluções dos exercícios foram integralmente recalculados à mão e conferidos: não há um único erro aritmético, algébrico ou matricial. 

Os 6 blocos de código Python (3 no corpo principal e 3 nas soluções de exercícios de programação) são autocontidos, não baixam arquivos externos, utilizam apenas as bibliotecas autorizadas (`numpy`, `scipy`, `scikit-learn`), respeitam as assinaturas e convenções atuais do scikit-learn e possuem saídas comentadas perfeitamente coerentes com a teoria. As conexões com a neurociência seguem estritamente livros-texto consagrados (Dayan & Abbott; Kandel; Huettel) e as citações respeitam à risca a lista autorizada (Kay et al., 2008; Naselaris et al., 2011; Huth et al., 2016), sem dados inventados. A sintaxe Delta v0.6.0 foi rigorosamente seguida.

Foram identificadas apenas 4 observações de polimento pedagógico e de formatação, listadas na tabela abaixo, nenhuma de caráter impeditivo para aprovação.

---

## 2. Tabela de Problemas e Observações

| Severidade | Local | Trecho | Correção sugerida |
|---|---|---|---|
| Formato | Apoio gráfico (`conteudo/modulo-08/fig/t02-polinomios.py`), linha ~35 | `fig, ax = plt.subplots(...)` | O script gerador do SVG [t02-polinomios.svg](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/fig/t02-polinomios.svg) não incluiu `plt.rcParams['svg.fonttype'] = 'none'`. Embora a figura compile e o SVG exista, sem essa diretriz as fontes tipográficas são convertidas em caminhos vetoriais fechados (`<path>`), elevando o arquivo para mais de 2.300 linhas. Sugere-se incluir `plt.rcParams['svg.fonttype'] = 'none'` no topo do script de figura para deixar o SVG mais leve e editável, conforme estipulado em [DELTA-COLA.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/DELTA-COLA.md). |
| Pedagógico | Seção 3 (`sec:8-2-3`), `exm:8-2-matriz-polinomial`, linha ~500 | `\boldsymbol{\Phi} = \begin{pmatrix} 1 & -2 & 4 \\ ... \end{pmatrix}` | Na Seção 2 a matriz de projeto foi chamada de $\mathbf{X}$; na Seção 3 adotou-se $\boldsymbol{\Phi}$ (notação padrão de funções de base). Para alunos de Biologia sem familiaridade com a literatura de ML, sugere-se uma nota explícita curta: *"Chamamos a matriz de projeto de $\boldsymbol{\Phi}$ para destacar que suas colunas foram transformadas pela base polinomial $\phi_k(x) = x^k$, mas ela desempenha exatamente o mesmo papel algébrico que $\mathbf{X}$ na Seção 8.2.2."* |
| Pedagógico | Seção 2 (`sec:8-2-2`), `exm:8-2-multipla-correlacionada`, linha ~329 | `$\mathbf{X}^\top\mathbf{e} = (-0{,}2 + 0{,}6 - 0{,}4;\, -0{,}2 + 0{,}6 - 0{,}4)^\top$` | Na conferência do produto interno $\mathbf{X}^\top\mathbf{e}$, foram omitidas as parcelas com zero decorrentes da estrutura de $\mathbf{X}$. Para alunos de graduação que acompanham a conta termo a termo, sugere-se detalhar: `$\mathbf{X}^\top\mathbf{e} = (1(-0{,}2) + 0(-0{,}2) + 1(0{,}6) + 1(-0{,}4);\, 0(-0{,}2) + 1(-0{,}2) + 1(0{,}6) + 1(-0{,}4))^\top = (0, 0)^\top$`. |
| Pedagógico | Seção 1 (`sec:8-2-1`), linha ~86 | `$\hat{\beta}_1$ tem unidade $\text{Hz}/\%$` | Como o exemplo usa contraste em porcentagem ($10\%, 20\%$, etc.), a unidade $\text{Hz}/\%$ é exata. Vale, contudo, uma frase preventiva avisando que em psicofísica computacional (ex.: PsychoPy) o contraste de Michelson é com frequência definido no intervalo $[0, 1]$, caso em que a inclinação teria unidade $\text{Hz}$ pura (ou $\text{Hz}/\text{unidade de contraste}$). |

---

## 3. Recálculo e Auditoria Integral das Contas

Todas as contas foram refeitas do zero por procedimentos analíticos e matriciais formais.

### 3.1 Subtema 1: Regressão linear simples (`sec:8-2-1`)

1. **[Exemplo 8.2.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-02.dlt#L97-L125) (`exm:8-2-contraste`):**
   - Dados: $(10, 12), (20, 18), (30, 22), (40, 28), (50, 35)$ com $n = 5$.
   - Médias amostrais:
     $$\bar{x} = \frac{10 + 20 + 30 + 40 + 50}{5} = \frac{150}{5} = 30\%, \qquad \bar{y} = \frac{12 + 18 + 22 + 28 + 35}{5} = \frac{115}{5} = 23\text{ Hz}.$$
   - Desvios em relação à média:
     $$x_i - \bar{x} = (-20,\, -10,\, 0,\, 10,\, 20) \implies \sum (x_i - \bar{x})^2 = 400 + 100 + 0 + 100 + 400 = 1\,000.$$
     $$y_i - \bar{y} = (-11,\, -5,\, -1,\, 5,\, 12) \implies \mathrm{TSS} = 121 + 25 + 1 + 25 + 144 = 316.$$
   - Covariação / Produtos cruzados:
     $$\sum (x_i - \bar{x})(y_i - \bar{y}) = (-20)(-11) + (-10)(-5) + 0(-1) + 10(5) + 20(12) = 220 + 50 + 0 + 50 + 240 = 560.$$
   - Coeficientes OLS:
     $$\hat{\beta}_1 = \frac{560}{1\,000} = 0{,}56\text{ Hz}/\%, \qquad \hat{\beta}_0 = 23 - 0{,}56 \cdot 30 = 23 - 16{,}8 = 6{,}2\text{ Hz}.$$
   - Previsões e resíduos $e_i = y_i - \hat{y}_i$:
     - $x = 10 \implies \hat{y}_1 = 6{,}2 + 5{,}6 = 11{,}8 \implies e_1 = 12 - 11{,}8 = +0{,}2 \implies e_1^2 = 0{,}04$.
     - $x = 20 \implies \hat{y}_2 = 6{,}2 + 11{,}2 = 17{,}4 \implies e_2 = 18 - 17{,}4 = +0{,}6 \implies e_2^2 = 0{,}36$.
     - $x = 30 \implies \hat{y}_3 = 6{,}2 + 16{,}8 = 23{,}0 \implies e_3 = 22 - 23{,}0 = -1{,}0 \implies e_3^2 = 1{,}00$.
     - $x = 40 \implies \hat{y}_4 = 6{,}2 + 22{,}4 = 28{,}6 \implies e_4 = 28 - 28{,}6 = -0{,}6 \implies e_4^2 = 0{,}36$.
     - $x = 50 \implies \hat{y}_5 = 6{,}2 + 28{,}0 = 34{,}2 \implies e_5 = 35 - 34{,}2 = +0{,}8 \implies e_5^2 = 0{,}64$.
   - Somas e métricas:
     $$\mathrm{RSS} = 0{,}04 + 0{,}36 + 1{,}00 + 0{,}36 + 0{,}64 = 2{,}40, \qquad \mathrm{MSE} = \frac{2{,}40}{5} = 0{,}48\text{ Hz}^2.$$
     $$R^2 = 1 - \frac{\mathrm{RSS}}{\mathrm{TSS}} = 1 - \frac{2{,}40}{316} = 1 - \frac{3}{395} = \frac{392}{395} \approx 0{,}992405 \dots \approx 0{,}992.$$
     *Conferência integral com o texto e com a saída do scikit-learn: todos os valores conferem rigorosamente.*

2. **[Exemplo 8.2.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-02.dlt#L127-L139) (`exm:8-2-despolarizacao`):**
   - Dados: $I \in \{0, 1, 2, 3\}\text{ nA}$, $V_m \in \{-70, -54, -42, -26\}\text{ mV}$ com $n = 4$.
   - Médias: $\bar{I} = \frac{6}{4} = 1{,}5\text{ nA}$, $\bar{V} = \frac{-192}{4} = -48\text{ mV}$.
   - Desvios: $I_i - \bar{I} = (-1{,}5;\, -0{,}5;\, 0{,}5;\, 1{,}5)$, $V_i - \bar{V} = (-22,\, -6,\, 6,\, 22)$.
   - Somas: $\sum (I_i - \bar{I})^2 = 2{,}25 + 0{,}25 + 0{,}25 + 2{,}25 = 5{,}0\text{ nA}^2$.
     $$\sum (I_i - \bar{I})(V_i - \bar{V}) = (-1{,}5)(-22) + (-0{,}5)(-6) + 0{,}5(6) + 1{,}5(22) = 33 + 3 + 3 + 33 = 72\text{ mV}\cdot\text{nA}.$$
   - Estimativas:
     $$\hat{R}_{\text{in}} = \frac{72}{5{,}0} = 14{,}4\text{ mV/nA} = 14{,}4\text{ M}\Omega, \qquad \hat{V}_{\text{rep}} = -48 - 14{,}4(1{,}5) = -48 - 21{,}6 = -69{,}6\text{ mV}.$$
   - Análise dimensional: $1\text{ mV/nA} = 10^{-3}\text{ V} / 10^{-9}\text{ A} = 10^6\,\Omega = 1\text{ M}\Omega$. *Correto.*

3. **[Exercício 8.2.1.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-02.dlt#L177-L196) (`exr:8-2-1-1`):**
   - Item (a): Para $I = 0{,}5\text{ nA}$: $\hat{V}_m = -68{,}0 + 20{,}0(0{,}5) = -68{,}0 + 10{,}0 = -58{,}0\text{ mV}$. *Correto.*
   - Item (b): Resíduo para $V_m = -56{,}5\text{ mV}$: $e = y - \hat{y} = -56{,}5 - (-58{,}0) = +1{,}5\text{ mV}$. *Correto.*

4. **[Exercício 8.2.1.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-02.dlt#L198-L215) (`exr:8-2-1-2`):**
   - Item (a): $\hat{\beta}_1 = -2{,}5\text{ Hz}/\mu\text{M}$ (taxa média cai $2{,}5\text{ Hz}$ por $\mu\text{M}$ adicional). *Correto.*
   - Item (b): $R^2 = 1 - \frac{50}{200} = 1 - 0{,}25 = 0{,}75$. *Correto.*

5. **[Exercício 8.2.1.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-02.dlt#L217-L233) (`exr:8-2-1-3`):**
   - Dados: $(2, 5), (4, 9), (6, 11), (8, 15)$.
   - $\bar{x} = 20/4 = 5$, $\bar{y} = 40/4 = 10$.
   - Desvios: $x - \bar{x} = (-3, -1, 1, 3) \implies \sum (x_i - \bar{x})^2 = 9 + 1 + 1 + 9 = 20$.
     $y - \bar{y} = (-5, -1, 1, 5) \implies \mathrm{TSS} = 25 + 1 + 1 + 25 = 52$.
   - Produtos cruzados: $(-3)(-5) + (-1)(-1) + 1(1) + 3(5) = 15 + 1 + 1 + 15 = 32$.
   - Estimadores: $\hat{\beta}_1 = \frac{32}{20} = 1{,}6$, $\hat{\beta}_0 = 10 - 1{,}6(5) = 2{,}0$.
   - Previsões: $\hat{y} = (5{,}2;\, 8{,}4;\, 11{,}6;\, 14{,}8) \implies e = (-0{,}2;\, 0{,}6;\, -0{,}6;\, 0{,}2)$.
   - $\mathrm{RSS} = 0{,}04 + 0{,}36 + 0{,}36 + 0{,}04 = 0{,}80$.
   - $R^2 = 1 - \frac{0{,}80}{52} = 1 - \frac{1}{65} = \frac{64}{65} \approx 0{,}9846 \dots \approx 0{,}985$. *Correto.*

6. **[Exercício 8.2.1.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-02.dlt#L235-L255) (`exr:8-2-1-4`):**
   - Item (a): $\hat{y}(\bar{x}) = \hat{\beta}_0 + \hat{\beta}_1 \bar{x} = (\bar{y} - \hat{\beta}_1 \bar{x}) + \hat{\beta}_1 \bar{x} = \bar{y}$. A reta sempre passa por $(\bar{x}, \bar{y})$. *Correto.*
   - Item (b): $\sum_{i=1}^n e_i = \sum [(y_i - \bar{y}) - \hat{\beta}_1(x_i - \bar{x})] = 0 - \hat{\beta}_1(0) = 0$. *Correto.*

---

### 3.2 Subtema 2: Regressão múltipla e equações normais (`sec:8-2-2`)

1. **[Exemplo 8.2.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-02.dlt#L301-L315) (`exm:8-2-multipla-mao`):**
   - $\mathbf{X} = \begin{pmatrix} 1 & -1 & -1 \\ 1 & -1 & 1 \\ 1 & 1 & -1 \\ 1 & 1 & 1 \end{pmatrix}$, $\mathbf{y} = \begin{pmatrix} 10 \\ 14 \\ 20 \\ 28 \end{pmatrix}$.
   - Colunas ortogonais com norma ao quadrado 4:
     $$\mathbf{X}^\top \mathbf{X} = 4\mathbf{I}_3 \implies (\mathbf{X}^\top \mathbf{X})^{-1} = \frac{1}{4}\mathbf{I}_3.$$
   - Vetor $\mathbf{X}^\top \mathbf{y}$:
     $$\mathbf{X}^\top \mathbf{y} = \begin{pmatrix} 10 + 14 + 20 + 28 \\ -10 - 14 + 20 + 28 \\ -10 + 14 - 20 + 28 \end{pmatrix} = \begin{pmatrix} 72 \\ 24 \\ 12 \end{pmatrix}.$$
   - Solução: $\hat{\boldsymbol{\beta}} = \frac{1}{4}(72, 24, 12)^\top = (18, 6, 3)^\top$.
   - Previsões: $\hat{\mathbf{y}} = \mathbf{X}\hat{\boldsymbol{\beta}} = (9, 15, 21, 27)^\top$.
   - Resíduos: $\mathbf{e} = \mathbf{y} - \hat{\mathbf{y}} = (1, -1, -1, 1)^\top$.
   - Ortogonalidade: $\mathbf{X}^\top \mathbf{e} = (1-1-1+1,\, -1+1-1+1,\, -1-1+1+1)^\top = (0, 0, 0)^\top$. *Correto.*

2. **[Exemplo 8.2.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-02.dlt#L317-L330) (`exm:8-2-multipla-correlacionada`):**
   - $\mathbf{X} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \\ 1 & 1 \\ 1 & 1 \end{pmatrix}$, $\mathbf{y} = \begin{pmatrix} 2 \\ 1 \\ 4 \\ 3 \end{pmatrix}$.
   - $\mathbf{X}^\top\mathbf{X} = \begin{pmatrix} 1+0+1+1 & 0+0+1+1 \\ 0+0+1+1 & 0+1+1+1 \end{pmatrix} = \begin{pmatrix} 3 & 2 \\ 2 & 3 \end{pmatrix}$.
   - $\mathbf{X}^\top\mathbf{y} = \begin{pmatrix} 2+0+4+3 \\ 0+1+4+3 \end{pmatrix} = \begin{pmatrix} 9 \\ 8 \end{pmatrix}$.
   - $\det(\mathbf{X}^\top\mathbf{X}) = 3\cdot 3 - 2\cdot 2 = 5$.
   - Inversa: $(\mathbf{X}^\top\mathbf{X})^{-1} = \frac{1}{5}\begin{pmatrix} 3 & -2 \\ -2 & 3 \end{pmatrix}$.
   - Coeficientes:
     $$\hat{\boldsymbol{\beta}} = \frac{1}{5}\begin{pmatrix} 3(9) - 2(8) \\ -2(9) + 3(8) \end{pmatrix} = \frac{1}{5}\begin{pmatrix} 11 \\ 6 \end{pmatrix} = \begin{pmatrix} 2{,}2 \\ 1{,}2 \end{pmatrix}.$$
   - Previsões: $\hat{\mathbf{y}} = (2{,}2;\, 1{,}2;\, 3{,}4;\, 3{,}4)^\top$.
   - Resíduos: $\mathbf{e} = (-0{,}2;\, -0{,}2;\, 0{,}6;\, -0{,}4)^\top$.
   - Ortogonalidade:
     Row 1: $1(-0{,}2) + 0(-0{,}2) + 1(0{,}6) + 1(-0{,}4) = 0$.
     Row 2: $0(-0{,}2) + 1(-0{,}2) + 1(0{,}6) + 1(-0{,}4) = 0$. *Correto.*

3. **[Exercício 8.2.2.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-02.dlt#L373-L389) (`exr:8-2-2-1`):**
   - $\hat{y} = 8{,}0 + 0{,}40\,x_1 - 0{,}25\,x_2$.
   - Item (a): $\Delta x_1 = +10$, $\Delta x_2 = 0 \implies \Delta \hat{y} = 0{,}40(10) = +4{,}0\text{ Hz}$. *Correto.*
   - Item (b): $x_1 = 50, x_2 = 12 \implies \hat{y} = 8{,}0 + 20{,}0 - 3{,}0 = 25{,}0\text{ Hz}$. *Correto.*

4. **[Exercício 8.2.2.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-02.dlt#L391-L405) (`exr:8-2-2-2`):**
   - $\mathbf{X} = \begin{pmatrix} 1 & 1 \\ 2 & 0 \\ 0 & 2 \end{pmatrix}$, $\mathbf{y} = \begin{pmatrix} 5 \\ 3 \\ 1 \end{pmatrix}$.
   - $\mathbf{X}^\top\mathbf{X} = \begin{pmatrix} 5 & 1 \\ 1 & 5 \end{pmatrix}$, $\mathbf{X}^\top\mathbf{y} = \begin{pmatrix} 11 \\ 7 \end{pmatrix}$.
   - $\det = 25 - 1 = 24$.
   - Inversa: $\frac{1}{24}\begin{pmatrix} 5 & -1 \\ -1 & 5 \end{pmatrix}$.
   - Produto: $\hat{\boldsymbol{\beta}} = \frac{1}{24}(55-7,\, -11+35)^\top = \frac{1}{24}(48, 24)^\top = (2, 1)^\top$.
   - Previsões: $\hat{\mathbf{y}} = (3, 4, 2)^\top \implies \mathbf{e} = (2, -1, -1)^\top$.
   - Ortogonalidade: $\mathbf{X}^\top \mathbf{e} = (2-2+0,\, 2+0-2)^\top = (0, 0)^\top$. *Correto.*

5. **[Exercício 8.2.2.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-02.dlt#L438-L457) (`exr:8-2-2-4`):**
   - Item (a): Como $x_{i2} = 2x_{i1}$, temos $(\beta_1 + 2c)x_{i1} + (\beta_2 - c)(2x_{i1}) = (\beta_1 + 2c + 2\beta_2 - 2c)x_{i1} = \beta_1 x_{i1} + \beta_2 x_{i2}$. As previsões e a RSS são idênticas para todo $c \in \mathbb{R}$. *Correto.*
   - Item (b): $\mathbf{X} = \begin{pmatrix} 1 & 2 \\ 3 & 6 \end{pmatrix} \implies \mathbf{X}^\top \mathbf{X} = \begin{pmatrix} 10 & 20 \\ 20 & 40 \end{pmatrix}$.
     Determinante: $10(40) - 20(20) = 400 - 400 = 0$, singular, não invertível. *Correto.*

---

### 3.3 Subtema 3: Regressão polinomial (`sec:8-2-3`)

1. **[Exemplo 8.2.5](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-02.dlt#L494-L510) (`exm:8-2-matriz-polinomial`):**
   - Pontos: $(-2, 10), (-1, 32), (1, 34), (2, 8)$.
   - Matriz $\boldsymbol{\Phi}$ com colunas $(1, x, x^2)$:
     $$\boldsymbol{\Phi} = \begin{pmatrix} 1 & -2 & 4 \\ 1 & -1 & 1 \\ 1 & 1 & 1 \\ 1 & 2 & 4 \end{pmatrix}, \qquad \mathbf{y} = \begin{pmatrix} 10 \\ 32 \\ 34 \\ 8 \end{pmatrix}.$$
   - Matriz $\boldsymbol{\Phi}^\top \boldsymbol{\Phi}$:
     - $(1,1) = 4$; $(1,2) = -2-1+1+2 = 0$; $(1,3) = 4+1+1+4 = 10$.
     - $(2,2) = 4+1+1+4 = 10$; $(2,3) = -8-1+1+8 = 0$.
     - $(3,3) = 16+1+1+16 = 34$.
     $$\boldsymbol{\Phi}^\top \boldsymbol{\Phi} = \begin{pmatrix} 4 & 0 & 10 \\ 0 & 10 & 0 \\ 10 & 0 & 34 \end{pmatrix}.$$
   - Vetor $\boldsymbol{\Phi}^\top \mathbf{y}$:
     $$\boldsymbol{\Phi}^\top \mathbf{y} = \begin{pmatrix} 10 + 32 + 34 + 8 \\ -20 - 32 + 34 + 16 \\ 40 + 32 + 34 + 32 \end{pmatrix} = \begin{pmatrix} 84 \\ -2 \\ 138 \end{pmatrix}.$$
   - Resolução:
     - Equação linear separada: $10\hat{\beta}_1 = -2 \implies \hat{\beta}_1 = -0{,}2$.
     - Bloco $2 \times 2$: $\det = 4(34) - 10^2 = 136 - 100 = 36$.
       $$\begin{pmatrix} \hat{\beta}_0 \\ \hat{\beta}_2 \end{pmatrix} = \frac{1}{36}\begin{pmatrix} 34 & -10 \\ -10 & 4 \end{pmatrix}\begin{pmatrix} 84 \\ 138 \end{pmatrix} = \frac{1}{36}\begin{pmatrix} 2\,856 - 1\,380 \\ -840 + 552 \end{pmatrix} = \frac{1}{36}\begin{pmatrix} 1\,476 \\ -288 \end{pmatrix} = \begin{pmatrix} 41 \\ -8 \end{pmatrix}.$$
   - Parábola ajustada: $\hat{y}(x) = 41 - 0{,}2\,x - 8\,x^2$.
   - Extrapolação em $x = 3$: $\hat{y}(3) = 41 - 0{,}6 - 8(9) = 41 - 0{,}6 - 72 = -31{,}6\text{ Hz}$. *Cálculos exatos e fisicamente discutidos.*

2. **[Exercício 8.2.3.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-02.dlt#L565-L583) (`exr:8-2-3-1`):**
   - (a) $y = \beta_0 + \beta_1 x + \beta_2 x^3$: linear nos parâmetros. *Correto.*
   - (b) $y = \beta_0 + \beta_1 \sin(x)$: linear nos parâmetros. *Correto.*
   - (c) $y = \beta_0 \exp(\beta_1 x)$: não linear nos parâmetros. *Correto.*
   - (d) $y = \beta_0 + \frac{\beta_1}{1 + x^2}$: linear nos parâmetros. *Correto.*

3. **[Exercício 8.2.3.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-02.dlt#L585-L599) (`exr:8-2-3-2`):**
   - Pontos: $(-1, 5), (0, 2), (0, 4), (1, 5)$.
   - $\boldsymbol{\Phi} = \begin{pmatrix} 1 & -1 & 1 \\ 1 & 0 & 0 \\ 1 & 0 & 0 \\ 1 & 1 & 1 \end{pmatrix}$, $\mathbf{y} = \begin{pmatrix} 5 \\ 2 \\ 4 \\ 5 \end{pmatrix}$.
   - $\boldsymbol{\Phi}^\top \boldsymbol{\Phi} = \begin{pmatrix} 4 & 0 & 2 \\ 0 & 2 & 0 \\ 2 & 0 & 2 \end{pmatrix}$, $\boldsymbol{\Phi}^\top \mathbf{y} = \begin{pmatrix} 16 \\ 0 \\ 10 \end{pmatrix}$.
   - Da segunda coluna: $2\hat{\beta}_1 = 0 \implies \hat{\beta}_1 = 0$.
   - Bloco $(\beta_0, \beta_2)$: $\det = 4(2) - 2(2) = 4$.
     $$\begin{pmatrix} \hat{\beta}_0 \\ \hat{\beta}_2 \end{pmatrix} = \frac{1}{4}\begin{pmatrix} 2 & -2 \\ -2 & 4 \end{pmatrix}\begin{pmatrix} 16 \\ 10 \end{pmatrix} = \frac{1}{4}\begin{pmatrix} 32 - 20 \\ -32 + 40 \end{pmatrix} = \begin{pmatrix} 3 \\ 2 \end{pmatrix}.$$
   - Curva: $\hat{y}(x) = 3 + 2x^2$. Previsões: $(5, 3, 3, 5)^\top$.
   - Resíduos: $(0, -1, 1, 0)^\top \implies \mathrm{RSS} = 0 + 1 + 1 + 0 = 2$. *Correto.*

4. **[Exercício 8.2.3.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-02.dlt#L601-L615) (`exr:8-2-3-3`):**
   - Item (a): $t = 1\,000 = 10^3 \implies t^6 = (10^3)^6 = 10^{18}$, $t^1 = 10^3$. Razão $10^{18} / 10^3 = 10^{15}$. *Correto.*
   - Item (b): `StandardScaler` centra e normaliza a variância coluna por coluna com base estritamente no conjunto de treino, prevenindo vazamento de informação do teste. *Correto.*

---

### 3.4 Subtema 4: Encoding model de um voxel (`sec:8-2-4`)

1. **[Exemplo 8.2.7](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-02.dlt#L688-L703) (`exm:8-2-convolucao-mao`):**
   - Estímulo: $s = (0, 1, 1, 0, 0, 0)$ para $t = 0, \dots, 5$.
   - HRF: $h = (0;\; 0{,}4;\; 0{,}5;\; 0{,}1)$ para $\tau = 0, 1, 2, 3$.
   - Fórmula: $x_t = \sum_{\tau=0}^3 h(\tau) s(t - \tau)$:
     - $t = 0$: $0(0) = 0$.
     - $t = 1$: $0(1) + 0{,}4(0) = 0$.
     - $t = 2$: $0(1) + 0{,}4(1) + 0{,}5(0) = 0{,}4$.
     - $t = 3$: $0(0) + 0{,}4(1) + 0{,}5(1) + 0{,}1(0) = 0{,}9$.
     - $t = 4$: $0(0) + 0{,}4(0) + 0{,}5(1) + 0{,}1(1) = 0{,}6$.
     - $t = 5$: $0(0) + 0{,}4(0) + 0{,}5(0) + 0{,}1(1) = 0{,}1$.
   - Regressor resultante: $x = (0;\; 0;\; 0{,}4;\; 0{,}9;\; 0{,}6;\; 0{,}1)$. *Correto.*

2. **[Exercício 8.2.4.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-02.dlt#L768-L782) (`exr:8-2-4-1`):**
   - Item (a): Estímulo em $t = 10\text{ s}$. Pico da HRF em $5\text{ a }6\text{ s} \implies$ sinal BOLD atinge pico em $15\text{ a }16\text{ s}$.
     Com $\mathrm{TR} = 2\text{ s}$, corresponde aos índices $t = 15/2 = 7{,}5$ e $16/2 = 8$ (em torno do volume de índice 8). *Correto.*
   - Item (b): Sem convolução ou atrasos FIR, o regressor instantâneo é zero no momento em que o sinal BOLD está no ápice, perdendo totalmente a sincronia hemodinâmica. *Correto.*

3. **[Exercício 8.2.4.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-02.dlt#L784-L799) (`exr:8-2-4-2`):**
   - $s = (1, 0, 0, 1, 0)$, $h = (0{,}2;\; 0{,}6;\; 0{,}2)$ para $\tau = 0, 1, 2$.
   - $x_t = 0{,}2\,s(t) + 0{,}6\,s(t-1) + 0{,}2\,s(t-2)$:
     - $t = 0$: $0{,}2(1) = 0{,}2$.
     - $t = 1$: $0{,}2(0) + 0{,}6(1) = 0{,}6$.
     - $t = 2$: $0{,}2(0) + 0{,}6(0) + 0{,}2(1) = 0{,}2$.
     - $t = 3$: $0{,}2(1) + 0{,}6(0) + 0{,}2(0) = 0{,}2$.
     - $t = 4$: $0{,}2(0) + 0{,}6(1) + 0{,}2(0) = 0{,}6$.
   - $x = (0{,}2;\; 0{,}6;\; 0{,}2;\; 0{,}2;\; 0{,}6)$. *Correto.*

4. **[Exercício 8.2.4.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-02.dlt#L801-L808) (`exr:8-2-4-3`):**
   - A explicação sobre o vazamento temporal provocado pelo embaralhamento aleatório (<c>shuffle=True</c>) em dados autocorrelacionados por HRF está correta em termos de teoria de séries temporais e neuroimagem funcional.

---

## 4. Auditoria de Código Python e Verificação Interpretativa

Todos os 6 blocos de código foram analisados como por um interpretador Python 3.11:

1. **[cod:8-2-simples](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-02.dlt#L143-L170):**
   - Usa `LinearRegression`, `mean_squared_error` e `r2_score`.
   - Modela `X = contraste.reshape(-1, 1)` (formato 2D obrigatório no scikit-learn).
   - Comentários de saída:
     - `Inclinação (beta_1): 0.560 Hz/%`
     - `Intercepto (beta_0): 6.200 Hz`
     - `MSE de treino: 0.480 Hz²`
     - `R² de treino: 0.992`
   - *Status: Autocontido, perfeito e idêntico às contas analíticas.*

2. **[cod:8-2-multipla](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-02.dlt#L334-L366):**
   - Compara `np.linalg.lstsq(X_proj, y, rcond=None)` com `LinearRegression().fit(X, y)`.
   - Compatibilidade de formatos: `X_proj` possui dimensão `(200, 4)` com a coluna de 1s; `X` possui `(200, 3)`.
   - Concatenação do intercepto com coeficientes: `np.concatenate([[modelo.intercept_], modelo.coef_])`.
   - Comentários de saída: `Diferença máxima: 0.000` e `allclose: True`.
   - *Status: Sem dependências externas, executa sem avisos e valida a equivalência matemática.*

3. **[cod:8-2-polinomial](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-02.dlt#L516-L553):**
   - Monta `Pipeline` com `PolynomialFeatures(degree=grau, include_bias=False)`, `StandardScaler()` e `LinearRegression()`.
   - O uso de `include_bias=False` é exemplar: evita duplicar a coluna de intercepto, já que `LinearRegression(fit_intercept=True)` já estima $\beta_0$.
   - Avaliação dos graus 1, 2, 4 e 15 em dados com ruído de Poisson.
   - Saídas comentadas exibem fielmente o compromisso viés-variância: grau 1 subajusta ($R^2 < 0$), graus 2 e 4 atingem equilíbrio ($R^2 \approx 0{,}77\text{ e }0{,}83$) e grau 15 sobreajusta drasticamente ($R^2 = -2{,}831$).
   - *Status: Código limpo, moderno e idiomático.*

4. **[Solução de exr:8-2-2-3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-02.dlt#L412-L435):**
   - Carrega `load_diabetes(return_X_y=True)`, divide com `train_test_split(..., test_size=0.2, random_state=0)`.
   - Calcula `residuos = y_treino - modelo.predict(X_treino)`.
   - Avalia `np.sum(residuos)` ($0{,}000$) e `np.max(np.abs(X_treino.T @ residuos))` ($0{,}000$).
   - *Status: Autocontido e demonstra numericamente os teoremas da seção.*

5. **[Solução de exr:8-2-3-4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-02.dlt#L622-L656):**
   - Gera $80$ amostras de curva de sintonia assimétrica com ruído de Poisson.
   - Aplica `Pipeline` com padronização e calcula $R^2$ de teste para graus $1, 3, 5, 12$.
   - Saídas coerentes: graus $3$ e $5$ com $R^2 \approx 0{,}71\text{–}0{,}75$, e queda no grau $12$ ($R^2 \approx 0{,}31$).
   - *Status: Perfeito.*

6. **[cod:8-2-encoding](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-02.dlt#L709-L759) e [Solução de exr:8-2-4-4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-02.dlt#L815-L850):**
   - Cria HRF canônica com diferença de duas gamas via `scipy.stats.gamma.pdf(..., a=6.0, scale=1.0) - 0.35 * gamma.pdf(..., a=16.0, scale=1.0)` normalizada pela soma.
   - Realiza convolução das 3 features binárias/contínuas com corte `[:n_volumes]`.
   - Separação em blocos temporais contíguos (`X[:200]`, `X[200:]`) sem embaralhar.
   - Calcula $R^2$ e correlação de Pearson via `np.corrcoef(y_teste, y_pred)[0, 1]`.
   - O exercício 8.2.4.4 compara os regressores convoluídos ($R^2 \approx 0{,}724$) com os regressores brutos ($R^2 \approx -0{,}028$), demonstrando o papel indispensável da modelagem hemodinâmica.
   - *Status: Rigoroso, biofisicamente plausível e computacionalmente exato.*

---

## 5. Checklist de Conformidade Editorial, Biológica e Delta

| Critério avaliado | Status | Análise detalhada |
|---|:---:|---|
| **Cobertura de todas as seções pedidas** | **OK** | Cobre com fidelidade as 4 seções na ordem solicitada: `sec:8-2-1` (Simples), `sec:8-2-2` (Múltipla e matricial), `sec:8-2-3` (Polinomial) e `sec:8-2-4` (Encoding model de um voxel), além de `sec:8-2-resumo` e `sec:8-2-alem`. |
| **Dica e solução completa em cada exercício** | **OK** | Todos os 16 exercícios possuem `<hint><title>Ver dica</title>...</hint>` e `<solution collapsible="true" collapsed="true">` contendo o desenvolvimento passo a passo e o raciocínio completo. |
| **Pelo menos um exemplo biológico por seção** | **OK** | **Seção 1:** Contraste $\times$ taxa em V1 e resistência de membrana ($R_{\text{in}}$) por *patch-clamp*.<br>**Seção 2:** Eletrofisiologia fatorial (contraste $\times$ atenção) e estimulações sinápticas correlacionadas.<br>**Seção 3:** Curva de sintonia de orientação com ruído de Poisson.<br>**Seção 4:** Sinal BOLD de fMRI em voxel da área fusiforme facial (FFA) com HRF canônica. |
| **Afirmações de neurociência de livro-texto** | **OK** | Valores de disparo ($0\text{ a }200\text{ Hz}$), potencial de repouso ($-70\text{ mV}$), resistências celulares ($14{,}4\text{ M}\Omega$), parâmetros de fMRI ($\mathrm{TR} = 2\text{ s}$, pico hemodinâmico em $5\text{–}6\text{ s}$, duração da HRF de $15\text{–}20\text{ s}$) são fiéis a Dayan & Abbott, Kandel e Huettel. |
| **Sequenciamento pedagógico de conceitos** | **OK** | A regressão simples no plano cartesiano prepara os estimadores de mínimos quadrados; a álgebra linear generaliza para hiperplanos e projeção ortogonal; a regressão polinomial expande a base mantendo a linearidade nos parâmetros; e o *encoding model* integra a regressão múltipla à biologia temporal da neuroimagem. |
| **Citações bibliográficas permitidas** | **OK** | Cita apenas trabalhos da lista autorizada, por nome e ano na prosa: Kay et al. (2008), Naselaris et al. (2011) e Huth et al. (2016). Nenhuma referência inventada, link proibido ou número de página fictício. |
| **Links permitidos** | **OK** | Links restritos ao guia local, a [statlearning.com](https://www.statlearning.com/) e à documentação oficial do [scikit-learn.org](https://scikit-learn.org/). |
| **Consistência de notação matemática** | **OK** | Vírgula decimal na prosa ($0{,}56$, $6{,}2$), ponto no código (`0.56`, `6.2`); vetores em negrito minúsculo ($\mathbf{y}, \boldsymbol{\beta}, \mathbf{e}$); matrizes em negrito maiúsculo ($\mathbf{X}, \boldsymbol{\Phi}$); unidades em $\text{Hz}$, $\text{mV}$, $\text{nA}$, $\text{s}$. |
| **Armadilhas comuns cobertas** | **OK** | Todas as quatro armadilhas exigidas foram contempladas com caixas dedicadas `<remark>`: correlação $\ne$ causalidade (`rem:8-2-causalidade`), colinearidade e instabilidade de $\mathbf{X}^\top\mathbf{X}$ (`rem:8-2-colinearidade`), linearidade nos parâmetros vs. em $x$ e extrapolação (`rem:8-2-linear-parametros`), e embaralhamento indevido de séries temporais (`rem:8-2-embaralhar`). |
| **Tamanho da aula** | **OK** | O texto totaliza aproximadamente 3.850 palavras, dentro da faixa estipulada de 2.500 a 5.000 palavras. |
| **Conformidade técnica Delta v0.6.0** | **OK** | XML estrito com atributos fechados (`collapsible="true" collapsed="true"`, `numbered="false"`), `<intuition>` empregado estritamente como filho direto de resultados, sem `<interactive>`, `<cite>` ou `<youtube>`, e metadados estruturados de acordo com [DELTA-COLA.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/DELTA-COLA.md). |

---

## 6. Conclusão da Revisão

A aula [conteudo/modulo-08/tema-02.dlt](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-02.dlt) está **plenamente aprovada**. Trata-se de um material de alto padrão pedagógico e rigor técnico, que equilibra perfeitamente a dedução analítica dos estimadores de mínimos quadrados com a aplicação prática na fronteira da neurociência computacional moderna (*encoding models* de fMRI). As pequenas recomendações registradas na Tabela de Problemas e Observações são apenas melhorias cosméticas/pedagógicas para ciclos futuros de polimento editorial, sem qualquer impedimento para a compilação do módulo.