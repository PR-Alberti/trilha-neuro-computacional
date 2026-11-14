# Relatório de Revisão Técnica — Módulo 02 · Tema 02 (Derivada)

- **Arquivo revisado:** [tema-02.dlt](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-02.dlt)
- **Scripts de figura vinculados:** [secante-tangente.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/fig/secante-tangente.py) e [sintonia-derivada.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/fig/sintonia-derivada.py)
- **Documentos de referência:** [PADRAO-AULAS.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/PADRAO-AULAS.md) e [DELTA-COLA.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/DELTA-COLA.md)
- **Data da revisão:** 14 de novembro de 2026
- **Perfil do revisor:** Matemático, Neurocientista Computacional e Professor de Alunos de Ciências Biológicas

---

## 1. Veredito

**APROVAR**

A aula [tema-02.dlt](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-02.dlt) apresenta qualidade conceitual, didática e formal exemplar. Todos os 12 exemplos e os 18 exercícios tiveram suas contas integralmente refeitas e conferidas — nenhuma divergência matemática foi encontrada. A cobertura dos subtemas exigidos pelo programa é completa e aprofundada na dosagem correta para alunos de Biologia em transição para a neurociência quantitativa e o aprendizado de máquina. 

As formulações neurobiológicas e fisiológicas (modelo LIF, modelo Hodgkin-Huxley, curvas de sintonia gaussianas no córtex visual primário, cinética de Michaelis–Menten, cooperatividade de Hill, eletroencefalograma e lei de Boyle na respiração alveolar) fundamentam-se com exatidão na literatura canônica (Dayan & Abbott; Gerstner et al.; Kandel; Guyton & Hall). O bloco opcional em Python roda de forma limpa e suas saídas coincidem com os comentários, e os scripts de geração de figuras SVG são robustos, elegantes e fiéis ao texto.

Não há erros impeditivos. Foram identificadas apenas 4 observações de polimento cosmético/pedagógico na tabela abaixo para consideração do autor em futuras passadas de refinamento.

---

## 2. Tabela de Problemas e Observações

| Severidade | Local | Trecho | Correção sugerida |
|---|---|---|---|
| Formato | Abertura, linha ~27 | `em que $\tau \approx 10\text{–}20\text{ ms}$ é a constante` | Em compiladores KaTeX/LaTeX com suporte estrito de fontes, uma meia-risca Unicode literal `–` dentro de `\text{...}` pode ocasionalmente emitir avisos de fonte ou falha de espaçamento. Sugere-se usar a convenção em prosa `$\tau \approx 10\text{ a }20\text{ ms}$` ou `$\tau \approx 10\text{--}20\text{ ms}$`. |
| Pedagógico | Seção 1 (`sec:2-2-1`), `exm:2-2-bio-taxas`, linha ~113 | `seu vértice — a <strong>taxa máxima de crescimento</strong> — ocorre exatamente na metade da capacidade, $N = K/2$, onde $\dfrac{dN}{dt} = \dfrac{rK}{4}$.` | Para alunos de biologia com base algébrica enferrujada, explicitar a passagem aritmética intermediária $r(K/2)(1 - (K/2)/K) = r(K/2)(1/2) = rK/4$ evita que o leitor tenha de adivinhar de onde surgiu o denominador $4$. |
| Formato | Script de figura [secante-tangente.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/fig/secante-tangente.py), linhas 85 e 92 | `ax.annotate("$Q_1$(3,5; 12,25)", ...)` e `ax.annotate("$Q_2$(2,5; 6,25)", ...)` | Enquanto na linha 77 usou-se `"$P(2, 4)$"` totalmente dentro de mathtext, em $Q_1$ e $Q_2$ as coordenadas ficaram fora de `$...$`. Isso gera fontes mistas no SVG (serifada KaTeX para a letra e sem serifa padrão para os números). Sugere-se uniformizar: `"$Q_1(3{,}5;\, 12{,}25)$"` e `"$Q_2(2{,}5;\, 6{,}25)$"`. |
| Formato | Script de figura [sintonia-derivada.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/fig/sintonia-derivada.py), linhas 91, 98 e 105 | `Máximo (+2,43 Hz/°)` e `ylabel("$f'(\\theta)$ (Hz/$^\\circ$)")` | Há uma pequena oscilação entre o caractere Unicode de grau `°` nas anotações das curvas e a macro LaTeX `$^\circ$` no eixo y e no texto da aula (`\text{Hz}/^\circ`). Sugere-se padronizar tudo como `\text{Hz}/^\circ` ou `\mathrm{Hz}/^\circ` para consistência visual. |

---

## 3. Checklist de Conformidade Editorial e Pedagógica

| Critério avaliado | Status | Análise detalhada |
|---|:---:|---|
| **Dica e solução completa em cada exercício** | **OK** | Todos os 18 exercícios contêm `<hint><title>Ver dica</title>...</hint>` com orientação conceitual e `<solution collapsible="true" collapsed="true">` com raciocínio analítico, etapas algébricas e interpretação física/biológica. |
| **Pelo menos um exemplo biológico por seção** | **OK** | **Seção 1:** Leitura de $dV/dt$ no potencial de membrana, modelos exponencial ($dN/dt=rN$) e logístico ($dN/dt=rN(1-N/K)$), e parametrização do neurônio LIF.<br>**Seção 2:** Não-diferenciabilidade do disparo tudo-ou-nada (degrau $H$), função de ativação ReLU e curva taxa-corrente $f\text{-}I$ com limiar e saturação.<br>**Seção 3:** Cinética enzimática de Michaelis–Menten ($v([S])$), oscilações alfa de EEG ($10\text{ Hz}$), pico de corrente pós-sináptica excitatória (EPSC em função alfa) e cooperatividade da equação de Hill.<br>**Seção 4:** Cascata fisiológica estímulo $\to$ potencial $\to$ taxa, curva logística sigmoide, discriminação de orientação na curva de sintonia gaussiana do V1 e crescimento bacteriano.<br>**Seção 5:** Michaelis–Menten implícita, lei de Boyle nos alvéolos pulmonares e expansão volumétrica/superficial de corpo celular esférico.<br>**Seção 6:** Ponto de inflexão na logística e na sigmoide, dinâmica de potencial excitatório sub-limiar e ponto de inflexão nos flancos da sintonia gaussiana. |
| **Afirmações de neurociência de livro-texto** | **OK** | Valores biofísicos rigorosos: repouso $E_L \approx -70\text{ mV}$, limiar $V_{\text{lim}} \approx -55\text{ mV}$, constante de tempo $\tau = 20\text{ ms}$, resistência de entrada $40\text{–}50\text{ M}\Omega$, corrente de injeção $0{,}3\text{–}0{,}4\text{ nA}$, amplitude de EEG em dezenas de $\mu\text{V}$, frequências fisiológicas (alfa $10\text{ Hz}$, gama $40\text{ Hz}$). A discriminação ótima de estímulo nos flancos da sintonia gaussiana (onde $|f'(\theta)|$ é máximo e a informação de Fisher atinge o pico) é clássica de Dayan & Abbott (*Theoretical Neuroscience*, caps. 1 e 3). |
| **Sequenciamento de conceitos (sem anacronismos)** | **OK** | A progressão didática é impecável: taxa média e reta secante $\to$ limite da razão incremental e reta tangente $\to$ continuidade vs. derivabilidade (bicos e saltos) $\to$ regras operatórias básicas $\to$ regra da cadeia $\to$ derivação implícita $\to$ derivadas sucessivas e concavidade. Conexões com módulos futuros (redes neurais, *backpropagation*, cálculo multivariável e programação) são contextualizadas explicitamente como horizontes futuros. |
| **Código Python e comentários de saída** | **OK** | O bloco [cod:2-2-razao-inc](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-02.dlt#L121-L140) é autocontido, sintaticamente válido em Python 3 / NumPy e as saídas comentadas (`h = 0.100 \| razao = 4.100000 \| erro = 0.100000`, etc.) coincidem perfeitamente com a execução numérica. O texto esclarece que o código é meramente ilustrativo para apoiar a intuição do limite. |
| **Scripts de figura e fidelidade gráfica** | **OK** | Ambos os scripts ([secante-tangente.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/fig/secante-tangente.py) e [sintonia-derivada.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/fig/sintonia-derivada.py)) usam `plt.rcParams['svg.fonttype'] = 'none'`, geram SVGs leves com fundo transparente e cores harmônicas da paleta Tailwind/Delta. As coordenadas, inclinações e pontos de destaque correspondem estritamente aos textos e legendas da aula. |
| **Consistência de notação matemática** | **OK** | Vírgula decimal sistemática na prosa e nas fórmulas KaTeX ($0{,}5$, $1{,}5$, $0{,}7311$, $2{,}43$), ponto decimal em código Python, intervalos escritos com ponto e vírgula ($[0{,}2;\, 1{,}2]$) para evitar ambiguidade com decimais, e unidades físicas formatadas em `\text{...}` ($\text{mV}$, $\text{ms}$, $\text{Hz}$, $\text{nA}$, $\text{pA}$, $\mu\text{m}$). |
| **Cobertura de todos os subtemas solicitados** | **OK** | Contempla com exatidão todos os 6 subtemas do índice oficial: `sec:2-2-1` (Introdução, $dV/dt$, LIF, crescimento populacional), `sec:2-2-2` (Condições de derivabilidade, degrau, bicos), `sec:2-2-3` (Propriedades algébricas e funções elementares), `sec:2-2-4` (Regra da cadeia e *backpropagation*), `sec:2-2-5` (Derivação implícita e taxas relacionadas) e `sec:2-2-6` (Derivadas de ordem superior, concavidade e inflexão). |
| **Tamanho da aula** | **OK** | A aula contém aproximadamente 4.300 palavras, enquadrando-se perfeitamente na faixa estipulada de 2.500 a 5.000 palavras para aulas extensas com 6 subtemas. |
| **Conformidade técnica Delta v0.6.0** | **OK** | Uso estrito de XML, todos os atributos com valor (`collapsible="true" collapsed="true"`), `<intuition>` empregado estritamente como filho direto de resultados (`theorem`, `definition`), `<ref>` com links válidos e cabeçalho com metadados e link ao índice do guia. |

---

## 4. Contas Conferidas (Auditoria Integral)

Todas as contas foram refeitas manualmente de ponta a ponta. Como não houve divergência numérica em nenhum item, apresenta-se a relação completa das verificações executadas por seção:

### 4.1 Subtema 1: Introdução (`sec:2-2-1`)

1. **[Taxa média de abertura](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-02.dlt#L49):**
   - Variação de $-70\text{ mV}$ para $-55\text{ mV}$ em $5\text{ ms}$: $\frac{-55 - (-70)}{5 - 0} = \frac{15}{5} = 3\text{ mV/ms}$. **Correto.**
2. **[Exemplo 2.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-02.dlt#L70-L90) (`exm:2-2-derivada-def`):**
   - Item (a): $f'(x) = \lim_{h \to 0}\frac{(x+h)^2 - x^2}{h} = \lim_{h \to 0}(2x + h) = 2x$. Em $a = 2$, $f(2) = 4$, $f'(2) = 4$. Reta tangente: $y - 4 = 4(x - 2) \implies y = 4x - 4$. **Correto.**
   - Item (b): $g'(x) = \lim_{h \to 0}\frac{\frac{1}{x+h} - \frac{1}{x}}{h} = \lim_{h \to 0}\frac{-h}{h x(x+h)} = -\frac{1}{x^2}$. **Correto.**
3. **[Exemplo 2.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-02.dlt#L92-L117) (`exm:2-2-bio-taxas`):**
   - Item (a): $V(t) = -70 + 10t - t^2 \implies \frac{dV}{dt} = 10 - 2t$. Em $t = 2\text{ ms}$: $V(2) = -54\text{ mV}$, $V'(2) = 6\text{ mV/ms}$. Em $t = 5\text{ ms}$: $V'(5) = 0\text{ mV/ms}$, pico em $V(5) = -45\text{ mV}$. **Correto.**
   - Item (b): $N(t) = 100 \cdot 2^t$. Taxa média em $[0, 2] = \frac{400 - 100}{2} = 150\text{ cél/ger}$; em $[2, 4] = \frac{1\,600 - 400}{2} = 600\text{ cél/ger}$. Vértice do modelo logístico em $N = K/2$: $\left.\frac{dN}{dt}\right|_{K/2} = r\frac{K}{2}\left(1 - \frac{1}{2}\right) = \frac{rK}{4}$. **Correto.**
4. **[Código Python](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-02.dlt#L121-L140) (`cod:2-2-razao-inc`):**
   - $h = 0{,}1 \implies \frac{2{,}1^2 - 4}{0{,}1} = \frac{0{,}41}{0{,}1} = 4{,}1 \implies \text{erro} = 0{,}1$.
   - $h = 0{,}01 \implies \frac{2{,}01^2 - 4}{0{,}01} = \frac{0{,}0401}{0{,}01} = 4{,}01 \implies \text{erro} = 0{,}01$.
   - $h = 0{,}001 \implies \frac{2{,}001^2 - 4}{0{,}001} = \frac{0{,}004001}{0{,}001} = 4{,}001 \implies \text{erro} = 0{,}001$. **Correto.**
5. **[Exercício 2.2.1.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-02.dlt#L147-L160) (`exr:2-2-1-1`):**
   - $f(x) = 3x^2 - 4x + 1 \implies f(x+h) - f(x) = 6xh + 3h^2 - 4h \implies f'(x) = 6x - 4$.
   - Em $x = 1$: $f(1) = 0$, $f'(1) = 2$. Reta tangente: $y - 0 = 2(x - 1) \implies y = 2x - 2$. **Correto.**
6. **[Exercício 2.2.1.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-02.dlt#L161-L182) (`exr:2-2-1-2`):**
   - Termo $R \cdot I = 50\text{ M}\Omega \cdot 0{,}4\text{ nA} = 20\text{ mV}$.
   - Equilíbrio: $-(V_{\text{eq}} - (-70)) + 20 = 0 \implies V_{\text{eq}} = -50\text{ mV}$.
   - Taxa: $\frac{dV}{dt} = \frac{-50 - V}{20}\text{ mV/ms}$. Em $V = -65\text{ mV}$: $\frac{15}{20} = +0{,}75\text{ mV/ms}$; em $V = -45\text{ mV}$: $\frac{-5}{20} = -0{,}25\text{ mV/ms}$. **Correto.**
7. **[Exercício 2.2.1.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-02.dlt#L184-L202) (`exr:2-2-1-3`):**
   - Item (a): $\lim_{h \to 0}\frac{\sqrt{x+h} - \sqrt{x}}{h}\frac{\sqrt{x+h}+\sqrt{x}}{\sqrt{x+h}+\sqrt{x}} = \frac{1}{2\sqrt{x}}$.
   - Item (b): $K = 1\,000 \implies N_{\text{óptimo}} = 500$. Taxa máxima: $0{,}4 \cdot 500 \cdot 0{,}5 = 100\text{ cél/h}$.
   - Comparações: em $N = 200$, $0{,}4 \cdot 200 \cdot 0{,}8 = 64\text{ cél/h}$; em $N = 1\,000$, taxa nula. **Correto.**

### 4.2 Subtema 2: Condições de Derivabilidade (`sec:2-2-2`)

8. **[Teorema 2.2 e demonstração](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-02.dlt#L214-L227) (`thm:2-2-deriv-cont`):**
   - $\lim_{x \to a}[f(x) - f(a)] = \lim_{x \to a}\frac{f(x)-f(a)}{x-a}(x-a) = f'(a) \cdot 0 = 0 \implies \lim_{x \to a} f(x) = f(a)$. **Correto.**
9. **[Exemplo 2.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-02.dlt#L246-L265) (`exm:2-2-bico-vertical`):**
   - ReLU em $0$: $f'_-(0) = \lim_{h \to 0^-} \frac{0}{h} = 0$, $f'_+(0) = \lim_{h \to 0^+} \frac{h}{h} = 1 \implies 0 \ne 1$ (bico).
   - $x^{1/3}$ em $0$: $\lim_{h \to 0} \frac{h^{1/3}}{h} = \lim_{h \to 0}\frac{1}{h^{2/3}} = +\infty$ (tangente vertical). **Correto.**
10. **[Exemplo 2.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-02.dlt#L267-L280) (`exm:2-2-taxa-limiar`):**
    - $r(I) = \max(0, 50(I - 0{,}3))$. Continuidade em $0{,}3$: $\lim_{I \to 0{,}3} r(I) = 0 = r(0{,}3)$.
    - Derivadas laterais: $r'_-(0{,}3) = 0$, $r'_+(0{,}3) = 50\text{ Hz/nA} \implies$ não derivável. **Correto.**
11. **[Exercício 2.2.2.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-02.dlt#L286-L304) (`exr:2-2-2-1`):**
    - $|x - 2|$ em $2$: $f'_-(2) = -1$, $f'_+(2) = 1 \implies$ não derivável.
    - Degrau $H$ em $0$: $\lim_{x \to 0^-} H(x) = 0 \ne 1 = \lim_{x \to 0^+} H(x) \implies$ descontínua, logo não derivável. **Correto.**
12. **[Exercício 2.2.2.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-02.dlt#L306-L320) (`exr:2-2-2-2`):**
    - Continuidade em $x = 1$: $1^2 + 1 = a(1) + b \implies a + b = 2$.
    - Igualdade das derivadas laterais: $f'_-(1) = 2(1) = 2$ e $f'_+(1) = a \implies a = 2$.
    - Substituição: $2 + b = 2 \implies b = 0$. **Correto.**
13. **[Exercício 2.2.2.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-02.dlt#L322-L339) (`exr:2-2-2-3`):**
    - Transição $I = 0{,}2$: $r(0{,}2) = 0$, $r'_-(0{,}2) = 0$, $r'_+(0{,}2) = 80\text{ Hz/nA} \implies$ bico.
    - Transição $I = 1{,}2$: $r(1{,}2) = 80(1{,}0) = 80$, $r'_-(1{,}2) = 80$, $r'_+(1{,}2) = 0\text{ Hz/nA} \implies$ bico. **Correto.**

### 4.3 Subtema 3: Propriedades (`sec:2-2-3`)

14. **[Demonstração das propriedades e elementares](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-02.dlt#L361-L385) (`prop:2-2-regras-algebricas` e `prop:2-2-derivadas-elem`):**
    - Produto: $\lim_{h \to 0} [\frac{f(x+h)-f(x)}{h}g(x+h) + f(x)\frac{g(x+h)-g(x)}{h}] = f'(x)g(x) + f(x)g'(x)$.
    - Seno: $\operatorname{sen}(x+h) - \operatorname{sen} x = \operatorname{sen} x(\cos h - 1) + \cos x \operatorname{sen} h$. Com $\frac{\cos h - 1}{h} \to 0$ e $\frac{\operatorname{sen} h}{h} \to 1$, resulta $\cos x$. **Correto.**
15. **[Exemplo 2.5](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-02.dlt#L387-L404) (`exm:2-2-regras-calc`):**
    - Item (a): $f(x) = 3x^4 - 4x^{1/2} + 2x^{-3} \implies f'(x) = 12x^3 - 2x^{-1/2} - 6x^{-4} = 12x^3 - \frac{2}{\sqrt{x}} - \frac{6}{x^4}$. **Correto.**
    - Item (b): $g(x) = e^x \cos x \implies g'(x) = e^x \cos x + e^x(-\operatorname{sen} x) = e^x(\cos x - \operatorname{sen} x)$. **Correto.**
16. **[Exemplo 2.6](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-02.dlt#L406-L426) (`exm:2-2-mm-eeg`):**
    - Item (a): $v'([S]) = \frac{V_{\max}(K_m + [S]) - V_{\max}[S] \cdot 1}{(K_m + [S])^2} = \frac{V_{\max} K_m}{(K_m + [S])^2}$. **Correto.**
    - Item (b): $y(t) = 40 \operatorname{sen}(20\pi t) \implies y'(t) = 40 \cdot 20\pi \cos(20\pi t) = 800\pi \cos(20\pi t) \approx 2\,513{,}27 \cos(20\pi t)\;\mu\text{V/s}$. **Correto.**
17. **[Exercício 2.2.3.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-02.dlt#L439-L461) (`exr:2-2-3-1`):**
    - Item (a): $f'(x) = 15x^2 - 6(-1)x^{-2} + 8(1/3)x^{-2/3} = 15x^2 + \frac{6}{x^2} + \frac{8}{3\sqrt[3]{x^2}}$. **Correto.**
    - Item (b): $g'(x) = 2x\operatorname{sen} x + x^2\cos x$. **Correto.**
    - Item (c): $h'(x) = \frac{(1/x)\cdot x - (\ln x)\cdot 1}{x^2} = \frac{1 - \ln x}{x^2}$. **Correto.**
18. **[Exercício 2.2.3.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-02.dlt#L463-L475) (`exr:2-2-3-2`):**
    - $I'(t) = \frac{50 e^t - 50t e^t}{e^{2t}} = \frac{50(1 - t)}{e^t}$.
    - Pico em $1 - t = 0 \implies t = 1\text{ ms}$. Valor: $I(1) = \frac{50}{e} \approx \frac{50}{2{,}71828} \approx 18{,}39\text{ pA}$. **Correto.**
19. **[Exercício 2.2.3.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-02.dlt#L477-L495) (`exr:2-2-3-3`):**
    - $\frac{d\theta}{d[L]} = \frac{n[L]^{n-1}(K + [L]^n) - [L]^n n[L]^{n-1}}{(K + [L]^n)^2} = \frac{n K [L]^{n-1}}{(K + [L]^n)^2}$.
    - Com $n = 2$, $K = 4\text{ mM}^2$, $[L] = 2\text{ mM}$: $\frac{2 \cdot 4 \cdot 2^{1}}{(4 + 4)^2} = \frac{16}{64} = 0{,}25\text{ mM}^{-1}$. **Correto.**

### 4.4 Subtema 4: Regra da Cadeia (`sec:2-2-4`)

20. **[Exemplo 2.7](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-02.dlt#L520-L544) (`exm:2-2-cadeia-est-sig`):**
    - Item (a): $\frac{dr}{dI} = \frac{dr}{dV}\frac{dV}{dI} = (2{,}5\text{ Hz/mV}) \cdot (40\text{ mV/nA}) = 100\text{ Hz/nA}$. **Correto.**
    - Item (b): $\sigma'(x) = -(1 + e^{-x})^{-2}(-e^{-x}) = \frac{1}{1 + e^{-x}}\frac{e^{-x}}{1 + e^{-x}} = \sigma(x)(1 - \sigma(x))$.
    - No ponto médio $x = 0$: $\sigma(0) = 0{,}5 \implies \sigma'(0) = 0{,}5(1 - 0{,}5) = 0{,}25$. Máximo quadrático comprovado por $1/4 - (p - 1/2)^2 \le 1/4$. **Correto.**
21. **[Exemplo 2.8](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-02.dlt#L546-L564) (`exm:2-2-sintonia-gaussiana`):**
    - $f(\theta) = 80 \exp(-(\theta - 90)^2 / (2 \cdot 400)) \implies f'(\theta) = -\frac{\theta - 90}{400} f(\theta)$.
    - Em $\theta = 90^\circ$: $f'(90^\circ) = 0$.
    - Em $\theta = 70^\circ$: $f(70^\circ) = 80 e^{-0{,}5} \approx 48{,}52\text{ Hz}$; $f'(70^\circ) = -\frac{-20}{400} \cdot 48{,}52 = 4 e^{-0{,}5} \approx +2{,}43\text{ Hz}/^\circ$.
    - Em $\theta = 110^\circ$: $f'(110^\circ) = -4 e^{-0{,}5} \approx -2{,}43\text{ Hz}/^\circ$. **Correto.**
22. **[Exercício 2.2.4.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-02.dlt#L584-L606) (`exr:2-2-4-1`):**
    - Item (a): $f(x) = (2x+5)^4 \implies 4(2x+5)^3 \cdot 2 = 8(2x+5)^3$. **Correto.**
    - Item (b): $g(x) = e^{-3x^2} \implies e^{-3x^2}(-6x) = -6x e^{-3x^2}$. **Correto.**
    - Item (c): $h(t) = \cos(2\pi f t + \varphi) \implies -\operatorname{sen}(2\pi f t + \varphi) \cdot 2\pi f = -2\pi f \operatorname{sen}(2\pi f t + \varphi)$. **Correto.**
23. **[Exercício 2.2.4.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-02.dlt#L608-L627) (`exr:2-2-4-2`):**
    - Item (a): $\frac{d}{dx}\ln(x^2 + 4) = \frac{2x}{x^2 + 4}$. **Correto.**
    - Item (b): $\frac{d}{dx}(a^x) = e^{x \ln a}\ln a = a^x \ln a$.
    - Para $N(t) = 100 \cdot 2^t$ em $t = 3$: $N'(3) = 100 \cdot 2^3 \ln 2 = 800 \ln 2 \approx 800 \cdot 0{,}693147 \approx 554{,}5\text{ cél/ger}$. **Correto.**
24. **[Exercício 2.2.4.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-02.dlt#L629-L654) (`exr:2-2-4-3`):**
    - Item (a): $\frac{dy}{dw_1} = \frac{dy}{dz_2}\frac{dz_2}{da_1}\frac{da_1}{dz_1}\frac{dz_1}{dw_1} = y(1 - y) \cdot w_2 \cdot a_1(1 - a_1) \cdot x$.
    - Item (b): com $x = 2, w_1 = 0, w_2 = 2$: $z_1 = 0 \implies a_1 = 0{,}5 \implies a_1(1-a_1) = 0{,}25$.
    - $z_2 = 2(0{,}5) = 1 \implies y = \sigma(1) \approx 0{,}7311 \implies y(1-y) \approx 0{,}7311 \cdot 0{,}2689 \approx 0{,}1966$.
    - Produto: $0{,}1966 \cdot 2 \cdot 0{,}25 \cdot 2 = 0{,}1966 \cdot 1{,}0 = 0{,}1966$. **Correto.**

### 4.5 Subtema 5: Derivação Implícita (`sec:2-2-5`)

25. **[Demonstração das inversas](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-02.dlt#L668-L684) (`prop:2-2-inversas`):**
    - $\ln x$: $e^y = x \implies e^y y' = 1 \implies y' = 1/e^y = 1/x$.
    - $\arctan x$: $\tan y = x \implies (1 + \tan^2 y)y' = 1 \implies y' = \frac{1}{1 + x^2}$. **Correto.**
26. **[Exemplo 2.9](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-02.dlt#L686-L706) (`exm:2-2-circulo-mm`):**
    - Círculo: $2x + 2y y' = 0 \implies y' = -x/y$. Produto $m_{\text{tang}} \cdot m_{\text{raio}} = (-x/y)(y/x) = -1$ (perpendicularidade).
    - Michaelis–Menten: $v'(K_m + [S]) + v = V_{\max} \implies v' = \frac{V_{\max} - v}{K_m + [S]} = \frac{V_{\max} K_m}{(K_m + [S])^2}$. **Correto.**
27. **[Exemplo 2.10](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-02.dlt#L708-L729) (`exm:2-2-boyle-pulmao`):**
    - Item (a): $\frac{dP}{dV}V + P = 0 \implies \frac{dP}{dV} = -\frac{P}{V}$.
    - Item (b): $\frac{dP}{dt} = -\frac{P}{V}\frac{dV}{dt} = -\frac{100\text{ kPa}}{2{,}5\text{ L}} \cdot (0{,}5\text{ L/s}) = -40 \cdot 0{,}5 = -20\text{ kPa/s}$. **Correto.**
28. **[Exercício 2.2.5.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-02.dlt#L736-L748) (`exr:2-2-5-1`):**
    - $3x^2 + 3y^2 y' = 9y + 9x y' \implies y' = \frac{3y - x^2}{y^2 - 3x}$.
    - Ponto $(2, 4)$: $2^3 + 4^3 = 72 = 9(2)(4)$. Inclinação: $\frac{3(4) - 4}{16 - 3(2)} = \frac{8}{10} = 0{,}8$. **Correto.**
29. **[Exercício 2.2.5.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-02.dlt#L750-L762) (`exr:2-2-5-2`):**
    - $\operatorname{sen} y = x \implies \cos y y' = 1 \implies y' = \frac{1}{\cos y} = \frac{1}{\sqrt{1 - \operatorname{sen}^2 y}} = \frac{1}{\sqrt{1 - x^2}}$ (com $\cos y > 0$ em $(-\pi/2, \pi/2)$). **Correto.**
30. **[Exercício 2.2.5.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-02.dlt#L764-L786) (`exr:2-2-5-3`):**
    - Item (a): $\frac{dV}{dt} = 4\pi r^2 \frac{dr}{dt} \implies 36\pi = 4\pi(9)\frac{dr}{dt} \implies \frac{dr}{dt} = 1\;\mu\text{m/min}$.
    - Item (b): $\frac{dA}{dt} = 8\pi r \frac{dr}{dt} = 8\pi(3)(1) = 24\pi \approx 75{,}40\;\mu\text{m}^2/\text{min}$. **Correto.**

### 4.6 Subtema 6: Derivadas de Ordem Superior (`sec:2-2-6`)

31. **[Exemplo 2.11](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-02.dlt#L815-L833) (`exm:2-2-inflexao-logistica-sig`):**
    - Item (a): $\frac{d^2N}{dt^2} = r\left(1 - \frac{2N}{K}\right)\frac{dN}{dt} = 0 \iff N = K/2$. Troca de sinal comprovada.
    - Item (b): $\sigma''(x) = \sigma'(x)(1 - 2\sigma(x)) = 0 \iff \sigma(x) = 1/2 \iff x = 0$. Inflexão confirmada. **Correto.**
32. **[Exemplo 2.12](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-02.dlt#L835-L847) (`exm:2-2-segunda-derivada-potencial`):**
    - $V(t) = -70 + 9t^2 - 2t^3 \implies V'(t) = 18t - 6t^2 = 6t(3 - t)$, $V''(t) = 18 - 12t$.
    - Inflexão: $18 - 12t = 0 \implies t = 1{,}5\text{ ms}$, com $V'(1{,}5) = 18(1{,}5) - 6(2{,}25) = 27 - 13{,}5 = 13{,}5\text{ mV/ms}$.
    - Máximo: $V'(3) = 0$, $V''(3) = 18 - 36 = -18 < 0$, valor de pico $V(3) = -70 + 81 - 54 = -43\text{ mV}$. **Correto.**
33. **[Exercício 2.2.6.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-02.dlt#L854-L875) (`exr:2-2-6-1`):**
    - $f(x) = x^3 - 6x^2 + 9x + 2 \implies f'(x) = 3(x-1)(x-3)$, $f''(x) = 6x - 12$, $f'''(x) = 6$.
    - Pontos críticos: $x = 1 \implies f''(1) = -6 < 0$ (máximo local, $f(1) = 6$); $x = 3 \implies f''(3) = +6 > 0$ (mínimo local, $f(3) = 2$).
    - Inflexão: $6x - 12 = 0 \implies x = 2$ (com $f(2) = 4$), concavidade para baixo em $x < 2$ e para cima em $x > 2$. **Correto.**
34. **[Exercício 2.2.6.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-02.dlt#L877-L888) (`exr:2-2-6-2`):**
    - $f''(\theta) = -\frac{1}{\sigma^2}f(\theta) - \frac{\theta - \theta_{\text{pref}}}{\sigma^2}f'(\theta) = \frac{f(\theta)}{\sigma^2}\left[\frac{(\theta - \theta_{\text{pref}})^2}{\sigma^2} - 1\right]$.
    - Anulação: $(\theta - \theta_{\text{pref}})^2 = \sigma^2 \iff \theta = \theta_{\text{pref}} \pm \sigma$. Troca de sinal comprovada entre o interior e o exterior da faixa $\pm \sigma$. **Correto.**
35. **[Exercício 2.2.6.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-02.dlt#L890-L913) (`exr:2-2-6-3`):**
    - Item (a): $V'(t) = 12 - 6t\text{ mV/ms}$, $V''(t) = -6\text{ mV/ms}^2$.
    - Item (b): $12 - 6t = 0 \implies t = 2\text{ ms}$. Pico: $V(2) = -70 + 24 - 12 = -58\text{ mV}$ (abaixo do limiar de $-55\text{ mV}$).
    - Taxas nos extremos e centro: $V'(0) = +12\text{ mV/ms}$, $V'(2) = 0$, $V'(4) = -12\text{ mV/ms}$ com $V(4) = -70\text{ mV}$.
    - Item (c): concavidade estritamente voltada para baixo ($V'' = -6 < 0$), despolarização desacelerando até $2\text{ ms}$ e repolarização acelerando de $2$ a $4\text{ ms}$. **Correto.**

---

## 5. Conclusão da Revisão

A aula [tema-02.dlt](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-02/tema-02.dlt) está plenamente **APROVADA**. Seu rigor analítico, riqueza de exemplos contextualizados e adequação estrita aos padrões Delta habilitam-na diretamente para a compilação e publicação na plataforma da trilha. As pequenas melhorias apontadas na Tabela de Problemas são de caráter puramente estético e podem ser integradas conforme a conveniência editorial.
