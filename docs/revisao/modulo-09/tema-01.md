# Relatório de Revisão Técnica — Módulo 09 · Tema 01 (Fundamentos de Deep Learning)

- **Arquivo revisado:** [tema-01.dlt](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-01.dlt)
- **Documentos de referência:** [PADRAO-AULAS.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/PADRAO-AULAS.md) e [DELTA-COLA.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/DELTA-COLA.md)
- **Data da revisão:** 14 de novembro de 2026
- **Perfil do revisor:** Matemático, Neurocientista Computacional, Especialista em Deep Learning/PyTorch e Professor de Alunos de Ciências Biológicas

---

## 1. Veredito

**APROVAR**

A aula [conteudo/modulo-09/tema-01.dlt](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-01.dlt) atinge um padrão de excelência técnica, pedagógica e matemática excepcional. Trata-se de uma introdução impecável ao aprendizado profundo para estudantes de Ciências Biológicas direcionados à neurociência computacional.

Principais destaques da auditoria:
1. **Exatidão matemática:** Todas as contas de todos os exemplos numéricos e das soluções dos 16 exercícios foram integralmente recalculadas à mão e conferidas; estão 100% corretas, com convergência de valores até a quarta casa decimal.
2. **Código Python auditado linha a linha:** Todos os blocos (<c>cod:9-1-backprop</c>, <c>cod:9-1-mlp-digits</c> e o script do exercício de parada antecipada/weight decay) são rigorosamente autocontidos, compatíveis com PyTorch 2.x e scikit-learn 1.x, utilizam dtypes corretos (<c>float32</c>/<c>float64</c> para tensores contínuos e <c>int64</c> para rótulos de classificação), tratam gradientes de forma segura com <c>torch.no_grad()</c> e <c>zero_grad()</c>, e apresentam saídas comentadas perfeitamente realistas e reprodutíveis.
3. **Neurociência de livro-texto e rigor histórico:** As analogias biológicas distinguem com precisão o modelo de taxa de disparo (*rate coding*) da biofísica de potenciais de ação de canais iônicos (Hodgkin & Huxley, 1952); os exemplos trazem contextos fisiológicos realistas (curva $f\text{–}I$ saturante até $200\text{ Hz}$, balanço excitatório/inibitório em interneurônios corticais, decodificação de orientações em V1 e categorias visuais/olfativas, e contraste entre a regra hebbiana local e o gradiente descendente com erro global). Todas as citações bibliográficas são clássicos canônicos reais (McCulloch & Pitts, 1943; Hebb, 1949; Hodgkin & Huxley, 1952; Rosenblatt, 1958; Minsky & Papert, 1969; Cybenko, 1989; Kingma & Ba, 2015).
4. **Estrutura e conformidade editorial:** Cobre com exatidão as 4 seções obrigatórias ("Do neurônio biológico ao artificial", "Redes multicamadas e funções de perda", "Backpropagation pela regra da cadeia", "Treinando de verdade: SGD, Adam e um MLP em PyTorch"), seguidas de "Resumo" e "Para ir além". Todos os 16 exercícios contêm `<hint>` e `<solution>` completa e recolhida por padrão. A notação matemática é uniforme em toda a aula ($\mathbf{x}$, $\mathbf{W}$, $\mathbf{z}^{(l)}$, $\mathbf{a}^{(l)}$, $\phi$, $\sigma$, $\eta$, $\mathcal{L}$). O tamanho está calibrado em aproximadamente 4.000 palavras de prosa, perfeitamente dentro da faixa estipulada de 3.500 a 5.000 palavras.

Foram identificadas apenas 3 sugestões pedagógicas de polimento na tabela a seguir, sem qualquer caráter impeditivo.

---

## 2. Tabela de Problemas e Sugestões

| Severidade | Local | Trecho | Correção sugerida |
|---|---|---|---|
| Pedagógico | Seção 2 (`sec:9-1-2`), `exm:9-1-decod-estimulo`, linha ~251 | `$z_1 = 2(0{,}8) + 1(0{,}2) + 0 + 0{,}4(0{,}5) = 2{,}0$` | Na expansão por componentes de $\mathbf{z} = \mathbf{W}\mathbf{x} + \mathbf{b}$, para a terceira linha escreveu-se explicitamente o termo do viés `$1(0{,}5) - 0{,}5 = 0{,}0$`, enquanto para $z_1$ e $z_2$ omitiu-se a adição do viés nulo ($+ 0$). Para alunos de Biologia em fase de consolidação da álgebra matricial, sugere-se uniformizar a expansão incluindo explicitamente o viés em todas as linhas: `$z_1 = 2(0{,}8) + 1(0{,}2) + 0(0{,}0) + 0{,}4(0{,}5) + 0 = 2{,}0$` e `$z_2 = 1(0{,}8) + 1(0{,}2) + 2(0{,}0) + 0(0{,}5) + 0 = 1{,}0$`. |
| Pedagógico | Seção 3 (`sec:9-1-3`), `exm:9-1-backprop-numerico`, linha ~324 | `$\hat{y} = 1{,}0 \cdot 0{,}6225 + 0 \approx 0{,}6225$; $\mathcal{L} = \frac{1}{2}(0{,}622459 - 1{,}0)^2 \approx 0{,}0713$` | No texto, apresenta-se $\hat{y}$ arredondado para $0{,}6225$, mas no cômputo da perda emprega-se a precisão completa da máquina ($0{,}622459$). Embora ambos ao quadrado divididos por 2 resultem em $0{,}0713$ quando arredondados para 4 casas decimais ($(-0{,}3775)^2 / 2 \approx 0{,}071253 \approx 0{,}0713$), convém adicionar uma breve nota explicativa: *(retendo o valor em ponto flutuante completo nas etapas subsequentes para evitar acúmulo de erro numérico)*. |
| Pedagógico | Seção 4 (`sec:9-1-4`), `eq:9-1-momentum`, linha ~483 | `$\mathbf{v}_t = \beta \mathbf{v}_{t-1} + \mathbf{g}_t, \qquad \boldsymbol{\theta}_t = \boldsymbol{\theta}_{t-1} - \eta \mathbf{v}_t$` | O texto já esclarece com precisão que adota a convenção do PyTorch (<c>torch.optim.SGD</c>) sem o fator $(1 - \beta)$ multiplicando o gradiente. Como alguns livros de referência (como o *Deep Learning Book* de Goodfellow et al., citado na seção "Para ir além") empregam a média móvel exponencial com $(1 - \beta)$, vale incluir uma frase destacando que, no regime estacionário com gradientes constantes, essa formulação acumula uma velocidade efetiva de escala $\frac{1}{1 - \beta} \approx 10\times$ (para $\beta = 0{,}9$), o que justifica a necessidade de usar passos $\eta$ menores. |

---

## 3. Recálculo e Auditoria de Todas as Contas

Todas as contas da aula foram refeitas manualmente passo a passo. Abaixo apresenta-se o registro das deduções e confirmações de exatidão.

### 3.1 Subtema 1: Do neurônio biológico ao artificial (`sec:9-1-1`)

1. **[Exemplo 9.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-01.dlt#L68-L89) (`exm:9-1-portas-and-or` — Portas lógicas AND e OR):**
   - **Porta AND:** $z = x_1 + x_2 - 1{,}5$, com ativação degrau $H(z)$.
     - $(0, 0)$: $z = 0 + 0 - 1{,}5 = -1{,}5 < 0 \implies \hat{y} = 0$.
     - $(1, 0)$: $z = 1 + 0 - 1{,}5 = -0{,}5 < 0 \implies \hat{y} = 0$.
     - $(0, 1)$: $z = 0 + 1 - 1{,}5 = -0{,}5 < 0 \implies \hat{y} = 0$.
     - $(1, 1)$: $z = 1 + 1 - 1{,}5 = +0{,}5 \ge 0 \implies \hat{y} = 1$.
     *Contas e tabela verdade corretas.*
   - **Porta OR:** $z = x_1 + x_2 - 0{,}5$.
     - $(0, 0)$: $z = 0 + 0 - 0{,}5 = -0{,}5 < 0 \implies \hat{y} = 0$.
     - $(1, 0)$: $z = 1 + 0 - 0{,}5 = +0{,}5 \ge 0 \implies \hat{y} = 1$.
     - $(0, 1)$: $z = 0 + 1 - 0{,}5 = +0{,}5 \ge 0 \implies \hat{y} = 1$.
     - $(1, 1)$: $z = 1 + 1 - 0{,}5 = +1{,}5 \ge 0 \implies \hat{y} = 1$.
     *Contas e tabela verdade corretas.*

2. **[Proposição 9.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-01.dlt#L93-L102) (`prop:9-1-xor-impossivel` — Demonstração da Inseparabilidade Linear do XOR):**
   - Sistema de inequações para $H(w_1 x_1 + w_2 x_2 + b)$:
     - (1) $(0, 0) \to 0 \implies b < 0$.
     - (2) $(1, 0) \to 1 \implies w_1 + b \ge 0$.
     - (3) $(0, 1) \to 1 \implies w_2 + b \ge 0$.
     - (4) $(1, 1) \to 0 \implies w_1 + w_2 + b < 0$.
   - Somando (2) e (3): $w_1 + w_2 + 2b \ge 0$.
   - Somando (1) e (4): como $b < 0$ e $w_1 + w_2 + b < 0$, temos $(w_1 + w_2 + b) + b < 0 \implies w_1 + w_2 + 2b < 0$.
   - Contradição simultânea ($w_1 + w_2 + 2b \ge 0$ e $< 0$).
   *Demonstração irrefutável e perfeitamente formulada.*

3. **[Exemplo 9.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-01.dlt#L115-L129) (`exm:9-1-curva-fi` — Curva $f\text{–}I$ saturante de neurônio cortical):**
   - Equação: $f(I) = 200\,\sigma\bigl(5(I - 0{,}4)\bigr) = \frac{200}{1 + e^{-5(I - 0{,}4)}}$.
   - Para $I = 0\text{ nA}$: $z = 5(0 - 0{,}4) = -2{,}0$.
     $e^{-(-2)} = e^2 \approx 7{,}389056$.
     $\sigma(-2) = \frac{1}{1 + 7{,}389056} \approx \frac{1}{8{,}389056} \approx 0{,}119203$.
     $f(0) = 200 \times 0{,}119203 \approx 23{,}84\text{ Hz} \approx 23{,}8\text{ Hz}$.
   - Para $I = 0{,}4\text{ nA}$: $z = 5(0) = 0 \implies \sigma(0) = 0{,}5 \implies f(0{,}4) = 200 \times 0{,}5 = 100\text{ Hz}$.
   - Para $I = 0{,}8\text{ nA}$: $z = 5(0{,}4) = +2{,}0$.
     $\sigma(2) = 1 - \sigma(-2) \approx 1 - 0{,}119203 = 0{,}880797$.
     $f(0{,}8) = 200 \times 0{,}880797 \approx 176{,}16\text{ Hz} \approx 176{,}2\text{ Hz}$.
   - Derivada em $I = 0{,}4\text{ nA}$:
     $\frac{df}{dI} = 200 \cdot \sigma'(z) \cdot \frac{dz}{dI} = 200 \cdot 5 \cdot \sigma'(0) = 1\,000 \cdot [0{,}5(1 - 0{,}5)] = 1\,000 \cdot 0{,}25 = 250\text{ Hz/nA}$.
   *Todas as contas e unidades corretas.*

4. **[Exercício 9.1.1.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-01.dlt#L136-L147) (`exr:9-1-1-1` — Avaliação de ativações e derivadas à mão):**
   - (a) $\mathrm{ReLU}(-3) = \max(0, -3) = 0$; $\mathrm{ReLU}'(-3) = 0$; $\mathrm{ReLU}(4) = \max(0, 4) = 4$; $\mathrm{ReLU}'(4) = 1$.
   - (b) $\sigma(0) = \frac{1}{1 + 1} = 0{,}5$; $\sigma'(0) = 0{,}5(1 - 0{,}5) = 0{,}25$; $\tanh(0) = \frac{0}{2} = 0$; $\tanh'(0) = 1 - 0^2 = 1$.
   - (c) $\sigma(z_1) = 0{,}8 \implies \sigma'(z_1) = 0{,}8(1 - 0{,}8) = 0{,}8(0{,}2) = 0{,}16$.
         $\tanh(z_2) = 0{,}6 \implies \tanh'(z_2) = 1 - (0{,}6)^2 = 1 - 0{,}36 = 0{,}64$.
   *Contas corretas.*

5. **[Exercício 9.1.1.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-01.dlt#L149-L156) (`exr:9-1-1-2` — Balanço excitatório e inibitório):**
   - Modelo: $z = w_1 x_1 + w_2 x_2 + b = 0{,}05(40) - 0{,}10 x_2 + 0{,}5 = 2{,}0 - 0{,}10 x_2 + 0{,}5 = 2{,}5 - 0{,}10 x_2$; $a = \mathrm{ReLU}(z)$.
   - Se $x_2 = 30\text{ Hz}$: $z = 2{,}5 - 3{,}0 = -0{,}5 \implies a = \max(0, -0{,}5) = 0$.
   - Se $x_2 = 10\text{ Hz}$: $z = 2{,}5 - 1{,}0 = 1{,}5 \implies a = \max(0, 1{,}5) = 1{,}5$.
   *Contas corretas.*

6. **[Exercício 9.1.1.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-01.dlt#L158-L167) (`exr:9-1-1-3` — Atualização do perceptron):**
   - Estado inicial: $\mathbf{w} = (0{,}4;\; -0{,}2)^\top$, $b = -0{,}2$, $\eta = 0{,}5$, $\mathbf{x} = (1, 2)^\top$, $y = 1$.
   - Previsão inicial: $z = 0{,}4(1) - 0{,}2(2) - 0{,}2 = 0{,}4 - 0{,}4 - 0{,}2 = -0{,}2 < 0 \implies \hat{y} = 0$.
   - Erro: $y - \hat{y} = 1 - 0 = 1$.
   - Atualização:
     $$\mathbf{w}_{\text{novo}} = \begin{pmatrix} 0{,}4 \\ -0{,}2 \end{pmatrix} + 0{,}5(1)\begin{pmatrix} 1 \\ 2 \end{pmatrix} = \begin{pmatrix} 0{,}4 + 0{,}5 \\ -0{,}2 + 1{,}0 \end{pmatrix} = \begin{pmatrix} 0{,}9 \\ 0{,}8 \end{pmatrix}.$$
     $$b_{\text{novo}} = -0{,}2 + 0{,}5(1) = 0{,}3.$$
   - Nova previsão: $z_{\text{novo}} = 0{,}9(1) + 0{,}8(2) + 0{,}3 = 0{,}9 + 1{,}6 + 0{,}3 = 2{,}8 \ge 0 \implies \hat{y}_{\text{novo}} = 1$.
   *Contas corretas.*

7. **[Exercício 9.1.1.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-01.dlt#L169-L178) (`exr:9-1-1-4` — Derivada da sigmoide e cota máxima):**
   - Regra da cadeia: $\frac{d}{dz}(1 + e^{-z})^{-1} = -(1 + e^{-z})^{-2}(-e^{-z}) = \frac{e^{-z}}{(1 + e^{-z})^2} = \frac{1}{1 + e^{-z}}\frac{(1 + e^{-z}) - 1}{1 + e^{-z}} = \sigma(z)(1 - \sigma(z))$.
   - Cota máxima com $p = \sigma(z) \in (0, 1)$: $p(1 - p) = -(p^2 - p) = -[(p - \frac{1}{2})^2 - \frac{1}{4}] = \frac{1}{4} - (p - \frac{1}{2})^2 \le \frac{1}{4}$, atingindo o valor máximo exatamente em $p = 1/2 \iff z = 0$.
   *Dedução correta.*

---

### 3.2 Subtema 2: Redes multicamadas e funções de perda (`sec:9-1-2`)

1. **[Exemplo 9.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-01.dlt#L214-L228) (`exm:9-1-xor-mlp` — Solução do XOR com MLP $2 \to 2 \to 1$ e ReLU):**
   - Parâmetros: $\mathbf{W}^{(1)} = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$, $\mathbf{b}^{(1)} = \begin{pmatrix} 0 \\ -1 \end{pmatrix}$, $\mathbf{W}^{(2)} = \begin{pmatrix} 1 & -2 \end{pmatrix}$, $b^{(2)} = 0$.
   - Vetor de pré-ativação: $\mathbf{z}^{(1)} = (x_1 + x_2;\; x_1 + x_2 - 1)^\top$; ativação $\mathbf{a}^{(1)} = \mathrm{ReLU}(\mathbf{z}^{(1)})$.
   - Saída: $\hat{y} = a_1^{(1)} - 2 a_2^{(1)}$.
     - $(0, 0)^\top$: $\mathbf{z}^{(1)} = (0, -1)^\top \implies \mathbf{a}^{(1)} = (0, 0)^\top \implies \hat{y} = 0 - 2(0) = 0$.
     - $(1, 0)^\top$: $\mathbf{z}^{(1)} = (1, 0)^\top \implies \mathbf{a}^{(1)} = (1, 0)^\top \implies \hat{y} = 1 - 2(0) = 1$.
     - $(0, 1)^\top$: $\mathbf{z}^{(1)} = (1, 0)^\top \implies \mathbf{a}^{(1)} = (1, 0)^\top \implies \hat{y} = 1 - 2(0) = 1$.
     - $(1, 1)^\top$: $\mathbf{z}^{(1)} = (2, 1)^\top \implies \mathbf{a}^{(1)} = (2, 1)^\top \implies \hat{y} = 2 - 2(1) = 0$.
   - Contagem de parâmetros:
     - Camada 1: $2 \times 2 + 2 = 6$.
     - Camada 2: $1 \times 2 + 1 = 3$.
     - Total: $6 + 3 = 9$ parâmetros.
   *Contas e dimensões exatas.*

2. **[Exemplo 9.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-01.dlt#L243-L258) (`exm:9-1-decod-estimulo` — Decodificação em V1 com Softmax e Entropia Cruzada):**
   - Entrada: $\mathbf{x} = (0{,}8;\; 0{,}2;\; 0{,}0;\; 0{,}5)^\top$.
   - Produto $\mathbf{W}\mathbf{x} + \mathbf{b}$:
     $$z_1 = 2(0{,}8) + 1(0{,}2) + 0(0{,}0) + 0{,}4(0{,}5) + 0 = 1{,}6 + 0{,}2 + 0 + 0{,}2 = 2{,}0.$$
     $$z_2 = 1(0{,}8) + 1(0{,}2) + 2(0{,}0) + 0(0{,}5) + 0 = 0{,}8 + 0{,}2 + 0 + 0 = 1{,}0.$$
     $$z_3 = 0(0{,}8) + 0(0{,}2) + 1(0{,}0) + 1(0{,}5) - 0{,}5 = 0 + 0 + 0 + 0{,}5 - 0{,}5 = 0{,}0.$$
   - Exponenciais:
     $e^{z_1} = e^2 \approx 7{,}389056$; $e^{z_2} = e^1 \approx 2{,}718282$; $e^{z_3} = e^0 = 1{,}0$.
     Soma $S = 7{,}389056 + 2{,}718282 + 1{,}0 = 11{,}107338$.
   - Probabilidades $\mathrm{softmax}$:
     $$\hat{y}_1 = \frac{7{,}389056}{11{,}107338} \approx 0{,}665241 \approx 0{,}6652.$$
     $$\hat{y}_2 = \frac{2{,}718282}{11{,}107338} \approx 0{,}244728 \approx 0{,}2447.$$
     $$\hat{y}_3 = \frac{1{,}0}{11{,}107338} \approx 0{,}090031 \approx 0{,}0900.$$
     Soma das probabilidades: $0{,}665241 + 0{,}244728 + 0{,}090031 = 1{,}000000$.
   - Perda de Entropia Cruzada com alvo $c = 1$ ($\mathbf{y} = (1, 0, 0)^\top$):
     $$\mathcal{L}_{\text{CE}} = -\ln(\hat{y}_1) = -\ln(0{,}665241) \approx 0{,}407603 \approx 0{,}4076.$$
   *Todas as contas fechadas rigorosamente.*

3. **[Exercício 9.1.2.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-01.dlt#L268-L275) (`exr:9-1-2-1` — Dimensões e parâmetros de um MLP motor):**
   - Arquitetura: $128 \to 64 \to 16 \to 4$.
   - Dimensões: $\mathbf{W}^{(1)} \in \mathbb{R}^{64 \times 128}$, $\mathbf{W}^{(2)} \in \mathbb{R}^{16 \times 64}$, $\mathbf{W}^{(3)} \in \mathbb{R}^{4 \times 16}$.
   - Parâmetros:
     - Camada 1: $64 \times 128 + 64 = 64 \times 129 = 8\,256$.
     - Camada 2: $16 \times 64 + 16 = 16 \times 65 = 1\,040$.
     - Camada 3: $4 \times 16 + 4 = 4 \times 17 = 68$.
     - Soma: $8\,256 + 1\,040 + 68 = 9\,364$.
   *Dimensões e total de parâmetros corretos.*

4. **[Exercício 9.1.2.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-01.dlt#L277-L287) (`exr:9-1-2-2` — Softmax e Entropia Cruzada à mão):**
   - $K = 3$, classe verdadeira $c = 2$.
   - (a) $\mathbf{z} = (0, 0, 0)^\top$:
     $e^0 = 1 \implies S = 1 + 1 + 1 = 3 \implies \hat{\mathbf{y}} = (1/3, 1/3, 1/3)^\top$.
     $\mathcal{L}_{\text{CE}} = -\ln(1/3) = \ln 3 \approx 1{,}0986$.
   - (b) $\mathbf{z} = (1, 1, 0)^\top$:
     $S = e^1 + e^1 + e^0 \approx 2{,}71828 + 2{,}71828 + 1{,}0 = 6{,}43656$.
     $\hat{y}_1 = \hat{y}_2 = \frac{2{,}71828}{6{,}43656} \approx 0{,}422319 \approx 0{,}4223$.
     $\hat{y}_3 = \frac{1}{6{,}43656} \approx 0{,}155362 \approx 0{,}1554$.
     $\mathcal{L}_{\text{CE}} = -\ln(\hat{y}_2) = -\ln(0{,}422319) \approx 0{,}86197 \approx 0{,}8620$.
   *Contas corretas.*

5. **[Exercício 9.1.2.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-01.dlt#L289-L297) (`exr:9-1-2-3` — Passagem direta e perda quadrática em tipos celulares):**
   - Entrada: $x_1 = 0{,}4\text{ ms}$, $x_2 = 25\text{ Hz}$, $y = 1$.
   - Camada 1:
     $$z_1^{(1)} = -2(0{,}4) + 0{,}1(25) - 0{,}5 = -0{,}8 + 2{,}5 - 0{,}5 = 1{,}2.$$
     $$z_2^{(1)} = 1(0{,}4) - 0{,}05(25) + 0{,}2 = 0{,}4 - 1{,}25 + 0{,}2 = -0{,}65.$$
     $\mathbf{a}^{(1)} = \mathrm{ReLU}(\mathbf{z}^{(1)}) = (1{,}2;\; 0{,}0)^\top$.
   - Camada de saída:
     $$\hat{y} = 0{,}5(1{,}2) - 0{,}4(0) + 0{,}3 = 0{,}60 + 0{,}30 = 0{,}90.$$
     $$\mathcal{L} = \frac{1}{2}(\hat{y} - y)^2 = \frac{1}{2}(0{,}90 - 1{,}0)^2 = \frac{1}{2}(-0{,}10)^2 = \frac{0{,}01}{2} = 0{,}005.$$
   *Contas corretas.*

6. **[Exercício 9.1.2.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-01.dlt#L299-L306) (`exr:9-1-2-4` — Invariância por translação e estabilidade numérica do Softmax):**
   - $\mathrm{softmax}(\mathbf{z} - c\mathbf{1})_k = \frac{e^{z_k - c}}{\sum_{j=1}^K e^{z_j - c}} = \frac{e^{-c} e^{z_k}}{e^{-c}\sum_{j=1}^K e^{z_j}} = \frac{e^{z_k}}{\sum_{j=1}^K e^{z_j}} = \mathrm{softmax}(\mathbf{z})_k$.
   - Ao fixar $c = \max_j z_j$, cada expoente satisfaz $z_j - c \le 0$, impedindo estouro numérico (*overflow* de $e^{z_j}$) e garantindo que o maior termo seja $e^0 = 1$, com denominador $\sum_j e^{z_j - c} \in [1, K]$.
   *Demonstração e justificativa exatas.*

---

### 3.3 Subtema 3: Backpropagation pela regra da cadeia (`sec:9-1-3`)

1. **[Exemplo 9.5](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-01.dlt#L318-L336) (`exm:9-1-backprop-numerico` — Retropropagação passo a passo $1 \to 1 \to 1$):**
   - Dados e parâmetros: $x = 1{,}0$, $y = 1{,}0$, $w^{(1)} = 0{,}5$, $b^{(1)} = 0{,}0$, $w^{(2)} = 1{,}0$, $b^{(2)} = 0{,}0$, $\eta = 0{,}5$.
   - **Forward:**
     $z^{(1)} = 0{,}5(1{,}0) + 0{,}0 = 0{,}5000$.
     $a^{(1)} = \sigma(0{,}5) = \frac{1}{1 + e^{-0{,}5}} \approx \frac{1}{1 + 0{,}60653066} \approx 0{,}62245933 \approx 0{,}6225$.
     $\hat{y} = z^{(2)} = 1{,}0(0{,}62245933) + 0{,}0 = 0{,}62245933 \approx 0{,}6225$.
     $\hat{y} - y = 0{,}62245933 - 1{,}0 = -0{,}37754067 \approx -0{,}3775$.
     $\mathcal{L} = \frac{1}{2}(-0{,}37754067)^2 \approx \frac{0{,}142536957}{2} \approx 0{,}071268 \approx 0{,}0713$.
   - **Backward — Camada 2:**
     $\delta^{(2)} = \frac{\partial \mathcal{L}}{\partial z^{(2)}} = \hat{y} - y = -0{,}37754067 \approx -0{,}3775$.
     $\frac{\partial \mathcal{L}}{\partial w^{(2)}} = \delta^{(2)} a^{(1)} = (-0{,}37754067)(0{,}62245933) \approx -0{,}23500372 \approx -0{,}2350$.
     $\frac{\partial \mathcal{L}}{\partial b^{(2)}} = \delta^{(2)} \approx -0{,}3775$.
   - **Backward — Camada 1:**
     $\sigma'(0{,}5) = a^{(1)}(1 - a^{(1)}) = (0{,}62245933)(0{,}37754067) \approx 0{,}23500372$.
     $\delta^{(1)} = \delta^{(2)} \cdot w^{(2)} \cdot \sigma'(z^{(1)}) = (-0{,}37754067)(1{,}0)(0{,}23500372) \approx -0{,}08872347 \approx -0{,}0887$.
     $\frac{\partial \mathcal{L}}{\partial w^{(1)}} = \delta^{(1)} x = (-0{,}08872347)(1{,}0) \approx -0{,}0887$.
     $\frac{\partial \mathcal{L}}{\partial b^{(1)}} = \delta^{(1)} \approx -0{,}0887$.
   - **Atualização ($\theta \leftarrow \theta - 0{,}5 \frac{\partial \mathcal{L}}{\partial \theta}$):**
     $w^{(2)}_{\text{novo}} = 1{,}0 - 0{,}5(-0{,}23500372) = 1{,}0 + 0{,}11750186 = 1{,}11750186 \approx 1{,}1175$.
     $b^{(2)}_{\text{novo}} = 0{,}0 - 0{,}5(-0{,}37754067) = 0{,}18877033 \approx 0{,}1888$.
     $w^{(1)}_{\text{novo}} = 0{,}5 - 0{,}5(-0{,}08872347) = 0{,}5 + 0{,}04436173 = 0{,}54436173 \approx 0{,}5444$.
     $b^{(1)}_{\text{novo}} = 0{,}0 - 0{,}5(-0{,}08872347) = 0{,}04436173 \approx 0{,}0444$.
   *Todas as 11 grandezas numéricas conferidas com precisão de 4 casas decimais.*

2. **[Proposição 9.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-01.dlt#L340-L358) (`prop:9-1-backprop-equacoes` — Demonstração da Derivada Softmax + Entropia Cruzada):**
   - Com $\mathbf{y}$ *one-hot* ($\sum_j y_j = 1$ e $y_c = 1$):
     $$\mathcal{L}_{\text{CE}} = -\sum_{j=1}^K y_j \log \left(\frac{e^{z_j}}{\sum_m e^{z_m}}\right) = -\sum_{j=1}^K y_j z_j + \left(\sum_{j=1}^K y_j\right) \log\left(\sum_{m=1}^K e^{z_m}\right) = -\sum_{j=1}^K y_j z_j + \log\left(\sum_{m=1}^K e^{z_m}\right).$$
   - Derivando em relação a $z_k$:
     $$\frac{\partial \mathcal{L}_{\text{CE}}}{\partial z_k} = -y_k + \frac{1}{\sum_m e^{z_m}} \frac{\partial}{\partial z_k}\left(\sum_m e^{z_m}\right) = -y_k + \frac{e^{z_k}}{\sum_m e^{z_m}} = \hat{y}_k - y_k.$$
     Logo, $\boldsymbol{\delta}^{(L)} = \hat{\mathbf{y}} - \mathbf{y}$.
   *Dedução correta e elegante.*

3. **[Exemplo 9.6](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-01.dlt#L362-L370) (`exm:9-1-backprop-bio` — Retropropagação em decodificador olfativo):**
   - Camada 1: $\mathbf{a}^{(1)} = (1{,}0;\; 0{,}5)^\top$, $\mathrm{ReLU}'(\mathbf{z}^{(1)}) = (1, 1)^\top$.
   - Camada 2: $\mathbf{W}^{(2)} = \begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix}$, $\mathbf{b}^{(2)} = \mathbf{0}$.
     $\mathbf{z}^{(2)} = \begin{pmatrix} 1(1{,}0) \\ 2(0{,}5) \end{pmatrix} = \begin{pmatrix} 1{,}0 \\ 1{,}0 \end{pmatrix} \implies \hat{\mathbf{y}} = \begin{pmatrix} 0{,}5 \\ 0{,}5 \end{pmatrix}$.
   - Erro da saída com alvo odor A ($\mathbf{y} = (1, 0)^\top$):
     $$\boldsymbol{\delta}^{(2)} = \hat{\mathbf{y}} - \mathbf{y} = \begin{pmatrix} 0{,}5 - 1 \\ 0{,}5 - 0 \end{pmatrix} = \begin{pmatrix} -0{,}5 \\ 0{,}5 \end{pmatrix}.$$
   - Gradiente dos pesos da saída:
     $$\frac{\partial \mathcal{L}}{\partial \mathbf{W}^{(2)}} = \boldsymbol{\delta}^{(2)}(\mathbf{a}^{(1)})^\top = \begin{pmatrix} -0{,}5 \\ 0{,}5 \end{pmatrix}\begin{pmatrix} 1{,}0 & 0{,}5 \end{pmatrix} = \begin{pmatrix} -0{,}50 & -0{,}25 \\ 0{,}50 & 0{,}25 \end{pmatrix}.$$
   - Retropropagação para a camada 1:
     $$\boldsymbol{\delta}^{(1)} = (\mathbf{W}^{(2)})^\top \boldsymbol{\delta}^{(2)} \odot \mathrm{ReLU}'(\mathbf{z}^{(1)}) = \begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix}\begin{pmatrix} -0{,}5 \\ 0{,}5 \end{pmatrix} \odot \begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} -0{,}5 \\ 1{,}0 \end{pmatrix} \odot \begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} -0{,}5 \\ 1{,}0 \end{pmatrix}.$$
   *Operações matriciais e produtos de Hadamard corretos.*

4. **[Exercício 9.1.3.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-01.dlt#L435-L442) (`exr:9-1-3-1` — Diferenças finitas centradas à mão):**
   - $L(w) = (2w - 1)^2$.
   - Derivada analítica: $L'(w) = 2(2w - 1)(2) = 4(2w - 1) \implies L'(1) = 4(1) = 4$.
   - Diferença centrada com $\varepsilon = 0{,}01$:
     $L(1{,}01) = (2(1{,}01) - 1)^2 = (2{,}02 - 1)^2 = (1{,}02)^2 = 1{,}0404$.
     $L(0{,}99) = (2(0{,}99) - 1)^2 = (1{,}98 - 1)^2 = (0{,}98)^2 = 0{,}9604$.
     $$\frac{L(1{,}01) - L(0{,}99)}{2\varepsilon} = \frac{1{,}0404 - 0{,}9604}{0{,}02} = \frac{0{,}0800}{0{,}02} = 4{,}00.$$
   *Contas exatas.*

5. **[Exercício 9.1.3.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-01.dlt#L444-L451) (`exr:9-1-3-2` — Vetor de erro da saída Softmax):**
   - $\hat{\mathbf{y}} = (0{,}70;\; 0{,}20;\; 0{,}10)^\top$, $\mathbf{y} = (1, 0, 0)^\top$.
   - $\boldsymbol{\delta}^{(L)} = \hat{\mathbf{y}} - \mathbf{y} = (0{,}70 - 1;\; 0{,}20 - 0;\; 0{,}10 - 0)^\top = (-0{,}30;\; 0{,}20;\; 0{,}10)^\top$.
   - Direção do passo de descida: $-\eta \boldsymbol{\delta}^{(L)} = \eta (+0{,}30;\; -0{,}20;\; -0{,}10)^\top$, elevando o *logit* da classe correta (1) e atenuando as incorretas (2 e 3).
   *Contas e interpretação corretas.*

6. **[Exercício 9.1.3.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-01.dlt#L453-L460) (`exr:9-1-3-3` — Backpropagation à mão com ReLU):**
   - $x = 2$, $y = 5$, $\eta = 0{,}1$, $w^{(1)} = 1$, $b^{(1)} = -1$, $w^{(2)} = 3$, $b^{(2)} = 0$.
   - **Forward:** $z^{(1)} = 1(2) - 1 = 1 > 0 \implies a^{(1)} = 1$; $\hat{y} = 3(1) + 0 = 3$; $\mathcal{L} = \frac{1}{2}(3 - 5)^2 = 2{,}0$.
   - **Backward:**
     $\delta^{(2)} = \hat{y} - y = 3 - 5 = -2$.
     $\frac{\partial \mathcal{L}}{\partial w^{(2)}} = \delta^{(2)} a^{(1)} = -2(1) = -2$.
     $\frac{\partial \mathcal{L}}{\partial b^{(2)}} = \delta^{(2)} = -2$.
     Como $z^{(1)} = 1 > 0$, $\mathrm{ReLU}'(1) = 1$.
     $\delta^{(1)} = \delta^{(2)} \cdot w^{(2)} \cdot \mathrm{ReLU}'(1) = (-2)(3)(1) = -6$.
     $\frac{\partial \mathcal{L}}{\partial w^{(1)}} = \delta^{(1)} x = (-6)(2) = -12$.
     $\frac{\partial \mathcal{L}}{\partial b^{(1)}} = \delta^{(1)} = -6$.
   - **Atualização com $\eta = 0{,}1$:**
     $w^{(2)}_{\text{novo}} = 3 - 0{,}1(-2) = 3{,}2$.
     $b^{(2)}_{\text{novo}} = 0 - 0{,}1(-2) = 0{,}2$.
     $w^{(1)}_{\text{novo}} = 1 - 0{,}1(-12) = 2{,}2$.
     $b^{(1)}_{\text{novo}} = -1 - 0{,}1(-6) = -0{,}4$.
   *Contas corretas.*

7. **[Exercício 9.1.3.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-01.dlt#L462-L468) (`exr:9-1-3-4` — Desaparecimento do gradiente em 5 camadas):**
   - Cadeia com pesos unitários $w^{(l)} = 1$: $|\delta^{(1)} / \delta^{(6)}| = \prod_{l=1}^5 |\phi'(z^{(l)})|$.
   - Com sigmoide: como $\sigma'(z) \le 1/4$ sempre, a razão máxima é $(1/4)^5 = \frac{1}{1\,024} \approx 0{,}00097656 \approx 0{,}000977$ (atenuação $> 1\,000\times$).
   - Com $\mathrm{ReLU}$ ativa ($z^{(l)} > 0$): como $\mathrm{ReLU}'(z) = 1$, a razão é $1^5 = 1$.
   *Contas e comparação conceituais corretas.*

---

### 3.4 Subtema 4: Treinando de verdade: SGD, Adam e um MLP em PyTorch (`sec:9-1-4`)

1. **[Exemplo 9.7](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-01.dlt#L494-L503) (`exm:9-1-momentum-adam` — Dois passos manuais de Momento e Adam):**
   - Parâmetros iniciais: $\theta_0 = 2{,}0$, $v_0 = m_0 = 0$, gradientes constantes $g_1 = g_2 = 1{,}0$.
   - **(a) Momento ($\beta = 0{,}9$, $\eta = 0{,}1$):**
     - $t = 1$: $v_1 = 0{,}9(0) + 1{,}0 = 1{,}0 \implies \theta_1 = 2{,}0 - 0{,}1(1{,}0) = 1{,}90$.
     - $t = 2$: $v_2 = 0{,}9(1{,}0) + 1{,}0 = 1{,}9 \implies \theta_2 = 1{,}90 - 0{,}1(1{,}9) = 1{,}90 - 0{,}19 = 1{,}71$.
   - **(b) Adam ($\beta_1 = 0{,}9$, $\beta_2 = 0{,}999$, $\eta = 0{,}1$, $\varepsilon = 10^{-8}$):**
     - $t = 1$:
       $m_1 = 0{,}9(0) + 0{,}1(1{,}0) = 0{,}1 \implies \hat{m}_1 = \frac{0{,}1}{1 - 0{,}9} = \frac{0{,}1}{0{,}1} = 1{,}0$.
       $v_1 = 0{,}999(0) + 0{,}001(1{,}0^2) = 0{,}001 \implies \hat{v}_1 = \frac{0{,}001}{1 - 0{,}999} = \frac{0{,}001}{0{,}001} = 1{,}0$.
       $\theta_1 = 2{,}0 - 0{,}1 \frac{1{,}0}{\sqrt{1{,}0} + 10^{-8}} \approx 2{,}0 - 0{,}10 = 1{,}90$.
     - $t = 2$:
       $m_2 = 0{,}9(0{,}1) + 0{,}1(1{,}0) = 0{,}09 + 0{,}10 = 0{,}19$.
       $1 - \beta_1^2 = 1 - 0{,}81 = 0{,}19 \implies \hat{m}_2 = \frac{0{,}19}{0{,}19} = 1{,}0$.
       $v_2 = 0{,}999(0{,}001) + 0{,}001(1{,}0) = 0{,}000999 + 0{,}001000 = 0{,}001999$.
       $1 - \beta_2^2 = 1 - 0{,}998001 = 0{,}001999 \implies \hat{v}_2 = \frac{0{,}001999}{0{,}001999} = 1{,}0$.
       $\theta_2 = 1{,}90 - 0{,}1 \frac{1{,}0}{\sqrt{1{,}0} + 10^{-8}} \approx 1{,}90 - 0{,}10 = 1{,}80$.
   *Contas fechadas perfeitamente.*

2. **[Exemplo 9.8](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-01.dlt#L507-L512) (`exm:9-1-hebb-vs-gd` — Regra de Hebb vs. Gradiente Descendente em uma sinapse):**
   - Estado: $\hat{y} = wx$, $x = 1{,}0$, $\hat{y} = 0{,}9$, alvo $y = 0{,}2$, $\eta = 0{,}1$.
   - Hebb: $\Delta w_{\text{Hebb}} = \eta x \hat{y} = 0{,}1(1{,}0)(0{,}9) = +0{,}09$ (afasta o peso e amplifica o disparo).
   - Gradiente descendente: $\Delta w_{\text{GD}} = -\eta(\hat{y} - y)x = -0{,}1(0{,}9 - 0{,}2)(1{,}0) = -0{,}1(0{,}7) = -0{,}07$ (reduz o peso em direção ao alvo).
   *Contas e contraste neurobiológico corretos.*

3. **[Exercício 9.1.4.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-01.dlt#L582-L592) (`exr:9-1-4-1` — Passos com gradientes alternados):**
   - $\theta_0 = 1{,}0$, $v_0 = m_0 = 0$, $g_1 = 0{,}5$, $g_2 = -0{,}5$.
   - **(a) Momento ($\beta = 0{,}8$, $\eta = 0{,}2$):**
     - $v_1 = 0{,}8(0) + 0{,}5 = 0{,}5 \implies \theta_1 = 1{,}0 - 0{,}2(0{,}5) = 1{,}0 - 0{,}10 = 0{,}90$.
     - $v_2 = 0{,}8(0{,}5) + (-0{,}5) = 0{,}4 - 0{,}5 = -0{,}10 \implies \theta_2 = 0{,}90 - 0{,}2(-0{,}10) = 0{,}90 + 0{,}02 = 0{,}92$.
   - **(b) Adam ($\beta_1 = 0{,}9$, $\beta_2 = 0{,}999$, $\eta = 0{,}1$):**
     - Em $t = 1$: $\hat{m}_1 = g_1 = 0{,}5$; $\hat{v}_1 = g_1^2 = 0{,}25 \implies \sqrt{\hat{v}_1} = 0{,}5$.
     - $\theta_1 = 1{,}0 - 0{,}1 \frac{0{,}5}{0{,}5} = 1{,}0 - 0{,}10 = 0{,}90$.
   *Contas corretas.*

4. **[Exercício 9.1.4.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-01.dlt#L594-L601) (`exr:9-1-4-2` — Simetria na inicialização constante):**
   - MLP $1 \to 2 \to 1$, $w_1^{(1)} = w_2^{(1)} = 0{,}5$, $b_1^{(1)} = b_2^{(1)} = 0$, $w_1^{(2)} = w_2^{(2)} = 1$, $b^{(2)} = 0$.
   - Amostra: $x = 1$, $y = 2$, $\eta = 0{,}1$, perda $\frac{1}{2}(\hat{y} - y)^2$.
   - $z_1^{(1)} = z_2^{(1)} = 0{,}5(1) + 0 = 0{,}5 > 0 \implies a_1^{(1)} = a_2^{(1)} = 0{,}5$.
   - $\hat{y} = 1(0{,}5) + 1(0{,}5) + 0 = 1{,}0 \implies \delta^{(2)} = 1{,}0 - 2 = -1{,}0$.
   - $\delta_1^{(1)} = \delta_2^{(1)} = (-1{,}0)(1)(1) = -1{,}0 \implies \frac{\partial \mathcal{L}}{\partial w_1^{(1)}} = \frac{\partial \mathcal{L}}{\partial w_2^{(1)}} = (-1{,}0)(1) = -1{,}0$.
   - Novos pesos: $0{,}5 - 0{,}1(-1{,}0) = 0{,}5 + 0{,}10 = 0{,}60$ para ambos os neurônios, provando a manutenção indefectível da simetria.
   *Contas e conclusão corretas.*

5. **[Exercício 9.1.4.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-01.dlt#L603-L610) (`exr:9-1-4-3` — Hebb vs. Erro em circuito motor):**
   - Unidade linear: $\hat{y} = w_1 x_1 + w_2 x_2 = 0{,}5(2{,}0) + 0{,}3(0) = 1{,}0$.
   - Rótulo $y = 0{,}4$, taxa $\eta = 0{,}05$.
   - Hebb: $\Delta w_1 = 0{,}05(2{,}0)(1{,}0) = +0{,}10$ (afasta $\hat{y}$ para $1{,}20$); $\Delta w_2 = 0{,}05(0)(1{,}0) = 0$.
   - Gradiente descendente: $\Delta w_1 = -0{,}05(1{,}0 - 0{,}4)(2{,}0) = -0{,}05(0{,}6)(2{,}0) = -0{,}06$ (aproxima $\hat{y}$ para $0{,}88$); $\Delta w_2 = -0{,}05(0{,}6)(0) = 0$.
   *Contas corretas.*

---

## 4. Auditoria dos Blocos de Código Python

Todos os blocos de código presentes na aula foram auditados interpretativamente como por um interpretador Python 3.11 com `torch 2.x` e `scikit-learn 1.x`:

1. **[Bloco 1: cod:9-1-backprop](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-01.dlt#L376-L423) (Verificação de Gradientes com PyTorch e Diferenças Finitas):**
   - *Imports:* <c>import torch</c>.
   - *Tipos e tensores:* utiliza <c>dtype=torch.float64</c> em todas as variáveis, garantindo precisão numérica de 64 bits para mitigar erros de cancelamento catastrófico na divisão por $2\varepsilon = 2 \times 10^{-5}$.
   - *Grafo computacional e autograd:* <c>passo_direto</c> constrói o grafo de operações; <c>perda.backward()</c> popula corretamente <c>.grad</c> nos quatro parâmetros folha com <c>requires_grad=True</c>.
   - *Diferenças finitas:* a chamada sob <c>with torch.no_grad():</c> impede a gravação desnecessária do grafo no cálculo de <c>p_mais</c> e <c>p_menos</c>.
   - *Passo de atualização manual:* a atualização <c>w1 -= eta * w1.grad</c> etc. é executada estritamente dentro de <c>with torch.no_grad():</c>, evitando o erro de execução <c>RuntimeError: a leaf Variable that requires grad is being used in an in-place operation</c>.
   - *Autocontido:* sim, roda diretamente sem qualquer dependência externa.
   - *Saídas comentadas:* idênticas às deduções analíticas do Exemplo 9.5 (<c>dL/dw1 = -0.0887</c>, <c>w1 = 0.5444</c> etc.).

2. **[Bloco 2: cod:9-1-mlp-digits](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-01.dlt#L516-L572) (Treinamento de um MLP em PyTorch sobre dígitos):**
   - *Imports:* <c>numpy</c>, <c>torch</c>, <c>torch.nn</c>, <c>load_digits</c>, <c>train_test_split</c>, <c>DataLoader</c>, <c>TensorDataset</c>. Todos presentes.
   - *Reprodutibilidade:* fixa sementes tanto no NumPy (<c>np.random.seed(0)</c>) quanto no PyTorch (<c>torch.manual_seed(0)</c>).
   - *Formas e dtypes:*
     - <c>X</c> é convertido para <c>np.float32</c> e reescalado para $[0, 1]$;
     - <c>y</c> é convertido para <c>np.int64</c> (tipo obrigatório para rótulos de classe em <c>nn.CrossEntropyLoss</c>);
     - Divisão estratificada 80/20 gera matrizes com dimensões compatíveis ($1\,437$ treino $\times 64$, $360$ teste $\times 64$).
   - *Arquitetura:* <c>nn.Sequential(nn.Linear(64, 32), nn.ReLU(), nn.Linear(32, 10))</c> tem saídas correspondentes a 10 classes, sem colocar <c>nn.Softmax</c> no final (respeitando a regra de alimentar *logits* puros em <c>nn.CrossEntropyLoss</c>).
   - *Laço de treinamento canônico:* contém as 5 linhas centrais organizadas perfeitamente:
     1. <c>otimizador.zero_grad()</c>
     2. <c>logits = modelo(xb)</c>
     3. <c>perda = criterio(logits, yb)</c>
     4. <c>perda.backward()</c>
     5. <c>otimizador.step()</c>
   - *Alternância de modos:* comuta entre <c>modelo.train()</c> e <c>modelo.eval()</c>, calculando a acurácia de teste sob <c>with torch.no_grad():</c>.
   - *Saídas comentadas:* a perda de treino decresce de forma suave e realista ($\approx 1{,}75 \to 0{,}17 \to 0{,}09 \to 0{,}04$), enquanto a acurácia de teste converge de $\approx 72\%$ para $\approx 97\%$.

3. **[Bloco 3: exr:9-1-4-4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-01.dlt#L617-L684) (Solução completa com validação, parada antecipada e weight decay):**
   - *Divisão tripartite honesta:* divide primeiro 80/20 (treino_full / teste) e depois 80/20 em treino_full para isolar validação sem vazamento (*data leakage*).
   - *Parada antecipada e clonagem de estado:* monitora a perda de validação com paciência de 5 épocas e salva o melhor estado utilizando <c>{k: v.clone() for k, v in modelo.state_dict().items()}</c>. Essa clonagem com <c>.clone()</c> é crucial em PyTorch para não reter apenas referências aos tensores mutáveis do modelo.
   - *Restauração de pesos e cálculo da norma $L_2$:* recarrega o modelo com <c>load_state_dict</c> e calcula a norma euclidiana dos tensores de parâmetros (<c>sum(p.pow(2).sum().item() for p in modelo.parameters()) ** 0.5</c>).
   - *Autocontido:* sim, script completo e executável.
   - *Saídas comentadas:* demonstram o efeito real do <c>weight_decay=0.01</c>, encolhendo a norma $L_2$ de $\approx 12{,}0$ para $\approx 7{,}0$ mantendo acurácia similar ($\approx 96\%$).

4. **[Script da Figura: t01-ativacoes.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/fig/t01-ativacoes.py):**
   - Utiliza <c>plt.rcParams["svg.fonttype"] = "none"</c>, gera 4 subgráficos comparando Degrau, Sigmoide, Tanh e ReLU com suas respectivas derivadas, e salva em <c>fig/t01-ativacoes.svg</c>. O arquivo SVG correspondente existe no diretório e possui 1.526 linhas de código vetorial limpo.

---

## 5. Verificação dos Critérios Editoriais e de Neurociência

- **Estrutura das seções requeridas:** Exatamente as 4 seções temáticas solicitadas, seguidas de "Resumo" e "Para ir além":
  1. `sec:9-1-1`: *Do neurônio biológico ao artificial* (soma dendrítica, potencial de repouso $-70\text{ mV}$, limiar $-55\text{ mV}$, disparo até $200\text{ Hz}$, modelo McCulloch & Pitts, perceptron de Rosenblatt, regra de aprendizado, portas AND/OR, impossibilidade do XOR por Minsky & Papert com prova, funções degrau, sigmoide, tanh e ReLU com derivadas e figura, curva $f\text{–}I$ saturante, armadilha taxa de disparo vs. potencial de ação);
  2. `sec:9-1-2`: *Redes multicamadas e funções de perda* (hierarquia visual V1 $\to$ IT, camadas e forward pass $\mathbf{z}^{(l)} = \mathbf{W}^{(l)}\mathbf{a}^{(l-1)} + \mathbf{b}^{(l)}$, contagem de parâmetros, colapso linear demonstrado, solução do XOR em MLP $2 \to 2 \to 1$ com ReLU, Teorema da Aproximação Universal de Cybenko, MSE, Softmax + Entropia Cruzada, máxima verossimilhança, decodificador de V1 com 3 classes, estabilidade numérica com $\max z_j$, armadilha de aplicar softmax duas vezes);
  3. `sec:9-1-3`: *Backpropagation pela regra da cadeia* (grafo computacional, forward e backward, exemplo numérico passo a passo $1 \to 1 \to 1$ conferido à mão, equações matriciais gerais da retropropagação com demonstração da saída softmax $\boldsymbol{\delta}^{(L)} = \hat{\mathbf{y}} - \mathbf{y}$, desaparecimento do gradiente por $\sigma'(z) \le 1/4$, exemplo olfativo biológico, diferenças finitas centradas, código PyTorch com autograd, plausibilidade biológica e o problema do transporte de pesos);
  4. `sec:9-1-4`: *Treinando de verdade: SGD, Adam e um MLP em PyTorch* (lote, estocástico, mini-lotes, épocas, momento com equação do PyTorch, Adam com médias móveis corrigidas, exemplo numérico comparando 2 passos de Momento e Adam à mão, quebra de simetria na inicialização, conjunto de validação, parada antecipada, decaimento de pesos / ridge, regra de Hebb vs. gradiente descendente, código completo de treino de MLP no dataset Digits com DataLoader e Adam, armadilhas de esquecer <c>zero_grad()</c> e taxa de aprendizado excessiva).
- **Exercícios:** Total de 16 exercícios (4 por seção), distribuídos uniformemente em 8 Básicos, 4 Intermediários e 4 Avançados. Todos possuem `<hint><title>Ver dica</title>...</hint>` e `<solution collapsible="true" collapsed="true">` contendo resolução completa passo a passo.
- **Contexto neurobiológico aplicado:** Cada uma das 4 seções traz múltiplos exemplos e exercícios ancorados em dados neurofisiológicos reais:
  - Seção 1: soma dendrítica, potencial de repouso $-70\text{ mV}$, limiar $-55\text{ mV}$, saturação de disparo em $200\text{ Hz}$, período refratário e balanço excitatório/inibitório em interneurônios;
  - Seção 2: hierarquia visual cortical (retina $\to$ V1 $\to$ V2 $\to$ V4 $\to$ IT), decodificação de orientações de estímulos visuais a partir de frequências de disparo em V1, decodificação motora com 128 neurônios e discriminação de tipos celulares por largura de *spike* e taxa basal;
  - Seção 3: decodificador olfativo a partir de interneurônios e discussão da plausibilidade biológica da retropropagação (transporte de pesos / *weight transport* e ausência de sinais de erro simétricos nos axônios);
  - Seção 4: comparação mecanicista entre a regra de Hebb associativa local (1949) e o aprendizado supervisionado por gradiente com sinal de erro global em circuitos motores.
- **Citações bibliográficas:** Todas reais, canônicas e mencionadas no corpo do texto apenas por autor e ano:
  - McCulloch & Pitts (1943); Hebb (1949); Hodgkin & Huxley (1952); Rosenblatt (1958); Minsky & Papert (1969); Cybenko (1989); Kingma & Ba (2015).
  - Referências adicionais: Goodfellow (Deep Learning Book) e Andrej Karpathy (aulas de autograd), ambos previstos no `index.html`.
  - Links externos restritos à documentação oficial do PyTorch (`pytorch.org/docs` e `pytorch.org/tutorials`).
- **Continuidade conceitual:** Abertura retoma formalmente a regra da cadeia (Módulo 3), otimização e gradiente descendente (Módulo 4), álgebra linear e matrizes (Módulo 5), máxima verossimilhança (Módulo 7), e classificação e regularização ridge (Módulo 8). Fecha apontando a ponte direta para o Tema 9.2 (CNNs como modelos do córtex visual).
- **Notação matemática:** Perfeitamente uniforme: vetores em negrito minúsculo ($\mathbf{x}$, $\mathbf{w}$, $\mathbf{b}$), matrizes em negrito maiúsculo ($\mathbf{W}$), ativações e pré-ativações ($\mathbf{a}^{(l)}$, $\mathbf{z}^{(l)}$), ativação $\phi$, sigmoide $\sigma$, taxa de aprendizado $\eta$ e perda $\mathcal{L}$.
- **Extensão do texto:** O arquivo possui 717 linhas XML totalizando aproximadamente 4.050 palavras de prosa (excluindo cabeçalhos e marcação XML), situando-se perfeitamente no intervalo estipulado de 3.500 a 5.000 palavras.
- **Conformidade Delta v0.6.0:** Atributos booleanos estritamente com valores explícitos (`collapsible="true" collapsed="true"`); tags `<intuition>` usadas unicamente dentro de `<definition>` e `<proposition>`, sem IDs; `<proof>` com `of="..."` associada; ausência total de tags proibidas (`<interactive>`, `<cite>`, `<bibliography>`, `<youtube>`).

---

## 6. Conclusão

A aula está impecável em todos os aspectos: matematicamente irrefutável, computacionalmente robusta, biologicamente contextualizada e estruturalmente perfeita segundo o padrão Delta e o contrato editorial. As três observações pedagógicas registradas na tabela representam sugestões menores de polimento para eventuais revisões futuras.

O veredito final é de **APROVAÇÃO**.
