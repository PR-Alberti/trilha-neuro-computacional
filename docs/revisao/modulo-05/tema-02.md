# Relatório de Revisão Técnica — Módulo 05 · Tema 02 (Sistemas lineares e transformações)

- **Arquivo revisado:** [tema-02.dlt](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-02.dlt)
- **Script de figura associado:** [transformacao-plano.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/fig/transformacao-plano.py) (gera [transformacao-plano.svg](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/fig/transformacao-plano.svg))
- **Documentos de referência:** [PADRAO-AULAS.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/PADRAO-AULAS.md) e [DELTA-COLA.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/DELTA-COLA.md)
- **Data da revisão:** 14 de novembro de 2026
- **Perfil do revisor:** Matemático, Neurocientista Computacional e Professor de Alunos de Ciências Biológicas

---

## 1. Veredito

**CORRIGIR**

A aula possui altíssima qualidade matemática, conceitual e pedagógica. Todas as contas de todos os 9 exemplos numéricos e dos 16 exercícios graduados foram integralmente recalculadas à mão e confrontadas com o texto e o código, sem que nenhum erro matemático fosse encontrado. O código Python/NumPy é moderno, didático e 100% executável nas quatro seções. A contextualização biológica (redes sinápticas, equilíbrios iônicos e condutâncias de membrana, decodificação olfatória, rastreamento comportamental de animais e condução de volume no EEG) é realista e perfeitamente ancorada na literatura clássica (*Dayan & Abbott; Kandel et al.*).

Entretanto, o veredito é **CORRIGIR** em cumprimento à regra estrita de compilação do [PADRAO-AULAS.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/PADRAO-AULAS.md) (*"A aula precisa compilar com `delta build` sem erro e passar no `delta lint`"*). Foi detectado um erro de compilação KaTeX na linha ~661 (`$\det &lt; 0$`), onde a entidade HTML `&lt;` foi usada dentro de delimitadores matemáticos, violando a regra de escape do Delta. Além da correção obrigatória dessa linha para desbloquear a compilação, foram registradas três observações de polimento pedagógico e de formato descritas a seguir.

---

## 2. Tabela de Problemas e Observações

| Severidade | Local | Trecho | Correção sugerida |
|---|---|---|---|
| **Formato** (Erro de compilação KaTeX) | Seção 3 (`sec:5-2-3`), `rem:5-2-armadilha-comp`, linha ~661 | `<item><strong>Sinal do determinante $2 \times 2$ e significado de $\det &lt; 0$:</strong> a fórmula é $ad - bc$ ...</item>` | O uso da entidade HTML `&lt;` dentro de matemática `$ ... $` provoca falha no processador KaTeX. Conforme a regra de escape de [DELTA-COLA.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/DELTA-COLA.md) ("Dentro de `$...$`: não escapar `<`"), substitua por `<` puro: `$\det < 0$`. |
| **Pedagógico** | Seção 1 (`sec:5-2-1`), `exr:5-2-1-2`, linha ~199 | `Em um microcircuito de dois neurônios pré-sinápticos e dois pós-sinápticos, a matriz de pesos sinápticos é $\mathbf{W} = \begin{pmatrix} 3 & -1 \\ 1 & 2 \end{pmatrix}$.` | A coluna 2 da matriz $\mathbf{W}$ possui pesos com sinais opostos ($-1$ e $+2$), sugerindo que o mesmo neurônio pré-sináptico $2$ inibe o neurônio pós $1$ e excita o neurônio pós $2$. Em neurobiologia real, pelo Princípio de Dale, um neurônio libera o mesmo neurotransmissor primário em todos os seus axônios. Sugere-se acrescentar uma breve observação explicativa na dica ou no enunciado: `*(Nota biológica: em circuitos reais, um neurônio é uniformemente excitatório ou inibitório; sinais mistos em uma coluna representam modelos abstratos ou a ação líquida integrada por interneurônios intermediários).*` |
| **Pedagógico** | Seção 4 (`sec:5-2-4`), linha ~811-817 | `\mathbf{x}(t) = \mathbf{A}\,\mathbf{s}(t), em que $\mathbf{A} \in \mathbb{R}^{M \times K}$ é a matriz de mistura (eletrodos × fontes)...` | Para alunos de Biologia sem experiência prévia com eletromagnetismo, convém explicitar a simplificação de unidades: na física do EEG real, $\mathbf{x}$ é medido em $\mu\text{V}$ e as fontes dipolares $\mathbf{s}$ têm momento em $\text{nAm}$ (nanoampère-metro), de modo que $\mathbf{A}$ possui dimensão física de transferência ($\mu\text{V}/\text{nAm}$). No tratamento didático da aula, tanto $\mathbf{s}$ quanto $\mathbf{x}$ são expressos em $\mu\text{V}$, atuando as entradas de $\mathbf{A}$ como coeficientes adimensionais de mistura geométrica. Uma frase curta esclarecendo essa convenção didática evita confusões dimensionais. |
| **Formato** | Seção 3 (`sec:5-2-3`), `def:5-2-transf-linear`, linha ~512 | `<item><strong>Aditividade:</strong> $T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})$; </item>` | Há um espaço em branco supérfluo imediatamente antes do fechamento `</item>`. Sugere-se remover o espaço para manter o XML estritamente limpo: `$T(\mathbf{u}) + T(\mathbf{v})$;</item>`. |

---

## 3. Recálculo e Auditoria de Contas

Todas as deduções, sistemas lineares, operações de linha, produtos matriciais, determinantes, inversas e conferências numéricas foram integralmente recalculados passo a passo.

### 3.1 Seção 1: Sistemas lineares na forma matricial (`sec:5-2-1`)

1. **[Exemplo 5.2.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-02.dlt#L85-L111) (`exm:5-2-inverter-rede`):**
   - Sistema: $\mathbf{W}\mathbf{r}_{\text{pré}} = \mathbf{r}_{\text{pós}}$ com $\mathbf{W} = \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix}$ e $\mathbf{r}_{\text{pós}} = (26, 33)^\top\text{ Hz}$.
   - Equações: $2r_1 + r_2 = 26 \implies r_2 = 26 - 2r_1$.
   - Substituição na segunda equação: $r_1 + 3(26 - 2r_1) = 33 \implies r_1 + 78 - 6r_1 = 33 \implies -5r_1 = -45 \implies r_1 = 9\text{ Hz}$.
   - Recuperação de $r_2$: $r_2 = 26 - 2(9) = 8\text{ Hz}$. Logo, $\mathbf{r}_{\text{pré}} = (9, 8)^\top\text{ Hz}$.
   - Conferência por linhas: $2(9) + 8 = 26\text{ Hz}$ e $9 + 3(8) = 33\text{ Hz}$. **Correto.**
   - Conferência por colunas: $9\begin{pmatrix} 2 \\ 1 \end{pmatrix} + 8\begin{pmatrix} 1 \\ 3 \end{pmatrix} = \begin{pmatrix} 18 + 8 \\ 9 + 24 \end{pmatrix} = \begin{pmatrix} 26 \\ 33 \end{pmatrix}\text{ Hz}$. **Correto.**

2. **[Exemplo 5.2.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-02.dlt#L113-L136) (`exm:5-2-mistura-regimes`):**
   - Solução iônica: Estoque $A$ ($10\text{ mM Na}^+$, $2\text{ mM K}^+$), Estoque $B$ ($4\text{ mM Na}^+$, $8\text{ mM K}^+$). Alvo: $76\;\mu\text{mol Na}^+$ e $44\;\mu\text{mol K}^+$.
   - Sistema: $\begin{cases} 10x_1 + 4x_2 = 76 \\ 2x_1 + 8x_2 = 44 \end{cases} \iff \begin{cases} 5x_1 + 2x_2 = 38 \\ x_1 + 4x_2 = 22 \end{cases}$.
   - $x_1 = 22 - 4x_2 \implies 5(22 - 4x_2) + 2x_2 = 38 \implies 110 - 18x_2 = 38 \implies 18x_2 = 72 \implies x_2 = 4\text{ mL}$.
   - $x_1 = 22 - 4(4) = 6\text{ mL}$.
   - Conferência: $\text{Na}^+ = 10(6) + 4(4) = 76\;\mu\text{mol}$; $\text{K}^+ = 2(6) + 8(4) = 44\;\mu\text{mol}$. Sistema SPD. **Correto.**
   - Estoque defeituoso $B'$ ($20\text{ mM Na}^+$, $4\text{ mM K}^+$): colunas proporcionais $\mathbf{a}_{:,2} = 2\mathbf{a}_{:,1}$ (razão $\text{Na}^+/\text{K}^+ = 5$).
     - Para alvo $(50, 10)^\top$: as duas equações reduzem-se a $x_1 + 2x_2 = 5$. Infinitas soluções (SPI): $x_1 = 5 - 2t$, $x_2 = t$. **Correto.**
     - Para alvo $(50, 12)^\top$: equações $x_1 + 2x_2 = 5$ e $x_1 + 2x_2 = 6$ são retas paralelas distintas. Contradição ($5 = 6$), sistema impossível (SI). **Correto.**

3. **[Código Python 5.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-02.dlt#L143-L163) (`cod:5-2-sistema`):**
   - `np.linalg.solve(W, r_pos)`: devolve `[9.0, 8.0]`. **Correto.**
   - Combinação de colunas: devolve `[26.0, 33.0]`. **Correto.**
   - Volumes de solução: devolve `[6.0, 4.0]`. **Correto.**

4. **[Exercício 5.2.1.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-02.dlt#L173-L195) (`exr:5-2-1-1`):**
   - Sistema: $\begin{cases} 2x_1 - x_2 = 5 \\ x_1 + 3x_2 = 6 \end{cases}$.
   - Matriz aumentada: $\left(\begin{array}{cc|c} 2 & -1 & 5 \\ 1 & 3 & 6 \end{array}\right)$. **Correto.**
   - $x_2 = 2x_1 - 5 \implies x_1 + 3(2x_1 - 5) = 6 \implies 7x_1 = 21 \implies x_1 = 3$.
   - $x_2 = 2(3) - 5 = 1$. Solução única $\mathbf{x} = (3, 1)^\top$ (SPD).
   - Conferência por colunas: $3\begin{pmatrix} 2 \\ 1 \end{pmatrix} + 1\begin{pmatrix} -1 \\ 3 \end{pmatrix} = \begin{pmatrix} 6 - 1 \\ 3 + 3 \end{pmatrix} = \begin{pmatrix} 5 \\ 6 \end{pmatrix}$. **Correto.**

5. **[Exercício 5.2.1.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-02.dlt#L197-L210) (`exr:5-2-1-2`):**
   - $\mathbf{W} = \begin{pmatrix} 3 & -1 \\ 1 & 2 \end{pmatrix}$, $\mathbf{r}_{\text{pós}} = (22, 19)^\top\text{ Hz}$.
   - Sistema: $3r_1 - r_2 = 22$ e $r_1 + 2r_2 = 19$.
   - $r_2 = 3r_1 - 22 \implies r_1 + 2(3r_1 - 22) = 19 \implies 7r_1 - 44 = 19 \implies 7r_1 = 63 \implies r_1 = 9\text{ Hz}$.
   - $r_2 = 3(9) - 22 = 5\text{ Hz}$.
   - Conferência por colunas: $9\begin{pmatrix} 3 \\ 1 \end{pmatrix} + 5\begin{pmatrix} -1 \\ 2 \end{pmatrix} = \begin{pmatrix} 27 - 5 \\ 9 + 10 \end{pmatrix} = \begin{pmatrix} 22 \\ 19 \end{pmatrix}\text{ Hz}$. **Correto.**

6. **[Exercício 5.2.1.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-02.dlt#L212-L227) (`exr:5-2-1-3`):**
   - Sistema: $2x + 4y = 10$ e $3x + 6y = k$.
   - Item (a): Colunas $(2, 3)^\top$ e $(4, 6)^\top = 2(2, 3)^\top$ são colineares; suas combinações lineares geram apenas a reta $y = \frac{3}{2}x$. Por linhas, dividindo $L_1$ por 2 e $L_2$ por 3, temos retas com mesmo coeficiente angular $-\frac{1}{2}$, logo paralelas ou coincidentes (nunca SPD). **Correto.**
   - Item (b): $x + 2y = 5$ e $x + 2y = k/3$. Coincidem se $k/3 = 5 \implies k = 15$ (SPI), com $(x, y)^\top = (5 - 2t,\; t)^\top$. Se $k \ne 15$, as retas são paralelas distintas (SI). **Correto.**

7. **[Exercício 5.2.1.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-02.dlt#L229-L244) (`exr:5-2-1-4`):**
   - $\mathbf{W} = \begin{pmatrix} 4 & -2 \\ 2 & -1 \end{pmatrix}$.
   - Item (a): Alvo $(10, 5)^\top\text{ Hz}$. O sistema reduz-se a $2r_1 - r_2 = 5 \implies r_2 = 2r_1 - 5$.
     Exigindo $r_1 \ge 0$ e $r_2 \ge 0$, temos $2r_1 - 5 \ge 0 \implies r_1 \ge 2{,}5\text{ Hz}$. Infinitas soluções válidas: $(r_1,\; 2r_1 - 5)^\top$ com $r_1 \ge 2{,}5\text{ Hz}$ (ex.: $r_1 = 4\text{ Hz}, r_2 = 3\text{ Hz} \implies \mathbf{W}\mathbf{r} = (16-6, 8-3)^\top = (10, 5)^\top$). **Correto.**
   - Item (b): Alvo $(10, 8)^\top\text{ Hz}$. Como a primeira linha de $\mathbf{W}$ é o dobro da segunda, toda saída física satisfaz $r_{\text{pós}, 1} = 2r_{\text{pós}, 2}$. Para o alvo $(10, 8)^\top$, teríamos $10 = 2(8) = 16$, contradição. O sistema é impossível (SI). **Correto.**

---

### 3.2 Seção 2: Eliminação de Gauss (`sec:5-2-2`)

1. **[Exemplo 5.2.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-02.dlt#L296-L325) (`exm:5-2-gauss-3x3`):**
   - Sistema: $2y + z = 3$, $x - y + 2z = -3$, $2x + y - z = 5$.
   - Matriz aumentada: $\left(\begin{array}{ccc|c} 0 & 2 & 1 & 3 \\ 1 & -1 & 2 & -3 \\ 2 & 1 & -1 & 5 \end{array}\right) \xrightarrow{L_1 \leftrightarrow L_2} \left(\begin{array}{ccc|c} 1 & -1 & 2 & -3 \\ 0 & 2 & 1 & 3 \\ 2 & 1 & -1 & 5 \end{array}\right)$.
   - $L_3 \leftarrow L_3 - 2L_1$: $[2 - 2, 1 - 2(-1), -1 - 2(2) \mid 5 - 2(-3)] = [0, 3, -5 \mid 11]$.
   - $L_2 \leftarrow \frac{1}{2}L_2$: $[0, 1, 1/2 \mid 3/2]$.
   - $L_3 \leftarrow L_3 - 3L_2$: $[0, 3 - 3(1), -5 - 3(1/2) \mid 11 - 3(3/2)] = [0, 0, -13/2 \mid 13/2]$.
   - Substituição regressiva:
     - Linha 3: $-\frac{13}{2}z = \frac{13}{2} \implies z = -1$.
     - Linha 2: $y + \frac{1}{2}(-1) = \frac{3}{2} \implies y = 2$.
     - Linha 1: $x - 2 + 2(-1) = -3 \implies x - 4 = -3 \implies x = 1$.
   - Conferência nas equações originais: $2(2) + (-1) = 3$; $1 - 2 + 2(-1) = -3$; $2(1) + 2 - (-1) = 5$. Solução $(1, 2, -1)^\top$. **Correto.**

2. **[Exemplo 5.2.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-02.dlt#L327-L349) (`exm:5-2-olfatorio-3x3`):**
   - Sistema de odorantes: $\begin{pmatrix} 1 & 2 & 1 \\ 2 & 5 & 1 \\ -1 & 1 & 3 \end{pmatrix}\begin{pmatrix} c_1 \\ c_2 \\ c_3 \end{pmatrix} = \begin{pmatrix} 7 \\ 13 \\ 4 \end{pmatrix}$.
   - $L_2 \leftarrow L_2 - 2L_1$: $[2 - 2, 5 - 4, 1 - 2 \mid 13 - 14] = [0, 1, -1 \mid -1]$.
   - $L_3 \leftarrow L_3 + L_1$: $[-1 + 1, 1 + 2, 3 + 1 \mid 4 + 7] = [0, 3, 4 \mid 11]$.
   - $L_3 \leftarrow L_3 - 3L_2$: $[0, 3 - 3, 4 - 3(-1) \mid 11 - 3(-1)] = [0, 0, 7 \mid 14]$.
   - Substituição regressiva:
     - $7c_3 = 14 \implies c_3 = 2\;\mu\text{M}$.
     - $c_2 - 2 = -1 \implies c_2 = 1\;\mu\text{M}$.
     - $c_1 + 2(1) + 2 = 7 \implies c_1 = 3\;\mu\text{M}$.
   - Conferência: $3 + 2(1) + 2 = 7$; $2(3) + 5(1) + 2 = 13$; $-3 + 1 + 3(2) = 4$. **Correto.**

3. **[Exemplo 5.2.5](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-02.dlt#L351-L369) (`exm:5-2-gauss-degenerado`):**
   - $\left(\begin{array}{ccc|c} 1 & 2 & -1 & 4 \\ 2 & 5 & 1 & 11 \\ 1 & 3 & 2 & b_3 \end{array}\right) \xrightarrow{L_2 - 2L_1,\; L_3 - L_1} \left(\begin{array}{ccc|c} 1 & 2 & -1 & 4 \\ 0 & 1 & 3 & 3 \\ 0 & 1 & 3 & b_3 - 4 \end{array}\right) \xrightarrow{L_3 - L_2} \left(\begin{array}{ccc|c} 1 & 2 & -1 & 4 \\ 0 & 1 & 3 & 3 \\ 0 & 0 & 0 & b_3 - 7 \end{array}\right)$.
   - Se $b_3 = 7$: linha $[0\; 0\; 0 \mid 0]$, $z = t$ livre.
     $y + 3t = 3 \implies y = 3 - 3t$.
     $x + 2(3 - 3t) - t = 4 \implies x + 6 - 7t = 4 \implies x = 7t - 2$.
     Solução geral: $(7t - 2,\; 3 - 3t,\; t)^\top$ (SPI). **Correto.**
   - Se $b_3 = 9$: linha $[0\; 0\; 0 \mid 2]$, contradição $0 = 2$ (SI). **Correto.**

4. **[Código Python 5.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-02.dlt#L373-L395) (`cod:5-2-gauss`):**
   - `sol1`: `[1.0, 2.0, -1.0]`. **Correto.**
   - `sol2`: `[3.0, 1.0, 2.0]`. **Correto.**
   - Captura de `LinAlgError` na matriz singular: impresso com sucesso. **Correto.**

5. **[Exercício 5.2.2.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-02.dlt#L406-L426) (`exr:5-2-2-1`):**
   - $\left(\begin{array}{ccc|c} 1 & 3 & -1 & 4 \\ 2 & 7 & 1 & 12 \\ -1 & -2 & 3 & -1 \end{array}\right) \xrightarrow{L_2 - 2L_1,\; L_3 + L_1} \left(\begin{array}{ccc|c} 1 & 3 & -1 & 4 \\ 0 & 1 & 3 & 4 \\ 0 & 1 & 2 & 3 \end{array}\right) \xrightarrow{L_3 - L_2} \left(\begin{array}{ccc|c} 1 & 3 & -1 & 4 \\ 0 & 1 & 3 & 4 \\ 0 & 0 & -1 & -1 \end{array}\right)$.
   - $-z = -1 \implies z = 1$.
   - $y + 3(1) = 4 \implies y = 1$.
   - $x + 3(1) - 1 = 4 \implies x = 2$.
   - Conferência: $2 + 3(1) - 1 = 4$; $2(2) + 7(1) + 1 = 12$; $-2 - 2(1) + 3(1) = -1$. Solução $(2, 1, 1)^\top$. **Correto.**

6. **[Exercício 5.2.2.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-02.dlt#L428-L450) (`exr:5-2-2-2`):**
   - Mistura de meios: glicose ($2, 1, 0$), glutamina ($1, 2, 1$), piruvato ($0, 1, 2$). Alvo: $(10, 16, 14)^\top\;\mu\text{mol}$.
   - Matriz aumentada: $\left(\begin{array}{ccc|c} 2 & 1 & 0 & 10 \\ 1 & 2 & 1 & 16 \\ 0 & 1 & 2 & 14 \end{array}\right) \xrightarrow{L_1 \leftrightarrow L_2} \left(\begin{array}{ccc|c} 1 & 2 & 1 & 16 \\ 2 & 1 & 0 & 10 \\ 0 & 1 & 2 & 14 \end{array}\right) \xrightarrow{L_2 - 2L_1} \left(\begin{array}{ccc|c} 1 & 2 & 1 & 16 \\ 0 & -3 & -2 & -22 \\ 0 & 1 & 2 & 14 \end{array}\right)$.
   - $L_2 \leftrightarrow L_3$ e $L_3 \leftarrow L_3 + 3L_2$:
     $\left(\begin{array}{ccc|c} 1 & 2 & 1 & 16 \\ 0 & 1 & 2 & 14 \\ 0 & -3 & -2 & -22 \end{array}\right) \longrightarrow \left(\begin{array}{ccc|c} 1 & 2 & 1 & 16 \\ 0 & 1 & 2 & 14 \\ 0 & 0 & 4 & 20 \end{array}\right)$.
   - $4v_C = 20 \implies v_C = 5\text{ mL}$; $v_B + 2(5) = 14 \implies v_B = 4\text{ mL}$; $v_A + 2(4) + 5 = 16 \implies v_A = 3\text{ mL}$.
   - Conferência: $2(3) + 4 = 10$; $3 + 2(4) + 5 = 16$; $4 + 2(5) = 14$. **Correto.**

7. **[Exercício 5.2.2.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-02.dlt#L452-L471) (`exr:5-2-2-3`):**
   - $\left(\begin{array}{ccc|c} 1 & -2 & 1 & 3 \\ 2 & -3 & 4 & 8 \\ 3 & -5 & 5 & b_3 \end{array}\right) \xrightarrow{L_2 - 2L_1,\; L_3 - 3L_1} \left(\begin{array}{ccc|c} 1 & -2 & 1 & 3 \\ 0 & 1 & 2 & 2 \\ 0 & 1 & 2 & b_3 - 9 \end{array}\right) \xrightarrow{L_3 - L_2} \left(\begin{array}{ccc|c} 1 & -2 & 1 & 3 \\ 0 & 1 & 2 & 2 \\ 0 & 0 & 0 & b_3 - 11 \end{array}\right)$.
   - Item (a): $b_3 = 11 \implies L_3 = [0\; 0\; 0 \mid 0]$. Variável livre $z = t$.
     $y = 2 - 2t$; $x - 2(2 - 2t) + t = 3 \implies x - 4 + 5t = 3 \implies x = 7 - 5t$. Solução $(7 - 5t,\; 2 - 2t,\; t)^\top$ (SPI). **Correto.**
   - Item (b): $b_3 = 12 \implies L_3 = [0\; 0\; 0 \mid 1]$, contradição $0 = 1$ (SI). **Correto.**

8. **[Exercício 5.2.2.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-02.dlt#L473-L496) (`exr:5-2-2-4`):**
   - Corrente de membrana: $I(V) = g_{\text{Na}}(V - 50) + g_{\text{K}}(V + 80) + g_{\text{L}}(V + 60)$.
   - Para $V = -70\text{ mV}$, $I = -440\text{ pA}$: $-120g_{\text{Na}} + 10g_{\text{K}} - 10g_{\text{L}} = -440 \xrightarrow{\div 10} -12g_{\text{Na}} + g_{\text{K}} - g_{\text{L}} = -44$.
   - Para $V = -20\text{ mV}$, $I = 160\text{ pA}$: $-70g_{\text{Na}} + 60g_{\text{K}} + 40g_{\text{L}} = 160 \xrightarrow{\div 10} -7g_{\text{Na}} + 6g_{\text{K}} + 4g_{\text{L}} = 16$.
   - Para $V = +30\text{ mV}$, $I = 760\text{ pA}$: $-20g_{\text{Na}} + 110g_{\text{K}} + 90g_{\text{L}} = 760 \xrightarrow{\div 10} -2g_{\text{Na}} + 11g_{\text{K}} + 9g_{\text{L}} = 76$.
   - Matriz escalonada por $L_2 - L_1 = [5, 5, 5 \mid 60]$ e $L_3 - L_1 = [10, 10, 10 \mid 120]$.
     Como $(L_3 - L_1) = 2(L_2 - L_1)$, a linha 3 zera identicamente: $[0\; 0\; 0 \mid 0]$.
   - Dividindo $L_2$ por $5$ e fazendo $L_2 \leftarrow L_2 + 12L_1$:
     $13g_{\text{K}} + 11g_{\text{L}} = 100$ e $g_{\text{Na}} + g_{\text{K}} + g_{\text{L}} = 12$.
     Para $g_{\text{L}} = 2\text{ nS} \implies 13g_{\text{K}} = 78 \implies g_{\text{K}} = 6\text{ nS} \implies g_{\text{Na}} = 12 - 6 - 2 = 4\text{ nS}$.
     Conferência em $V = -70$: $4(-120) + 6(10) + 2(-10) = -480 + 60 - 20 = -440\text{ pA}$. **Correto.**
   - Justificativa conceitual: $I(V)$ é linear em $V$ com inclinação $\sum g_i$ e intercepto $\sum g_i E_i$; três pontos na mesma reta produzem no máximo duas equações linearmente independentes. O bloqueio com TTX zera $g_{\text{Na}}$ e quebra a degenerescência. **Correto.**

---

### 3.3 Seção 3: A matriz como transformação do plano (`sec:5-2-3`)

1. **[Exemplo 5.2.6](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-02.dlt#L587-L608) (`exm:5-2-arena-rato`):**
   - $\mathbf{R}_{90^\circ} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$, $\mathbf{S} = \begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix}$.
   - $\mathbf{S}\mathbf{R}_{90^\circ} = \begin{pmatrix} 0 & -2 \\ 3 & 0 \end{pmatrix} \implies (\mathbf{S}\mathbf{R}_{90^\circ})\begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} -2 \\ 3 \end{pmatrix}$.
   - $\mathbf{R}_{90^\circ}\mathbf{S} = \begin{pmatrix} 0 & -3 \\ 2 & 0 \end{pmatrix} \implies (\mathbf{R}_{90^\circ}\mathbf{S})\begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} -3 \\ 2 \end{pmatrix}$.
   - Determinantes: $\det(\mathbf{S}\mathbf{R}_{90^\circ}) = 0 - (-6) = 6$ e $\det(\mathbf{R}_{90^\circ}\mathbf{S}) = 0 - (-6) = 6$. **Correto.**

2. **[Exemplo 5.2.7](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-02.dlt#L609-L633) (`exm:5-2-soma-diferenca-det`):**
   - $\mathbf{M} = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$, $\mathbf{r} = (20, 12)^\top\text{ Hz}$.
   - $\mathbf{M}\mathbf{r} = (20 + 12,\; 20 - 12)^\top = (32, 8)^\top\text{ Hz}$.
   - $\det\mathbf{M} = 1(-1) - 1(1) = -2$ (dobra áreas, inverte orientação). **Correto.**
   - $\mathbf{D} = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix} \implies \det\mathbf{D} = 4 - 4 = 0$. $\mathbf{D}\mathbf{r} = (r_1 + 2r_2)(1, 2)^\top$ colapsa todo o plano na reta $y = 2x$. **Correto.**

3. **[Código Python 5.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-02.dlt#L635-L655) (`cod:5-2-transformacoes`):**
   - `S @ R90 @ p`: `[-2.0, 3.0]`. **Correto.**
   - `R90 @ S @ p`: `[-3.0, 2.0]`. **Correto.**
   - Determinantes: `6.000`, `-2.000` e `0.000`. **Correto.**

4. **[Exercício 5.2.3.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-02.dlt#L665-L683) (`exr:5-2-3-1`):**
   - $T(\mathbf{e}_1) = (3, 1)^\top$, $T(\mathbf{e}_2) = (-1, 2)^\top \implies \mathbf{A} = \begin{pmatrix} 3 & -1 \\ 1 & 2 \end{pmatrix}$.
   - $T\begin{pmatrix} 2 \\ -3 \end{pmatrix} = \begin{pmatrix} 3(2) + (-1)(-3) \\ 1(2) + 2(-3) \end{pmatrix} = \begin{pmatrix} 6 + 3 \\ 2 - 6 \end{pmatrix} = \begin{pmatrix} 9 \\ -4 \end{pmatrix}$.
   - $\det\mathbf{A} = 3(2) - (-1)(1) = 6 + 1 = 7$ (multiplica áreas por 7, preserva orientação). **Correto.**

5. **[Exercício 5.2.3.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-02.dlt#L685-L706) (`exr:5-2-3-2`):**
   - $\theta = -60^\circ$: $\mathbf{R}_{-60^\circ} = \begin{pmatrix} 1/2 & \sqrt{3}/2 \\ -\sqrt{3}/2 & 1/2 \end{pmatrix}$.
   - Ponto $\mathbf{p} = (2,\; 2\sqrt{3})^\top\text{ cm}$:
     $\mathbf{p}' = \begin{pmatrix} \frac{1}{2}(2) + \frac{\sqrt{3}}{2}(2\sqrt{3}) \\ -\frac{\sqrt{3}}{2}(2) + \frac{1}{2}(2\sqrt{3}) \end{pmatrix} = \begin{pmatrix} 1 + 3 \\ -\sqrt{3} + \sqrt{3} \end{pmatrix} = \begin{pmatrix} 4 \\ 0 \end{pmatrix}\text{ cm}$.
   - Distâncias: $\|\mathbf{p}\| = \sqrt{4 + 12} = 4\text{ cm}$ e $\|\mathbf{p}'\| = 4\text{ cm}$.
   - Determinante: $\left(\frac{1}{2}\right)^2 - \left(\frac{\sqrt{3}}{2}\right)\!\left(-\frac{\sqrt{3}}{2}\right) = \frac{1}{4} + \frac{3}{4} = 1$. **Correto.**

6. **[Exercício 5.2.3.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-02.dlt#L708-L728) (`exr:5-2-3-3`):**
   - $\mathbf{F} = \begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix}$, $\mathbf{C} = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$.
   - $\mathbf{C}\mathbf{F} = \begin{pmatrix} -1 & 2 \\ 0 & 1 \end{pmatrix} \implies (\mathbf{C}\mathbf{F})\begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$.
   - $\mathbf{F}\mathbf{C} = \begin{pmatrix} -1 & -2 \\ 0 & 1 \end{pmatrix} \implies (\mathbf{F}\mathbf{C})\begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} -3 \\ 1 \end{pmatrix}$.
   - $\det\mathbf{F} = -1$, $\det\mathbf{C} = 1 \implies \det(\mathbf{C}\mathbf{F}) = -1 = \det(\mathbf{F}\mathbf{C}) = (\det\mathbf{F})(\det\mathbf{C})$. **Correto.**

7. **[Exercício 5.2.3.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-02.dlt#L730-L748) (`exr:5-2-3-4`):**
   - $\mathbf{P} = \begin{pmatrix} 1/2 & 1/2 \\ 1/2 & 1/2 \end{pmatrix}$, $\mathbf{Q} = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$.
   - $\det\mathbf{P} = \frac{1}{4} - \frac{1}{4} = 0$; $\det\mathbf{Q} = 2 - 1 = 1$.
   - Idempotência: $\mathbf{P}^2 = \begin{pmatrix} 1/4+1/4 & 1/4+1/4 \\ 1/4+1/4 & 1/4+1/4 \end{pmatrix} = \mathbf{P}$.
   - Vetores distintos $\mathbf{r}_a = (20, 10)^\top$ e $\mathbf{r}_b = (15, 15)^\top$: ambos produzem $\mathbf{P}\mathbf{r} = (15, 15)^\top\text{ Hz}$, destruindo a informação da diferença $r_1 - r_2$. **Correto.**

---

### 3.4 Seção 4: Matriz inversa e mistura de fontes no EEG (`sec:5-2-4`)

1. **[Exemplo 5.2.8](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-02.dlt#L821-L842) (`exm:5-2-inversa-comp`):**
   - $\mathbf{A} = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} \implies \det\mathbf{A} = 1 \implies \mathbf{A}^{-1} = \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix}$.
     $\mathbf{A}\mathbf{A}^{-1} = \begin{pmatrix} 2 - 1 & -2 + 2 \\ 1 - 1 & -1 + 2 \end{pmatrix} = \mathbf{I}_2$.
   - $\mathbf{B} = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} \implies \det\mathbf{B} = 1 \implies \mathbf{B}^{-1} = \begin{pmatrix} 1 & -2 \\ 0 & 1 \end{pmatrix}$.
   - $\mathbf{A}\mathbf{B} = \begin{pmatrix} 2 & 5 \\ 1 & 3 \end{pmatrix} \implies \det(\mathbf{A}\mathbf{B}) = 6 - 5 = 1 \implies (\mathbf{A}\mathbf{B})^{-1} = \begin{pmatrix} 3 & -5 \\ -1 & 2 \end{pmatrix}$.
   - Ordem invertida: $\mathbf{B}^{-1}\mathbf{A}^{-1} = \begin{pmatrix} 1 & -2 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix} = \begin{pmatrix} 1 + 2 & -1 - 4 \\ 0 - 1 & 0 + 2 \end{pmatrix} = \begin{pmatrix} 3 & -5 \\ -1 & 2 \end{pmatrix} = (\mathbf{A}\mathbf{B})^{-1}$.
   - Ordem direta errada: $\mathbf{A}^{-1}\mathbf{B}^{-1} = \begin{pmatrix} 1 & -3 \\ -1 & 4 \end{pmatrix} \ne (\mathbf{A}\mathbf{B})^{-1}$. **Correto.**

2. **[Exemplo 5.2.9](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-02.dlt#L844-L867) (`exm:5-2-eeg-desmistura`):**
   - Matriz de mistura: $\mathbf{A} = \begin{pmatrix} 0{,}8 & 0{,}4 \\ 0{,}2 & 0{,}6 \end{pmatrix}$.
   - $\det\mathbf{A} = 0{,}48 - 0{,}08 = 0{,}4 \implies \frac{1}{0{,}4} = 2{,}5$.
   - $\mathbf{A}^{-1} = 2{,}5\begin{pmatrix} 0{,}6 & -0{,}4 \\ -0{,}2 & 0{,}8 \end{pmatrix} = \begin{pmatrix} 1{,}5 & -1{,}0 \\ -0{,}5 & 2{,}0 \end{pmatrix}$.
   - Conferência $\mathbf{A}\mathbf{A}^{-1}$: $\begin{pmatrix} 1{,}2 - 0{,}2 & -0{,}8 + 0{,}8 \\ 0{,}3 - 0{,}3 & -0{,}2 + 1{,}2 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = \mathbf{I}_2$.
   - Desmistura de $\mathbf{X} = \begin{pmatrix} 10 & 14 & -2 \\ 5 & 1 & 7 \end{pmatrix}\;\mu\text{V}$:
     $\mathbf{S} = \mathbf{A}^{-1}\mathbf{X} = \begin{pmatrix} 1{,}5 & -1{,}0 \\ -0{,}5 & 2{,}0 \end{pmatrix}\begin{pmatrix} 10 & 14 & -2 \\ 5 & 1 & 7 \end{pmatrix} = \begin{pmatrix} 15 - 5 & 21 - 1 & -3 - 7 \\ -5 + 10 & -7 + 2 & 1 + 14 \end{pmatrix} = \begin{pmatrix} 10 & 20 & -10 \\ 5 & -5 & 15 \end{pmatrix}\;\mu\text{V}$.
   - Conferência direta com $\mathbf{A}\mathbf{S}$:
     - $t=1$: $\begin{pmatrix} 0{,}8(10)+0{,}4(5) \\ 0{,}2(10)+0{,}6(5) \end{pmatrix} = \begin{pmatrix} 10 \\ 5 \end{pmatrix}$.
     - $t=2$: $\begin{pmatrix} 0{,}8(20)+0{,}4(-5) \\ 0{,}2(20)+0{,}6(-5) \end{pmatrix} = \begin{pmatrix} 16 - 2 \\ 4 - 3 \end{pmatrix} = \begin{pmatrix} 14 \\ 1 \end{pmatrix}$.
     - $t=3$: $\begin{pmatrix} 0{,}8(-10)+0{,}4(15) \\ 0{,}2(-10)+0{,}6(15) \end{pmatrix} = \begin{pmatrix} -8 + 6 \\ -2 + 9 \end{pmatrix} = \begin{pmatrix} -2 \\ 7 \end{pmatrix}$. **Correto.**

3. **[Código Python 5.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-02.dlt#L871-L894) (`cod:5-2-eeg`):**
   - Inversa `np.linalg.inv(A)`: `[[1.5, -1.0], [-0.5, 2.0]]`. **Correto.**
   - Reconstrução `np.linalg.solve(A, X_amostra)`: `[[10.0, 20.0, -10.0], [5.0, -5.0, 15.0]]`. **Correto.**
   - Simulação contínua com $250$ pontos: `np.allclose(S, S_rec)` devolve `True`. **Correto.**

4. **[Exercício 5.2.4.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-02.dlt#L905-L923) (`exr:5-2-4-1`):**
   - Item (a): $\mathbf{A} = \begin{pmatrix} 4 & 2 \\ 3 & 2 \end{pmatrix} \implies \det\mathbf{A} = 8 - 6 = 2 \ne 0$.
     $\mathbf{A}^{-1} = \frac{1}{2}\begin{pmatrix} 2 & -2 \\ -3 & 4 \end{pmatrix} = \begin{pmatrix} 1 & -1 \\ -3/2 & 2 \end{pmatrix}$.
     $\mathbf{A}\mathbf{A}^{-1} = \begin{pmatrix} 4 - 3 & -4 + 4 \\ 3 - 3 & -3 + 4 \end{pmatrix} = \mathbf{I}_2$. **Correto.**
   - Item (b): $\mathbf{B} = \begin{pmatrix} 6 & -3 \\ -4 & 2 \end{pmatrix} \implies \det\mathbf{B} = 12 - 12 = 0$. Singular. **Correto.**

5. **[Exercício 5.2.4.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-02.dlt#L925-L945) (`exr:5-2-4-2`):**
   - $\mathbf{A} = \begin{pmatrix} 0{,}9 & 0{,}3 \\ 0{,}1 & 0{,}7 \end{pmatrix} \implies \det\mathbf{A} = 0{,}63 - 0{,}03 = 0{,}6$.
   - $\mathbf{A}^{-1} = \frac{1}{0{,}6}\begin{pmatrix} 0{,}7 & -0{,}3 \\ -0{,}1 & 0{,}9 \end{pmatrix} = \frac{1}{6}\begin{pmatrix} 7 & -3 \\ -1 & 9 \end{pmatrix}$.
   - Para $\mathbf{X} = \begin{pmatrix} 15 & 9 & -3 \\ 5 & 7 & 11 \end{pmatrix}\;\mu\text{V}$:
     $\mathbf{S} = \frac{1}{6}\begin{pmatrix} 7 & -3 \\ -1 & 9 \end{pmatrix}\begin{pmatrix} 15 & 9 & -3 \\ 5 & 7 & 11 \end{pmatrix} = \frac{1}{6}\begin{pmatrix} 105 - 15 & 63 - 21 & -21 - 33 \\ -15 + 45 & -9 + 63 & 3 + 99 \end{pmatrix} = \frac{1}{6}\begin{pmatrix} 90 & 42 & -54 \\ 30 & 54 & 102 \end{pmatrix} = \begin{pmatrix} 15 & 7 & -9 \\ 5 & 9 & 17 \end{pmatrix}\;\mu\text{V}$.
   - Conferência em $t=3$: $0{,}9(-9) + 0{,}3(17) = -8{,}1 + 5{,}1 = -3$; $0{,}1(-9) + 0{,}7(17) = -0{,}9 + 11{,}9 = 11$. **Correto.**

6. **[Exercício 5.2.4.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-02.dlt#L947-L970) (`exr:5-2-4-3`):**
   - $\mathbf{P} = \begin{pmatrix} 1 & 3 \\ 0 & 1 \end{pmatrix} \implies \mathbf{P}^{-1} = \begin{pmatrix} 1 & -3 \\ 0 & 1 \end{pmatrix}$; $\mathbf{Q} = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} \implies \mathbf{Q}^{-1} = \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix}$.
   - $\mathbf{P}\mathbf{Q} = \begin{pmatrix} 5 & 4 \\ 1 & 1 \end{pmatrix} \implies \det(\mathbf{P}\mathbf{Q}) = 1 \implies (\mathbf{P}\mathbf{Q})^{-1} = \begin{pmatrix} 1 & -4 \\ -1 & 5 \end{pmatrix}$.
   - $\mathbf{Q}^{-1}\mathbf{P}^{-1} = \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix}\begin{pmatrix} 1 & -3 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & -4 \\ -1 & 5 \end{pmatrix} = (\mathbf{P}\mathbf{Q})^{-1}$.
   - Sistema $(\mathbf{P}\mathbf{Q})\mathbf{x} = \begin{pmatrix} 17 \\ 5 \end{pmatrix}$:
     $\mathbf{x} = \begin{pmatrix} 1 & -4 \\ -1 & 5 \end{pmatrix}\begin{pmatrix} 17 \\ 5 \end{pmatrix} = \begin{pmatrix} 17 - 20 \\ -17 + 25 \end{pmatrix} = \begin{pmatrix} -3 \\ 8 \end{pmatrix}$.
   - Conferência: $5(-3) + 4(8) = 17$; $1(-3) + 1(8) = 5$. **Correto.**

7. **[Exercício 5.2.4.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/tema-02.dlt#L972-L1000) (`exr:5-2-4-4`):**
   - $\mathbf{A} = \begin{pmatrix} 0{,}50 & 0{,}50 \\ 0{,}49 & 0{,}51 \end{pmatrix}$.
   - $\det\mathbf{A} = (0{,}50)(0{,}51) - (0{,}50)(0{,}49) = 0{,}255 - 0{,}245 = 0{,}01$.
   - $\mathbf{A}^{-1} = \frac{1}{0{,}01}\begin{pmatrix} 0{,}51 & -0{,}50 \\ -0{,}49 & 0{,}50 \end{pmatrix} = \begin{pmatrix} 51 & -50 \\ -49 & 50 \end{pmatrix}$.
   - Sinal limpo para $\mathbf{s} = (20, 10)^\top\;\mu\text{V}$:
     $\mathbf{x}_{\text{limpo}} = \begin{pmatrix} 0{,}50(20) + 0{,}50(10) \\ 0{,}49(20) + 0{,}51(10) \end{pmatrix} = \begin{pmatrix} 15{,}0 \\ 14{,}9 \end{pmatrix}\;\mu\text{V}$.
   - Sinal com ruído $\boldsymbol{\varepsilon} = (0{,}5;\; -0{,}5)^\top\;\mu\text{V} \implies \mathbf{x}_{\text{medido}} = (15{,}5;\; 14{,}4)^\top\;\mu\text{V}$.
   - Reconstrução:
     $\hat{\mathbf{s}} = \begin{pmatrix} 51(15{,}5) - 50(14{,}4) \\ -49(15{,}5) + 50(14{,}4) \end{pmatrix} = \begin{pmatrix} 790{,}5 - 720{,}0 \\ -759{,}5 + 720{,}0 \end{pmatrix} = \begin{pmatrix} 70{,}5 \\ -39{,}5 \end{pmatrix}\;\mu\text{V}$.
   - Erro: $\hat{\mathbf{s}} - \mathbf{s} = (50{,}5;\; -49{,}5)^\top\;\mu\text{V} = \mathbf{A}^{-1}\boldsymbol{\varepsilon}$.
   - Normas:
     $\|\boldsymbol{\varepsilon}\| = \sqrt{0{,}5^2 + (-0{,}5)^2} = \sqrt{0{,}5} \approx 0{,}7071\;\mu\text{V}$.
     $\|\hat{\mathbf{s}} - \mathbf{s}\| = \sqrt{50{,}5^2 + (-49{,}5)^2} = \sqrt{2\,550{,}25 + 2\,450{,}25} = \sqrt{5\,000{,}5} \approx 70{,}7142\;\mu\text{V}$.
     Fator de amplificação: $\frac{70{,}7142}{0{,}707107} = 100 = \frac{1}{\det\mathbf{A}}$. **Correto.**

---

**Nenhum erro matemático encontrado.**

---

## 4. Auditoria dos Critérios Editoriais e Pedagógicos

| Critério | Status | Detalhamento |
|---|---|---|
| **Dica e solução completa em cada exercício** | Conforme | Todos os 16 exercícios (4 por seção) contêm `<hint>` específico e `<solution collapsible="true" collapsed="true">` com raciocínio completo, desenvolvimento algébrico explícito e interpretação física/biológica, e não apenas o resultado numérico final. |
| **Pelo menos um exemplo biológico por seção** | Conforme | **Seção 1:** inversão de pesos em rede pré/pós-sináptica (`exm:5-2-inverter-rede`), mistura de soluções iônicas $\text{Na}^+/\text{K}^+$ (`exm:5-2-mistura-regimes`), decodificação pré-sináptica (`exr:5-2-1-2`) e balanço $E/I$ degenerado (`exr:5-2-1-4`).<br>**Seção 2:** decodificação de concentrações odorantes no sistema olfatório (`exm:5-2-olfatorio-3x3`), meio de cultura celular (`exr:5-2-2-2`) e determinação de condutâncias passivas de membrana $\text{Na}^+, \text{K}^+, \text{L}$ (`exr:5-2-2-4`).<br>**Seção 3:** correção de eixos de vídeo em arena circular de comportamento animal (`exm:5-2-arena-rato`), modos de soma e contraste diferencial de disparos (`exm:5-2-soma-diferenca-det`), rotação de rastreamento (`exr:5-2-3-2`) e projeção que colapsa informação neural (`exr:5-2-3-4`).<br>**Seção 4:** condução de volume e separação de fontes corticais alfa e beta no EEG (`exm:5-2-eeg-desmistura`, `cod:5-2-eeg`, `exr:5-2-4-2` e `exr:5-2-4-4`). |
| **Afirmações de neurociência de livro-texto** | Conforme | Modelagem linear da condução de volume no EEG ($V = \mathbf{A}\mathbf{s}$), correntes e condutâncias iônicas de repouso ($I(V) = \sum g_i(V - E_i)$), potenciais de reversão padrão ($E_{\text{Na}} \approx +50\text{ mV}$, $E_{\text{K}} \approx -80\text{ mV}$, $E_{\text{L}} \approx -60\text{ mV}$), bloqueio farmacológico seletivo com TTX e bandas de frequência do EEG (alfa a 10 Hz, beta a 20 Hz) rigorosamente respaldadas pela literatura (*Dayan & Abbott; Kandel et al.*). |
| **Apresentação progressiva de conceitos** | Conforme | Progressão didática impecável: parte de sistemas $2 \times 2$ e suas leituras por linhas/colunas, avança para a eliminação de Gauss em $3 \times 3$, formaliza matrizes como transformações lineares e determinantes, e culmina na inversão matricial aplicada ao EEG. Menções a temas avançados (espaços vetoriais, autovalores, SVD, ICA) são explicitamente situadas em seus respectivos temas futuros. |
| **Código Python funcional** | Conforme | Os 4 blocos de código (`cod:5-2-sistema`, `cod:5-2-gauss`, `cod:5-2-transformacoes` e `cod:5-2-eeg`) são autocontidos, utilizam práticas padrão do NumPy moderno (`np.linalg.solve`, `np.linalg.det`, `np.linalg.inv`, operador `@`, tratamento de `LinAlgError`), rodam sem dependências externas e possuem comentários com as saídas esperadas exatas. |
| **Consistência de notação** | Conforme | Vetores em negrito minúsculo ($\mathbf{x}, \mathbf{b}, \mathbf{r}_{\text{pré}}, \mathbf{r}_{\text{pós}}, \mathbf{s}, \mathbf{u}, \mathbf{v}, \mathbf{p}, \mathbf{e}_1, \mathbf{e}_2$), matrizes em negrito maiúsculo ($\mathbf{A}, \mathbf{W}, \mathbf{S}, \mathbf{R}_\theta, \mathbf{C}_k, \mathbf{P}_x, \mathbf{M}, \mathbf{D}, \mathbf{I}_n, \mathbf{B}, \mathbf{X}, \mathbf{P}, \mathbf{Q}$), escalares em itálico ($a_{ij}, x_i, r_i, c, k, \theta, t$), decimais com vírgula na prosa e no KaTeX ($0{,}5$, $2{,}5$, $0{,}01$) e ponto no código Python (`0.5`, `2.5`). |
| **Cobertura dos subtemas exigidos** | Conforme | Cobre com fidelidade as quatro seções delineadas pelo gestor: (1) Sistemas lineares na forma matricial; (2) Eliminação de Gauss; (3) A matriz como transformação do plano (determinante 2×2); (4) Matriz inversa e mistura de fontes no EEG, com blocos NumPy em todas as seções. |
| **Extensão e tamanho da aula** | Conforme | O arquivo possui 1 036 linhas e aproximadamente 4 600 palavras de prosa, situando-se perfeitamente dentro da faixa-alvo estipulada de até ~5 500 palavras de prosa. **A aula não passa do limite de 5 500 palavras de prosa.** |
| **Auditoria do script de figura** | Conforme | O script [transformacao-plano.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-05/fig/transformacao-plano.py) utiliza `plt.rcParams["svg.fonttype"] = "none"`, salva `transformacao-plano.svg` em `fig/`, exibe grade 2×2 ilustrando a identidade, rotação de $45^\circ$, cisalhamento e a matriz de soma e diferença, com rótulos em português, distinção de cores para determinantes positivos e negativos, e legenda completa. |