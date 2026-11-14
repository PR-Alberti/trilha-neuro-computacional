# Relatório de Revisão Técnica — Módulo 02 · Tema 01 (Limite)

- **Arquivo revisado:** [tema-01.dlt](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt)
- **Documentos de referência:** [PADRAO-AULAS.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/PADRAO-AULAS.md) e [DELTA-COLA.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/DELTA-COLA.md)
- **Scripts de figura analisados:** [epsilon-delta.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/fig/epsilon-delta.py), [michaelis-menten.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/fig/michaelis-menten.py) e [degrau.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/fig/degrau.py)
- **Data da revisão:** 14 de novembro de 2026
- **Perfil do revisor:** Matemático, Neurocientista Computacional e Professor de Alunos de Ciências Biológicas

---

## 1. Veredito

**CORRIGIR**

A aula apresenta uma redação de altíssima qualidade técnica, clareza pedagógica e rigor conceitual. O texto conduz com sensibilidade o estudante de Biologia pela transição do pré-cálculo para o cálculo infinitesimal, as demonstrações matemáticas são formalmente sólidas e acessíveis, **todas as contas foram refeitas e estão 100% corretas (zero erros matemáticos)**, e todas as afirmações de neurociência e biofísica estão ancoradas na literatura padrão de livro-texto (Hodgkin–Huxley, Dayan & Abbott, Kandel, Hille, Johnston & Wu). A sintaxe Delta v0.6.0 está impecável e os scripts geradores de figuras em Python produzem exatamente os SVGs necessários.

O veredito de **CORRIGIR** decorre de um descumprimento estrutural objetivo do contrato editorial definido em [PADRAO-AULAS.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/PADRAO-AULAS.md):
> *"Pelo menos 2 `<example>` resolvidos passo a passo, e pelo menos 1 com contexto biológico realista: potencial de repouso ≈ −70 mV, disparo de 0–200 Hz, TR do fMRI ≈ 2 s etc."*

Na **Seção 2 (`sec:2-1-2`)**, ambos os exemplos resolvidos em `<example>` ([exm:2-1-ed-linear](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L223-L234) e [exm:2-1-ed-quadratica](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L236-L251)) são puramente matemáticos e desprovidos de contexto biológico (embora haja uma analogia com bomba de perfusão na introdução da seção e um bioensaio no exercício `exr:2-1-2-2`). A correção necessária é pontual, simples e não disruptiva: basta contextualizar o `exm:2-1-ed-linear` como um modelo biológico linear (por exemplo, a resposta de fluorescência de um biosensor $F(x) = 3x + 1$), preservando estritamente os coeficientes numéricos ($a = 2$, $L = 7$, $\varepsilon = 0{,}6$, $\delta = 0{,}2$) para manter a correspondência exata com a [Figura 2.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L219-L221) e seu script [epsilon-delta.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/fig/epsilon-delta.py).

Foram adicionadas à tabela abaixo mais 3 observações pontuais de polimento pedagógico e formatação para facilitar a aprovação definitiva na próxima iteração.

---

## 2. Tabela de Problemas e Observações

| Severidade | Local | Trecho | Correção sugerida |
|---|---|---|---|
| **Pedagógico** | Seção 2 (`sec:2-1-2`), `exm:2-1-ed-linear` (linhas ~223-234) e `exm:2-1-ed-quadratica` (linhas ~236-251) | `<example id="exm:2-1-ed-linear"><title>Prova $\varepsilon$-$\delta$ para uma função linear</title>Prove pela definição formal que $\lim_{x \to 2} (3x + 1) = 7$...</example>` e `<example id="exm:2-1-ed-quadratica">...$\lim_{x \to 3} x^2 = 9$...</example>` | A seção descumpre o requisito de [PADRAO-AULAS.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/PADRAO-AULAS.md) ("pelo menos 1 `<example>` com contexto biológico realista"), pois ambos os exemplos são puramente abstratos. Recomenda-se contextualizar o `exm:2-1-ed-linear` com um cenário biológico concreto: por exemplo, a curva de calibração linear de um biosensor ou fotômetro óptico $F(x) = 3x + 1$ (onde $x$ é a concentração de ligante em $\mu\text{M}$ e $F$ é a emissão em u.a.). Ao manter a expressão $3x + 1$, o centro $a = 2$, o alvo $L = 7$ e a tolerância $\varepsilon = 0{,}6$, toda a demonstração formal é preservada sem necessidade de alterar a [Figura 2.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L219-L221) nem o script Python. |
| **Pedagógico** | Seção 2 (`sec:2-1-2`), `fig:2-1-epsilon-delta`, linha ~220 (legenda) e linhas ~217-218 (texto) | `<caption>Ilustração da definição $\varepsilon$-$\delta$ para $\lim_{x \to 2}(3x + 1) = 7$ com $\varepsilon = 0{,}6$ e $\delta = \varepsilon/3 = 0{,}2$. Qualquer $x \ne 2$ na faixa $(1{,}8;\; 2{,}2)$ produz $f(x)$ dentro da faixa $(6{,}4;\; 7{,}6)$.</caption>` | No gráfico SVG gerado por [epsilon-delta.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/fig/epsilon-delta.py#L58-L59), o ponto $(a, L) = (2, 7)$ é plotado com uma bolinha aberta (vazia). Embora o script tenha o comentário explicativo `# Ponto (a, L) aberto para destacar que x != a na definição`, estudantes iniciantes de Biologia podem inferir erroneamente que $f(x) = 3x + 1$ possui uma descontinuidade ou "buraco" em $x = 2$ (como no `exm:2-1-buraco`). Sugere-se incluir uma oração na legenda ou na prosa esclarecendo: `(o ponto $(2, 7)$ é representado com círculo aberto apenas para enfatizar que a definição formal considera exclusivamente $x \ne 2$, e não por descontinuidade da reta)`. |
| **Formato** | Seção 6 (`sec:2-1-6`), `thm:2-1-sen-x-sobre-x`, linha ~811 e ~817 | `e $T = (1, \tan x)$ a interseção da semirreta $OP$...` e `Área de $\triangle OAT = \dfrac{1}{2} \cdot 1 \cdot \tan x = \dfrac{\operatorname{sen} x}{2\cos x}$.` | O texto utiliza rigorosamente o padrão em português `\operatorname{sen}` em toda a aula, mas para a tangente adotou o comando em inglês `\tan`. Para manter uniformidade absoluta na notação em português conforme [PADRAO-AULAS.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/PADRAO-AULAS.md), sugere-se usar `\operatorname{tg}` (`\operatorname{tg} x`) ou explicitar a equivalência internacional `\tan x = \operatorname{tg} x` na primeira ocorrência. |
| **Pedagógico** | Seção 4 (`sec:2-1-4`), `sub:2-1-4-continuidade`, linha ~570 | `todos os polinômios, as exponenciais $e^x$ e $a^x$ ($a > 0$), as funções $\operatorname{sen}(x)$ e $\cos(x)$, bem como o sigmoide logístico...` | A lista de funções contínuas cita seno e cosseno, mas não menciona a tangente nem quocientes trigonométricos. Como a continuidade do cosseno e a razão de quocientes são usadas logo adiante na prova do Teorema do Sanduíche (Subtema 6), sugere-se acrescentar uma breve observação: `bem como quocientes como $\tan(x) = \operatorname{sen}(x)/\cos(x)$ em todos os pontos onde $\cos(x) \ne 0$`. |

---

## 3. Análise Detalhada dos Critérios Editoriais e Pedagógicos

### 3.1 Cobertura dos subtemas obrigatórios
A aula cobre com profundidade e rigor todos os subtemas previstos no guia (`referencias/Guia.txt`) e na ordem exata:
1. **Introdução** ([sec:2-1-1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L40-L179)): Intuição física e biológica através da velocidade instantânea do potencial de ação ($\Delta V / \Delta t$), definição intuitiva formalizada em [def:2-1-limite-intuitivo](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L49-L57), tabela numérica de aproximação bilateral e independência entre o valor limite $L$ e a existência de $f(a)$.
2. **Definição formal ($\varepsilon$-$\delta$)** ([sec:2-1-2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L181-L310)): Formalização rigorosa em [def:2-1-epsilon-delta](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L192-L205), teorema de unicidade do limite ([thm:2-1-unicidade](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L209-L215)), suporte gráfico completo via [fig:2-1-epsilon-delta](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L219-L221) e exemplos resolvidos passo a passo para funções lineares e quadráticas.
3. **Propriedades operatórias e limites no infinito** ([sec:2-1-3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L312-L484)): Demonstração em `<proof>` da propriedade da soma via desigualdade triangular; tratamento algébrico de indeterminações $0/0$ por fatoração e racionalização; limites no infinito ($1/x^r \to 0$), limites infinitos e assíntotas verticais/horizontais em [sub:2-1-3-infinito](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L348-L355); modelo biológico de saturação enzimática de Michaelis–Menten em [exm:2-1-michaelis-menten](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L378-L401) com gráfico [fig:2-1-michaelis-menten](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L403-L405).
4. **Limites laterais e continuidade** ([sec:2-1-4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L486-L641)): Definição formal de limites laterais ([def:2-1-limites-laterais](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L495-L501)), equivalência com o limite bilateral ([thm:2-1-laterais-bilateral](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L503-L507)), modelo de disparo tudo-ou-nada como função degrau de Heaviside em [exm:2-1-heaviside](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L509-L527) com [fig:2-1-degrau](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L529-L531); definição precisa de continuidade em um ponto ([def:2-1-continuidade](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L560-L568)) e classificação completa das descontinuidades (removível, de salto e infinita).
5. **Limites de funções compostas** ([sec:2-1-5](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L643-L772)): Teorema da composta ([thm:2-1-composta](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L652-L660)) com destaque indispensável para a hipótese de continuidade da função externa $f$ em $L$; contraexemplo instrutivo com a função degrau; aplicações a potenciais de relaxamento e taxas de disparo com curva sigmoide.
6. **Teorema do Sanduíche/Confronto** ([sec:2-1-6](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L774-L928)): Enunciado e demonstração formal com $\varepsilon$-$\delta$ em [thm:2-1-sanduiche](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L783-L801); dedução geométrica clássica completa do limite fundamental $\lim_{x \to 0} \frac{\operatorname{sen} x}{x} = 1$ no círculo unitário em [thm:2-1-sen-x-sobre-x](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L805-L826); aplicações a oscilações amortecidas neurais e ressonância sub-limiar de membrana.
7. **Fechamento**: Seção "Resumo" ([sec:2-1-resumo](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L930-L941)) com 7 itens objetivos contendo as fórmulas-chave; e seção "Para ir além" ([sec:2-1-alem](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L943-L953)) integrando os materiais do módulo (Guidorizzi, Anton e Stewart) e preparando o gancho para o Tema 2.2 (Derivada).

### 3.2 Exercícios, dicas e soluções
A aula conta com **18 exercícios** (exatamente 3 por seção), cumprindo à risca todas as diretrizes de [PADRAO-AULAS.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/PADRAO-AULAS.md):
- Títulos rigorosamente graduados em "Básico", "Intermediário" e "Avançado";
- **100% dos exercícios possuem `<hint>`** com orientações conceituais que destravam o estudante sem entregar o resultado;
- **100% dos exercícios possuem `<solution collapsible="true" collapsed="true">`**, todas com raciocínio analítico completo, passos algébricos explícitos e interpretação contextual, e não apenas o número final;
- Pelo menos um exercício de cada seção traz aplicação realista à biologia ou à neurociência:
  - Subtema 1: `exr:2-1-1-3` (taxa instantânea de proliferação bacteriana);
  - Subtema 2: `exr:2-1-2-2` (precisão de pipetagem em bioensaio de fluorescência);
  - Subtema 3: `exr:2-1-3-3` (condutância e saturação de receptores pós-sinápticos);
  - Subtema 4: `exr:2-1-4-3` (corrente iônica de sódio: abertura abrupta vs. suave com curva sigmoide);
  - Subtema 5: `exr:2-1-5-3` (relaxamento pós-inibitório e curva de Boltzmann de abertura de canais);
  - Subtema 6: `exr:2-1-6-3` (ressonância elétrica sub-limiar de membrana e envoltórias de amortecimento).

### 3.3 Exemplos biológicos por seção
- **Seção 1 (`sec:2-1-1`):** Cumprido. [exm:2-1-taxa-potencial](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L87-L116) modela a taxa instantânea de subida do potencial de membrana neuronal ($V(t) = -70 + 5t^2\text{ mV}$) em janelas de tempo decrescentes perto de $t = 2\text{ ms}$, antecipando a derivada.
- **Seção 2 (`sec:2-1-2`):** **Não cumprido nos blocos `<example>`.** Ambos os exemplos são puramente abstratos ($3x + 1$ e $x^2$). Embora a abertura traga uma analogia qualitativa com bomba de perfusão e o exercício intermediário aplique a um ensaio biológico, [PADRAO-AULAS.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/PADRAO-AULAS.md) exige pelo menos um `<example>` resolvido com contexto biológico realista em cada seção.
- **Seção 3 (`sec:2-1-3`):** Cumprido. [exm:2-1-michaelis-menten](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L378-L401) aborda a saturação enzimática e captação de neurotransmissores com parâmetros realistas ($V_{\max} = 120\;\mu\text{mol/(L}\cdot\text{min)}$, $K_m = 2{,}0\text{ mmol/L}$) e interpretação física da assíntota horizontal.
- **Seção 4 (`sec:2-1-4`):** Cumprido. [exm:2-1-heaviside](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L509-L527) formaliza o limiar de disparo neuronal tudo-ou-nada ($V_{\text{lim}} = -55\text{ mV}$) com o degrau de Heaviside e neurônios de McCulloch–Pitts.
- **Seção 5 (`sec:2-1-5`):** Cumprido. [exm:2-1-taxa-estacionaria](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L696-L711) modela o relaxamento do potencial de membrana ($\tau = 10\text{ ms}$) encadeado com uma curva sigmoide de taxa de disparo em Hz.
- **Seção 6 (`sec:2-1-6`):** Cumprido. [exm:2-1-adaptacao-amortecida](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L842-L855) analisa a adaptação da taxa de disparo com retroalimentação negativa e oscilação amortecida ($r(t) = 30 + 20\,e^{-t/50}\cos(0{,}2\,t)\text{ Hz}$).

### 3.4 Rigor das afirmações de neurociência e biofísica
Todas as afirmações de neurociência são rigorosamente de livro-texto (Dayan & Abbott; Kandel et al.; Hille; Gerstner et al.):
- Potenciais de repouso ($-70\text{ mV}$), limiares de despolarização ($-55\text{ mV}$) e potenciais de reversão de Nernst para sódio ($E_{\text{Na}} = +55\text{ mV}$) são os valores biofísicos canônicos;
- A relação entre condutância, força eletromotriz e corrente iônica ($I = g(V - E)$) está com unidades físicas perfeitamente consistentes: $\text{nS} \times \text{mV} = (10^{-9}\text{ S}) \times (10^{-3}\text{ V}) = 10^{-12}\text{ A} = 1\text{ pA}$, com convenção fisiológica correta (corrente negativa representando influxo de cátions $\text{Na}^+$ na célula);
- As curvas sigmoides logísticas e de ativação de Boltzmann estão de acordo com a biofísica de canais iônicos dependentes de voltagem;
- A ressonância elétrica sub-limiar em neurônios piramidais e oscilações theta/beta amortecidas em torno do repouso reproduzem a literatura consolidada (Hutcheon & Yarom, 2000; Izhikevich, 2007).

### 3.5 Progressão didática e pré-requisitos
- O encadeamento conceitual é exemplar: parte da intuição geométrica e numérica, passa pelo rigor métrico do $\varepsilon$-$\delta$, desenvolve a álgebra operatória e assintótica, introduz os limites laterais para construir a definição de continuidade e culmina na composta e no aperto.
- Nenhum conceito de módulos futuros é empregado sem aviso. A única antecipação ocorre no Subtema 1, onde o termo "funções contínuas" é mencionado no comentário [rem:2-1-armadilha-subst](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L118-L124), mas com o aviso explícito e imediato: `"(que veremos no Subtema 4)"`, em estrita observância a [PADRAO-AULAS.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/PADRAO-AULAS.md).

### 3.6 Código Python e scripts de figura
- **Blocos de código no corpo da aula:** Não há blocos `<code lang="python">` no texto de `tema-01.dlt`. Isso está perfeitamente correto: o Módulo 2 é de Cálculo Real puro, e a regra 3 de [PADRAO-AULAS.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/PADRAO-AULAS.md) restringe blocos de código executáveis aos módulos 6, 8 e 9 (e trechos dos módulos 4, 5 e 7).
- **Scripts geradores de figura:** Foram auditados os 3 scripts em `conteudo/modulo-02/fig/`:
  1. [epsilon-delta.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/fig/epsilon-delta.py): define `plt.rcParams["svg.fonttype"] = "none"`, fundo transparente, eixos e rótulos em português, e salva `epsilon-delta.svg` reproduzindo com exatidão a faixa $7{,}0 \pm 0{,}6$ e $2{,}0 \pm 0{,}2$;
  2. [michaelis-menten.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/fig/michaelis-menten.py): plota a curva hiperbólica $v([S]) = 120\,[S]/(2{,}0 + [S])$, assíntota horizontal $V_{\max} = 120$ e o ponto de meia ativação $(K_m, V_{\max}/2) = (2{,}0;\; 60)$, gerando `michaelis-menten.svg`;
  3. [degrau.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/fig/degrau.py): plota a função degrau em $V_{\text{lim}} = -55\text{ mV}$ com círculo aberto em $(-55, 0)$ e círculo fechado em $(-55, 1)$, gerando `degrau.svg`.
  Todos os scripts rodam de forma autocontida sem erros e produzem arquivos SVG válidos e leves que correspondem integralmente ao texto.

### 3.7 Notação, estilo e extensão
- **Idioma e tom:** Português do Brasil com tratamento em segunda pessoa ("você"), tom convidativo e matematicamente rigoroso;
- **Termos em inglês:** Todos apresentados em itálico entre parênteses na primeira ocorrência (*horizontal asymptote*, *vertical asymptote*, *removable discontinuity*, *jump discontinuity*, *infinite discontinuity*, *squeeze theorem*);
- **Formatação numérica:** Uso correto de vírgula na prosa e em fórmulas LaTeX com chaves de escape ($0{,}5$, $0{,}05$, $73{,}1\text{ Hz}$ etc.);
- **Extensão:** O documento possui aproximadamente 4.100 palavras, situando-se perfeitamente na faixa estipulada de 2.500 a 5.000 palavras para um tema com 6 subtemas.

---

## 4. Auditoria e Recálculo Passo a Passo de Todas as Contas

Todas as contas dos exemplos resolvidos, tabelas e soluções dos 18 exercícios foram refeitas passo a passo:

### 4.1 Subtema 1: Introdução (`sec:2-1-1`)
1. **[Exemplo 2.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L59-L85) (`exm:2-1-buraco`):**
   - $f(x) = \dfrac{x^2 - 1}{x - 1} = x + 1$ para $x \ne 1$.
   - Tabela `tbl:2-1-buraco`:
     - $x = 0{,}9 \implies f(0{,}9) = 1{,}9$; $x = 1{,}1 \implies f(1{,}1) = 2{,}1$;
     - $x = 0{,}99 \implies f(0{,}99) = 1{,}99$; $x = 1{,}01 \implies f(1{,}01) = 2{,}01$;
     - $x = 0{,}999 \implies f(0{,}999) = 1{,}999$; $x = 1{,}001 \implies f(1{,}001) = 2{,}001$.
   - $\lim_{x \to 1} f(x) = 1 + 1 = 2$. **Correto.**
2. **[Exemplo 2.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L87-L116) (`exm:2-1-taxa-potencial`):**
   - $V(t) = -70 + 5t^2$. Em $t = 2$: $V(2) = -70 + 5(4) = -50\text{ mV}$.
   - $m(t) = \dfrac{V(t) - V(2)}{t - 2} = \dfrac{5t^2 - 20}{t - 2} = \dfrac{5(t - 2)(t + 2)}{t - 2} = 5(t + 2)$ para $t \ne 2$.
   - Tabela `tbl:2-1-taxa-potencial`:
     - $t = 1{,}5$: $V(1{,}5) = -70 + 5(2{,}25) = -58{,}75\text{ mV}$; $m(1{,}5) = 5(3{,}5) = 17{,}5\text{ mV/ms}$. Conferência: $\frac{-58{,}75 - (-50)}{1{,}5 - 2} = \frac{-8{,}75}{-0{,}5} = 17{,}5$. **Correto.**
     - $t = 1{,}9$: $V(1{,}9) = -70 + 5(3{,}61) = -51{,}95\text{ mV}$; $m(1{,}9) = 5(3{,}9) = 19{,}5\text{ mV/ms}$. Conferência: $\frac{-1{,}95}{-0{,}1} = 19{,}5$. **Correto.**
     - $t = 1{,}99$: $V(1{,}99) = -70 + 5(3{,}9601) = -50{,}1995\text{ mV}$; $m(1{,}99) = 5(3{,}99) = 19{,}95\text{ mV/ms}$. Conferência: $\frac{-0{,}1995}{-0{,}01} = 19{,}95$. **Correto.**
     - $t = 2{,}01$: $V(2{,}01) = -70 + 5(4{,}0401) = -49{,}7995\text{ mV}$; $m(2{,}01) = 5(4{,}01) = 20{,}05\text{ mV/ms}$. Conferência: $\frac{0{,}2005}{0{,}01} = 20{,}05$. **Correto.**
     - $t = 2{,}1$: $V(2{,}1) = -70 + 5(4{,}41) = -47{,}95\text{ mV}$; $m(2{,}1) = 5(4{,}1) = 20{,}5\text{ mV/ms}$. Conferência: $\frac{2{,}05}{0{,}1} = 20{,}5$. **Correto.**
     - $t = 2{,}5$: $V(2{,}5) = -70 + 5(6{,}25) = -38{,}75\text{ mV}$; $m(2{,}5) = 5(4{,}5) = 22{,}5\text{ mV/ms}$. Conferência: $\frac{11{,}25}{0{,}5} = 22{,}5$. **Correto.**
   - $\lim_{t \to 2} m(t) = 5(2 + 2) = 20\text{ mV/ms}$. **Correto.**
3. **[Exercício 2.1.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L126-L140) (`exr:2-1-1-1`):**
   - $f(x) = \dfrac{x^2 - 9}{x - 3} = x + 3$ para $x \ne 3$.
   - $f(2{,}9) = 5{,}9$; $f(2{,}99) = 5{,}99$; $f(3{,}01) = 6{,}01$; $f(3{,}1) = 6{,}1$.
   - Limite: $\lim_{x \to 3} f(x) = 3 + 3 = 6$. **Correto.**
4. **[Exercício 2.1.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L142-L153) (`exr:2-1-1-2`):**
   - $h(x) = 2x + 3$ para $x \ne 4$; $h(4) = 0$.
   - Limite quando $x \to 4$: $2(4) + 3 = 11$. $h(4) = 0 \ne 11$. **Correto.**
5. **[Exercício 2.1.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L155-L178) (`exr:2-1-1-3`):**
   - $N(t) = 100 + 20t^2$. Em $t = 3$: $N(3) = 100 + 20(9) = 280$ células.
   - $r(t) = \dfrac{(100 + 20t^2) - 280}{t - 3} = \dfrac{20(t^2 - 9)}{t - 3} = 20(t + 3)$ para $t \ne 3$.
   - $r(2{,}9) = 20(5{,}9) = 118\text{ células/h}$; $r(3{,}1) = 20(6{,}1) = 122\text{ células/h}$.
   - $\lim_{t \to 3} r(t) = 20(3 + 3) = 120\text{ células/h}$. **Correto.**

### 4.2 Subtema 2: Definição formal (`sec:2-1-2`)
1. **[Exemplo 2.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L223-L234) (`exm:2-1-ed-linear`):**
   - $|f(x) - L| = |(3x + 1) - 7| = |3x - 6| = 3|x - 2| < \varepsilon \iff |x - 2| < \varepsilon / 3$.
   - Escolha $\delta = \varepsilon / 3$. Para $\varepsilon = 0{,}6 \implies \delta = 0{,}2$. Prova formal correta. **Correto.**
2. **[Exemplo 2.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L236-L251) (`exm:2-1-ed-quadratica`):**
   - $|x^2 - 9| = |x - 3|\,|x + 3|$. Com $\delta \le 1$, $|x - 3| < 1 \implies 2 < x < 4 \implies 5 < x + 3 < 7 \implies |x + 3| < 7$.
   - $|x^2 - 9| < 7|x - 3| < \varepsilon \iff |x - 3| < \varepsilon / 7$.
   - Escolha $\delta = \min(1,\, \varepsilon/7)$. Prova formal rigorosa. **Correto.**
3. **[Exercício 2.2.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L261-L280) (`exr:2-1-2-1`):**
   - $|(5x - 2) - 13| = 5|x - 3| < 0{,}05 \implies |x - 3| < 0{,}01$. Logo $\delta = 0{,}01$.
   - Fórmula geral: $\delta = \varepsilon / 5$. **Correto.**
4. **[Exercício 2.2.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L283-L294) (`exr:2-1-2-2`):**
   - $F(c) = 4c + 20$. Alvo em $c_0 = 5$: $F(5) = 40$.
   - $|(4c + 20) - 40| = 4|c - 5| < 0{,}2 \implies |c - 5| < 0{,}05\;\mu\text{M}$.
   - Intervalo: $(5 - 0{,}05;\; 5 + 0{,}05) = (4{,}95;\; 5{,}05)\;\mu\text{M}$. **Correto.**
5. **[Exercício 2.2.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L296-L309) (`exr:2-1-2-3`):**
   - $|x^2 - 16| = |x - 4|\,|x + 4|$. Para $\delta \le 1$, $|x - 4| < 1 \implies 3 < x < 5 \implies 7 < x + 4 < 9 \implies |x + 4| < 9$.
   - $\delta = \min(1,\, \varepsilon / 9)$.
   - Para $\varepsilon = 0{,}18$: $\delta = \min(1,\, 0{,}18 / 9) = \min(1,\, 0{,}02) = 0{,}02$. **Correto.**

### 4.3 Subtema 3: Propriedades (`sec:2-1-3`)
1. **[Exemplo 2.5](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L357-L376) (`exm:2-1-indet-fator-rac`):**
   - Item (a): $\lim_{x \to 2} \dfrac{x^2 - 5x + 6}{x - 2} = \lim_{x \to 2} \dfrac{(x - 2)(x - 3)}{x - 2} = 2 - 3 = -1$. **Correto.**
   - Item (b): $\dfrac{\sqrt{x + 9} - 3}{x} \cdot \dfrac{\sqrt{x + 9} + 3}{\sqrt{x + 9} + 3} = \dfrac{x}{x(\sqrt{x + 9} + 3)} = \dfrac{1}{\sqrt{x + 9} + 3} \to \dfrac{1}{3 + 3} = \dfrac{1}{6}$. **Correto.**
2. **[Exemplo 2.6](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L378-L401) (`exm:2-1-michaelis-menten`):**
   - $v([S]) = \dfrac{120\,[S]}{2{,}0 + [S]}$.
   - Item (a): $v(2{,}0) = \dfrac{120 \cdot 2{,}0}{4{,}0} = 60\;\mu\text{mol/(L}\cdot\text{min)} = \dfrac{V_{\max}}{2}$. **Correto.**
   - Item (b): $\lim_{[S] \to +\infty} \dfrac{120}{\dfrac{2{,}0}{[S]} + 1} = \dfrac{120}{0 + 1} = 120 = V_{\max}$. **Correto.**
3. **[Exercício 2.3.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L415-L433) (`exr:2-1-3-1`):**
   - Item (a): $2(-1)^3 - 4(-1) + 5 = -2 + 4 + 5 = 7$. **Correto.**
   - Item (b): $\lim_{x \to 5} \dfrac{x^2 - 25}{x - 5} = \lim_{x \to 5} (x + 5) = 10$. **Correto.**
4. **[Exercício 2.3.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L435-L455) (`exr:2-1-3-2`):**
   - Item (a): $\dfrac{\sqrt{x + 4} - 2}{x} = \dfrac{1}{\sqrt{x + 4} + 2} \to \dfrac{1}{2 + 2} = \dfrac{1}{4} = 0{,}25$. **Correto.**
   - Item (b): $\lim_{x \to +\infty} \dfrac{6 + 3/x}{2 + 5/x^2} = \dfrac{6}{2} = 3$. **Correto.**
5. **[Exercício 2.3.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L457-L482) (`exr:2-1-3-3`):**
   - Item (a): $g(0{,}5) = \dfrac{18 \cdot 0{,}5}{0{,}5 + 0{,}5} = \dfrac{9}{1} = 9\text{ nS} = \dfrac{g_{\max}}{2}$. **Correto.**
   - Item (b): $\lim_{[T] \to +\infty} \dfrac{18}{0{,}5/[T] + 1} = 18\text{ nS}$. **Correto.**
   - Item (c): $\lim_{[T] \to 0^+} \dfrac{g([T])}{[T]} = \lim_{[T] \to 0^+} \dfrac{18}{0{,}5 + [T]} = \dfrac{18}{0{,}5} = 36\text{ nS/(mmol/L)}$. **Correto.**

### 4.4 Subtema 4: Limites laterais (`sec:2-1-4`)
1. **[Exemplo 2.7](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L509-L527) (`exm:2-1-heaviside`):**
   - $y(V) = H(V + 55)$.
   - $\lim_{V \to -55^-} y(V) = 0$; $\lim_{V \to -55^+} y(V) = 1$.
   - Como $0 \ne 1$, o limite bilateral não existe. **Correto.**
2. **[Exemplo 2.8](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L533-L553) (`exm:2-1-modulo-partes`):**
   - Item (a): $\lim_{x \to 0^-} \frac{-x}{x} = -1$; $\lim_{x \to 0^+} \frac{x}{x} = 1 \implies$ não existe. **Correto.**
   - Item (b): $\lim_{x \to 2^-} (x^2 + 1) = 5$; $\lim_{x \to 2^+} (7 - x) = 5 \implies \lim_{x \to 2} g(x) = 5$. **Correto.**
3. **[Exercício 2.4.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L590-L604) (`exr:2-1-4-1`):**
   - $\lim_{x \to 3^-} (2x + 1) = 7$; $\lim_{x \to 3^+} (x^2 - 2) = 7 \implies \lim_{x \to 3} f(x) = 7$.
   - $f(3) = 10 \ne 7 \implies$ descontinuidade removível. **Correto.**
4. **[Exercício 2.4.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L606-L618) (`exr:2-1-4-2`):**
   - $\lim_{x \to 2^-} g(x) = 2k - 4$; $\lim_{x \to 2^+} g(x) = 4 + k$.
   - $2k - 4 = 4 + k \implies k = 8$. Conferência: $2(8) - 4 = 12$ e $4 + 8 = 12$. **Correto.**
5. **[Exercício 2.4.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L620-L639) (`exr:2-1-4-3`):**
   - Item (a): $\lim_{V \to -40^-} I(V) = 0\text{ pA}$; $\lim_{V \to -40^+} I(V) = 10(-40 - 55) = 10(-95) = -950\text{ pA}$. Descontinuidade de salto. **Correto.**
   - Item (b): $I_{\text{suave}}(-40) = \dfrac{10(-95)}{1 + e^0} = \dfrac{-950}{2} = -475\text{ pA}$. **Correto.**

### 4.5 Subtema 5: Limites de funções compostas (`sec:2-1-5`)
1. **[Exemplo 2.9](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L671-L694) (`exm:2-1-composta-algebrica`):**
   - Item (a): $\lim_{x \to 0} \operatorname{sen} x = 0 \implies e^0 = 1$. **Correto.**
   - Item (b): $\lim_{x \to 4} (x^2 + 9) = 25 \implies \sqrt{25} = 5$. **Correto.**
   - Item (c): $\lim_{x \to 1} \frac{x^2 - 1}{x - 1} = 2 \implies \sigma(2) = \frac{1}{1 + e^{-2}} \approx \frac{1}{1 + 0{,}135335} \approx 0{,}880797 \approx 0{,}881$. **Correto.**
2. **[Exemplo 2.10](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L696-L711) (`exm:2-1-taxa-estacionaria`):**
   - $\lim_{t \to +\infty} V(t) = -70 + 20(1 - 0) = -50\text{ mV}$.
   - $f(-50) = \dfrac{100}{1 + e^{-(-50 + 55)/5}} = \dfrac{100}{1 + e^{-1}}$.
   - Com $e^{-1} \approx 0{,}367879 \implies \frac{100}{1{,}367879} \approx 73{,}1058 \approx 73{,}1\text{ Hz}$. **Correto.**
3. **[Exercício 2.5.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L718-L738) (`exr:2-1-5-1`):**
   - Item (a): $\lim_{x \to 0} (x^2 + \pi) = \pi \implies \cos(\pi) = -1$. **Correto.**
   - Item (b): $\lim_{x \to 3} ((x + 3) - 5) = \lim_{x \to 3} (x - 2) = 1 \implies \ln(1) = 0$. **Correto.**
4. **[Exercício 2.5.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L740-L754) (`exr:2-1-5-2`):**
   - Para $x \ne 0$: $-x^2 < 0 \implies H(-x^2) = 0 \to 0 \ne H(0) = 1$.
   - Para $g_2(x) = x$: laterais $0$ e $1 \implies$ limite não existe. Violação de continuidade de $H$ em $0$. **Correto.**
5. **[Exercício 2.5.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L756-L771) (`exr:2-1-5-3`):**
   - $V_\infty = -80 + 10(1 - 0) = -70\text{ mV}$.
   - $P(-70) = \dfrac{1}{1 + e^0} = \dfrac{1}{2} = 0{,}5$ ($50\%$ dos canais abertos). **Correto.**

### 4.6 Subtema 6: Teorema do sanduíche/confronto (`sec:2-1-6`)
1. **[Teorema 2.6](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L805-L826) (`thm:2-1-sen-x-sobre-x`):**
   - $\triangle OAP = \frac{\operatorname{sen} x}{2} \le \text{setor } OAP = \frac{x}{2} \le \triangle OAT = \frac{\operatorname{sen} x}{2\cos x}$.
   - Multiplicação por $\frac{2}{\operatorname{sen} x} > 0 \implies 1 \le \frac{x}{\operatorname{sen} x} \le \frac{1}{\cos x} \implies \cos x \le \frac{\operatorname{sen} x}{x} \le 1$.
   - Paridade para $-\pi/2 < x < 0$. Como $\lim_{x \to 0} \cos x = 1 \implies \lim_{x \to 0} \frac{\operatorname{sen} x}{x} = 1$. Dedução rigorosa. **Correto.**
2. **[Exemplo 2.11](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L828-L840) (`exm:2-1-x2-sen`):**
   - $-1 \le \operatorname{sen}(1/x) \le 1 \implies -x^2 \le x^2\operatorname{sen}(1/x) \le x^2 \implies \lim = 0$. **Correto.**
3. **[Exemplo 2.12](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L842-L855) (`exm:2-1-adaptacao-amortecida`):**
   - $-20\,e^{-t/50} \le 20\,e^{-t/50}\cos(0{,}2\,t) \le 20\,e^{-t/50}$.
   - $30 - 20\,e^{-t/50} \le r(t) \le 30 + 20\,e^{-t/50}$. Como $e^{-t/50} \to 0 \implies \lim_{t \to +\infty} r(t) = 30\text{ Hz}$. **Correto.**
4. **[Exercício 2.6.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L865-L875) (`exr:2-1-6-1`):**
   - $-|x| \le |x|\cos(1/x) \le |x|$. Como $-|x| \to 0$ e $|x| \to 0 \implies \lim = 0$. **Correto.**
5. **[Exercício 2.6.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L877-L899) (`exr:2-1-6-2`):**
   - Item (a): $\lim_{x \to 0} 5 \cdot \dfrac{\operatorname{sen}(5x)}{5x} = 5(1) = 5$. **Correto.**
   - Item (b): $\dfrac{3 \cdot \frac{\operatorname{sen}(3x)}{3x}}{2 \cdot \frac{\operatorname{sen}(2x)}{2x}} \to \dfrac{3(1)}{2(1)} = \dfrac{3}{2} = 1{,}5$. **Correto.**
6. **[Exercício 2.6.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-01.dlt#L901-L927) (`exr:2-1-6-3`):**
   - Item (a): $g(t) = -70 - 8\,e^{-t/20}$, $h(t) = -70 + 8\,e^{-t/20}$, com $g(t) \le V(t) \le h(t)$. **Correto.**
   - Item (b): $\lim_{t \to +\infty} g(t) = \lim_{t \to +\infty} h(t) = -70\text{ mV} \implies \lim V(t) = -70\text{ mV}$. **Correto.**
   - Item (c): $t \ge 20\ln(4) \implies -t/20 \le -\ln(4) = \ln(1/4) \implies e^{-t/20} \le 0{,}25$.
     $|V(t) - (-70)| \le 8\,e^{-t/20} \le 8(0{,}25) = 2\text{ mV}$.
     Tempo numérico: $20\ln(4) = 20(1{,}386294) \approx 27{,}7\text{ ms}$. **Correto.**

---

## 5. Contas Conferidas

Abaixo listamos todos os identificadores de exemplos e exercícios cujas contas foram integralmente recalculadas e consideradas exatas:

- `exm:2-1-buraco`
- `exm:2-1-taxa-potencial`
- `exr:2-1-1-1`
- `exr:2-1-1-2`
- `exr:2-1-1-3`
- `exm:2-1-ed-linear`
- `exm:2-1-ed-quadratica`
- `exr:2-1-2-1`
- `exr:2-1-2-2`
- `exr:2-1-2-3`
- `exm:2-1-indet-fator-rac`
- `exm:2-1-michaelis-menten`
- `exr:2-1-3-1`
- `exr:2-1-3-2`
- `exr:2-1-3-3`
- `exm:2-1-heaviside`
- `exm:2-1-modulo-partes`
- `exr:2-1-4-1`
- `exr:2-1-4-2`
- `exr:2-1-4-3`
- `exm:2-1-composta-algebrica`
- `exm:2-1-taxa-estacionaria`
- `exr:2-1-5-1`
- `exr:2-1-5-2`
- `exr:2-1-5-3`
- `exm:2-1-x2-sen`
- `exm:2-1-adaptacao-amortecida`
- `exr:2-1-6-1`
- `exr:2-1-6-2`
- `exr:2-1-6-3`
