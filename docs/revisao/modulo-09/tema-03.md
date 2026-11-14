# Relatório de Revisão Técnica — Módulo 09 · Tema 03 (RNN: Redes Neurais Recorrentes)

- **Arquivo revisado:** [conteudo/modulo-09/tema-03.dlt](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-03.dlt)
- **Documentos de referência:** [docs/PADRAO-AULAS.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/PADRAO-AULAS.md) e [docs/DELTA-COLA.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/DELTA-COLA.md)
- **Data da revisão:** 14 de novembro de 2026
- **Perfil do revisor:** Matemático, Neurocientista Computacional, Especialista em Deep Learning/PyTorch e Professor de Alunos de Ciências Biológicas

---

## 1. Veredito

**APROVAR**

A aula [conteudo/modulo-09/tema-03.dlt](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-03.dlt) atinge um padrão de excelência técnica, matemática, biológica e didática exemplar. Trata-se de uma ponte conceitual perfeita entre o aprendizado profundo de sequências e a neurociência de sistemas corticais dinâmicos, especialmente calibrada para estudantes de Ciências Biológicas.

Principais conclusões da auditoria:
1. **Exatidão matemática e algébrica:** Todas as contas de todos os exemplos numéricos e de todas as soluções dos 12 exercícios foram recalculadas à mão de forma independente e estão 100% corretas (passo a passo de ativações $\tanh$ e $\sigma$, discretização de Euler da equação de taxa neuronal, derivadas parciais e produto de Jacobianas no BPTT, norma e fator de corte de gradiente, contagem teórica e prática de parâmetros de LSTM e GRU, equações de estado e de célula, e projeções populacionais em autoespaços de atratores de linha).
2. **Código Python auditado linha a linha:** Todos os blocos de código (`cod:9-3-rnn-basica`, `cod:9-3-bptt-grad`, `cod:9-3-lstm-parametros`, `cod:9-3-integrador-pca` e as soluções de exercícios em código) são rigorosamente autocontidos, compatíveis com PyTorch 2.x e scikit-learn 1.x, utilizam dtypes corretos (`float32`), tratam o formato de lotes de forma consistente (`batch_first=True`), empregam boas práticas de otimização (`clip_grad_norm_`, `zero_grad()`, `torch.no_grad()`), e apresentam saídas comentadas perfeitamente reprodutíveis e biologicamente plausíveis.
3. **Neurociência de livro-texto e rigor histórico nas citações:** Todas as citações bibliográficas são clássicos canônicos reais, datados com precisão e descritos no contexto exato de sua contribuição (Dayan & Abbott; Elman, 1990; Hochreiter, 1991; Bengio, Simard & Frasconi, 1994; Fuster & Alexander, 1971; Goldman-Rakic, 1995; Hochreiter & Schmidhuber, 1997; Cho et al., 2014; Mante, Sussillo, Shenoy & Newsome, 2013; Sussillo & Barak, 2013). Os fenômenos fisiológicos abordados (constantes de tempo de membrana $\tau \approx 10\text{--}20\text{ ms}$, taxas de disparo basais e estimuladas, registros contínuos de LFP e EEG com artefatos de movimento, persistência de disparos no córtex pré-frontal durante respostas atrasadas e decodificação populacional de evidência sensorial) refletem a literatura consagrada da área.
4. **Estrutura e conformidade editorial:** A aula cobre com rigor e fluidez todas as 4 seções temáticas exigidas ("Estado oculto e recorrência", "Retropropagação no tempo e o gradiente que some", "LSTM e GRU", "RNNs como modelos de dinâmica cortical"), precedidas pela contextualização biológica inicial ("Por que isso importa", objetivos e pré-requisitos) e concluídas por "Resumo" e "Para ir além". Todos os 12 exercícios possuem título graduado (Básico, Intermediário, Avançado), `<hint>` e `<solution>` completa e recolhida por padrão. A notação matemática é perfeitamente uniforme ($\mathbf{x}_t$, $\mathbf{h}_t$, $\mathbf{W}_{hh}$, $\mathbf{W}_{xh}$, $\mathbf{b}$, $\sigma$, $\tanh$, $\mathcal{L}$). A extensão da prosa situa-se em torno de 4.100 palavras, perfeitamente dentro da faixa regulamentar de 3.500 a 5.000 palavras.

Identificaram-se apenas 4 sugestões de refinamento didático na tabela a seguir, sem qualquer natureza impeditiva.

---

## 2. Tabela de Problemas e Sugestões

| Severidade | Local | Trecho | Correção sugerida |
|---|---|---|---|
| Pedagógico | Seção 1 (`sec:9-3-1`), `prop:9-3-euler-taxa`, linhas ~79–88 | `$\mathbf{r}_{t+1} = \left(1 - \frac{\Delta t}{\tau}\right)\mathbf{r}_t + \frac{\Delta t}{\tau}\, f(\mathbf{W}\mathbf{r}_t + \mathbf{I}_t)$` | Na formulação contínua discretizada por Euler explícito, o estado em $t+1$ depende do estado em $t$ e da entrada em $t$. Na definição de RNN simples (`eq:9-3-rnn`), adota-se a convenção de indexação $\mathbf{h}_t = \tanh(\mathbf{W}_{hh} \mathbf{h}_{t-1} + \mathbf{W}_{xh} \mathbf{x}_t + \mathbf{b}_h)$. Para evitar que alunos de Biologia estranhem o deslocamento de um passo no índice da entrada (em Euler, $\mathbf{I}_t$ afeta $\mathbf{r}_{t+1}$; na RNN, $\mathbf{x}_t$ afeta $\mathbf{h}_t$), sugere-se incluir uma breve frase explicativa: *(reindexando $t \leftarrow t-1$, o passo de Euler coincide exatamente com a convenção da RNN onde o estímulo atual $\mathbf{x}_t$ atualiza $\mathbf{h}_t$ a partir do estado anterior $\mathbf{h}_{t-1}$)*. |
| Pedagógico | Seção 3 (`sec:9-3-3`), `def:9-3-gru`, linha ~447 | `$\tilde{\mathbf{h}}_t = \tanh\bigl(\mathbf{W}_{xh}\mathbf{x}_t + \mathbf{W}_{hh}(\mathbf{r}_t \odot \mathbf{h}_{t-1}) + \mathbf{b}_h\bigr)$` | O texto já esclarece com precisão que adota a formulação original de Cho et al. (2014) para a combinação de $\mathbf{h}_{t-1}$ e $\tilde{\mathbf{h}}_t$ via $(1 - \mathbf{z}_t)$ e $\mathbf{z}_t$. Vale adicionar uma nota curta mencionando que, na implementação do PyTorch (`nn.GRU`), o portão de reinicialização $\mathbf{r}_t$ atua após a transformação linear do estado oculto ($\mathbf{r}_t \odot (\mathbf{W}_{hh}\mathbf{h}_{t-1} + \mathbf{b}_{hh})$) para permitir paralelização eficiente de operações matriciais com BLAS/cuDNN. |
| Pedagógico | Seção 3 (`sec:9-3-3`), `exm:9-3-pfc-memoria`, linha ~477 | `$... \text{mantém } h_2 = 0{,}10 \cdot \tanh(1{,}451) \approx 0{,}090$` | O cálculo está perfeitamente correto. Para facilitar o acompanhamento passo a passo por estudantes que usam calculadora científica pela primeira vez, convém explicitar o valor intermediário da tangente hiperbólica: `$h_2 = 0{,}10 \cdot \tanh(1{,}451) \approx 0{,}10 \cdot 0{,}8959 \approx 0{,}0896 \approx 0{,}090$`. |
| Pedagógico | Seção 4 (`sec:9-3-4`), `exm:9-3-mante-pfc`, linhas ~595–598 | `$\frac{1{,}0}{\sqrt{2}}$, $\frac{2{,}0}{\sqrt{2}}$, $\frac{2{,}0}{\sqrt{2}}$` | As projeções sobre o vetor unitário $\mathbf{v}_1$ estão deduzidas com elegância analítica exata. Como o exemplo é seguido por gráficos e simulações com números em ponto flutuante, sugere-se acrescentar os valores decimais correspondentes entre parênteses: `$\frac{1{,}0}{\sqrt{2}} \approx 0{,}707$`, `$\frac{2{,}0}{\sqrt{2}} = \sqrt{2} \approx 1{,}414$` e `$\frac{2{,}0}{\sqrt{2}} \approx 1{,}414$`, reforçando a constância exata durante o período de silêncio ($t=2$ e $t=3$). |

---

## 3. Recálculo e Auditoria de Todas as Contas

Todas as contas dos exemplos resolvidos e das soluções dos 12 exercícios foram refeitas manualmente, passo a passo. Segue o registro discriminado das deduções confirmadas.

### 3.1 Subtema 1: Estado oculto e recorrência (`sec:9-3-1`)

1. **[Exemplo 9.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-03.dlt#L95-L106) (`exm:9-3-passo-escalar` — Propagação passo a passo com estado escalar):**
   - Parâmetros: $n_x = n_h = n_y = 1$, $h_0 = 0$, $w_{hh} = 0{,}5$, $w_{xh} = 0{,}5$, $b_h = 0$, $w_{hy} = 2{,}0$, $b_y = -0{,}1$.
   - Entrada: $(x_1, x_2, x_3) = (1{,}0;\; 0{,}4;\; -0{,}8)$.
   - **Passo $t = 1$ ($x_1 = 1{,}0$):**
     $$z_1 = 0{,}5(0) + 0{,}5(1{,}0) + 0 = 0{,}5$$
     $$h_1 = \tanh(0{,}5) = \frac{e^{0{,}5} - e^{-0{,}5}}{e^{0{,}5} + e^{-0{,}5}} = \frac{1{,}648721 - 0{,}606531}{1{,}648721 + 0{,}606531} \approx 0{,}462117 \approx 0{,}4621$$
     $$\hat{y}_1 = 2{,}0(0{,}462117) - 0{,}1 = 0{,}924234 - 0{,}1 \approx 0{,}8242$$
   - **Passo $t = 2$ ($x_2 = 0{,}4$):**
     $$z_2 = 0{,}5(0{,}462117) + 0{,}5(0{,}4) = 0{,}231059 + 0{,}2 = 0{,}431059 \approx 0{,}4311$$
     $$h_2 = \tanh(0{,}431059) = \frac{1{,}538886 - 0{,}649821}{1{,}538886 + 0{,}649821} \approx 0{,}406218 \approx 0{,}4062$$
     $$\hat{y}_2 = 2{,}0(0{,}406218) - 0{,}1 = 0{,}812437 - 0{,}1 \approx 0{,}7124$$
   - **Passo $t = 3$ ($x_3 = -0{,}8$):**
     $$z_3 = 0{,}5(0{,}406218) + 0{,}5(-0{,}8) = 0{,}203109 - 0{,}4 = -0{,}196891 \approx -0{,}1969$$
     $$h_3 = \tanh(-0{,}196891) \approx -0{,}194389 \approx -0{,}1944$$
     $$\hat{y}_3 = 2{,}0(-0{,}194389) - 0{,}1 = -0{,}388778 - 0{,}1 \approx -0{,}4888$$
   - *Valores perfeitamente conferidos.*

2. **[Proposição 9.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-03.dlt#L75-L89) (`prop:9-3-euler-taxa` — Discretização de Euler da equação de taxa neural):**
   - Equação diferencial contínua: $\tau \frac{d\mathbf{r}}{dt} = -\mathbf{r}(t) + f(\mathbf{W}\mathbf{r}(t) + \mathbf{I}(t))$.
   - Aproximação de Euler: $\frac{d\mathbf{r}}{dt} \approx \frac{\mathbf{r}_{t+1} - \mathbf{r}_t}{\Delta t}$.
   - Substituição: $\tau \frac{\mathbf{r}_{t+1} - \mathbf{r}_t}{\Delta t} = -\mathbf{r}_t + f(\mathbf{W}\mathbf{r}_t + \mathbf{I}_t) \iff \mathbf{r}_{t+1} - \mathbf{r}_t = -\frac{\Delta t}{\tau}\mathbf{r}_t + \frac{\Delta t}{\tau} f(\dots)$.
   - Rearranjo: $\mathbf{r}_{t+1} = \left(1 - \frac{\Delta t}{\tau}\right)\mathbf{r}_t + \frac{\Delta t}{\tau} f(\mathbf{W}\mathbf{r}_t + \mathbf{I}_t)$.
   - Caso particular $\Delta t = \tau$: $1 - 1 = 0$ e $\frac{\Delta t}{\tau} = 1 \implies \mathbf{r}_{t+1} = f(\mathbf{W}\mathbf{r}_t + \mathbf{I}_t)$.
   - *Demonstração algébrica exata.*

3. **[Exemplo 9.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-03.dlt#L108-L119) (`exm:9-3-disparo-euler` — Dinâmica de taxa de disparo com passo $\Delta t = 5\text{ ms}$):**
   - Parâmetros: $\tau = 20\text{ ms}$, $\Delta t = 5\text{ ms} \implies \alpha = \frac{5}{20} = 0{,}25$, $1 - \alpha = 0{,}75$.
   - Taxa basal $r_0 = 12\text{ Hz}$, entrada constante $f(I(t)) = 60\text{ Hz} \implies \alpha \cdot 60 = 0{,}25 \times 60 = 15\text{ Hz}$.
   - Relação de recorrência: $r_{t+1} = 0{,}75\, r_t + 15$.
   - $t = 1$ ($5\text{ ms}$): $r_1 = 0{,}75(12) + 15 = 9 + 15 = 24\text{ Hz}$.
   - $t = 2$ ($10\text{ ms}$): $r_2 = 0{,}75(24) + 15 = 18 + 15 = 33\text{ Hz}$.
   - $t = 3$ ($15\text{ ms}$): $r_3 = 0{,}75(33) + 15 = 24{,}75 + 15 = 39{,}75\text{ Hz}$.
   - *Valores perfeitamente conferidos.*

4. **[Exercício 9.3.1.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-03.dlt#L162-L173) (`exr:9-3-1-1` — Cálculo à mão com estado escalar):**
   - Parâmetros: $h_0 = 0{,}2$, $w_{hh} = 0{,}5$, $w_{xh} = 1{,}0$, $b_h = 0$, $w_{hy} = 2{,}0$, $b_y = 0{,}1$.
   - Entrada: $(x_1, x_2) = (0{,}4;\; -0{,}6)$.
   - $t = 1$: $z_1 = 0{,}5(0{,}2) + 1{,}0(0{,}4) = 0{,}1 + 0{,}4 = 0{,}5 \implies h_1 = \tanh(0{,}5) \approx 0{,}4621$.
   - $t = 2$: $z_2 = 0{,}5(0{,}462117) + 1{,}0(-0{,}6) = 0{,}231059 - 0{,}6 = -0{,}368941 \approx -0{,}36895 \implies h_2 = \tanh(-0{,}368941) \approx -0{,}353086 \approx -0{,}3531$.
   - Saída: $\hat{y}_2 = 2{,}0(-0{,}353086) + 0{,}1 = -0{,}706173 + 0{,}1 \approx -0{,}6062$.
   - *Contas e arredondamentos exatos.*

5. **[Exercício 9.3.1.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-03.dlt#L175-L187) (`exr:9-3-1-2` — Equação de taxa neuronal discretizada):**
   - Parâmetros: $\tau = 20\text{ ms}$, $\Delta t = 5\text{ ms} \implies \alpha = 0{,}25$, $1 - \alpha = 0{,}75$.
   - $r_0 = 10\text{ Hz}$, $f(\dots) = 50\text{ Hz} \implies 0{,}25 \times 50 = 12{,}5\text{ Hz}$.
   - Regra: $r_{t+1} = 0{,}75\, r_t + 12{,}5$.
   - $r_1 = 0{,}75(10) + 12{,}5 = 7{,}5 + 12{,}5 = 20\text{ Hz}$.
   - $r_2 = 0{,}75(20) + 12{,}5 = 15 + 12{,}5 = 27{,}5\text{ Hz}$.
   - $r_3 = 0{,}75(27{,}5) + 12{,}5 = 20{,}625 + 12{,}5 = 33{,}125\text{ Hz}$.
   - *Contas exatas.*

6. **[Exercício 9.3.1.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-03.dlt#L189-L213) (`exr:9-3-1-3` — Formas de tensores no PyTorch):**
   - Entrada: $X \in \mathbb{R}^{16 \times 40 \times 12}$ (`batch_first=True`).
   - Camada: `nn.RNN(input_size=12, hidden_size=24, batch_first=True)`.
   - Camada de leitura: `nn.Linear(in_features=24, out_features=2)`.
   - Saída `out`: dimensão $(N, T, n_h) = (16, 40, 24)$.
   - Saída `h_final`: dimensão $(D \cdot \text{num\_layers}, N, n_h) = (1, 16, 24)$.
   - Saída `y_hat`: dimensão $(16, 40, 2)$.
   - *Formatos de tensores perfeitamente consistentes com as convenções do PyTorch.*

---

### 3.2 Subtema 2: Retropropagação no tempo e o gradiente que some (`sec:9-3-2`)

1. **[Proposição 9.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-03.dlt#L234-L256) (`prop:9-3-jacobiana-rnn` — Jacobiana temporal e decaimento exponencial):**
   - Derivada local de $\tanh$: $\frac{d}{dz}\tanh(z) = 1 - \tanh^2(z) = 1 - h^2$.
   - Jacobiana de passo: $(\mathbf{J}_t)_{ij} = \frac{\partial h_{t,i}}{\partial h_{t-1,j}} = (1 - h_{t,i}^2)(\mathbf{W}_{hh})_{ij} \iff \mathbf{J}_t = \mathrm{diag}(1 - \mathbf{h}_t^2)\mathbf{W}_{hh}$.
   - Regra da cadeia temporal: $\frac{\partial \mathbf{h}_T}{\partial \mathbf{h}_k} = \prod_{t=T}^{k+1} \mathbf{J}_t$.
   - Caso escalar com $w = 0{,}5$ em $T = 20$:
     $$0{,}5^{20} = \frac{1}{2^{20}} = \frac{1}{1\,048\,576} \approx 9{,}536743 \times 10^{-7} \approx 9{,}5 \times 10^{-7}$$
   - Caso escalar com $w = 1{,}5$ em $T = 20$:
     $$1{,}5^{20} = \left(\frac{3}{2}\right)^{20} = \frac{3\,486\,784\,401}{1\,048\,576} \approx 3\,325{,}2567 \approx 3\,325$$
   - *Valores numéricos e deduções analíticas exatos.*

2. **[Exemplo 9.5](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-03.dlt#L277-L294) (`exm:9-3-bptt-escalar` — Cálculo à mão de derivadas temporais na BPTT):**
   - Estados: $h_1 \approx 0{,}4621$, $h_2 \approx 0{,}4062$, $h_3 \approx -0{,}1944$, $w_{hh} = 0{,}5$, perda $\mathcal{L} = \frac{1}{2}h_3^2$.
   - Fatores $(1 - h_t^2)$:
     - $1 - h_3^2 = 1 - (-0{,}1944)^2 = 1 - 0{,}037791 = 0{,}962209 \approx 0{,}9622$
     - $1 - h_2^2 = 1 - (0{,}4062)^2 = 1 - 0{,}164998 = 0{,}835002 \approx 0{,}8350$
     - $1 - h_1^2 = 1 - (0{,}4621)^2 = 1 - 0{,}213536 = 0{,}786464 \approx 0{,}7865$
   - Jacobianas de passo:
     - $J_3 = 0{,}5 \times 0{,}9622 = 0{,}4811$
     - $J_2 = 0{,}5 \times 0{,}8350 = 0{,}4175$
   - Derivada total temporal:
     $$\frac{\partial h_3}{\partial h_1} = J_3 \cdot J_2 = 0{,}4811 \times 0{,}4175 = 0{,}200859 \approx 0{,}2009$$
   - Retropropagação da perda:
     - $\frac{\partial \mathcal{L}}{\partial h_3} = h_3 \approx -0{,}1944$
     - $\frac{\partial \mathcal{L}}{\partial h_2} = \frac{\partial \mathcal{L}}{\partial h_3} J_3 = (-0{,}1944)(0{,}4811) = -0{,}093526 \approx -0{,}0935$
     - $\frac{\partial \mathcal{L}}{\partial h_1} = \frac{\partial \mathcal{L}}{\partial h_2} J_2 = (-0{,}0935)(0{,}4175) = -0{,}039036 \approx -0{,}0390$
   - Derivada em relação a $w_{hh}$ ($\frac{\partial^+ h_k}{\partial w_{hh}} = (1 - h_k^2)h_{k-1}$):
     - Termo $k = 3$: $(-0{,}1944)(0{,}9622)(0{,}4062) = -0{,}075981 \approx -0{,}0760$
     - Termo $k = 2$: $(-0{,}0935)(0{,}8350)(0{,}4621) = -0{,}036077 \approx -0{,}0361$
     - Termo $k = 1$: como $h_0 = 0$, o termo é nulo ($0$)
     - Soma total: $\frac{\partial \mathcal{L}}{\partial w_{hh}} \approx -0{,}0760 - 0{,}0361 = -0{,}1121$
   - *Cálculos auditados e perfeitamente exatos.*

3. **[Exemplo 9.6](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-03.dlt#L296-L303) (`exm:9-3-corte-gradiente` — Corte de gradiente em janela de EEG):**
   - Vetor $\mathbf{g} = [3{,}0;\; -4{,}0;\; 12{,}0]^\top$, limiar $c = 2{,}6$.
   - Norma euclidiana: $\|\mathbf{g}\|_2 = \sqrt{3^2 + (-4)^2 + 12^2} = \sqrt{9 + 16 + 144} = \sqrt{169} = 13{,}0$.
   - Como $13{,}0 > 2{,}6$, reescalamento por $\frac{c}{\|\mathbf{g}\|_2} = \frac{2{,}6}{13{,}0} = 0{,}2$.
   - Vetor cortado: $\mathbf{g}_{\text{clip}} = 0{,}2 \times [3{,}0;\; -4{,}0;\; 12{,}0]^\top = [0{,}6;\; -0{,}8;\; 2{,}4]^\top$.
   - Norma conferida: $\sqrt{0{,}6^2 + (-0{,}8)^2 + 2{,}4^2} = \sqrt{0{,}36 + 0{,}64 + 5{,}76} = \sqrt{6{,}76} = 2{,}6$.
   - *Contas e propriedades geométricas exatas.*

4. **[Exercício 9.3.2.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-03.dlt#L345-L358) (`exr:9-3-2-1` — Produto de Jacobianas escalares à mão):**
   - Parâmetros: $w_{hh} = 0{,}8$, $h_1 = 0{,}5$, $h_2 = 0{,}0$, $h_3 = -0{,}5$.
   - $J_1 = 0{,}8(1 - 0{,}5^2) = 0{,}8(1 - 0{,}25) = 0{,}8 \times 0{,}75 = 0{,}60$.
   - $J_2 = 0{,}8(1 - 0{,}0^2) = 0{,}8(1 - 0) = 0{,}8 \times 1{,}00 = 0{,}80$.
   - $J_3 = 0{,}8(1 - (-0{,}5)^2) = 0{,}8(1 - 0{,}25) = 0{,}8 \times 0{,}75 = 0{,}60$.
   - Produto: $\frac{\partial h_3}{\partial h_0} = J_3 \cdot J_2 \cdot J_1 = 0{,}60 \times 0{,}80 \times 0{,}60 = 0{,}288$.
   - *Contas exatas.*

5. **[Exercício 9.3.2.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-03.dlt#L360-L375) (`exr:9-3-2-2` — Autovalores, raio espectral e decaimento em circuito neural):**
   - Matriz $\mathbf{W}_{hh} = \begin{pmatrix} 0{,}6 & 0{,}0 \\ 0{,}2 & 0{,}5 \end{pmatrix}$.
   - Equação característica: $\det(\mathbf{W}_{hh} - \lambda \mathbf{I}) = (0{,}6 - \lambda)(0{,}5 - \lambda) = 0 \implies \lambda_1 = 0{,}6, \lambda_2 = 0{,}5$.
   - Raio espectral: $\rho(\mathbf{W}_{hh}) = \max(|\lambda_1|, |\lambda_2|) = 0{,}6$.
   - Como $\rho < 1$, o sistema é contrátil e o gradiente decai exponencialmente:
     - Modo dominante: $0{,}6^{20} \approx 3{,}656158 \times 10^{-5} \approx 3{,}66 \times 10^{-5}$.
     - Modo secundário: $0{,}5^{20} \approx 9{,}536743 \times 10^{-7} \approx 9{,}54 \times 10^{-7}$.
   - *Autovalores e ordens de grandeza perfeitamente exatos.*

6. **[Exercício 9.3.2.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-03.dlt#L377-L391) (`exr:9-3-2-3` — BPTT truncado em sinal contínuo de LFP):**
   - Frequência de amostragem: $f_s = 100\text{ Hz} \implies \Delta t = \frac{1\,000\text{ ms}}{100} = 10\text{ ms/amostra}$.
   - Janela de truncamento $K = 25$ passos: $25 \times 10\text{ ms} = 250\text{ ms} = 0{,}25\text{ s}$.
   - Intervalo pista-resposta: $2{,}0\text{ s} = 2\,000\text{ ms}$ ($200$ passos).
   - Como $2\,000\text{ ms} \gg 250\text{ ms}$ (abrange 8 blocos com `.detach()`), o grafo de diferenciação automática é truncado a cada $250\text{ ms}$, tornando impossível o aprendizado da contingência temporal.
   - *Contas e justificativa física corretas.*

---

### 3.3 Subtema 3: LSTM e GRU (`sec:9-3-3`)

1. **[Proposição 9.5](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-03.dlt#L424-L435) (`prop:9-3-fluxo-celula` — Fluxo aditivo de gradiente na célula da LSTM):**
   - Equação: $\mathbf{c}_t = \mathbf{f}_t \odot \mathbf{c}_{t-1} + \mathbf{i}_t \odot \tilde{\mathbf{c}}_t$.
   - Derivada componente a componente: $\frac{\partial c_{t,j}}{\partial c_{t-1,k}} = f_{t,j} \delta_{jk} \implies \frac{\partial \mathbf{c}_t}{\partial \mathbf{c}_{t-1}} = \mathrm{diag}(\mathbf{f}_t)$.
   - Para $f_t \approx 1$, $\prod_{t} f_t \approx 1$, preservando o gradiente ao longo de muitos passos (carrossel de erro constante).
   - *Dedução correta.*

2. **Contagem de parâmetros teóricos versus PyTorch (linhas 452–455):**
   - Parâmetros por bloco afim com $1$ viés: $n_h(n_h + n_x + 1)$.
   - Parâmetros por bloco no PyTorch com $2$ vieses (`bias_ih` e `bias_hh`): $n_h(n_h + n_x + 2)$.
   - Para $n_x = 10, n_h = 20$:
     - PyTorch por bloco: $20 \times (20 + 10 + 2) = 20 \times 32 = 640$.
     - RNN simples ($1$ bloco): $1 \times 640 = 640$.
     - GRU ($3$ blocos): $3 \times 640 = 1\,920$.
     - LSTM ($4$ blocos): $4 \times 640 = 2\,560$.
   - *Valores idênticos aos obtidos por código PyTorch nas linhas 496–498.*

3. **[Exemplo 9.7](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-03.dlt#L456-L470) (`exm:9-3-lstm-mao` — Um passo de LSTM escalar à mão):**
   - Parâmetros: $c_0 = 1{,}0$, $h_0 = 0$, $x_1 = 1{,}0$.
   - Pesos e vieses:
     - Esquecimento: $w_{xf}=0, b_f=2{,}0 \implies f_1 = \sigma(2{,}0) = \frac{1}{1 + e^{-2}} \approx \frac{1}{1 + 0{,}135335} \approx 0{,}880797 \approx 0{,}8808$.
     - Entrada: $w_{xi}=1{,}0, b_i=-1{,}0 \implies i_1 = \sigma(1{,}0 - 1{,}0) = \sigma(0) = 0{,}5000$.
     - Candidato: $w_{xc}=0{,}5, b_c=0 \implies \tilde{c}_1 = \tanh(0{,}5) \approx 0{,}462117 \approx 0{,}4621$.
     - Saída: $w_{xo}=0, b_o=1{,}0 \implies o_1 = \sigma(1{,}0) = \frac{1}{1 + e^{-1}} \approx \frac{1}{1 + 0{,}367879} \approx 0{,}731059 \approx 0{,}7311$.
   - Atualização do estado da célula:
     $$c_1 = f_1 c_0 + i_1 \tilde{c}_1 = (0{,}880797)(1{,}0) + (0{,}5000)(0{,}462117) = 0{,}880797 + 0{,}231059 = 1{,}111856 \approx 1{,}1119$$
     *(pelas aproximações a 4 casas: $0{,}8808 + 0{,}5000 \times 0{,}4621 = 0{,}8808 + 0{,}23105 = 1{,}11185 \approx 1{,}1119$)*.
   - Estado oculto:
     $$\tanh(1{,}111856) \approx 0{,}804716 \approx 0{,}8047$$
     $$h_1 = o_1 \tanh(c_1) = 0{,}731059 \times 0{,}804716 \approx 0{,}588294 \approx 0{,}5883$$
   - *Valores perfeitamente conferidos.*

4. **[Exemplo 9.8](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-03.dlt#L471-L478) (`exm:9-3-pfc-memoria` — Memória de trabalho pré-frontal resistente a distratores):**
   - Estado inicial da célula: $c_1 = 1{,}5$.
   - Distrator: $x_2 = -2{,}0$.
   - Portões ativados: $f_2 = 0{,}98$, $i_2 = 0{,}02$, $\tilde{c}_2 = -0{,}95$, $o_2 = 0{,}10$.
   - Novo estado da célula:
     $$c_2 = (0{,}98)(1{,}5) + (0{,}02)(-0{,}95) = 1{,}470 - 0{,}019 = 1{,}451$$
   - Novo estado oculto:
     $$\tanh(1{,}451) \approx 0{,}895889 \implies h_2 = 0{,}10 \times 0{,}895889 \approx 0{,}089589 \approx 0{,}090$$
   - *Contas exatas.*

5. **[Exercício 9.3.3.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-03.dlt#L526-L540) (`exr:9-3-3-1` — Contagem de parâmetros de LSTM e GRU):**
   - Dimensões: $n_x = 16$, $n_h = 32$.
   - (a) Fórmula teórica ($1$ viés por portão):
     - Parâmetros por bloco: $n_h(n_h + n_x + 1) = 32 \times (32 + 16 + 1) = 32 \times 49 = 1\,568$.
     - LSTM ($4$ blocos): $4 \times 1\,568 = 6\,272$.
     - GRU ($3$ blocos): $3 \times 1\,568 = 4\,704$.
   - (b) PyTorch ($2$ vieses por portão):
     - Parâmetros por bloco: $n_h(n_h + n_x + 2) = 32 \times (32 + 16 + 2) = 32 \times 50 = 1\,600$.
     - LSTM no PyTorch (`nn.LSTM`): $4 \times 1\,600 = 6\,400$.
     - GRU no PyTorch (`nn.GRU`): $3 \times 1\,600 = 4\,800$.
   - *Multiplicações e contagens perfeitamente corretas.*

6. **[Exercício 9.3.3.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-03.dlt#L542-L549) (`exr:9-3-3-2` — Papel dos portões na limpeza da memória de trabalho):**
   - Análise fisiológica do chaveamento de portões: retenção com $f_t \approx 1, i_t \approx 0$; apagamento no início da nova tentativa com $f_t \approx 0$; gravação do novo estímulo com $i_t \approx 1$.
   - *Fundamentação teórica irretocável.*

7. **[Exercício 9.3.3.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-03.dlt#L551-L560) (`exr:9-3-3-3` — Atenuação em sequência longa mesmo com LSTM):**
   - Portão de esquecimento: $f_t = \sigma(1{,}0) = \frac{1}{1 + e^{-1}} \approx 0{,}7310586 \approx 0{,}7311$.
   - Para $T = 20$ passos:
     $$0{,}7311^{20} \approx 0{,}0019047 \approx 1{,}9 \times 10^{-3} \quad (0{,}7310586^{20} \approx 0{,}0019013 \approx 1{,}901 \times 10^{-3})$$
   - Para $T = 100$ passos ($T = 20 \times 5$):
     $$(0{,}7311^{20})^5 \approx (1{,}9013 \times 10^{-3})^5 \approx 2{,}478 \times 10^{-14} \approx 2{,}5 \times 10^{-14}$$
   - *Potências e conclusões sobre inicialização positiva de $b_f$ exatas.*

---

### 3.4 Subtema 4: RNNs como modelos de dinâmica cortical (`sec:9-3-4`)

1. **[Exemplo 9.9](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-03.dlt#L581-L600) (`exm:9-3-mante-pfc` — Leitura populacional versus neurônios individuais no córtex pré-frontal):**
   - Sistema dinâmico: $\mathbf{h}_t = \mathbf{W}\mathbf{h}_{t-1} + \mathbf{b}_x x_t$, com $\mathbf{W} = \begin{pmatrix} 0{,}5 & -0{,}5 \\ -0{,}5 & 0{,}5 \end{pmatrix}$, $\mathbf{b}_x = \begin{pmatrix} 0{,}8 \\ -0{,}2 \end{pmatrix}$, $\mathbf{h}_0 = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$.
   - Sequência $(x_1, x_2, x_3) = (1, 1, 0)$.
   - **Passo $t = 1$ ($x_1 = 1$):**
     $$\mathbf{h}_1 = \mathbf{W}\mathbf{0} + \begin{pmatrix} 0{,}8 \\ -0{,}2 \end{pmatrix}(1) = \begin{pmatrix} 0{,}8 \\ -0{,}2 \end{pmatrix}$$
   - **Passo $t = 2$ ($x_2 = 1$):**
     $$\mathbf{W}\mathbf{h}_1 = \begin{pmatrix} 0{,}5(0{,}8) - 0{,}5(-0{,}2) \\ -0{,}5(0{,}8) + 0{,}5(-0{,}2) \end{pmatrix} = \begin{pmatrix} 0{,}4 + 0{,}1 \\ -0{,}4 - 0{,}1 \end{pmatrix} = \begin{pmatrix} 0{,}5 \\ -0{,}5 \end{pmatrix}$$
     $$\mathbf{h}_2 = \begin{pmatrix} 0{,}5 \\ -0{,}5 \end{pmatrix} + \begin{pmatrix} 0{,}8 \\ -0{,}2 \end{pmatrix}(1) = \begin{pmatrix} 1{,}3 \\ -0{,}7 \end{pmatrix}$$
   - **Passo $t = 3$ ($x_3 = 0$):**
     $$\mathbf{h}_3 = \mathbf{W}\mathbf{h}_2 + \mathbf{0} = \begin{pmatrix} 0{,}5(1{,}3) - 0{,}5(-0{,}7) \\ -0{,}5(1{,}3) + 0{,}5(-0{,}7) \end{pmatrix} = \begin{pmatrix} 0{,}65 + 0{,}35 \\ -0{,}65 - 0{,}35 \end{pmatrix} = \begin{pmatrix} 1{,}0 \\ -1{,}0 \end{pmatrix}$$
   - **Projeção populacional em $\mathbf{v}_1 = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ -1 \end{pmatrix}$:**
     - Fórmula: $\mathbf{v}_1^\top \mathbf{h}_t = \frac{h_{t,1} - h_{t,2}}{\sqrt{2}}$.
     - $t = 1$: $\frac{0{,}8 - (-0{,}2)}{\sqrt{2}} = \frac{1{,}0}{\sqrt{2}}$.
     - $t = 2$: $\frac{1{,}3 - (-0{,}7)}{\sqrt{2}} = \frac{2{,}0}{\sqrt{2}}$.
     - $t = 3$: $\frac{1{,}0 - (-1{,}0)}{\sqrt{2}} = \frac{2{,}0}{\sqrt{2}}$.
   - *Nota matemática:* Como $\mathbf{W}\mathbf{v}_1 = 1 \cdot \mathbf{v}_1$, o vetor $\mathbf{v}_1$ é autovetor com autovalor $\lambda = 1$ (atrator de linha neutramente estável), demonstrando por que a evidência integrada é perfeitamente preservada no atraso. Contas irrefutáveis.

2. **[Exemplo 9.10](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-03.dlt#L602-L609) (`exm:9-3-integrador-linear` — Integrador perfeito versus regra ótima em sinal sensorial ruidoso):**
   - Parâmetros: $T = 20$, $x_t \sim \mathcal{N}(\mu, 0{,}8^2)$ com $\mu = \pm 0{,}25$.
   - Soma $S = \sum_{t=1}^{20} x_t$ sob $\mu = +0{,}25$:
     $$\mathbb{E}[S] = 20 \times 0{,}25 = 5{,}0$$
     $$\mathrm{Var}(S) = 20 \times 0{,}8^2 = 20 \times 0{,}64 = 12{,}8$$
     $$\mathrm{DP}(S) = \sqrt{12{,}8} \approx 3{,}577709 \approx 3{,}578$$
   - Escore $z$ para o limiar de decisão $S > 0$:
     $$z = \frac{5{,}0 - 0}{3{,}577709} \approx 1{,}39754 \approx 1{,}398$$
   - Probabilidade acumulada normal $\Phi(1{,}39754)$:
     $$\mathbb{P}(S > 0) = \Phi(1{,}398) \approx 0{,}91887 \approx 0{,}919 \quad (91{,}9\%)$$
   - Erro-padrão da proporção amostral para $N = 400$ testes:
     $$\mathrm{EP} = \sqrt{\frac{p(1 - p)}{N}} = \sqrt{\frac{0{,}919 \times 0{,}081}{400}} = \sqrt{\frac{0{,}074439}{400}} = \sqrt{0{,}0001861} \approx 0{,}01364 \approx 0{,}014$$
   - Justifica com rigor por que a acurácia amostral de $0{,}933$ observada no script está perfeitamente compatível com o teto bayesiano populacional de $0{,}919$.
   - *Cálculos probabilísticos exatos.*

3. **[Exercício 9.3.4.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-03.dlt#L711-L726) (`exr:9-3-4-1` — Integrador perfeito versus integrador com vazamento):**
   - Estímulo: $(x_1, x_2, x_3, x_4) = (0{,}5;\; 0{,}5;\; 0;\; 0)$, $h_0 = 0$.
   - **Modelo A ($h_t = 1{,}0\, h_{t-1} + x_t$):**
     - $h_1 = 1{,}0(0) + 0{,}5 = 0{,}5$
     - $h_2 = 1{,}0(0{,}5) + 0{,}5 = 1{,}0$
     - $h_3 = 1{,}0(1{,}0) + 0 = 1{,}0$
     - $h_4 = 1{,}0(1{,}0) + 0 = 1{,}0$
     - Ponto fixo em $x = 0$: $h^* = 1{,}0\, h^* \iff 0 = 0$ (linha contínua de atratores).
   - **Modelo B ($h_t = 0{,}8\, h_{t-1} + x_t$):**
     - $h_1 = 0{,}8(0) + 0{,}5 = 0{,}5$
     - $h_2 = 0{,}8(0{,}5) + 0{,}5 = 0{,}4 + 0{,}5 = 0{,}9$
     - $h_3 = 0{,}8(0{,}9) + 0 = 0{,}72$
     - $h_4 = 0{,}8(0{,}72) + 0 = 0{,}576$
     - Ponto fixo em $x = 0$: $h^* = 0{,}8\, h^* \iff 0{,}2\, h^* = 0 \iff h^* = 0$ (ponto isolado de equilíbrio).
   - *Contas exatas.*

4. **[Exercício 9.3.4.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-03.dlt#L728-L735) (`exr:9-3-4-2` — Forma dos estados ocultos para PCA):**
   - Dimensões: $N = 120$ tentativas, $T = 50$ passos, $n_h = 32$ unidades.
   - Matriz 3D: $(120, 50, 32)$.
   - Remodelação para PCA 2D: $(120 \times 50, 32) = (6\,000, 32)$ observações em $\mathbb{R}^{32}$.
   - Projeção `PCA(n_components=3)`: resulta em $(6\,000, 3)$.
   - Reorganização para trajetórias médias: `.reshape(120, 50, 3).mean(axis=0)` resulta em $(50, 3)$.
   - *Formatos e manipulações tensoriais corretas.*

5. **[Exercício 9.3.4.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-03.dlt#L737-L797) (`exr:9-3-4-3` — Experimento em código com atraso pós-estímulo):**
   - Estrutura temporal: $15$ passos de estímulo ruidoso + $10$ passos de silêncio ($T = 25$).
   - Separação na componente principal dominante: PC1 em $t = 25$ mantém $1{,}40$ (classe positiva) contra $-2{,}31$ (classe negativa), preservando acurácia de $93{,}0\%$.
   - *Valores empíricos e lógica do script conferidos.*

---

## 4. Auditoria de Código Python (PyTorch 2.x e scikit-learn 1.x)

Todos os scripts da aula foram inspecionados detalhadamente linha a linha:

1. **Bloco 1 (`cod:9-3-rnn-basica`, linhas 123–151):**
   - **Autocontenção:** importa `torch` e `torch.nn as nn`.
   - **Formato dos tensores:** `x` com forma `(1, 3, 1)` respeita `batch_first=True`. `h0` com `(1, 1, 1)` atende à assinatura do PyTorch `(num_layers, batch_size, hidden_size)`.
   - **Saídas comentadas:** formas de `x`, `out` e `h_final`, bem como valores numéricos de `h_t` e `y_hat`, coincidem exatamente com o Exemplo 9.3 recalculado à mão.

2. **Bloco 2 (solução do `exr:9-3-1-3`, linhas 194–210):**
   - **Autocontenção:** importa `torch` e `torch.nn as nn`, define semente `torch.manual_seed(0)`.
   - **Compatibilidade PyTorch 2.x:** `nn.RNN` com `batch_first=True` e `nn.Linear` operando sobre a última dimensão do tensor 3D `(16, 40, 24)`.

3. **Bloco 3 (`cod:9-3-bptt-grad`, linhas 307–334):**
   - **Autocontenção:** importa `torch` e `torch.nn as nn`.
   - **Diferenciação automática:** utiliza `h0.requires_grad = True` e mede o gradiente acumulado por `h_final.squeeze().backward()`. O artifício de fixar $h_0 = 10^{-7}$ mantém $1 - h_t^2 \approx 1$ em todos os 20 passos, isolando analiticamente o efeito exponencial de $w^{20}$.
   - **Função de corte:** utiliza `torch.nn.utils.clip_grad_norm_([param], max_norm=2.6)`, retornando a norma anterior ($13{,}0$) e alterando `param.grad` in-place para $[0{,}6;\; -0{,}8;\; 2{,}4]^\top$.

4. **Bloco 4 (`cod:9-3-lstm-parametros`, linhas 482–515):**
   - **Autocontenção:** importa `torch` e `torch.nn as nn`.
   - **Disposição interna de portões no PyTorch:** preenche corretamente `weight_ih_l0` e `bias_ih_l0` seguindo a ordem nativa do PyTorch (`i, f, g, o`):
     - Linha 0 (portão de entrada $i$): peso $1{,}0$, viés $-1{,}0$;
     - Linha 1 (portão de esquecimento $f$): peso $0{,}0$, viés $2{,}0$;
     - Linha 2 (célula candidata $g$ / $\tilde{c}$): peso $0{,}5$, viés $0{,}0$;
     - Linha 3 (portão de saída $o$): peso $0{,}0$, viés $1{,}0$.
   - **Saídas comentadas:** `c1 = 1.1119` e `h1 = 0.5883` reproduzem com precisão de 4 casas decimais o Exemplo 9.7.

5. **Bloco 5 (`cod:9-3-integrador-pca`, linhas 613–698):**
   - **Autocontenção:** importa `numpy as np`, `torch`, `torch.nn as nn` e `from sklearn.decomposition import PCA`.
   - **Geração e dtypes:** dados gerados com `np.random.default_rng(0)`, convertidos para tensores `torch.float32`.
   - **Treinamento:** modelo com `nn.GRU` e `nn.Linear`, função de custo `nn.BCEWithLogitsLoss()`, otimizador `Adam(lr=0.01)`, com `clip_grad_norm_` aplicado a cada época.
   - **Avaliação e PCA:** conversão limpa com `.numpy()` (dentro de bloco `with torch.no_grad():`), PCA bidimensional ajustada sobre a matriz $(8000, 16)$, com inversão automática de sinal para padronizar a direção visual de PC1. Resultados comentados perfeitamente condizentes com a teoria bayesiana.

6. **Bloco 6 (solução do `exr:9-3-4-3`, linhas 742–794):**
   - **Autocontenção:** script completo com geração de dados contendo atraso nulo (`np.concatenate`), treinamento com GRU e projeção unidimensional por PCA.

---

## 5. Auditoria de Neurociência e Citações Bibliográficas

Todas as referências históricas e afirmações biológicas foram confrontadas com a literatura de referência:

1. **Dayan & Abbott (2001, *Theoretical Neuroscience*):** A equação diferencial de taxa neuronal de população $\tau \frac{d\mathbf{r}}{dt} = -\mathbf{r} + f(\mathbf{W}\mathbf{r} + \mathbf{I})$ é a pedra fundamental dos modelos contínuos corticais de taxa (*Wilson-Cowan e afins*).
2. **Elman (1990, *Cognitive Science*):** "Finding Structure in Time" é a referência clássica que introduziu o modelo SRN (*Simple Recurrent Network*), pioneiro no compartilhamento de pesos temporais.
3. **Hochreiter (1991, Diploma Thesis) e Bengio, Simard & Frasconi (1994, *IEEE TNN*):** Citação absolutamente precisa sobre a descoberta e demonstração formal do problema do gradiente que desaparece/explode em dependências de longo prazo.
4. **Fuster & Alexander (1971, *Science*) e Goldman-Rakic (1995, *Neuron*):** Os dois maiores marcos empíricos da atividade persistente durante períodos de atraso (*delayed response task*) em neurônios piramidais do córtex pré-frontal dorsolateral.
5. **Hochreiter & Schmidhuber (1997, *Neural Computation*):** Artigo seminal que introduziu a arquitetura LSTM e o carrossel de erro constante (*constant error carousel*).
6. **Cho et al. (2014, *EMNLP*):** Artigo canônico que formulou a GRU (*Gated Recurrent Unit*).
7. **Mante, Sussillo, Shenoy & Newsome (2013, *Nature*) e Sussillo & Barak (2013, *Neural Computation*):** Os trabalhos seminais modernos que estabeleceram o paradigma de treinar RNNs em tarefas comportamentais de decisão sensorial e identificar variedades atratoras e pontos fixos no espaço de estados populacional.
8. **Parâmetros fisiológicos adotados:** Constantes de tempo corticais ($\tau \approx 10\text{--}20\text{ ms}$), taxas de disparo típicas de neurônios piramidais ($10\text{--}60\text{ Hz}$), amostragem de LFP ($100\text{ Hz}$), épocas de EEG sujeitas a artefatos musculares e janelas temporais de $250\text{ ms}$ a $2\text{ s}$ refletem parâmetros experimentais realistas de neurofisiologia.

---

## 6. Verificação dos Critérios Editoriais e Pedagógicos

| Critério | Requisito do Contrato | Avaliação na Aula |
|---|---|---|
| **Público-alvo** | Alunos de Biologia, base matemática elementar, sem experiência prévia em DL | **Excelente.** A analogia da fita métrica/esteira para o estado da célula, a conexão explícita com a equação de Euler de biofísica e o cuidado de explicar formas de tensores no PyTorch tornam a aula plenamente acessível e rigorosa. |
| **Identificadores Delta** | Únicos, formato `sec:9-3-S`, `def:9-3-nome`, `prop:9-3-nome`, `exm:9-3-nome`, `exr:9-3-S-k` | **100% conforme.** Todos os IDs seguem o padrão prescrito sem acentos ou caracteres especiais. |
| **Ambientes e tags Delta** | Proibido `<interactive>`, `<cite>`, `<bibliography>`; `<intuition>` apenas como filha de resultados | **100% conforme.** Nenhuma tag proibida foi utilizada. Os blocos `<intuition>` aparecem exclusivamente no interior de `<definition>`. |
| **Figuras locais** | Máximo 3, SVG existente, gerado por script Python em `fig/` | **100% conforme.** A figura `fig/t03-gradiente-bptt.svg` possui script gerador autocontido `fig/t03-gradiente-bptt.py` e arquivo SVG leve e válido. |
| **Exercícios** | 3 a 5 por subtema, títulos graduados, com `<hint>` e `<solution>` recolhida | **100% conforme.** Exatamente 3 exercícios por subtema (total de 12), graduados em Básico, Intermediário e Avançado, todos com dica e solução recolhida por padrão. |
| **Exemplo biológico por seção** | Pelo menos um por subtema | **100% conforme.** Todos os subtemas contam com exemplos aplicados a dinâmica de disparo cortical, registros de EEG/LFP, memória de trabalho no córtex pré-frontal ou integração de evidência sensorial. |
| **Consistência de notação** | Vetores minúsculos em negrito ($\mathbf{x}$), matrizes maiúsculas em negrito ($\mathbf{W}$), conjuntos ($\mathbb{R}$) | **100% conforme.** A notação é rigorosa e consistente em toda a aula. |
| **Extensão** | 3.500 a 5.000 palavras de prosa | **100% conforme.** A aula possui aproximadamente 4.100 palavras de prosa. |

---

## 7. Conclusão

A aula está integralmente apta para publicação no ecossistema Delta. O texto sintetiza teoria matemática, modelagem computacional e neurobiologia comportamental com rara elegância e precisão. Recomenda-se a aprovação imediata do arquivo, restando ao autor a incorporação facultativa das pequenas notas de detalhamento pedagógico sugeridas na Tabela da Seção 2.