# Relatório de Revisão Técnica — Módulo 02 · Tema 03 (Integral de Riemann)

- **Arquivo revisado:** [tema-03.dlt](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-03.dlt)
- **Documentos de referência:** [PADRAO-AULAS.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/PADRAO-AULAS.md) e [DELTA-COLA.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/DELTA-COLA.md)
- **Scripts de figura analisados:** [somas-riemann.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/fig/somas-riemann.py) e [auc-farmaco.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/fig/auc-farmaco.py)
- **Data da revisão:** 14 de novembro de 2026
- **Perfil do revisor:** Matemático, Neurocientista Computacional e Professor de Alunos de Ciências Biológicas

---

## 1. Veredito

**CORRIGIR**

A aula [tema-03.dlt](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-03.dlt) é um trabalho de excelência pedagógica, técnica e conceitual. A transição do conceito de taxa instantânea (derivada) para acúmulo (integral) é conduzida de forma intuitiva e rigorosa, fechando com precisão o ciclo do Cálculo Real por meio do Teorema Fundamental do Cálculo. **Todas as contas dos 12 exemplos resolvidos, do bloco de código numérico e das soluções dos 18 exercícios foram integralmente refeitas e estão 100% corretas (zero erros matemáticos)**. Todas as formulações biológicas e neurofisiológicas (acúmulo de carga em canais sinápticos AMPA/NMDA em $\text{fC}$, farmacocinética de exposição $\text{AUC}$, resposta hemodinâmica BOLD do fMRI com amostragem por $\text{TR}$, ondas alfa de EEG e ativação *softplus* em redes neurais) apoiam-se na literatura canônica padrão (Dayan & Abbott; Kandel et al.; Guyton & Hall; Goodfellow et al.).

O veredito de **CORRIGIR** decorre exclusivamente de um erro de formato/marcação Delta na linha ~255 que quebra a resolução de referência cruzada, somado a pequenos ajustes pontuais de formatação e clareza pedagógica:
1. **Tag inexistente na sintaxe Delta (Formato):** Na linha ~255 ([sec:2-3-2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-03.dlt#L255)), utilizou-se a tag XML `<eqref>eq:2-3-estimativa</eqref>`. Conforme documentado em [DELTA-COLA.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/DELTA-COLA.md), o Delta v0.6.0 não possui tag `<eqref>` no corpo do texto (onde se exige `<ref to="id"/>`), reservando `\eqref{id}` apenas para o interior de fórmulas matemáticas KaTeX. Por isso, a referência cruzada não compila como link clicável com prévia. O ajuste é imediato: trocar por `(<ref to="eq:2-3-estimativa"/>)` (exatamente como o autor escreveu na linha ~532).
2. **Ambiguidade visual de cancelamento (Pedagógico):** No `exm:2-3-tfc-basico` (linha ~561), a passagem intermediária `(-cos \pi) - (-cos 0) = -(-1) - (-1) = 1 + 1 = 2` gera uma ilusão de ótica de cancelamento da forma $X - X = 0$ para iniciantes. Sugere-se explicitar com colchetes: `\Big(-(-1)\Big) - (-1) = 1 - (-1) = 1 + 1 = 2`.
3. **Meia-risca Unicode em modo texto KaTeX (Formato):** Na linha ~709, a expressão `$5\text{–}6\text{ s}$` traz a meia-risca literal `–` dentro de `\text{...}`, sujeita a avisos ou falhas de espaçamento em compiladores estritos. Padronizar para `$5\text{ a }6\text{ s}$` ou `$5\text{--}6\text{ s}$`.
4. **Vírgula decimal em mathtext no script de figura (Formato):** Em [auc-farmaco.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/fig/auc-farmaco.py#L53), a legenda `label="$C(t) = 10\\,e^{-0,2t}$"` carece de chaves na vírgula decimal (`-0{,}2t`), gerando espaçamento de pontuação indevido no SVG.
5. **Harmonização de caixas de armadilha (Pedagógico):** A Seção 5 é a única que não possui um `<remark>` destacado com "Armadilha comum", embora o texto aborde o erro típico de calcular áreas sem separar pelas raízes. Recomenda-se adicionar um `<remark>` para total simetria com as demais 5 seções.

São correções pontuais, cirúrgicas e que não exigem reescrita de conteúdo, permitindo aprovação imediata assim que aplicadas pelo autor.

---

## 2. Tabela de Problemas e Observações

| Severidade | Local | Trecho | Correção sugerida |
|---|---|---|---|
| **Formato** | Seção 2 (`sec:2-3-2`), linha ~255 | `Dividindo a desigualdade <eqref>eq:2-3-estimativa</eqref> por $b - a > 0$, obtemos...` | A tag `<eqref>` não existe no vocabulário de tags XML do Delta v0.6.0. Conforme [DELTA-COLA.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/DELTA-COLA.md), referências cruzadas na prosa usam estritamente `<ref to="id"/>` (o comando `\eqref{id}` existe apenas dentro de blocos matemáticos KaTeX). Com a tag incorreta, o compilador não gera o link clicável com prévia interativa (*popover*) nem o rótulo automático ("Equação 2.1"). Substituir por: `Dividindo a desigualdade (<ref to="eq:2-3-estimativa"/>) por $b - a > 0$, obtemos...`, padronizando com a linha ~532 da Seção 4. |
| **Pedagógico** | Seção 4 (`sec:2-3-4`), `exm:2-3-tfc-basico`, linha ~561 | `$$\int_0^{\pi} \operatorname{sen} x\,dx = \Big[-\cos x\Big]_0^{\pi} = (-\cos \pi) - (-\cos 0) = -(-1) - (-1) = 1 + 1 = 2.$$` | A conta está matematicamente exata (o primeiro termo é $-(-1) = 1$ e a subtração do segundo termo é $-(-1) = +1$). Porém, para estudantes de Biologia com base matemática em recuperação, a justaposição `-( -1 ) - ( -1 )` cria uma forte ilusão de ótica de cancelamento da forma $X - X = 0$ (o estudante lê impulsivamente $1 - 1 = 0$ e não entende de onde surgiu $1 + 1$). Recomenda-se separar claramente a operação de subtração dos sinais internos: `\Big(-\cos\pi\Big) - \Big(-\cos 0\Big) = \Big(-(-1)\Big) - (-1) = 1 - (-1) = 1 + 1 = 2`. |
| **Formato** | Seção 5 (`sec:2-3-5`), `exm:2-3-hrf-bold`, linha ~709 | `pico por volta de $5\text{–}6\text{ s}$ seguido de um pequeno vale...` | O uso de meia-risca Unicode literal `–` dentro do comando KaTeX `\text{...}` pode provocar avisos de compilação ou inconsistências de espaçamento dependendo da fonte carregada pelo navegador. Sugere-se substituir por `$5\text{ a }6\text{ s}$` ou pela convenção LaTeX `$5\text{--}6\text{ s}$`, exatamente como padronizado nas revisões anteriores do módulo. |
| **Formato** | Script de figura [auc-farmaco.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/fig/auc-farmaco.py), linha 53 | `ax.plot(t, c, color=cor_curva, linewidth=2.5, label="$C(t) = 10\\,e^{-0,2t}$")` | No renderizador mathtext do Matplotlib, a vírgula dentro de `$10\\,e^{-0,2t}$` é tratada como separador de argumentos (pontuação matemática), inserindo um espaçamento indesejado após a vírgula no gráfico (`-0, 2t`). Recomenda-se isolar a vírgula com chaves: `label="$C(t) = 10\\,e^{-0{,}2t}$"`. |
| **Pedagógico** | Seção 5 (`sec:2-3-5`), após `exm:2-3-hrf-bold`, linha ~728 | Ausência de bloco `<remark>` com título "Armadilha comum" | As Seções 1, 2, 3, 4 e 6 possuem caixas `<remark>` estruturadas de "Armadilha comum". Na Seção 5, a armadilha mais frequente dos alunos — integrar $f(x)$ diretamente sem separar nas raízes quando a função muda de sinal, obtendo área líquida em vez de área geométrica, ou subtrair curvas na ordem errada gerando área negativa — é tratada na prosa e no exercício `exr:2-3-5-1`, mas não em uma caixa destacada. Sugere-se incluir um `<remark id="rem:2-3-armadilha-areas"><title>Armadilha comum</title>Nunca calcule a área total integrando diretamente uma função que cruza o eixo $x$ sem antes encontrar suas raízes... Lembre-se: áreas geométricas são sempre não negativas.</remark>`. |
| **Pedagógico** | Seção 1 (`sec:2-3-1`) e Seção 6 (`sec:2-3-6`), linhas ~56-60 e ~792 | Termos em inglês ausentes na primeira menção | Conforme [PADRAO-AULAS.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/PADRAO-AULAS.md), termos técnicos devem apresentar a equivalência em inglês entre parênteses na primeira menção: em `def:2-3-soma-riemann` faltam os termos *left Riemann sum*, *right Riemann sum* e *midpoint rule*; em `thm:2-3-substituicao` falta *u-substitution* / *integration by substitution*; e em `def:2-3-primitiva` falta *antiderivative* (o autor incluiu com perfeição em AUC: *area under the curve*). |

---

## 3. Checklist de Conformidade Editorial e Pedagógica

| Critério avaliado | Status | Análise detalhada |
|---|:---:|---|
| **Dica e solução completa em cada exercício** | **OK** | Todos os 18 exercícios contêm `<hint><title>Ver dica</title>...</hint>` com pistas conceituais que orientam o raciocínio sem antecipar a resposta, e `<solution collapsible="true" collapsed="true">` com demonstração passo a passo, desenvolvimento algébrico explícito e interpretação biológica/física. |
| **Pelo menos um exemplo biológico por seção** | **OK** | **Seção 1:** [exm:2-3-carga-bold](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-03.dlt#L121-L141) calcula carga sináptica em $\text{fC}$ a partir de correntes em $\text{pA}$ e área sob sinal BOLD de fMRI ($\text{TR} = 2\text{ s}$).<br>**Seção 2:** [exm:2-3-prop-correntes](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-03.dlt#L264-L281) decompõe correntes sinápticas excitatórias AMPA e NMDA por linearidade e aditividade; [exm:2-3-prop-taxa-media](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-03.dlt#L283-L300) obtém taxa de disparo média em $\text{Hz}$ de neurônio cortical.<br>**Seção 3:** [exm:2-3-crescimento-populacao](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-03.dlt#L430-L451) reconstrói crescimento bacteriano e massa acumulada em infusão intravenosa contínua de anestésico.<br>**Seção 4:** [exm:2-3-corrente-sinaptica-tfc](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-03.dlt#L569-L589) calcula a carga acumulada de corrente sináptica exponencial $I(t) = I_0 e^{-t/\tau}$, carga assintótica total e conecta $dQ/dt = I(t)$ via TFC Parte 1.<br>**Seção 5:** [exm:2-3-auc-farmacocinetica](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-03.dlt#L685-L705) calcula a AUC farmacocinética em modelo monocompartimental de eliminação; [exm:2-3-hrf-bold](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-03.dlt#L707-L728) modela a resposta hemodinâmica do fMRI com amostragem discreta por $\text{TR} = 2\text{ s}$.<br>**Seção 6:** [exm:2-3-subst-ml-eeg](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-03.dlt#L838-L863) deduz a primitiva da sigmoide como função *softplus* (ativação suave em redes neurais) e calcula a integral de ciclo e meio ciclo de onda alfa de EEG ($10\text{ Hz}$, $50\;\mu\text{V}$). |
| **Afirmações de neurociência de livro-texto** | **OK** | Todas as grandezas fisiológicas estão perfeitamente calibradas com a literatura padrão (Dayan & Abbott; Kandel et al.): correntes sinápticas em picoamperes ($\text{pA}$), cargas elétricas em femtocoulombs ($1\text{ pA}\cdot\text{ms} = 1\text{ fC}$) e picocoulombs ($1\text{ nA}\cdot\text{ms} = 1\text{ pC}$), constantes de tempo de decaimento sináptico ($\tau = 5\text{ ms}$ e $10\text{ ms}$), resposta hemodinâmica com pico entre 5 e 6 segundos e vale pós-estímulo (*undershoot*), amostragem de fMRI em $\text{TR} = 2\text{ s}$, e oscilações alfa de EEG a $10\text{ Hz}$ com amplitude na faixa de dezenas de microvolts. Nenhuma citação inventada. |
| **Sequenciamento de conceitos (sem anacronismos)** | **OK** | A cadeia lógica é exemplar: aproximação discreta por retângulos $\to$ limite da soma de Riemann $\to$ propriedades algébricas e valor médio $\to$ problema inverso da taxa (primitiva) $\to$ Teorema Fundamental do Cálculo unificando diferenciação e integração $\to$ cálculo de áreas com mudança de sinal e entre curvas $\to$ mudança de variável desfazendo a regra da cadeia. Conexões com módulos posteriores (integrais múltiplas no Módulo 3, programação no Módulo 6 e probabilidade contínua no Módulo 7) são devidamente contextualizadas com avisos prévios. |
| **Código Python e comentários de saída** | **OK** | O bloco opcional [cod:2-3-riemann](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-03.dlt#L150-L175) é autocontido, roda perfeitamente em Python 3 com NumPy e as saídas comentadas (`n=4`, `n=10`, `n=100`, `n=1000` para soma à esquerda, direita e ponto médio) coincidem estritamente até a 6ª casa decimal com os cálculos analíticos e numéricos. |
| **Scripts de figura e fidelidade gráfica** | **OK** | Os dois scripts ([somas-riemann.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/fig/somas-riemann.py) e [auc-farmaco.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/fig/auc-farmaco.py)) usam `plt.rcParams['svg.fonttype'] = 'none'`, produzem SVGs leves e com fundo transparente. Os valores plotados ($E_4 = 1{,}75$, $D_4 = 3{,}75$, valor exato $8/3 \approx 2{,}67$, $\text{AUC}(0, 10) \approx 43{,}23$, $\text{AUC}_{\text{total}} = 50$) são idênticos aos do texto e das legendas. |
| **Consistência de notação matemática** | **OK** | Uso rigoroso de vírgula decimal na prosa e KaTeX com escape de chaves ($0{,}5$, $1{,}75$, $2{,}67$, $43{,}23$), ponto decimal em Python, intervalos formatados com ponto e vírgula ($[0{,}5;\; 1{,}5]$), e unidades físicas padronizadas em `\text{...}` ($\text{pA}$, $\text{fC}$, $\text{pC}$, $\text{ms}$, $\text{s}$, $\text{Hz}$, $\text{mg/L}$, $\text{h}$, $\mu\text{V}$, $\text{cm/s}$, $\text{cm}$). |
| **Cobertura de todos os subtemas solicitados** | **OK** | Cobre integralmente os 6 subtemas da ementa oficial: `sec:2-3-1` (Introdução, somas de Riemann com figura, $Q = \int I\,dt$), `sec:2-3-2` (Propriedades operatórias e valor médio), `sec:2-3-3` (Primitiva e tabela imediata), `sec:2-3-4` (TFC Partes 1 e 2), `sec:2-3-5` (Cálculo de áreas, AUC farmacocinética e HRF BOLD) e `sec:2-3-6` (Mudança de variável). |
| **Tamanho da aula** | **OK** | A aula contém aproximadamente 4.050 palavras no corpo textual (excluindo tags XML), situando-se perfeitamente na faixa estipulada de 2.500 a 5.000 palavras para aulas completas com 6 subtemas. |
| **Conformidade técnica Delta v0.6.0** | **ATENÇÃO** | O documento respeita quase todas as regras duras (XML estrito, `<chapter id="tema-2-3">` único, atributos com valor, `<intuition>` apenas como filho de definição/teorema/proposição), mas apresenta uma **tag não suportada** `<eqref>` na linha ~255 que precisa ser corrigida para `<ref to="...">`. |

---

## 4. Auditoria e Recálculo Passo a Passo das Contas

Todas as contas foram refeitas manualmente de forma independente. Como **não houve divergência em nenhum item**, apresenta-se a confirmação analítica estruturada por seção:

### 4.1 Subtema 1 — Introdução (`sec:2-3-1`)
- **Texto introdutório (linha 47):** Corrente constante de $50\text{ pA}$ por $4\text{ ms}$:
  $$Q = I \cdot \Delta t = 50\text{ pA} \cdot 4\text{ ms} = 200\text{ pA}\cdot\text{ms} = 200 \times 10^{-12}\text{ A} \times 10^{-3}\text{ s} = 200 \times 10^{-15}\text{ C} = 200\text{ fC}. \quad \text{[Correto]}$$
- **Exemplo [exm:2-3-riemann-x2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-03.dlt#L89-L119):** $f(x) = x^2$ em $[0, 2]$, $n = 4 \implies \Delta x = 0{,}5$.
  - Extremos esquerdos $\{0;\; 0{,}5;\; 1{,}0;\; 1{,}5\}$:
    $$E_4 = (0 + 0{,}25 + 1{,}0 + 2{,}25) \cdot 0{,}5 = 3{,}5 \cdot 0{,}5 = 1{,}75. \quad \text{[Correto]}$$
  - Extremos direitos $\{0{,}5;\; 1{,}0;\; 1{,}5;\; 2{,}0\}$:
    $$D_4 = (0{,}25 + 1{,}0 + 2{,}25 + 4{,}0) \cdot 0{,}5 = 7{,}5 \cdot 0{,}5 = 3{,}75. \quad \text{[Correto]}$$
  - Pontos médios $\{0{,}25;\; 0{,}75;\; 1{,}25;\; 1{,}75\}$:
    $$M_4 = (0{,}0625 + 0{,}5625 + 1{,}5625 + 3{,}0625) \cdot 0{,}5 = 5{,}25 \cdot 0{,}5 = 2{,}625. \quad \text{[Correto]}$$
  - Limite com somatório de quadrados:
    $$D_n = \sum_{i=1}^n \left(\frac{2i}{n}\right)^2 \frac{2}{n} = \frac{8}{n^3} \frac{n(n+1)(2n+1)}{6} = \frac{4}{3}\left(1 + \frac{1}{n}\right)\left(2 + \frac{1}{n}\right) \xrightarrow{n \to \infty} \frac{8}{3} \approx 2{,}666667. \quad \text{[Correto]}$$
- **Exemplo [exm:2-3-carga-bold](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-03.dlt#L121-L141):**
  - Item (a): $E_5 = (0 + 80 + 60 + 35 + 15) \cdot 2 = 190 \cdot 2 = 380\text{ fC}$; $D_5 = (80 + 60 + 35 + 15 + 5) \cdot 2 = 195 \cdot 2 = 390\text{ fC}$. $\text{[Correto]}$
  - Item (b): $E_6 = (0{,}0 + 0{,}4 + 1{,}2 + 1{,}5 + 0{,}8 + 0{,}1) \cdot 2 = 4{,}0 \cdot 2 = 8{,}0\%\cdot\text{s}$; $D_6 = (0{,}4 + 1{,}2 + 1{,}5 + 0{,}8 + 0{,}1 - 0{,}2) \cdot 2 = 3{,}8 \cdot 2 = 7{,}6\%\cdot\text{s}$. $\text{[Correto]}$
- **Código Python [cod:2-3-riemann](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-03.dlt#L150-L175):** Saídas exatas para $n \in \{4, 10, 100, 1000\}$ coincidem rigorosamente com os comentários (ex.: para $n = 10$, $E_{10} = 2{,}280000$, $D_{10} = 3{,}080000$, $M_{10} = 2{,}660000$). $\text{[Correto]}$
- **Exercício [exr:2-3-1-1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-03.dlt#L177-L190):** $f(x) = 2x + 1$ em $[1, 3]$, $\Delta x = 0{,}5$. $E_4 = (3 + 4 + 5 + 6) \cdot 0{,}5 = 9$; $D_4 = (4 + 5 + 6 + 7) \cdot 0{,}5 = 11$; $M_4 = (3{,}5 + 4{,}5 + 5{,}5 + 6{,}5) \cdot 0{,}5 = 10$. Área do trapézio: $\frac{3 + 7}{2} \cdot 2 = 10$. $\text{[Correto]}$
- **Exercício [exr:2-3-1-2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-03.dlt#L192-L203):** $D_n = \sum_{i=1}^n \left(\frac{3i}{n}\right)\frac{3}{n} = \frac{9}{n^2}\frac{n(n+1)}{2} = \frac{9}{2}(1 + 1/n) \to 4{,}5$. Área do triângulo: $\frac{3 \cdot 3}{2} = 4{,}5$. $\text{[Correto]}$
- **Exercício [exr:2-3-1-3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-03.dlt#L205-L223):** $\Delta t = 2\text{ ms}$. $E_4 = (0 + 60 + 20 - 30) \cdot 2 = 100\text{ fC}$; $D_4 = (60 + 20 - 30 - 10) \cdot 2 = 80\text{ fC}$. $\text{[Correto]}$

### 4.2 Subtema 2 — Propriedades (`sec:2-3-2`)
- **Exemplo [exm:2-3-prop-correntes](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-03.dlt#L264-L281):**
  - Item (a): $2(120) + 80 = 240 + 80 = 320\text{ fC}$. $\text{[Correto]}$
  - Item (b): $\int_{20}^{50} = 410 - 320 = 90\text{ fC}$. $\text{[Correto]}$
- **Exemplo [exm:2-3-prop-taxa-media](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-03.dlt#L283-L300):**
  - Item (a): $r_{\text{méd}} = \frac{30}{0{,}5} = 60\text{ Hz}$. $\text{[Correto]}$
  - Item (b): $20 \cdot 1{,}0 \le \int \le 45 \cdot 1{,}0 \implies 20 \le \int_{0{,}5}^{1{,}5} r(t)\,dt \le 45\text{ disparos}$. $\text{[Correto]}$
- **Remark [rem:2-3-produto](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-03.dlt#L302-L307):** $\int_0^1 x\,dx = 1/2$; $\int_0^1 x^2\,dx = 1/3 \ne (1/2)(1/2) = 1/4$. $\text{[Correto]}$
- **Exercício [exr:2-3-2-1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-03.dlt#L309-L325):**
  - (a) $3(6) - 2(5) = 18 - 10 = 8$. $\text{[Correto]}$
  - (b) $6 + (-2) = 4$. $\text{[Correto]}$
  - (c) $-4$. $\text{[Correto]}$
- **Exercício [exr:2-3-2-2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-03.dlt#L327-L340):** $0 \le x \le 1 \implies 1 \le 1 + x^3 \le 2 \implies 1 \le \sqrt{1 + x^3} \le \sqrt{2}$. Com $b - a = 1$, $1 \le \int_0^1 \sqrt{1+x^3}\,dx \le \sqrt{2}$ e $f_{\text{méd}} \in [1, \sqrt{2}]$. $\text{[Correto]}$
- **Exercício [exr:2-3-2-3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-03.dlt#L342-L354):** $\int_0^{0{,}5} r(t)\,dt = 80 \cdot 0{,}5 = 40$; total em $[0, 2] = 40 + 35 = 75$ disparos; $r_{\text{méd}} = 75 / 2{,}0 = 37{,}5\text{ Hz}$. $\text{[Correto]}$

### 4.3 Subtema 3 — Primitiva (`sec:2-3-3`)
- **Exemplo [exm:2-3-primitiva-tabela](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-03.dlt#L409-L428):**
  - Item (a): $\int (6x^2 - 4x^{1/2} + 3/x)\,dx = 2x^3 - \frac{8}{3}x^{3/2} + 3\ln x + C$. Derivação confere termo a termo. $\text{[Correto]}$
  - Item (b): $\int (5e^{-2t} + 4\cos t)\,dt = -\frac{5}{2}e^{-2t} + 4\operatorname{sen} t + C$. Derivação confere. $\text{[Correto]}$
- **Exemplo [exm:2-3-crescimento-populacao](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-03.dlt#L430-L451):**
  - Item (a): $N(t) = \frac{100}{0{,}2}e^{0{,}2t} + C = 500e^{0{,}2t} + C$; $N(0) = 500 + C = 700 \implies C = 200$. $N(t) = 500e^{0{,}2t} + 200$. $\text{[Correto]}$
  - Item (b): $m(t) = 12t - 0{,}3t^2 + C$; $m(0) = 5 \implies C = 5$. $m(10) = 5 + 120 - 30 = 95\text{ mg}$. $\text{[Correto]}$
- **Exercício [exr:2-3-3-1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-03.dlt#L461-L478):**
  - (a) $x^4 - 3x^2 + 5x + C$. $\text{[Correto]}$
  - (b) $\frac{3}{4}e^{4x} - 2\ln x - \cos x + C$. $\text{[Correto]}$
- **Exercício [exr:2-3-3-2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-03.dlt#L480-L493):** $f'(x) = x^{3/2} + x^{-1/2} \implies f(x) = \frac{2}{5}x^{5/2} + 2\sqrt{x} + C$; $f(1) = 2/5 + 2 + C = 4 \implies C = 8/5$. $\text{[Correto]}$
- **Exercício [exr:2-3-3-3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-03.dlt#L495-L507):** $s(t) = -12e^{-0{,}5t} + 2t + C$; $s(0) = -12 + C = 0 \implies C = 12$; $s(4) = 20 - 12e^{-2} \approx 20 - 12(0{,}135) = 18{,}38\text{ cm}$. $\text{[Correto]}$

### 4.4 Subtema 4 — Teorema Fundamental do Cálculo (`sec:2-3-4`)
- **Exemplo [exm:2-3-tfc-basico](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-03.dlt#L551-L567):**
  - Item (a): $[-\cos x]_0^\pi = (-\cos\pi) - (-\cos 0) = -(-1) - (-1) = 2$. $\text{[Correto]}$
  - Item (b): $F'(x) = \ln(x^2 + 1) \cdot (x^2)' = 2x\ln(x^2 + 1)$. $\text{[Correto]}$
- **Exemplo [exm:2-3-corrente-sinaptica-tfc](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-03.dlt#L569-L589):**
  - Item (a): $Q(T) = 500(1 - e^{-T/5})\text{ fC}$; $Q(5) = 500(1 - e^{-1}) \approx 500(1 - 0{,}368) = 316\text{ fC}$. $\text{[Correto]}$
  - Item (b): $Q_{\text{total}} = 500\text{ fC} = 0{,}5\text{ pC}$; $dQ/dT = I_0 e^{-T/\tau} = I(T)$. $\text{[Correto]}$
- **Exercício [exr:2-3-4-1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-03.dlt#L599-L617):**
  - (a) $[x^3 - x^2 + x]_1^3 = (27 - 9 + 3) - (1 - 1 + 1) = 21 - 1 = 20$. $\text{[Correto]}$
  - (b) $[e^x]_0^{\ln 3} = 3 - 1 = 2$. $\text{[Correto]}$
- **Exercício [exr:2-3-4-2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-03.dlt#L619-L629):** $g'(x) = \frac{1}{1 + (3x)^2} \cdot 3 = \frac{3}{1 + 9x^2}$; $g'(1) = \frac{3}{10} = 0{,}3$. $\text{[Correto]}$
- **Exercício [exr:2-3-4-3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-03.dlt#L631-L651):**
  - (a) $Q(T) = [800e^{-t/10}]_0^T = -800(1 - e^{-T/10})\text{ fC}$; $Q(10) \approx -800(0{,}632) = -505{,}6\text{ fC}$. $\text{[Correto]}$
  - (b) $Q_{\text{total}} = -800\text{ fC}$; $-800(1 - e^{-T/10}) = -400 \implies e^{-T/10} = 0{,}5 \implies T = 10\ln 2 \approx 6{,}93\text{ ms}$. $\text{[Correto]}$

### 4.5 Subtema 5 — Cálculo de áreas (`sec:2-3-5`)
- **Exemplo [exm:2-3-auc-farmacocinetica](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-03.dlt#L685-L705):**
  - Item (a): $\text{AUC}(0, T) = \frac{10}{0{,}2}(1 - e^{-0{,}2T}) = 50(1 - e^{-0{,}2T})$; para $T = 10\text{ h}$, $50(1 - e^{-2}) \approx 50(1 - 0{,}13534) = 43{,}233 \approx 43{,}23\text{ mg}\cdot\text{h/L}$. $\text{[Correto]}$
  - Item (b): $\text{AUC}_{\text{total}} = 50\text{ mg}\cdot\text{h/L}$. $\text{[Correto]}$
- **Exemplo [exm:2-3-hrf-bold](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-03.dlt#L707-L728):** $h(t) = t/3 - t^2/36$ em $[0, 12]$.
  - Item (a): $h(6) = 1$, $h'(6) = 0$, $h''(6) = -1/18 < 0$ (pico). Área exata: $[t^2/6 - t^3/108]_0^{12} = 24 - 16 = 8$. $\text{[Correto]}$
  - Item (b): $h(0) = 0$, $h(2) = 5/9$, $h(4) = 8/9$, $h(6) = 1$, $h(8) = 8/9$, $h(10) = 5/9$, $h(12) = 0$.
    $$E_6 = D_6 = \left(0 + \frac{5}{9} + \frac{8}{9} + 1 + \frac{8}{9} + \frac{5}{9}\right) \cdot 2 = \frac{35}{9} \cdot 2 = \frac{70}{9} \approx 7{,}778 \approx 7{,}78.$$
    Erro relativo: $\frac{8 - 70/9}{8} = \frac{2/9}{8} = \frac{1}{36} \approx 2{,}78\% < 3\%$. $\text{[Correto]}$
- **Exercício [exr:2-3-5-1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-03.dlt#L730-L742):** $f(x) = x^2 - 4$ em $[0, 3]$. Raiz $x = 2$. $\int_0^2 = 8/3 - 8 = -16/3$; $\int_2^3 = -3 - (-16/3) = 7/3$. Área total: $|-16/3| + 7/3 = 23/3 \approx 7{,}67$. Integral líquida: $-16/3 + 7/3 = -3$. $\text{[Correto]}$
- **Exercício [exr:2-3-5-2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-03.dlt#L744-L758):** Interseções: $4 - x^2 = x + 2 \implies x = -2$ e $x = 1$. Em $[-2, 1]$, $4 - x^2 \ge x + 2$.
  $$\int_{-2}^1 (2 - x - x^2)\,dx = \left[2x - \frac{x^2}{2} - \frac{x^3}{3}\right]_{-2}^1 = \frac{7}{6} - \left(-\frac{20}{6}\right) = \frac{27}{6} = \frac{9}{2} = 4{,}5. \quad \text{[Correto]}$$
- **Exercício [exr:2-3-5-3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-03.dlt#L760-L780):**
  - Item (a): $\text{AUC}_A = 12 / 0{,}3 = 40$; $\text{AUC}_B = 8 / 0{,}2 = 40\text{ mg}\cdot\text{h/L}$. $\text{[Correto]}$
  - Item (b): $12e^{-0{,}3t^*} = 8e^{-0{,}2t^*} \implies e^{0{,}1t^*} = 1{,}5 \implies t^* = 10\ln(1{,}5) \approx 4{,}05\text{ h}$. $\text{[Correto]}$

### 4.6 Subtema 6 — Mudança de variável (`sec:2-3-6`)
- **Exemplo [exm:2-3-subst-tecnica](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-03.dlt#L813-L836):**
  - Item (a): $u = x^2 \implies \int \cos u\,du = \operatorname{sen}(x^2) + C$. $\text{[Correto]}$
  - Item (b): $u = 1 + x^2$, limites $1$ a $2$: $\frac{1}{2}[\ln u]_1^2 = \frac{\ln 2}{2}$. $\text{[Correto]}$
  - Item (c): $u = -t/\tau \implies -\tau e^{-t/\tau} + C$. $\text{[Correto]}$
- **Exemplo [exm:2-3-subst-ml-eeg](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-03.dlt#L838-L863):**
  - Item (a): $u = 1 + e^x \implies \int \frac{1}{u}\,du = \ln(1 + e^x) + C = \operatorname{softplus}(x) + C$. Derivação confere $\sigma(x)$. $\text{[Correto]}$
  - Item (b): $u = 2\pi f t$. Ciclo $[0, 1/f] \implies \frac{A}{2\pi f}[-\cos u]_0^{2\pi} = 0$. Meio ciclo $[0, 1/(2f)] \implies \frac{A}{2\pi f}[-\cos u]_0^\pi = \frac{A}{\pi f}$. Para $A = 50\;\mu\text{V}$, $f = 10\text{ Hz} \implies \frac{5}{\pi} \approx 1{,}5915... \approx 1{,}59\;\mu\text{V}\cdot\text{s}$. $\text{[Correto]}$
- **Exercício [exr:2-3-6-1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-03.dlt#L870-L888):**
  - (a) $u = x^3 + 1 \implies \frac{(x^3 + 1)^5}{5} + C$. $\text{[Correto]}$
  - (b) $u = \operatorname{sen} x$, limites $0$ a $1 \implies [u^3/3]_0^1 = 1/3$. $\text{[Correto]}$
- **Exercício [exr:2-3-6-2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-03.dlt#L890-L898):** $u = x^2 + 5$, limites $5$ a $9$: $\frac{1}{2}\int_5^9 u^{-1/2}\,du = [\sqrt{u}]_5^9 = 3 - \sqrt{5} \approx 0{,}7639 \approx 0{,}764$. $\text{[Correto]}$
- **Exercício [exr:2-3-6-3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-03.dlt#L900-L918):** $u = 1 + e^{-(t - 3)}$, limites $1 + e^3$ a $1 + e^{-3}$: $[u^{-1}]_{1+e^3}^{1+e^{-3}} = \frac{1}{1 + e^{-3}} - \frac{1}{1 + e^3} = \frac{e^3 - 1}{e^3 + 1} \approx \frac{19{,}09}{21{,}09} \approx 0{,}90517 \approx 0{,}905$. Coincide com $\sigma(3) - \sigma(-3)$. $\text{[Correto]}$

---

## 5. Contas Conferidas

Lista completa dos identificadores de exemplos, blocos de código e exercícios cujas contas foram integralmente recalculadas e consideradas **100% corretas**:

- `exm:2-3-riemann-x2` (Somas de Riemann à esquerda, à direita, no ponto médio e limite exato de $\int_0^2 x^2\,dx$)
- `exm:2-3-carga-bold` (Carga sináptica em femtocoulombs e área percentual sob o sinal BOLD)
- `cod:2-3-riemann` (Simulação numérica NumPy em 4 resoluções com saídas coincidentes até a 6ª casa decimal)
- `exr:2-3-1-1` (Somas de Riemann para reta e área de trapézio)
- `exr:2-3-1-2` (Limite de somas à direita para $\int_0^3 x\,dx$ e área de triângulo)
- `exr:2-3-1-3` (Corrente sináptica bifásica e carga líquida acumulada)
- `exm:2-3-prop-correntes` (Linearidade e aditividade de correntes sinápticas AMPA e NMDA)
- `exm:2-3-prop-taxa-media` (Taxa de disparo média em Hz e cotas de monotonicidade)
- `rem:2-3-produto` (Contraexemplo da não-distributividade da integral em relação ao produto)
- `exr:2-3-2-1` (Propriedades operatórias de linearidade, aditividade e inversão de limites)
- `exr:2-3-2-2` (Estimativa de monotonicidade e valor médio de $\sqrt{1+x^3}$)
- `exr:2-3-2-3` (Taxa média ponderada por duração de janelas temporais compostas)
- `exm:2-3-primitiva-tabela` (Integrais indefinidas imediatas e conferência por diferenciação)
- `exm:2-3-crescimento-populacao` (Equações com taxa e condição inicial em cultura bacteriana e infusão de anestésico)
- `exr:2-3-3-1` (Primitivas elementares e testes por derivação)
- `exr:2-3-3-2` (Reescrita algébrica de potências fracionárias e determinação da constante inicial)
- `exr:2-3-3-3` (Integração de velocidade exponencial e distância percorrida em fuga de peixe)
- `exm:2-3-tfc-basico` (TFC Parte 2 em seno e TFC Parte 1 com regra da cadeia em limite quadrático)
- `exm:2-3-corrente-sinaptica-tfc` (Carga de decaimento sináptico exponencial, limite assintótico e taxa instantânea)
- `exr:2-3-4-1` (Integrais definidas diretas por polinômio e exponencial via TFC Parte 2)
- `exr:2-3-4-2` (Derivada de função acumuladora com argumento linear via TFC Parte 1)
- `exr:2-3-4-3` (Corrente inibitória negativa, carga assintótica e tempo de meia-carga com $\ln 2$)
- `exm:2-3-auc-farmacocinetica` (Área sob a curva de eliminação plasmática parcial e total)
- `exm:2-3-hrf-bold` (Resposta hemodinâmica BOLD: pico, concavidade, área analítica e aproximação por TR)
- `exr:2-3-5-1` (Área geométrica total vs. integral líquida com troca de sinal em $x^2 - 4$)
- `exr:2-3-5-2` (Área da região delimitada entre parábola e reta)
- `exr:2-3-5-3` (Comparação de bioequivalência por AUC entre formulações farmacocinéticas e ponto de cruze)
- `exm:2-3-subst-tecnica` (Substituições trigonométrica, racional com $\ln$ e exponencial)
- `exm:2-3-subst-ml-eeg` (Primitiva da sigmoide para ativação *softplus* e integrais de ciclo/meio ciclo em EEG)
- `exr:2-3-6-1` (Substituição polinomial e trigonométrica imediata com troca de limites)
- `exr:2-3-6-2` (Substituição com raiz no denominador e atualização de extremos de integração)
- `exr:2-3-6-3` (Variação de peso sináptico por derivada da sigmoide, substituição e conexão analítica)
