# Relatório de Revisão Técnica — Módulo 05 · Tema 01 (Vetores, Matrizes e Operações)

- **Arquivo revisado:** [tema-01.dlt](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-01.dlt)
- **Script de figura associado:** [matriz-dados.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/fig/matriz-dados.py)
- **Documentos de referência:** [PADRAO-AULAS.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/PADRAO-AULAS.md) e [DELTA-COLA.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/DELTA-COLA.md)
- **Data da revisão:** 14 de novembro de 2026
- **Perfil do revisor:** Matemático, Neurocientista Computacional e Professor de Alunos de Ciências Biológicas

---

## 1. Veredito

**APROVAR**

A aula cumpre rigorosamente todos os requisitos matemáticos, pedagógicos, de neurociência e de formatação Delta v0.6.0 estabelecidos para a trilha. Todas as contas de exemplos e exercícios foram integralmente refeitas e verificadas passo a passo, sem nenhum erro de cálculo ou de dimensão. O código Python/NumPy é autocontido, correto e ilustrativo em todas as quatro seções. A contextualização biológica (taxas de disparo em Hz, matrizes de eletrofisiologia/cálcio neurônios × tempo, sinal BOLD no fMRI, canais/frequências em EEG e circuitos sinápticos excitatórios/inibitórios) é consistente com a literatura padrão (Dayan & Abbott; Kandel).

Foram identificadas 3 observações pontuais de polimento pedagógico e de formato, detalhadas na tabela a seguir, sem impacto impeditivo.

---

## 2. Tabela de Problemas e Observações

| Severidade | Local | Trecho | Correção sugerida |
|---|---|---|---|
| Pedagógico | Seção 3 (`sec:5-1-3`), `exm:5-1-rede-linear`, linha ~586 | `Já a coluna 2 mostra que o neurônio pré-sináptico 2 fala simultaneamente com sinal oposto para os dois alvos: ele inibe o pós-sináptico 1 (-1) e excita fortemente o pós-sináptico 2 (+3).` | Em neurobiologia real, o Princípio de Dale estabelece que a imensa maioria dos neurônios libera o mesmo neurotransmissor primário em todos os seus terminais (sendo puramente excitatório ou puramente inibitório para todos os seus alvos). Em redes neurais artificiais e modelos lineares abstratos, pesos de sinais mistos na mesma coluna são comuns. Sugere-se acrescentar uma breve nota ao final do parágrafo: `*(Nota biológica: em circuitos reais, pelo Princípio de Dale, um mesmo neurônio pré-sináptico costuma ser uniformemente excitatório ou inibitório para seus alvos; colunas com sinais mistos ocorrem tipicamente em modelos abstratos de aprendizado de máquina ou quando $W_{ij}$ representa a ação líquida via interneurônios intermediários).*` |
| Pedagógico | Seção 2 (`sec:5-1-2`), `def:5-1-transposta`, linha ~329 | `$$(\mathbf{A}^\top)_{ij} = a_{ji} \qquad (1 \le i \le n,\; 1 \le j \le m).$$` | Para alunos de Biologia sem familiaridade prévia com transposição, a troca dos limites dos índices ($i$ variando até $n$ e $j$ até $m$) pode parecer confusa à primeira vista ao comparar com a definição anterior onde $\mathbf{A} \in \mathbb{R}^{m \times n}$. Sugere-se explicitar brevemente na frase seguinte: `Note a troca: como $\mathbf{A}^\top$ tem dimensão $n \times m$, seu índice de linha $i$ varia de $1$ a $n$ e seu índice de coluna $j$ varia de $1$ a $m$.` |
| Formato | Seção 4 (`sec:5-1-4`), `exr:5-1-4-3`, linha ~914 | `<solution collapsible="true" collapsed="true"> Multiplicamos $\mathbf{W}$ ($2 \times 3$) por $\mathbf{X}$ ($3 \times 4$)...` | No exercício `exr:5-1-4-3`, a solução apresenta diretamente a lista de contas sem dividir em alíneas (a) e (b), pois o enunciado foi redigido em período contínuo. Embora matematicamente completa e correta, para uniformidade com os demais 15 exercícios da aula, recomenda-se estruturar o enunciado com `<list marker="a">` (item a: calcular $\mathbf{Y}$; item b: identificar o instante de pico) e refletir essas alíneas na `<solution>`. |

---

## 3. Recálculo e Auditoria de Contas

Todas as contas foram integralmente recalculadas à mão e confrontadas com as soluções e blocos de código.

### 3.1 Seção 1: Vetores: o estado de uma população (`sec:5-1-1`)

1. **[Exemplo 5.1.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-01.dlt#L111-L132) (`exm:5-1-populacao`):**
   - Dados: $\mathbf{r}_A = (12, 30, 8, 10)^\top\text{ Hz}$ e $\mathbf{r}_B = (16, 26, 10, 10)^\top\text{ Hz}$.
   - Item (a): $\bar{\mathbf{r}} = 0{,}5\mathbf{r}_A + 0{,}5\mathbf{r}_B = (6+8, 15+13, 4+5, 5+5)^\top = (14, 28, 9, 10)^\top\text{ Hz}$. **Correto.**
   - Item (b): $\Delta\mathbf{r} = \mathbf{r}_B - \mathbf{r}_A = (16-12, 26-30, 10-8, 10-10)^\top = (4, -4, 2, 0)^\top\text{ Hz}$.
     Norma: $\|\Delta\mathbf{r}\| = \sqrt{4^2 + (-4)^2 + 2^2 + 0^2} = \sqrt{16 + 16 + 4 + 0} = \sqrt{36} = 6\text{ Hz}$. **Correto.**

2. **[Exemplo 5.1.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-01.dlt#L134-L152) (`exm:5-1-combinacao-escalar`):**
   - Dados: $\mathbf{u} = (2, -1, 4)^\top$ e $\mathbf{v} = (1, 3, -2)^\top$.
   - Item (a): $\mathbf{w} = 3\mathbf{u} - 2\mathbf{v} = (6, -3, 12)^\top - (2, 6, -4)^\top = (6-2, -3-6, 12-(-4))^\top = (4, -9, 16)^\top$. **Correto.**
   - Item (b): $\mathbf{u}^\top\mathbf{v} = 2(1) + (-1)(3) + 4(-2) = 2 - 3 - 8 = -9$.
     Norma: $\|\mathbf{v}\| = \sqrt{1^2 + 3^2 + (-2)^2} = \sqrt{1 + 9 + 4} = \sqrt{14} \approx 3{,}741657... \approx 3{,}742$. **Correto.**

3. **[Código Python 5.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-01.dlt#L159-L180) (`cod:5-1-vetores`):**
   - Média `0.5 * r_A + 0.5 * r_B`: `[14.0, 28.0, 9.0, 10.0]`. **Correto.**
   - Diferença `delta_r`: `[4, -4, 2, 0]`. **Correto.**
   - Norma `np.linalg.norm(delta_r)`: `6.000`. **Correto.**
   - Produto escalar `u @ v`: `-9`. **Correto.**

4. **[Exercício 5.1.1.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-01.dlt#L191-L213) (`exr:5-1-1-1`):**
   - Dados: $\mathbf{a} = (3, -1, 0)^\top$ e $\mathbf{b} = (1, 1, -1)^\top$.
   - Item (a): $2\mathbf{a} + \mathbf{b} = (6, -2, 0)^\top + (1, 1, -1)^\top = (7, -1, -1)^\top$. **Correto.**
   - Item (b): $\mathbf{a} - 3\mathbf{b} = (3, -1, 0)^\top - (3, 3, -3)^\top = (3-3, -1-3, 0-(-3))^\top = (0, -4, 3)^\top$. **Correto.**
   - Item (c): $\mathbf{a} - \mathbf{b} = (3-1, -1-1, 0-(-1))^\top = (2, -2, 1)^\top$.
     $\|\mathbf{a} - \mathbf{b}\| = \sqrt{2^2 + (-2)^2 + 1^2} = \sqrt{4 + 4 + 1} = \sqrt{9} = 3$. **Correto.**

5. **[Exercício 5.1.1.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-01.dlt#L215-L234) (`exr:5-1-1-2`):**
   - Dados: $\mathbf{r}_V = (24, 8, 12, 4)^\top\text{ Hz}$ e $\mathbf{r}_H = (10, 22, 12, 16)^\top\text{ Hz}$.
   - Item (a): $\bar{\mathbf{r}} = \frac{1}{2}(24+10, 8+22, 12+12, 4+16)^\top = \frac{1}{2}(34, 30, 24, 20)^\top = (17, 15, 12, 10)^\top\text{ Hz}$. **Correto.**
   - Item (b): $\Delta\mathbf{r} = \mathbf{r}_H - \mathbf{r}_V = (10-24, 22-8, 12-12, 16-4)^\top = (-14, 14, 0, 12)^\top\text{ Hz}$.
     Interpretação biológica: neurônio 1 dispara mais para vertical ($-14 < 0$); neurônios 2 e 4 preferem horizontal ($+14$ e $+12$); neurônio 3 é invariante à orientação ($\Delta r_3 = 0$). **Correto.**

6. **[Exercício 5.1.1.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-01.dlt#L236-L259) (`exr:5-1-1-3`):**
   - Dados: $\mathbf{u} = (2, -2, 1, 0)^\top$ e $\mathbf{v} = (5, -2, 4, 1)^\top$.
   - Item (a): $\|\mathbf{u}\| = \sqrt{2^2 + (-2)^2 + 1^2 + 0^2} = \sqrt{4+4+1+0} = \sqrt{9} = 3$.
     $\mathbf{u}^\top\mathbf{v} = 2(5) + (-2)(-2) + 1(4) + 0(1) = 10 + 4 + 4 + 0 = 18$. **Correto.**
   - Item (b): $\mathbf{u}^\top(\mathbf{v} + k\mathbf{u}) = \mathbf{u}^\top\mathbf{v} + k\|\mathbf{u}\|^2 = 18 + 9k = 0 \implies k = -2$.
     Conferência: $\mathbf{v} - 2\mathbf{u} = (5-4, -2+4, 4-2, 1-0)^\top = (1, 2, 2, 1)^\top$.
     $\mathbf{u}^\top(1, 2, 2, 1)^\top = 2(1) + (-2)(2) + 1(2) + 0(1) = 2 - 4 + 2 + 0 = 0$. **Correto.**

7. **[Exercício 5.1.1.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-01.dlt#L261-L285) (`exr:5-1-1-4`):**
   - Dados: $\mathbf{r}_1 = (30, 10, 20)^\top\text{ Hz}$, $\mathbf{r}_2 = (10, 50, 0)^\top\text{ Hz}$, $\mathbf{r}(\alpha) = \alpha\mathbf{r}_1 + (1-\alpha)\mathbf{r}_2$.
   - Item (a): para $\alpha = 0{,}25$:
     $\mathbf{r}(0{,}25) = 0{,}25(30, 10, 20)^\top + 0{,}75(10, 50, 0)^\top = (7{,}5, 2{,}5, 5{,}0)^\top + (7{,}5, 37{,}5, 0)^\top = (15, 40, 5)^\top\text{ Hz}$. **Correto.**
   - Item (b): $r_1(\alpha) = 30\alpha + 10(1-\alpha) = 10 + 20\alpha$; $r_2(\alpha) = 10\alpha + 50(1-\alpha) = 50 - 40\alpha$.
     $r_1(\alpha) = r_2(\alpha) \implies 10 + 20\alpha = 50 - 40\alpha \implies 60\alpha = 40 \implies \alpha = \frac{40}{60} = \frac{2}{3} \approx 0{,}667$.
     Taxa comum: $r_1(2/3) = 10 + 20(2/3) = \frac{70}{3} \approx 23{,}33\text{ Hz}$; $r_2(2/3) = 50 - 40(2/3) = \frac{70}{3}\text{ Hz}$. **Correto.**

---

### 3.2 Seção 2: Matrizes: a gravação inteira numa tabela (`sec:5-1-2`)

1. **[Exemplo 5.1.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-01.dlt#L360-L381) (`exm:5-1-gravacao-centralizacao`):**
   - Matriz $\mathbf{X} \in \mathbb{R}^{3 \times 4}$:
     $$\mathbf{X} = \begin{pmatrix} 10 & 14 & 12 & 16 \\ 20 & 18 & 22 & 20 \\ 5 & 9 & 7 & 11 \end{pmatrix}$$
   - Item (a): dimensão $3 \times 4$. Série do neurônio 2 (linha 2): $(20, 18, 22, 20)$. População no instante $t=3$ (coluna 3): $(12, 22, 7)^\top$. **Correto.**
   - Item (b): médias por linha:
     $\mu_1 = \frac{10+14+12+16}{4} = \frac{52}{4} = 13\text{ Hz}$;
     $\mu_2 = \frac{20+18+22+20}{4} = \frac{80}{4} = 20\text{ Hz}$;
     $\mu_3 = \frac{5+9+7+11}{4} = \frac{32}{4} = 8\text{ Hz}$.
     Centralização $\tilde{\mathbf{X}} = \mathbf{X} - \boldsymbol{\mu}$:
     Linha 1: $(10-13, 14-13, 12-13, 16-13) = (-3, 1, -1, 3)$;
     Linha 2: $(20-20, 18-20, 22-20, 20-20) = (0, -2, 2, 0)$;
     Linha 3: $(5-8, 9-8, 7-8, 11-8) = (-3, 1, -1, 3)$.
     Soma de cada linha: $-3+1-1+3 = 0$; $0-2+2+0 = 0$; $-3+1-1+3 = 0$. **Correto.**

2. **[Exemplo 5.1.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-01.dlt#L383-L396) (`exm:5-1-transposta-ops`):**
   - $\mathbf{A} = \begin{pmatrix} 1 & -2 & 4 \\ 0 & 3 & 5 \end{pmatrix}$, $\mathbf{B} = \begin{pmatrix} 2 & 4 & -1 \\ 3 & -1 & 1 \end{pmatrix}$.
   - $2\mathbf{A} - \mathbf{B} = \begin{pmatrix} 2 & -4 & 8 \\ 0 & 6 & 10 \end{pmatrix} - \begin{pmatrix} 2 & 4 & -1 \\ 3 & -1 & 1 \end{pmatrix} = \begin{pmatrix} 0 & -8 & 9 \\ -3 & 7 & 9 \end{pmatrix}$. **Correto.**
   - $\mathbf{A} + \mathbf{B} = \begin{pmatrix} 3 & 2 & 3 \\ 3 & 2 & 6 \end{pmatrix} \implies (\mathbf{A}+\mathbf{B})^\top = \begin{pmatrix} 3 & 3 \\ 2 & 2 \\ 3 & 6 \end{pmatrix}$.
   - $\mathbf{A}^\top + \mathbf{B}^\top = \begin{pmatrix} 1 & 0 \\ -2 & 3 \\ 4 & 5 \end{pmatrix} + \begin{pmatrix} 2 & 3 \\ 4 & -1 \\ -1 & 1 \end{pmatrix} = \begin{pmatrix} 3 & 3 \\ 2 & 2 \\ 3 & 6 \end{pmatrix}$. Coincidem. **Correto.**

3. **[Código Python 5.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-01.dlt#L398-L421) (`cod:5-1-matrizes`):**
   - `X.shape`: `(3, 4)`. **Correto.**
   - `X[1, :]`: `[20, 18, 22, 20]`. **Correto.**
   - `X[:, 2]`: `[12, 22, 7]`. **Correto.**
   - `X.T.shape`: `(4, 3)`. **Correto.**
   - `X.mean(axis=1, keepdims=True)`: `[13.0, 20.0, 8.0]`. **Correto.**
   - Linha 1 de `X_cent`: `[-3.0, 1.0, -1.0, 3.0]`. **Correto.**

4. **[Exercício 5.1.2.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-01.dlt#L432-L449) (`exr:5-1-2-1`):**
   - $\mathbf{M} = \begin{pmatrix} 3 & -1 & 0 & 4 \\ 2 & 5 & -3 & 1 \end{pmatrix}$.
   - Item (a): dimensão $2 \times 4$; $m_{13} = 0$, $m_{21} = 2$, $m_{24} = 1$. **Correto.**
   - Item (b): $\mathbf{M}^\top = \begin{pmatrix} 3 & 2 \\ -1 & 5 \\ 0 & -3 \\ 4 & 1 \end{pmatrix}$, dimensão $4 \times 2$. **Correto.**

5. **[Exercício 5.1.2.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-01.dlt#L451-L468) (`exr:5-1-2-2`):**
   - $\mathbf{F} = \begin{pmatrix} 1{,}8 & 0{,}4 & 0{,}2 \\ 0{,}3 & 2{,}1 & 0{,}6 \\ 0{,}5 & 0{,}5 & 1{,}4 \end{pmatrix}$ ($3$ voxels $\times$ $3$ estímulos).
   - Item (a): linha 2 = $(0{,}3;\; 2{,}1;\; 0{,}6)$. O maior valor é $2{,}1$ na coluna 2 (casas). **Correto.**
   - Item (b): coluna 3 (ferramentas) = $(0{,}2;\; 0{,}6;\; 1{,}4)^\top$.
     Média do voxel 1 (linha 1): $\mu_1 = \frac{1{,}8 + 0{,}4 + 0{,}2}{3} = \frac{2{,}4}{3} = 0{,}8$. **Correto.**

6. **[Exercício 5.1.2.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-01.dlt#L470-L491) (`exr:5-1-2-3`):**
   - $\mathbf{X} = \begin{pmatrix} 8 & 12 & 10 & 14 & 6 \\ 15 & 15 & 21 & 18 & 21 \end{pmatrix}$.
   - Item (a): $\mu_1 = \frac{8+12+10+14+6}{5} = \frac{50}{5} = 10\text{ Hz}$; $\mu_2 = \frac{15+15+21+18+21}{5} = \frac{90}{5} = 18\text{ Hz}$. **Correto.**
   - Item (b): $\tilde{\mathbf{X}} = \begin{pmatrix} 8-10 & 12-10 & 10-10 & 14-10 & 6-10 \\ 15-18 & 15-18 & 21-18 & 18-18 & 21-18 \end{pmatrix} = \begin{pmatrix} -2 & 2 & 0 & 4 & -4 \\ -3 & -3 & 3 & 0 & 3 \end{pmatrix}\text{ Hz}$.
     Somas: $-2+2+0+4-4 = 0$ e $-3-3+3+0+3 = 0$. **Correto.**

7. **[Exercício 5.1.2.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-01.dlt#L493-L513) (`exr:5-1-2-4`):**
   - $\mathbf{A} = \begin{pmatrix} 2 & 5 \\ -1 & 4 \end{pmatrix}$.
   - Item (a): $\mathbf{A}^\top = \begin{pmatrix} 2 & -1 \\ 5 & 4 \end{pmatrix} \implies \mathbf{A}+\mathbf{A}^\top = \begin{pmatrix} 4 & 4 \\ 4 & 8 \end{pmatrix} \implies \mathbf{S} = \frac{1}{2}(\mathbf{A}+\mathbf{A}^\top) = \begin{pmatrix} 2 & 2 \\ 2 & 4 \end{pmatrix}$.
     Como $\mathbf{S}^\top = \begin{pmatrix} 2 & 2 \\ 2 & 4 \end{pmatrix} = \mathbf{S}$, a matriz é simétrica. **Correto.**
   - Item (b): $\mathbf{S}^\top = (\frac{1}{2}(\mathbf{A}+\mathbf{A}^\top))^\top = \frac{1}{2}(\mathbf{A}^\top + (\mathbf{A}^\top)^\top) = \frac{1}{2}(\mathbf{A}^\top + \mathbf{A}) = \mathbf{S}$. Válido para qualquer $\mathbf{A} \in \mathbb{R}^{n \times n}$. **Correto.**

---

### 3.3 Seção 3: Produto matriz-vetor como pesos sinápticos (`sec:5-1-3`)

1. **[Exemplo 5.1.5](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-01.dlt#L569-L587) (`exm:5-1-rede-linear`):**
   - $\mathbf{W} = \begin{pmatrix} 2 & -1 & 1 \\ 0 & 3 & -2 \end{pmatrix}$ ($2 \times 3$), $\mathbf{r}_{\text{pré}} = (10, 4, 5)^\top\text{ Hz}$.
   - Linhas: $r_{\text{pós}, 1} = 2(10) + (-1)(4) + 1(5) = 20 - 4 + 5 = 21\text{ Hz}$;
     $r_{\text{pós}, 2} = 0(10) + 3(4) + (-2)(5) = 0 + 12 - 10 = 2\text{ Hz}$.
   - Colunas: $10\begin{pmatrix} 2 \\ 0 \end{pmatrix} + 4\begin{pmatrix} -1 \\ 3 \end{pmatrix} + 5\begin{pmatrix} 1 \\ -2 \end{pmatrix} = \begin{pmatrix} 20-4+5 \\ 0+12-10 \end{pmatrix} = \begin{pmatrix} 21 \\ 2 \end{pmatrix}\text{ Hz}$. **Correto.**

2. **[Exemplo 5.1.6](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-01.dlt#L589-L600) (`exm:5-1-linearidade-comb`):**
   - $\mathbf{A} = \begin{pmatrix} 1 & 2 \\ 3 & -1 \\ 0 & 4 \end{pmatrix}$, $\mathbf{x} = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$, $\mathbf{y} = \begin{pmatrix} -1 \\ 3 \end{pmatrix}$.
   - $\mathbf{A}\mathbf{x} = (1(2)+2(1), 3(2)-1(1), 0(2)+4(1))^\top = (4, 5, 4)^\top$.
   - $\mathbf{A}\mathbf{y} = (1(-1)+2(3), 3(-1)-1(3), 0(-1)+4(3))^\top = (5, -6, 12)^\top$.
   - $\mathbf{z} = 2\mathbf{x} - \mathbf{y} = (4-(-1), 2-3)^\top = (5, -1)^\top \implies \mathbf{A}\mathbf{z} = (1(5)+2(-1), 3(5)-1(-1), 0(5)+4(-1))^\top = (3, 16, -4)^\top$.
   - $2\mathbf{A}\mathbf{x} - \mathbf{A}\mathbf{y} = (8-5, 10-(-6), 8-12)^\top = (3, 16, -4)^\top$. Coincidem perfeitamente. **Correto.**

3. **[Código Python 5.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-01.dlt#L602-L619) (`cod:5-1-matriz-vetor`):**
   - `W @ r_pre`: `[21, 2]`. **Correto.**
   - Pelas colunas: `[21, 2]`. **Correto.**

4. **[Exercício 5.1.3.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-01.dlt#L629-L649) (`exr:5-1-3-1`):**
   - $\mathbf{A} = \begin{pmatrix} 3 & -2 & 1 \\ 0 & 4 & -1 \end{pmatrix}$, $\mathbf{x} = (2, 5, -3)^\top$.
   - Item (a): $(\mathbf{A}\mathbf{x})_1 = 3(2) + (-2)(5) + 1(-3) = 6 - 10 - 3 = -7$;
     $(\mathbf{A}\mathbf{x})_2 = 0(2) + 4(5) + (-1)(-3) = 0 + 20 + 3 = 23$.
   - Item (b): $2\begin{pmatrix} 3 \\ 0 \end{pmatrix} + 5\begin{pmatrix} -2 \\ 4 \end{pmatrix} + (-3)\begin{pmatrix} 1 \\ -1 \end{pmatrix} = \begin{pmatrix} 6-10-3 \\ 0+20+3 \end{pmatrix} = \begin{pmatrix} -7 \\ 23 \end{pmatrix}$. **Correto.**

5. **[Exercício 5.1.3.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-01.dlt#L651-L675) (`exr:5-1-3-2`):**
   - Microcircuito: 3 pré $\to$ 2 pós ($A, B$).
     Conexões para $A$ (linha 1): $1 \to A$ ($+2$), $2 \to A$ ($0$), $3 \to A$ ($-3$);
     Conexões para $B$ (linha 2): $1 \to B$ ($-1$), $2 \to B$ ($+4$), $3 \to B$ ($+1$).
   - Item (a): $\mathbf{W} = \begin{pmatrix} 2 & 0 & -3 \\ -1 & 4 & 1 \end{pmatrix}$. **Correto.**
   - Item (b): $\mathbf{r}_{\text{pré}} = (10, 5, 4)^\top\text{ Hz}$.
     $r_A = 2(10) + 0(5) + (-3)(4) = 20 - 12 = 8\text{ Hz}$;
     $r_B = -1(10) + 4(5) + 1(4) = -10 + 20 + 4 = 14\text{ Hz}$.
     $\mathbf{r}_{\text{pós}} = (8, 14)^\top\text{ Hz}$. **Correto.**

6. **[Exercício 5.1.3.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-01.dlt#L677-L698) (`exr:5-1-3-3`):**
   - Item (a): $\mathbf{A} = \begin{pmatrix} 4 & -2 & 7 \\ 1 & 5 & -3 \end{pmatrix}$.
     $\mathbf{A}\mathbf{e}_1 = \begin{pmatrix} 4 \\ 1 \end{pmatrix}$, $\mathbf{A}\mathbf{e}_2 = \begin{pmatrix} -2 \\ 5 \end{pmatrix}$, $\mathbf{A}\mathbf{e}_3 = \begin{pmatrix} 7 \\ -3 \end{pmatrix}$. Extrai colunas. **Correto.**
   - Item (b): $\mathbf{x} = 2\mathbf{e}_1 - \mathbf{e}_2 + 5\mathbf{e}_3 \implies \mathbf{B}\mathbf{x} = 2\begin{pmatrix} 3 \\ 1 \end{pmatrix} - \begin{pmatrix} -1 \\ 4 \end{pmatrix} + 5\begin{pmatrix} 0 \\ 2 \end{pmatrix} = \begin{pmatrix} 6+1+0 \\ 2-4+10 \end{pmatrix} = \begin{pmatrix} 7 \\ 8 \end{pmatrix}$.
     Conferência matricial com $\mathbf{B} = \begin{pmatrix} 3 & -1 & 0 \\ 1 & 4 & 2 \end{pmatrix}$: $\begin{pmatrix} 3(2)-1(-1)+0(5) \\ 1(2)+4(-1)+2(5) \end{pmatrix} = \begin{pmatrix} 7 \\ 8 \end{pmatrix}$. **Correto.**

7. **[Exercício 5.1.3.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-01.dlt#L700-L721) (`exr:5-1-3-4`):**
   - $\mathbf{W} = \begin{pmatrix} 2 & -1 & -1 \\ -1 & 3 & -2 \end{pmatrix}$, $r_1 = 15\text{ Hz}$, $r_2 = 10\text{ Hz}$.
   - Item (a): $r_3 = 0 \implies \mathbf{r}_{\text{pós}} = \begin{pmatrix} 2(15) - 1(10) \\ -1(15) + 3(10) \end{pmatrix} = \begin{pmatrix} 20 \\ 15 \end{pmatrix}\text{ Hz}$. **Correto.**
   - Item (b): $r_{\text{pós}, 1} = 20 - r_3 = 0 \implies r_3 = 20\text{ Hz}$.
     $r_{\text{pós}, 2} = -15 + 30 - 2(20) = 15 - 40 = -25\text{ Hz}$.
     Interpretação biológica: taxas de disparo não podem ser negativas; no neurônio real o sinal satura em $0\text{ Hz}$ (silenciamento por hiperpolarização abaixo do limiar). **Correto.**

---

### 3.4 Seção 4: Produto de matrizes (`sec:5-1-4`)

1. **[Exemplo 5.1.7](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-01.dlt#L782-L805) (`exm:5-1-duas-camadas`):**
   - $\mathbf{W}_1 = \begin{pmatrix} 1 & 0 \\ 2 & -1 \\ 0 & 3 \end{pmatrix}$ ($3 \times 2$), $\mathbf{W}_2 = \begin{pmatrix} 1 & 1 & -1 \\ 0 & 2 & 1 \end{pmatrix}$ ($2 \times 3$), $\mathbf{X}_0 = \begin{pmatrix} 10 & 5 \\ 2 & 4 \end{pmatrix}$ ($2 \times 2$).
   - Item (a): $\mathbf{W}_{\text{eq}} = \mathbf{W}_2 \mathbf{W}_1$:
     $(1, 1): 1(1) + 1(2) + (-1)(0) = 3$;
     $(1, 2): 1(0) + 1(-1) + (-1)(3) = -4$;
     $(2, 1): 0(1) + 2(2) + 1(0) = 4$;
     $(2, 2): 0(0) + 2(-1) + 1(3) = 1$.
     $\mathbf{W}_{\text{eq}} = \begin{pmatrix} 3 & -4 \\ 4 & 1 \end{pmatrix}$. **Correto.**
   - Item (b):
     $\mathbf{X}_1 = \mathbf{W}_1 \mathbf{X}_0 = \begin{pmatrix} 1(10)+0(2) & 1(5)+0(4) \\ 2(10)-1(2) & 2(5)-1(4) \\ 0(10)+3(2) & 0(5)+3(4) \end{pmatrix} = \begin{pmatrix} 10 & 5 \\ 18 & 6 \\ 6 & 12 \end{pmatrix}$.
     $\mathbf{X}_2 = \mathbf{W}_2 \mathbf{X}_1 = \begin{pmatrix} 10+18-6 & 5+6-12 \\ 0+36+6 & 0+12+12 \end{pmatrix} = \begin{pmatrix} 22 & -1 \\ 42 & 24 \end{pmatrix}$.
     Direto: $\mathbf{W}_{\text{eq}} \mathbf{X}_0 = \begin{pmatrix} 3(10)-4(2) & 3(5)-4(4) \\ 4(10)+1(2) & 4(5)+1(4) \end{pmatrix} = \begin{pmatrix} 22 & -1 \\ 42 & 24 \end{pmatrix}$. Coincidem em todos os instantes. **Correto.**

2. **[Exemplo 5.1.8](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-01.dlt#L807-L827) (`exm:5-1-nao-comutativo`):**
   - $\mathbf{A} = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$, $\mathbf{B} = \begin{pmatrix} 3 & 0 \\ 1 & 2 \end{pmatrix}$.
   - Item (a): $\mathbf{A}\mathbf{B} = \begin{pmatrix} 1(3)+2(1) & 1(0)+2(2) \\ 0(3)+1(1) & 0(0)+1(2) \end{pmatrix} = \begin{pmatrix} 5 & 4 \\ 1 & 2 \end{pmatrix}$;
     $\mathbf{B}\mathbf{A} = \begin{pmatrix} 3(1)+0(0) & 3(2)+0(1) \\ 1(1)+2(0) & 1(2)+2(1) \end{pmatrix} = \begin{pmatrix} 3 & 6 \\ 1 & 4 \end{pmatrix}$.
     Logo, $\mathbf{A}\mathbf{B} \ne \mathbf{B}\mathbf{A}$. **Correto.**
   - Item (b): $(\mathbf{A}\mathbf{B})^\top = \begin{pmatrix} 5 & 1 \\ 4 & 2 \end{pmatrix}$.
     $\mathbf{B}^\top \mathbf{A}^\top = \begin{pmatrix} 3 & 1 \\ 0 & 2 \end{pmatrix}\begin{pmatrix} 1 & 0 \\ 2 & 1 \end{pmatrix} = \begin{pmatrix} 3(1)+1(2) & 3(0)+1(1) \\ 0(1)+2(2) & 0(0)+2(1) \end{pmatrix} = \begin{pmatrix} 5 & 1 \\ 4 & 2 \end{pmatrix}$.
     Contraste com $\mathbf{A}^\top \mathbf{B}^\top = \begin{pmatrix} 1 & 0 \\ 2 & 1 \end{pmatrix}\begin{pmatrix} 3 & 1 \\ 0 & 2 \end{pmatrix} = \begin{pmatrix} 3 & 1 \\ 6 & 4 \end{pmatrix} \ne (\mathbf{A}\mathbf{B})^\top$. **Correto.**

3. **[Código Python 5.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-01.dlt#L829-L848) (`cod:5-1-prod-matrizes`):**
   - `W_eq`: `[[3, -4], [4, 1]]`. **Correto.**
   - `W_eq @ X0`: `[[22, -1], [42, 24]]`. **Correto.**
   - `W2 @ (W1 @ X0)`: `[[22, -1], [42, 24]]`. **Correto.**
   - `A @ B`: `[[5, 4], [1, 2]]`. **Correto.**
   - `B @ A`: `[[3, 6], [1, 4]]`. **Correto.**
   - `A * B` (produto Hadamard): `[[3, 0], [0, 2]]`. **Correto.**

4. **[Exercício 5.1.4.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-01.dlt#L859-L883) (`exr:5-1-4-1`):**
   - $\mathbf{A} \in \mathbb{R}^{2 \times 3}$, $\mathbf{B} \in \mathbb{R}^{3 \times 2}$, $\mathbf{C} \in \mathbb{R}^{2 \times 2}$.
   - Item (a):
     - $\mathbf{A}\mathbf{B}$: $(2 \times 3)(3 \times 2) \to 2 \times 2$ (definido);
     - $\mathbf{B}\mathbf{A}$: $(3 \times 2)(2 \times 3) \to 3 \times 3$ (definido);
     - $\mathbf{A}\mathbf{C}$: $(2 \times 3)(2 \times 2)$ (não definido, $3 \ne 2$);
     - $\mathbf{C}\mathbf{A}$: $(2 \times 2)(2 \times 3) \to 2 \times 3$ (definido). **Correto.**
   - Item (b): $\mathbf{A} = \begin{pmatrix} 1 & 0 & -2 \\ 3 & 1 & 4 \end{pmatrix}$, $\mathbf{B} = \begin{pmatrix} 2 & -1 \\ 5 & 0 \\ 1 & 3 \end{pmatrix}$.
     $\mathbf{A}\mathbf{B} = \begin{pmatrix} 1(2)+0(5)-2(1) & 1(-1)+0(0)-2(3) \\ 3(2)+1(5)+4(1) & 3(-1)+1(0)+4(3) \end{pmatrix} = \begin{pmatrix} 0 & -7 \\ 15 & 9 \end{pmatrix}$.
     $\mathbf{B}\mathbf{A} = \begin{pmatrix} 2(1)-1(3) & 2(0)-1(1) & 2(-2)-1(4) \\ 5(1)+0(3) & 5(0)+0(1) & 5(-2)+0(4) \\ 1(1)+3(3) & 1(0)+3(1) & 1(-2)+3(4) \end{pmatrix} = \begin{pmatrix} -1 & -1 & -8 \\ 5 & 0 & -10 \\ 10 & 3 & 10 \end{pmatrix}$. **Correto.**

5. **[Exercício 5.1.4.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-01.dlt#L885-L906) (`exr:5-1-4-2`):**
   - $\mathbf{P} = \begin{pmatrix} 2 & 1 \\ -1 & 3 \end{pmatrix}$, $\mathbf{Q} = \begin{pmatrix} 1 & 4 \\ 2 & 0 \end{pmatrix}$.
   - Item (a): $\mathbf{P}\mathbf{Q} = \begin{pmatrix} 2(1)+1(2) & 2(4)+1(0) \\ -1(1)+3(2) & -1(4)+3(0) \end{pmatrix} = \begin{pmatrix} 4 & 8 \\ 5 & -4 \end{pmatrix}$;
     $\mathbf{P} * \mathbf{Q} = \begin{pmatrix} 2(1) & 1(4) \\ -1(2) & 3(0) \end{pmatrix} = \begin{pmatrix} 2 & 4 \\ -2 & 0 \end{pmatrix}$. **Correto.**
   - Item (b): $\mathbf{P}\mathbf{I}_2 = \begin{pmatrix} 2(1)+1(0) & 2(0)+1(1) \\ -1(1)+3(0) & -1(0)+3(1) \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ -1 & 3 \end{pmatrix} = \mathbf{P}$;
     $\mathbf{I}_2\mathbf{P} = \begin{pmatrix} 1(2)+0(-1) & 1(1)+0(3) \\ 0(2)+1(-1) & 0(1)+1(3) \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ -1 & 3 \end{pmatrix} = \mathbf{P}$. **Correto.**

6. **[Exercício 5.1.4.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-01.dlt#L908-L934) (`exr:5-1-4-3`):**
   - $\mathbf{W} = \begin{pmatrix} 1 & -1 & 2 \\ 0 & 2 & 1 \end{pmatrix}$ ($2 \times 3$), $\mathbf{X} = \begin{pmatrix} 10 & 12 & 8 & 14 \\ 4 & 6 & 4 & 2 \\ 3 & 1 & 5 & 0 \end{pmatrix}$ ($3 \times 4$).
   - $\mathbf{Y} = \mathbf{W}\mathbf{X}$ ($2 \times 4$):
     - Linha 1 (pós-sináptico 1):
       $t = 1$: $10 - 4 + 2(3) = 12\text{ Hz}$;
       $t = 2$: $12 - 6 + 2(1) = 8\text{ Hz}$;
       $t = 3$: $8 - 4 + 2(5) = 14\text{ Hz}$;
       $t = 4$: $14 - 2 + 2(0) = 12\text{ Hz}$.
     - Linha 2 (pós-sináptico 2):
       $t = 1$: $0 + 2(4) + 3 = 11\text{ Hz}$;
       $t = 2$: $0 + 2(6) + 1 = 13\text{ Hz}$;
       $t = 3$: $0 + 2(4) + 5 = 13\text{ Hz}$;
       $t = 4$: $0 + 2(2) + 0 = 4\text{ Hz}$.
     - $\mathbf{Y} = \begin{pmatrix} 12 & 8 & 14 & 12 \\ 11 & 13 & 13 & 4 \end{pmatrix}\text{ Hz}$.
     - Maior taxa do neurônio pós-sináptico 1: instante $t = 3$ com $14\text{ Hz}$. **Correto.**

7. **[Exercício 5.1.4.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-01.dlt#L936-L960) (`exr:5-1-4-4`):**
   - $\mathbf{W}_1 = \begin{pmatrix} 2 & -1 \\ 1 & 1 \end{pmatrix}$, $\mathbf{W}_2 = \begin{pmatrix} 1 & 3 \\ -2 & 0 \end{pmatrix}$.
   - Item (a): $\mathbf{W}_{\text{eq}} = \mathbf{W}_2 \mathbf{W}_1 = \begin{pmatrix} 1(2)+3(1) & 1(-1)+3(1) \\ -2(2)+0(1) & -2(-1)+0(1) \end{pmatrix} = \begin{pmatrix} 5 & 2 \\ -4 & 2 \end{pmatrix}$. **Correto.**
   - Item (b): $(\mathbf{W}_2 \mathbf{W}_1)^\top = \begin{pmatrix} 5 & -4 \\ 2 & 2 \end{pmatrix}$.
     $\mathbf{W}_1^\top \mathbf{W}_2^\top = \begin{pmatrix} 2 & 1 \\ -1 & 1 \end{pmatrix}\begin{pmatrix} 1 & -2 \\ 3 & 0 \end{pmatrix} = \begin{pmatrix} 2+3 & -4+0 \\ -1+3 & 2+0 \end{pmatrix} = \begin{pmatrix} 5 & -4 \\ 2 & 2 \end{pmatrix}$. Coincidem.
     Ordem direta $\mathbf{W}_2^\top \mathbf{W}_1^\top = \begin{pmatrix} 1 & -2 \\ 3 & 0 \end{pmatrix}\begin{pmatrix} 2 & 1 \\ -1 & 1 \end{pmatrix} = \begin{pmatrix} 2+2 & 1-2 \\ 6+0 & 3+0 \end{pmatrix} = \begin{pmatrix} 4 & -1 \\ 6 & 3 \end{pmatrix} \ne (\mathbf{W}_2 \mathbf{W}_1)^\top$. **Correto.**
   - Item (c): Justificativa conceitual do colapso de camadas lineares sucessivas e a necessidade imperativa de funções de ativação não lineares em redes profundas. **Correto.**

---

**Nenhum erro matemático encontrado.**

---

## 4. Auditoria dos Critérios Editoriais e Pedagógicos

| Critério | Status | Detalhamento |
|---|---|---|
| **Dica e solução completa em cada exercício** | Conforme | Todos os 16 exercícios (4 por seção) possuem `<hint>` específico e `<solution collapsible="true" collapsed="true">` com a dedução matemática e o raciocínio biológico completos, e não apenas o resultado numérico final. |
| **Exemplo biológico em cada seção** | Conforme | Seção 1: taxas populacionais no córtex motor (`exm:5-1-populacao`), córtex visual (`exr:5-1-1-2`) e mistura de odores (`exr:5-1-1-4`); Seção 2: gravação de eletrofisiologia/cálcio (`exm:5-1-gravacao-centralizacao`), dados de fMRI voxels × estímulos (`exr:5-1-2-2`) e centralização temporal (`exr:5-1-2-3`); Seção 3: rede feedforward linear (`exm:5-1-rede-linear`), circuito pré/pós (`exr:5-1-3-2`) e balanço excitação/inibição (`exr:5-1-3-4`); Seção 4: propagação de gravação temporal por camadas sinápticas (`exm:5-1-duas-camadas` e `exr:5-1-4-3`). |
| **Afirmações de neurociência de livro-texto** | Conforme | Todas as grandezas fisiológicas (taxas de disparo de 0 a dezenas de Hz, saturação refratária, limiar de disparo, sinal BOLD, bandas de frequência em EEG) e convenções sinápticas ($W_{ij}$ de $j$ para $i$) estão perfeitamente alinhadas aos livros-texto clássicos (*Dayan & Abbott; Kandel et al.; Gerstner et al.*). |
| **Apresentação progressiva de conceitos** | Conforme | Nenhum conceito de tópicos futuros é usado sem anúncio explícito. A transposta é apresentada intencionalmente na Seção 1 para notação de coluna e formalizada na Seção 2; sistemas lineares e inversão são remetidos ao Tema 5.2; PCA ao Tema 5.6; e não-linearidades ao Módulo 9. |
| **Código Python funcional** | Conforme | Os quatro blocos (`cod:5-1-vetores`, `cod:5-1-matrizes`, `cod:5-1-matriz-vetor` e `cod:5-1-prod-matrizes`) são 100% autocontidos, utilizam práticas modernas de NumPy (operador `@`, `keepdims=True`, distinção entre `axis=1` e `axis=0`, aviso sobre `*` vs. `@`) e trazem a saída exata comentada. |
| **Consistência de notação** | Conforme | Vetores em negrito minúsculo ($\mathbf{r}, \mathbf{x}, \mathbf{u}, \mathbf{v}, \mathbf{w}, \mathbf{a}, \mathbf{b}, \mathbf{e}_j, \mathbf{y}, \mathbf{z}$), matrizes em negrito maiúsculo ($\mathbf{X}, \mathbf{A}, \mathbf{B}, \mathbf{W}, \mathbf{M}, \mathbf{F}, \mathbf{S}, \mathbf{I}, \mathbf{P}, \mathbf{Q}, \mathbf{Y}$), escalares em itálico ($x_i, a_{ij}, W_{ij}, \alpha, \beta, c, k, t, \mu_i$), vetor de médias em negrito grego ($\boldsymbol{\mu}$), transposta com $(\cdot)^\top$ e decimais com vírgula na prosa/KaTeX ($0{,}5$, $2{,}1$, etc.) e ponto no código. |
| **Cobertura dos subtemas exigidos** | Conforme | Cobriu rigorosamente as 4 seções definidas pelo gestor: (1) Vetores: o estado de uma população; (2) Matrizes: a gravação inteira numa tabela; (3) Produto matriz-vetor como pesos sinápticos; (4) Produto de matrizes. |
| **Extensão e tamanho da aula** | Conforme | O arquivo possui 996 linhas e aproximadamente 4 400 palavras de prosa, situando-se perfeitamente dentro da faixa-alvo estipulada de 3 500 a 5 500 palavras. |
| **Auditoria do script de figura** | Conforme | O script [matriz-dados.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/fig/matriz-dados.py) utiliza `plt.rcParams["svg.fonttype"] = "none"`, salva `matriz-dados.svg` na pasta `fig/`, possui todos os rótulos em português, e ilustra com clareza a dupla interpretação de linhas (séries temporais de neurônios) e colunas (vetor de população em $t = 20$). |
