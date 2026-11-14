# Relatório de Revisão Técnica — Módulo 01 · Tema 01 (Álgebra)

- **Arquivo revisado:** [tema-01.dlt](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-01.dlt)
- **Documentos de referência:** [PADRAO-AULAS.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/PADRAO-AULAS.md) e [DELTA-COLA.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/DELTA-COLA.md)
- **Data da revisão:** 14 de novembro de 2026
- **Perfil do revisor:** Matemático, Neurocientista Computacional e Professor de Alunos de Ciências Biológicas

---

## 1. Veredito

**APROVAR**

A aula está em excelente nível didático, matemático e biofísico. Todas as contas foram integralmente recalculadas e conferidas (exemplos e soluções dos 12 exercícios), a estrutura respeita com precisão o contrato editorial e a sintaxe Delta v0.6.0, as contextualizações biológicas são autênticas de livro-texto (Dayan & Abbott; Kandel; Schmidt-Nielsen; Guyton & Hall) e a progressão atende perfeitamente ao público-alvo (alunos de Biologia iniciando a trilha em direção à Neurociência Computacional).

Foram apontadas apenas 3 observações pontuais de polimento pedagógico/formatação na tabela abaixo, nenhuma de caráter impeditivo.

---

## 2. Tabela de Problemas e Observações

| Severidade | Local | Trecho | Correção sugerida |
|---|---|---|---|
| Pedagógico | Seção 1 (`sec:1-1-1`), linha ~108 | `(ordem de grandeza $10^{11}$, isto é, centenas de bilhões)` | O valor $8{,}6 \times 10^{10} \approx 86$ bilhões aproxima-se de $10^{11}$ ($100$ bilhões). A expressão "centenas de bilhões" (no plural) pode induzir o estudante a pensar em $200$ a $500$ bilhões. Sugere-se: `(ordem de grandeza $10^{11}$, isto é, cerca de cem bilhões)`. |
| Formato | Seção 3 (`sec:1-1-3`), `rem:1-1-armadilha-desig`, linha ~555 | `o sinal $<$ prende $x$ <em>dentro</em> ... o sinal $>$ expulsa $x$` | Embora esteja entre delimitadores matemáticos `$...$`, para eliminar qualquer ambiguidade com parsers XML estritos ou linters de marcação, sugere-se escrever por extenso ou como símbolos de desigualdade formais: `o sinal de menor ($<$) prende $x$ ... o sinal de maior ($>$) expulsa $x$`. |
| Pedagógico | Seção 3 (`sec:1-1-3`), `exr:1-1-3-4`, linha ~613 | `obtemos $[-150,\, 200)\text{ pA}$` | Para consistência absoluta com a convenção de intervalos adotada em todo o texto (onde números com vírgula ou proximidade visual usam ponto e vírgula), sugere-se usar ponto e vírgula: `$[-150;\, 200)\text{ pA}$`. |

---

## 3. Recálculo e Auditoria de Contas

Todas as contas foram refeitas passo a passo:

### 3.1 Subtema 1: Potenciação (`sec:1-1-1`)

1. **[Exemplo 1.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-01.dlt#L116-L134) (`exm:1-1-cultura`):**
   - Item (a): $t = \frac{120\text{ min}}{20\text{ min}} = 6$ gerações. $N(6) = 100 \cdot 2^6 = 100 \cdot 64 = 6\,400$ bactérias. **Correto.**
   - Item (b): $\frac{N(8)}{N(5)} = \frac{100 \cdot 2^8}{100 \cdot 2^5} = 2^{8-5} = 2^3 = 8$. **Correto.**
2. **[Exemplo 1.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-01.dlt#L136-L155) (`exm:1-1-neuro-sinapses`):**
   - Item (a): $(1{,}5 \times 10^8) \cdot (6{,}0 \times 10^3) = (1{,}5 \cdot 6{,}0) \times 10^{8+3} = 9{,}0 \times 10^{11}$ sinapses.
     Como a mantissa $9{,}0 \ge \sqrt{10} \approx 3{,}16$, a ordem de grandeza é $10^{11+1} = 10^{12}$ (1 trilhão na escala curta do PB). **Correto.**
   - Item (b): $\frac{1{,}5 \times 10^8}{8{,}6 \times 10^{10}} = \frac{1{,}5}{8{,}6} \times 10^{-2} \approx 0{,}1744 \times 10^{-2} = 1{,}74 \times 10^{-3} \approx 0{,}17\%$. **Correto.**
3. **[Exemplo 1.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-01.dlt#L157-L168) (`exm:1-1-fracionarios`):**
   - Numerador: $x^{3/2} \cdot x^{-1/2} = x^{3/2 - 1/2} = x^1$. Denominador: $(x^2)^{1/4} = x^{2 \cdot (1/4)} = x^{1/2}$.
   - Quociente: $x^1 / x^{1/2} = x^{1/2} = \sqrt{x}$.
   - Conferência com $x = 16$: $\frac{16^{3/2} \cdot 16^{-1/2}}{(16^2)^{1/4}} = \frac{64 \cdot (1/4)}{256^{1/4}} = \frac{16}{4} = 4 = \sqrt{16}$. **Correto.**
4. **[Exercício 1.1.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-01.dlt#L180-L198) (`exr:1-1-1-1`):**
   - Item (a): $(-3)^2 - 3^2 + 5^0 = 9 - 9 + 1 = 1$. **Correto.**
   - Item (b): $\frac{2^5 \cdot 2^{-2}}{(2^2)^2} = \frac{2^3}{2^4} = 2^{-1} = 0{,}5$. **Correto.**
5. **[Exercício 1.1.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-01.dlt#L200-L209) (`exr:1-1-1-2`):**
   - Razão: $\frac{1{,}5 \times 10^{-3}}{1{,}0 \times 10^{-7}} = 1{,}5 \times 10^{-3 - (-7)} = 1{,}5 \times 10^4 = 15\,000$.
   - Como $1{,}5 < 3{,}16$, ordem de grandeza $10^4$. **Correto.**
6. **[Exercício 1.1.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-01.dlt#L211-L226) (`exr:1-1-1-3`):**
   - $A(x) = \frac{(9x^3)^{1/2} \cdot x^{-1/2}}{x^2} = \frac{3x^{3/2} \cdot x^{-1/2}}{x^2} = \frac{3x}{x^2} = \frac{3}{x}$.
   - Para $x = 6$: $A(6) = 3/6 = 0{,}5$.
   - Conferência direta com $x = 6$: $\frac{\sqrt{9 \cdot 216} \cdot (1/\sqrt{6})}{36} = \frac{\sqrt{1944 / 6}}{36} = \frac{\sqrt{324}}{36} = \frac{18}{36} = 0{,}5$. **Correto.**
7. **[Exercício 1.1.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-01.dlt#L228-L250) (`exr:1-1-1-4`):**
   - Item (a): $\frac{B_B}{B_A} = \frac{B_0 (16 M_A)^{3/4}}{B_0 M_A^{3/4}} = 16^{3/4} = (2^4)^{3/4} = 2^3 = 8$. **Correto.**
   - Item (b): $b = B/M = B_0 M^{3/4 - 1} = B_0 M^{-1/4}$.
     $\frac{b_B}{b_A} = 16^{-1/4} = \frac{1}{16^{1/4}} = \frac{1}{2} = 0{,}5$. **Correto.**

---

### 3.2 Subtema 2: Equação (`sec:1-1-2`)

1. **[Exemplo 1.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-01.dlt#L307-L330) (`exm:1-1-ohm-nernst`):**
   - Item (a): $I = \frac{\Delta V}{R_{\text{in}}} = \frac{15 \times 10^{-3}\text{ V}}{40 \times 10^6\;\Omega} = 0{,}375 \times 10^{-9}\text{ A} = 0{,}375\text{ nA} = 375\text{ pA}$.
     Conferência: $40 \times 10^6 \times 0{,}375 \times 10^{-9} = 15 \times 10^{-3}\text{ V} = 15\text{ mV}$. **Correto.**
   - Item (b): $E_{\text{ion}} = \frac{RT}{zF} \ln\left(\frac{[\text{íon}]_{\text{ext}}}{[\text{íon}]_{\text{int}}}\right) \implies z = \frac{RT}{E_{\text{ion}} F} \ln\left(\frac{[\text{íon}]_{\text{ext}}}{[\text{íon}]_{\text{int}}}\right)$. **Correto.**
2. **[Exemplo 1.5](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-01.dlt#L332-L347) (`exm:1-1-bhaskara`):**
   - $2x^2 - 10x + 8 = 0 \implies \Delta = (-10)^2 - 4(2)(8) = 100 - 64 = 36$.
   - $x = \frac{10 \pm 6}{4} \implies x_1 = 4, \quad x_2 = 1$.
   - Conferência: $2(16) - 40 + 8 = 0$; $2(1) - 10 + 8 = 0$. **Correto.**
3. **[Exemplo 1.6](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-01.dlt#L349-L366) (`exm:1-1-exp`):**
   - Item (a): $2^x = 64 = 2^6 \implies x = 6$. **Correto.**
   - Item (b): $50 \cdot 2^t = 3\,200 \implies 2^t = 64 = 2^6 \implies t = 6$ gerações. **Correto.**
4. **[Exercício 1.2.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-01.dlt#L377-L388) (`exr:1-1-2-1`):**
   - $3(x - 2) + 4 = 5x - 10 \implies 3x - 2 = 5x - 10 \implies 8 = 2x \implies x = 4$.
   - Conferência: $3(2)+4 = 10$; $5(4)-10 = 10$. **Correto.**
5. **[Exercício 1.2.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-01.dlt#L390-L403) (`exr:1-1-2-2`):**
   - $V_m - V_{\text{rep}} = -55 - (-70) = 15\text{ mV} = 15 \times 10^{-3}\text{ V}$.
   - $I = \frac{15 \times 10^{-3}}{50 \times 10^6} = 0{,}3 \times 10^{-9}\text{ A} = 0{,}3\text{ nA}$.
   - Conferência: $-70 + 50(0{,}3) = -55\text{ mV}$. **Correto.**
6. **[Exercício 1.2.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-01.dlt#L405-L427) (`exr:1-1-2-3`):**
   - Item (a): $3x^2 - 6x - 24 = 0 \iff x^2 - 2x - 8 = 0 \implies \Delta = 4 - 4(1)(-8) = 36$.
     $x = \frac{2 \pm 6}{2} \implies x_1 = 4, \quad x_2 = -2$.
     Conferência: $3(16) - 24 - 24 = 0$; $3(4) + 12 - 24 = 0$. **Correto.**
   - Item (b): $3 \cdot 2^{x+1} = 96 \implies 2^{x+1} = 32 = 2^5 \implies x + 1 = 5 \implies x = 4$.
     Conferência: $3 \cdot 2^5 = 96$. **Correto.**
7. **[Exercício 1.2.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-01.dlt#L429-L454) (`exr:1-1-2-4`):**
   - Item (a): $R_{\text{eq}}(R_1 + R_2) = R_1 R_2 \implies R_2(R_1 - R_{\text{eq}}) = R_{\text{eq}} R_1 \implies R_2 = \frac{R_{\text{eq}} R_1}{R_1 - R_{\text{eq}}}$. **Correto.**
   - Item (b): $R_2 = \frac{20 \cdot 30}{30 - 20} = \frac{600}{10} = 60\text{ M}\Omega$.
     Conferência: $\frac{30 \cdot 60}{30 + 60} = \frac{1\,800}{90} = 20\text{ M}\Omega$. **Correto.**
   - Item (c): Denominador $R_1 - R_{\text{eq}} > 0 \implies R_1 > R_{\text{eq}}$, refletindo que vias condutivas em paralelo sempre diminuem a resistência equivalente da membrana. **Correto.**

---

### 3.3 Subtema 3: Desigualdade (`sec:1-1-3`)

1. **[Exemplo 1.7](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-01.dlt#L513-L524) (`exm:1-1-limiar`):**
   - $-70 + 50I \ge -55 \implies 50I \ge 15 \implies I \ge 0{,}3\text{ nA} \implies I \in [0{,}3;\, +\infty)\text{ nA}$. **Correto.**
2. **[Exemplo 1.8](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-01.dlt#L526-L548) (`exm:1-1-inversao-faixa`):**
   - Item (a): $-3x + 6 > 18 \implies -3x > 12 \implies x < -4 \implies x \in (-\infty, -4)$.
     Conferência com $x = -5$: $-3(-5) + 6 = 21 > 18$. **Correto.**
   - Item (b): $|\text{pH} - 7{,}40| \le 0{,}05 \iff -0{,}05 \le \text{pH} - 7{,}40 \le 0{,}05 \iff [7{,}35;\, 7{,}45]$. **Correto.**
3. **[Exercício 1.3.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-01.dlt#L559-L570) (`exr:1-1-3-1`):**
   - $-4x + 7 \ge 23 \implies -4x \ge 16 \implies x \le -4 \implies (-\infty, -4]$.
     Conferência com $x = -5$: $-4(-5) + 7 = 27 \ge 23$. **Correto.**
4. **[Exercício 1.3.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-01.dlt#L572-L583) (`exr:1-1-3-2`):**
   - $|T - 37{,}0| \le 0{,}5 \iff 36{,}5 \le T \le 37{,}5 \iff [36{,}5;\, 37{,}5]\,^\circ\text{C}$. **Correto.**
5. **[Exercício 1.3.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-01.dlt#L585-L600) (`exr:1-1-3-3`):**
   - $-4 < 2x - 6 < 4 \implies 2 < 2x < 10 \implies 1 < x < 5 \implies (1, 5)$.
   - Fatoração: $2|x - 3| < 4 \implies |x - 3| < 2$, com centro $a = 3$ e raio $r = 2$.
     Conferência: $(3 - 2,\, 3 + 2) = (1, 5)$. **Correto.**
6. **[Exercício 1.3.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-01.dlt#L602-L617) (`exr:1-1-3-4`):**
   - $-80 \le -68 + 80I < -52 \implies -12 \le 80I < 16$.
   - Divisão por $80$: $-0{,}15 \le I < 0{,}20\text{ nA} \implies [-0{,}15;\, 0{,}20)\text{ nA}$.
   - Em pA: $[-150,\, 200)\text{ pA}$.
   - Conferência nos extremos: $I = -0{,}15\text{ nA} \implies V_m = -68 - 12 = -80\text{ mV}$; $I = 0{,}20\text{ nA} \implies V_m = -68 + 16 = -52\text{ mV}$. **Correto.**

---

## 4. Checklist de Conformidade Editorial e Pedagógica

| Critério avaliado | Status | Análise detalhada |
|---|:---:|---|
| **Dica e solução completa em cada exercício** | **OK** | Todos os 12 exercícios possuem `<hint><title>Ver dica</title>...</hint>` e `<solution collapsible="true" collapsed="true">` com o raciocínio completo e conferência explícita. |
| **Pelo menos um exemplo biológico por seção** | **OK** | **Seção 1:** Crescimento bacteriano ($N(t) = 100 \cdot 2^t$), sinapses corticais ($8{,}6 \times 10^{10}$ neurônios), gradiente de $\text{Ca}^{2+}$ e alometria metabólica (Kleiber).<br>**Seção 2:** Lei de Ohm em membrana celular ($\Delta V = R_{\text{in}} I$), equação de Nernst, limiar de disparo e canais iônicos em paralelo.<br>**Seção 3:** Condição de disparo e reobase, regulação de pH sanguíneo arterial, homeotermia e janela sub-limiar de estimulação. |
| **Afirmações de neurociência de livro-texto** | **OK** | Potenciais de membrana ($-70\text{ mV}$, $-55\text{ mV}$), resistências de entrada ($40\text{--}80\text{ M}\Omega$), correntes patch-clamp (pico em centenas de $\text{pA}$ a frações de $\text{nA}$), gradiente de cálcio ($100\text{ nmol/L}$ interno vs. $1{,}5\text{ mmol/L}$ externo) e contagem neuronal cerebral ($8{,}6 \times 10^{10}$) seguem fielmente Dayan & Abbott (*Theoretical Neuroscience*) e Kandel (*Principles of Neural Science*). |
| **Sequenciamento pedagógico de conceitos** | **OK** | Nenhum conceito é presumido sem apresentação. Propriedades de potências antecedem expoentes racionais e notação científica; princípios de equivalência antecedem Bhaskara e exponenciais; desigualdades lineares antecedem vizinhanças modulares. Logaritmos e limites recebem notas pontuais explícitas de preparação para o Tema 1.3 e Módulo 2. |
| **Código Python e figuras executáveis** | **OK** | O script [crescimento-bacteriano.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/fig/crescimento-bacteriano.py) em `conteudo/modulo-01/fig/` é perfeitamente válido, usa fundo transparente, fontes legíveis e gera o arquivo SVG referenciado [crescimento-bacteriano.svg](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/fig/crescimento-bacteriano.svg). A aula em si não possui blocos `<code>` (apenas módulos com programação os exigem). |
| **Consistência de notação matemática** | **OK** | Uso rigoroso de vírgula decimal ($0{,}5$, $1{,}5$), notação de conjuntos com `\mathbb{R}` e `\mathbb{Z}`, separação clara de intervalos com ponto e vírgula quando há vírgula decimal, e notação científica padronizada ($c \times 10^k$). |
| **Cobertura de todos os subtemas pedidos** | **OK** | Cobre integralmente os 3 subtemas especificados no guia original para Álgebra: `1-1-1 Potenciação`, `1-1-2 Equação` e `1-1-3 Desigualdade`. |
| **Tamanho dentro do padrão** | **OK** | O texto possui aproximadamente 4.100 palavras, situando-se com folga no intervalo estipulado de 2.500 a 5.000 palavras. |
| **Conformidade técnica Delta v0.6.0** | **OK** | Atributos com valores explícitos, `id`s padronizados e sem caracteres inválidos, `<intro>`, `<eyebrow>`, `<remark>`, `<observation>`, `<proof>`, `<solution>`, metadados com link ao guia e `<toc scope="project" depth="1"/>` estruturados de acordo com [DELTA-COLA.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/DELTA-COLA.md). |

---

## 5. Conclusão da Revisão

A aula [tema-01.dlt](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-01.dlt) está **aprovada sem necessidade de retrabalho estrutural ou matemático**. As pequenas sugestões listadas na Tabela de Problemas podem ser incorporadas oportunamente em ciclos de polimento editorial, sem impedir a compilação e publicação da aula.
