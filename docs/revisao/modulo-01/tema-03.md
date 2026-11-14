# Relatório de Revisão Técnica — Módulo 01 · Tema 03 (Funções)

- **Arquivo revisado:** [tema-03.dlt](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-03.dlt)
- **Scripts de figura revisados:** [sigmoide.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/fig/sigmoide.py) e [curva-sintonia.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/fig/curva-sintonia.py)
- **Documentos de referência:** [PADRAO-AULAS.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/PADRAO-AULAS.md) e [DELTA-COLA.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/DELTA-COLA.md)
- **Data da revisão:** 14 de novembro de 2026
- **Perfil do revisor:** Matemático, Neurocientista Computacional e Professor de Alunos de Ciências Biológicas

---

## 1. Veredito

**APROVAR**

A aula [tema-03.dlt](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-03.dlt) apresenta padrão de excelência sob todas as óticas de avaliação: rigor matemático impecável, exatidão biofísica e neurocientífica ancorada nos livros-texto clássicos (*Dayan & Abbott*, *Kandel*, *Gerstner et al.*), progressão didática acolhedora e formadora para estudantes de Ciências Biológicas, e estrita conformidade com a sintaxe do Delta v0.6.0.

Todas as contas dos 8 exemplos resolvidos e das soluções dos 16 exercícios propostos foram integralmente recalculadas passo a passo, confirmando precisão numérica e algébrica absoluta em 100% dos itens (sem qualquer divergência matemática). Os scripts das figuras [sigmoide.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/fig/sigmoide.py) e [curva-sintonia.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/fig/curva-sintonia.py) geram exatamente o que o texto e as legendas descrevem, respeitando os parâmetros técnicos estipulados (`plt.rcParams['svg.fonttype'] = 'none'`, fundos transparentes e legendas didáticas em português).

Foram registradas apenas observações pontuais de polimento pedagógico e de formato na tabela a seguir, nenhuma de caráter impeditivo para a aprovação e publicação do tema.

---

## 2. Tabela de Problemas e Observações

| Severidade | Local | Trecho | Correção sugerida |
|---|---|---|---|
| Formato | Seção 3 (`sec:1-3-3`), `<proof of="prop:1-3-criterio-inversa">`, linha ~504 | `(o raciocínio para funções estritamente decrescentes é idêntico, apenas trocando $<$ por $>$)` | Embora os símbolos estejam entre delimitadores matemáticos `$...$`, alguns parsers XML estritos ou linters de marcação podem levantar alertas de falso positivo para caracteres `<` e `>` soltos. Sugere-se escrever por extenso ou usar comandos LaTeX nominais: `(o raciocínio para funções estritamente decrescentes é idêntico, apenas trocando o sinal de menor ($\lt$) pelo de maior ($\gt$))`. |
| Pedagógico | Seção 4 (`sec:1-3-4`), [exr:1-3-4-4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-03.dlt#L842), linha ~842 | `passando por $(6, 50)$, $(10;\, 66{,}7)$, $(14, 75)$, $(18, 80)$ e $(38, 90)$` | O ponto $(10;\, 66{,}7)$ adotou ponto e vírgula por conta da vírgula decimal, enquanto os outros pares com valores inteiros usaram vírgula simples. Para reforçar a consistência com estudantes de biologia habituados a números decimais, sugere-se padronizar o separador com ponto e vírgula em todos os pares ordenados no plano: `passando por $(6;\, 50)$, $(10;\, 66{,}7)$, $(14;\, 75)$, $(18;\, 80)$ e $(38;\, 90)$`. |
| Pedagógico | Seção 4 (`sec:1-3-4`), [exr:1-3-4-3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-03.dlt#L807), linha ~807 | `o ponto $(0{,}3;\, 30)$ no gráfico de $r$ corresponde ao ponto $(30\text{ Hz};\, 0{,}3\text{ nA})$ no gráfico de $r^{-1}$` | No item (a) correspondente (linha ~805), as coordenadas do ponto de meia resposta incluíram as unidades físicas: `$(0{,}3\text{ nA};\, 30\text{ Hz})$`. No item (c), a primeira referência omitiu as unidades e a segunda as incluiu. Sugere-se manter as unidades em ambas as menções para enfatizar a troca física das grandezas nos eixos: `o ponto $(0{,}3\text{ nA};\, 30\text{ Hz})$ no gráfico de $r$ corresponde ao ponto $(30\text{ Hz};\, 0{,}3\text{ nA})$ no gráfico de $r^{-1}$`. |
| Pedagógico | Seção 1 (`sec:1-3-1`), [def:1-3-modelos-neurais](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-03.dlt#L92), linha ~92 | `soma-se uma taxa espontânea de linha de base $r_0 \ge 0$, escrevendo $f(\theta) = r_0 + r_{\text{max}} \cdot \exp(\dots)$` | O texto prevê com precisão a modulação aditiva explorada no exercício 1.3.4.2. Sugere-se explicitar a unidade física de $r_0$ já na definição (`taxa espontânea de linha de base $r_0 \ge 0$ (em $\text{Hz}$)`), mantendo a perfeita clareza dimensional característica da aula. |

---

## 3. Recálculo e Auditoria de Contas

Todas as contas foram integralmente recalculadas. Como nenhuma divergência foi encontrada nos cálculos originais, apresentamos abaixo a memória de cálculo completa de cada bloco para fins de auditoria e registro técnico.

### 3.1 Subtema 1: Introdução (`sec:1-3-1`)

1. **[Exemplo 1.3.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-03.dlt#L111-L148) (`exm:1-3-sintonia-sigmoide`):**
   - *Item (a) — Curva de sintonia gaussiana:*
     $f(\theta) = 50 \cdot \exp\!\left(-\frac{(\theta - 90^\circ)^2}{2 \cdot (20^\circ)^2}\right) = 50 \cdot \exp\!\left(-\frac{(\theta - 90^\circ)^2}{800}\right)$.
     - $\theta = 90^\circ$: expoente $= 0 \implies f(90^\circ) = 50 \cdot e^0 = 50\text{ Hz}$. **Correto.**
     - $\theta = 110^\circ$: $\Delta\theta = +20^\circ = +\sigma$. Expoente $= -\frac{400}{800} = -0{,}5$. Com $\exp(-0{,}5) \approx 0{,}60653$: $50 \times 0{,}60653 = 30{,}327 \approx 30{,}3\text{ Hz}$. **Correto.**
     - $\theta = 50^\circ$: $\Delta\theta = -40^\circ = -2\sigma$. Expoente $= -\frac{1\,600}{800} = -2{,}0$. Com $\exp(-2) \approx 0{,}135335$: $50 \times 0{,}135335 = 6{,}767 \approx 6{,}8\text{ Hz}$. **Correto.**
   - *Item (b) — Sigmoide logística $f$–$I$:*
     $r(I) = \frac{80}{1 + \exp\left(-\frac{I - 0{,}5}{0{,}1}\right)}$.
     - $I = 0{,}5\text{ nA}$: expoente $= 0 \implies r(0{,}5) = \frac{80}{1 + 1} = 40\text{ Hz}$. **Correto.**
     - $I = 0{,}6\text{ nA}$: expoente $= -\frac{0{,}1}{0{,}1} = -1 \implies r(0{,}6) = \frac{80}{1 + e^{-1}} \approx \frac{80}{1{,}367879} \approx 58{,}48 \approx 58{,}5\text{ Hz}$. **Correto.**
     - $I = 0{,}4\text{ nA}$: expoente $= -\frac{-0{,}1}{0{,}1} = +1 \implies r(0{,}4) = \frac{80}{1 + e^1} \approx \frac{80}{3{,}71828} \approx 21{,}517 \approx 21{,}5\text{ Hz}$. **Correto.**
     - Simetria em torno de $I_{50}$: $58{,}483 + 21{,}517 = 80{,}0\text{ Hz} = r_{\text{max}}$. **Correto.**

2. **[Exemplo 1.3.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-03.dlt#L150-L176) (`exm:1-3-hill-relu`):**
   - *Item (a) — Equação de Hill:* $E([L]) = \frac{100 \cdot [L]^2}{4 + [L]^2}$.
     - $[L] = 1\;\mu\text{M}$: $E(1) = \frac{100 \cdot 1}{4 + 1} = \frac{100}{5} = 20\%$. **Correto.**
     - $[L] = 2\;\mu\text{M}$: $E(2) = \frac{100 \cdot 4}{4 + 4} = \frac{400}{8} = 50\%$ (confirma $\text{EC}_{50} = 2\;\mu\text{M}$). **Correto.**
     - $[L] = 4\;\mu\text{M}$: $E(4) = \frac{100 \cdot 16}{4 + 16} = \frac{1\,600}{20} = 80\%$. **Correto.**
     - $[L] = 6\;\mu\text{M}$: $E(6) = \frac{100 \cdot 36}{4 + 36} = \frac{3\,600}{40} = 90\%$. **Correto.**
   - *Item (b) — Linear com limiar (ReLU):* $r(I) = \max\bigl(0,\, 50(I - 0{,}2)\bigr)$.
     - $I = 0{,}1\text{ nA}$: $50(0{,}1 - 0{,}2) = -5 \implies \max(0, -5) = 0\text{ Hz}$. **Correto.**
     - $I = 0{,}2\text{ nA}$: $50(0{,}2 - 0{,}2) = 0 \implies \max(0, 0) = 0\text{ Hz}$. **Correto.**
     - $I = 0{,}6\text{ nA}$: $50(0{,}6 - 0{,}2) = 50 \cdot 0{,}4 = 20 \implies \max(0, 20) = 20\text{ Hz}$. **Correto.**

3. **[Exercício 1.3.1.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-03.dlt#L186-L202) (`exr:1-3-1-1`):**
   - *Item (a):* $f(x) = \frac{1}{\sqrt{x - 3}} \implies x - 3 > 0 \implies x > 3 \implies D_f = (3, +\infty)$.
     $g(x) = \ln(5 - x) \implies 5 - x > 0 \implies x < 5 \implies D_g = (-\infty, 5)$. **Correto.**
   - *Item (b):* Para $x = 0$ em $x^2 + y^2 = 25$, $y^2 = 25 \implies y = \pm 5$. A reta vertical corta a curva nos pontos $(0, 5)$ e $(0, -5)$, falhando no teste da reta vertical. **Correto.**

4. **[Exercício 1.3.1.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-03.dlt#L204-L220) (`exr:1-3-1-2`):**
   - $f(\theta) = 60 \cdot \exp\!\left(-\frac{(\theta - 45^\circ)^2}{2 \cdot (15^\circ)^2}\right) = 60 \cdot \exp\!\left(-\frac{(\theta - 45^\circ)^2}{450}\right)$.
     - $\theta = 45^\circ$: $60 \cdot e^0 = 60\text{ Hz}$. **Correto.**
     - $\theta = 60^\circ$: expoente $= -\frac{15^2}{2 \cdot 15^2} = -0{,}5 \implies 60 \times 0{,}6065 = 36{,}39 \approx 36{,}4\text{ Hz}$. **Correto.**
     - $\theta = 15^\circ$: expoente $= -\frac{(-30)^2}{450} = -\frac{900}{450} = -2 \implies 60 \times 0{,}1353 = 8{,}118 \approx 8{,}1\text{ Hz}$. **Correto.**

5. **[Exercício 1.3.1.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-03.dlt#L222-L248) (`exr:1-3-1-3`):**
   - *Item (a):* $E(10) = \frac{120 \cdot 10}{20} = 60\text{ pA}$; $E(30) = \frac{120 \cdot 30}{40} = 90\text{ pA}$; $E(90) = \frac{120 \cdot 90}{100} = 108\text{ pA}$. **Correto.**
   - *Item (b):* $\frac{120[L]}{10 + [L]} = 40 \implies 120[L] = 400 + 40[L] \implies 80[L] = 400 \implies [L] = 5\;\mu\text{M}$.
     Conferência direta: $E(5) = \frac{120 \cdot 5}{15} = \frac{600}{15} = 40\text{ pA}$. **Correto.**

6. **[Exercício 1.3.1.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-03.dlt#L250-L270) (`exr:1-3-1-4`):**
   - *Item (a):* $x - 1 > 0 \implies x > 1$; $9 - x > 0 \implies x < 9$. Interseção: $(1, 9)$. **Correto.**
   - *Item (b):* $0 \le 20 I - 4 \le 200 \implies 4 \le 20 I \le 204 \implies 0{,}2 \le I \le 10{,}2\text{ nA}$. Intervalo $[0{,}2;\, 10{,}2]\text{ nA}$. **Correto.**

---

### 3.2 Subtema 2: Composição de função (`sec:1-3-2`)

1. **[Exemplo 1.3.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-03.dlt#L302-L336) (`exm:1-3-cadeia-neural`):**
   - *Item (a):* $(r \circ V)(I) = \max\bigl(0,\, 4((-70 + 100 I) - (-55))\bigr) = \max\bigl(0,\, 4(100 I - 15)\bigr) = \max\bigl(0,\, 400(I - 0{,}15)\bigr)$. **Correto.**
   - *Item (b):* $400(I - 0{,}15) > 0 \implies I > 0{,}15\text{ nA} = 150\text{ pA}$ (reobase). **Correto.**
   - *Item (c):*
     - $I = 0{,}10\text{ nA}$: $V(0{,}10) = -60\text{ mV} \implies r(-60) = \max(0,\, 4(-60 + 55)) = 0\text{ Hz}$. **Correto.**
     - $I = 0{,}25\text{ nA}$: $V(0{,}25) = -45\text{ mV} \implies r(-45) = 4(-45 + 55) = 40\text{ Hz}$. Pela composta: $400(0{,}25 - 0{,}15) = 400 \cdot 0{,}10 = 40\text{ Hz}$. **Correto.**

2. **[Exemplo 1.3.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-03.dlt#L338-L365) (`exm:1-3-ordem-decomposicao`):**
   - *Item (a):* $(g \circ f)(x) = \sqrt{x - 4}$, $D_{g \circ f} = [4, +\infty)$, $(g \circ f)(4) = 0$.
     $(f \circ g)(x) = \sqrt{x} - 4$, $D_{f \circ g} = [0, +\infty)$, $(f \circ g)(4) = \sqrt{4} - 4 = -2$. **Correto.**
   - *Item (b):* $u(\theta) = \theta - 90$, $v(u) = -\frac{u^2}{800}$, $w(v) = 50 e^v$.
     $(w \circ v \circ u)(\theta) = 50 \exp\left(-\frac{(\theta - 90)^2}{800}\right)$. **Correto.**

3. **[Exercício 1.3.2.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-03.dlt#L376-L398) (`exr:1-3-2-1`):**
   - *Item (a):* $(g \circ f)(x) = (3x - 2)^2 + 1 = 9x^2 - 12x + 5$.
     $(f \circ g)(x) = 3(x^2 + 1) - 2 = 3x^2 + 1$. **Correto.**
   - *Item (b):* Em $x = 2$: $f(2) = 4 \implies g(4) = 17$; $9(4) - 24 + 5 = 17$.
     $g(2) = 5 \implies f(5) = 13$; $3(4) + 1 = 13$. Como $17 \ne 13$, $g \circ f \ne f \circ g$. **Correto.**

4. **[Exercício 1.3.2.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-03.dlt#L400-L410) (`exr:1-3-2-2`):**
   - $(g \circ f)(x) = \ln(2x - 6)$, $2x - 6 > 0 \implies x > 3 \implies D_{g \circ f} = (3, +\infty)$. **Correto.**
   - $(f \circ g)(x) = 2\ln(x) - 6$, $x \in D_g \implies x > 0 \implies D_{f \circ g} = (0, +\infty)$. **Correto.**

5. **[Exercício 1.3.2.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-03.dlt#L412-L429) (`exr:1-3-2-3`):**
   - *Item (a):* $z(x) = 3x - 6$ e $h(z) = \frac{1}{1 + e^{-z}} \implies (h \circ z)(x) = \frac{1}{1 + e^{-(3x - 6)}}$. **Correto.**
   - *Item (b):* $z(2) = 3(2) - 6 = 0 \implies h(0) = \frac{1}{1 + 1} = 0{,}5$ (ponto de meia ativação). **Correto.**

6. **[Exercício 1.3.2.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-03.dlt#L431-L466) (`exr:1-3-2-4`):**
   - *Item (a):* $c = 4\;\mu\text{M} \implies I(4) = \frac{0{,}5 \cdot 4}{5} = 0{,}4\text{ nA} \implies V(0{,}4) = -70 + 80(0{,}4) = -38\text{ mV} \implies r(-38) = \max(0,\, 5(-38 + 54)) = 5 \cdot 16 = 80\text{ Hz}$. **Correto.**
   - *Item (b):* $r > 0 \implies V > -54\text{ mV} \implies -70 + 80 I > -54 \implies 80 I > 16 \implies I > 0{,}2\text{ nA}$.
     $\frac{0{,}5 c}{1 + c} > 0{,}2 \implies 0{,}5 c > 0{,}2 + 0{,}2 c \implies 0{,}3 c > 0{,}2 \implies c > \frac{2}{3}\;\mu\text{M} \approx 0{,}67\;\mu\text{M}$. **Correto.**
   - *Item (c):* $\lim_{c \to \infty} I(c) = 0{,}5\text{ nA} \implies V_{\text{sup}} = -70 + 80(0{,}5) = -30\text{ mV} \implies r_{\text{sup}} = 5(-30 + 54) = 5 \cdot 24 = 120\text{ Hz}$. **Correto.**

---

### 3.3 Subtema 3: Inversa (`sec:1-3-3`)

1. **[Exemplo 1.3.5](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-03.dlt#L513-L542) (`exm:1-3-inversa-sigmoide-hill`):**
   - *Item (a) — Inversa da sigmoide:*
     $r = \frac{r_{\text{max}}}{1 + e^{-(I - I_{50})/s}} \implies e^{-(I - I_{50})/s} = \frac{r_{\text{max}} - r}{r} \implies -(I - I_{50})/s = \ln\left(\frac{r_{\text{max}} - r}{r}\right) \implies I(r) = I_{50} + s \ln\left(\frac{r}{r_{\text{max}} - r}\right)$ para $r \in (0, r_{\text{max}})$. **Correto.**
     Aplicação numérica ($r = 64\text{ Hz}$, $r_{\text{max}} = 80\text{ Hz}$, $I_{50} = 0{,}5\text{ nA}$, $s = 0{,}1\text{ nA}$):
     $\frac{64}{80 - 64} = 4 \implies I(64) = 0{,}5 + 0{,}1 \ln(4) \approx 0{,}5 + 0{,}1(1{,}38629) = 0{,}5 + 0{,}1386 = 0{,}6386 \approx 0{,}639\text{ nA}$.
     Conferência direta: $-(0{,}6386 - 0{,}5)/0{,}1 = -1{,}386 \implies e^{-1{,}386} = 0{,}25 \implies r = \frac{80}{1{,}25} = 64\text{ Hz}$. **Correto.**
   - *Item (b) — Inversa da equação de Hill:*
     $E = \frac{E_{\text{max}} [L]^n}{\text{EC}_{50}^n + [L]^n} \implies [L]^n = \text{EC}_{50}^n \frac{E}{E_{\text{max}} - E} \implies [L](E) = \text{EC}_{50} \left(\frac{E}{E_{\text{max}} - E}\right)^{1/n}$. **Correto.**
     Aplicação numérica ($E_{\text{max}} = 100\%$, $\text{EC}_{50} = 2\;\mu\text{M}$, $n = 2$, $E = 80\%$):
     $[L](80) = 2 \left(\frac{80}{20}\right)^{1/2} = 2 \sqrt{4} = 4\;\mu\text{M}$. **Correto.**

2. **[Exemplo 1.3.6](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-03.dlt#L544-L572) (`exm:1-3-inversa-gaussiana`):**
   - *Item (a):* $(\pm 20^\circ)^2 = 400 \implies f(70^\circ) = f(110^\circ) \approx 30{,}3\text{ Hz}$. Entradas distintas com a mesma saída $\implies$ não injetora. **Correto.**
   - *Item (b) — Inversa no flanco direito ($\theta \ge \theta_{\text{pref}}$):*
     $(\theta - \theta_{\text{pref}})^2 = 2\sigma^2 \ln(r_{\text{max}}/r) \implies \theta(r) = \theta_{\text{pref}} + \sigma \sqrt{2 \ln(r_{\text{max}}/r)}$. **Correto.**
     Para $r = 25\text{ Hz}$: $\frac{50}{25} = 2 \implies \sqrt{2\ln 2} \approx \sqrt{1{,}386294} \approx 1{,}17741$.
     $\theta(25) = 90^\circ + 20^\circ \times 1{,}17741 \approx 90^\circ + 23{,}55^\circ = 113{,}55^\circ$.
     Largura total à meia altura (FWHM): $2 \times 23{,}55^\circ = 47{,}1^\circ \approx 2{,}355\,\sigma$. **Correto.**

3. **[Exercício 1.3.3.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-03.dlt#L583-L602) (`exr:1-3-3-1`):**
   - *Item (a):* $y = 3x - 9 \implies x = \frac{y + 9}{3} \implies f^{-1}(y) = \frac{y + 9}{3}$.
     Conferência: $f(5) = 6 \implies f^{-1}(6) = \frac{15}{3} = 5$. **Correto.**
   - *Item (b):* $N = 100 e^{0{,}2 t} \implies e^{0{,}2 t} = \frac{N}{100} \implies 0{,}2 t = \ln(N/100) \implies t(N) = 5\ln(N/100)$ para $N > 0$. **Correto.**

4. **[Exercício 1.3.3.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-03.dlt#L604-L621) (`exr:1-3-3-2`):**
   - $[L](E) = 5 \left(\frac{E}{100 - E}\right)^{1/2}$.
     - $E = 20\%$: $[L](20) = 5 \sqrt{\frac{20}{80}} = 5 \sqrt{1/4} = 2{,}5\;\mu\text{M}$. Conferência: $\frac{100(6{,}25)}{31{,}25} = 20\%$. **Correto.**
     - $E = 80\%$: $[L](80) = 5 \sqrt{\frac{80}{20}} = 5 \sqrt{4} = 10\;\mu\text{M}$. Conferência: $\frac{100(100)}{125} = 80\%$. **Correto.**

5. **[Exercício 1.3.3.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-03.dlt#L623-L645) (`exr:1-3-3-3`):**
   - *Item (a):* $h(2) = h(4) = 2 \implies$ não injetora em $\mathbb{R}$. Em $(-\infty, 3]$, $x - 3 \le 0 \implies x - 3 = -\sqrt{y - 1} \implies h^{-1}(y) = 3 - \sqrt{y - 1}$ para $y \in [1, +\infty)$.
     Conferência: $h(1) = 5 \implies h^{-1}(5) = 3 - 2 = 1$. **Correto.**
   - *Item (b) — Flanco esquerdo:* $\theta - 90^\circ \le 0 \implies \theta(r) = 90^\circ - 20^\circ \sqrt{2\ln(50/r)}$.
     Para $r = 25\text{ Hz}$: $\theta(25) = 90^\circ - 23{,}55^\circ = 66{,}45^\circ$. (Simetria: $66{,}45^\circ + 113{,}55^\circ = 180^\circ$). **Correto.**

6. **[Exercício 1.3.3.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-03.dlt#L647-L672) (`exr:1-3-3-4`):**
   - *Item (a):* $I(r) = 0{,}4 + 0{,}2 \ln\left(\frac{r}{100 - r}\right)$, com $r \in (0, 100)\text{ Hz}$. **Correto.**
   - *Item (b):* Para $r = 20\text{ Hz}$: $\frac{20}{80} = \frac{1}{4} \implies I(20) = 0{,}4 - 0{,}2 \ln(4) \approx 0{,}4 - 0{,}2(1{,}386) = 0{,}4 - 0{,}277 = 0{,}123\text{ nA}$.
     Conferência direta: $-(0{,}123 - 0{,}4)/0{,}2 = 1{,}385 \implies e^{1{,}385} \approx 4 \implies r = \frac{100}{5} = 20\text{ Hz}$. **Correto.**
   - *Item (c):* $I(50) = 0{,}4\text{ nA}$ (corrente) $\ne \frac{1}{r(0{,}4)} = \frac{1}{50\text{ Hz}} = 0{,}02\text{ s}$ (tempo/período). $r = 0$ e $r = 100$ geram $\ln(0)$ e divisão por zero. **Correto.**

---

### 3.4 Subtema 4: Gráfico (`sec:1-3-4`)

1. **[Exemplo 1.3.7](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-03.dlt#L714-L731) (`exm:1-3-transformacoes-sintonia`):**
   - *Item (a):* $\theta - 130^\circ = (\theta - 40^\circ) - 90^\circ \implies$ deslocamento horizontal de $40^\circ$ para a direita. **Correto.**
   - *Item (b):* $r_{\text{max}} = 50 \to 75 \implies$ estiramento vertical por fator $1{,}5$ (modulação de ganho). Linha de base $r_0 = 10\text{ Hz} \implies$ deslocamento vertical de $+10\text{ Hz}$ (pico $60\text{ Hz}$, caudas $10\text{ Hz}$). **Correto.**
   - *Item (c):* $\sigma = 20^\circ \to 10^\circ \implies$ compressão horizontal por $1/2$ ao redor de $90^\circ$ (o dobro de seletividade). **Correto.**
   - *Item (d):* $I - 0{,}8 = (I - 0{,}3) - 0{,}5 \implies$ deslocamento horizontal de $0{,}3\text{ nA}$ para a direita (menor excitabilidade). **Correto.**

2. **[Exemplo 1.3.8](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-03.dlt#L733-L749) (`exm:1-3-leitura-reflexao`):**
   - *Item (a):* $h(0) = 100(1 - 1) = 0$ (origem $(0, 0)$); estritamente crescente; assíntota horizontal $y = 100$. **Correto.**
   - *Item (b):* Para $x_0 = 2\ln 2 \approx 1{,}386$: $e^{-0{,}5(2\ln 2)} = e^{-\ln 2} = 0{,}5 \implies h(2\ln 2) = 100(1 - 0{,}5) = 50$.
     Ponto em $h$: $(2\ln 2;\, 50) \approx (1{,}386;\, 50)$. Ponto em $h^{-1}$: $(50;\, 2\ln 2) \approx (50;\, 1{,}386)$.
     Conferência da inversa: $h^{-1}(y) = -2\ln(1 - y/100) \implies h^{-1}(50) = -2\ln(0{,}5) = 2\ln 2$. **Correto.**

3. **[Exercício 1.3.4.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-03.dlt#L759-L775) (`exr:1-3-4-1`):**
   - *Item (a):* $g_1(x) = (x - 3)^2 + 2$: desloca $3$ à direita e $2$ para cima; vértice $(3, 2)$. **Correto.**
   - *Item (b):* $g_2(x) = 2x^2$: estiramento vertical por fator $2$; vértice $(0, 0)$. **Correto.**
   - *Item (c):* $g_3(x) = -(x + 1)^2$: desloca $1$ à esquerda e reflete no eixo $x$; vértice $(-1, 0)$. **Correto.**

4. **[Exercício 1.3.4.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-03.dlt#L777-L792) (`exr:1-3-4-2`):**
   - *Item (a):* $\theta = 90^\circ \implies f_A(90) = 10 + 40 = 50\text{ Hz}$; $f_B(90) = 60\text{ Hz}$. Nas caudas distantes: $f_A \to 10\text{ Hz}$; $f_B \to 0\text{ Hz}$. **Correto.**
   - *Item (b):* $A$ tem linha de base espontânea (deslocamento vertical $+10$); $B$ tem modulação multiplicativa de ganho (fator $60/40 = 1{,}5$). **Correto.**

5. **[Exercício 1.3.4.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-03.dlt#L794-L810) (`exr:1-3-4-3`):**
   - *Item (a):* Assíntota horizontal $r = 60\text{ Hz}$. Meia resposta: $I_{50} = 0{,}3\text{ nA}$, $r = 30\text{ Hz} \implies (0{,}3\text{ nA};\, 30\text{ Hz})$. **Correto.**
   - *Item (b):* Deslocamento horizontal de $0{,}4\text{ nA}$ para a direita. **Correto.**
   - *Item (c):* Ponto simétrico em $r^{-1}$: $(30\text{ Hz};\, 0{,}3\text{ nA})$. **Correto.**

6. **[Exercício 1.3.4.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-03.dlt#L812-L847) (`exr:1-3-4-4`):**
   - *Item (a):* $I_{\text{lim}} = 2$ (limiar); $r_{\text{max}} = 100\text{ Hz}$ (saturação); $K = 4$ (incremento de meia resposta acima do limiar: em $I = 6$, $u = 4 \implies 100(4/8) = 50\text{ Hz}$). Silêncio abaixo do limiar, crescimento estrito acima do limiar e assíntota de saturação. **Correto.**
   - *Item (b) — Cálculo dos pontos ($u = I - 2$):*
     - $I = 0$: $r(0) = 0\text{ Hz}$. **Correto.**
     - $I = 2$: $r(2) = 0\text{ Hz}$. **Correto.**
     - $I = 6$ ($u = 4$): $100 \cdot \frac{4}{8} = 50\text{ Hz}$. **Correto.**
     - $I = 10$ ($u = 8$): $100 \cdot \frac{8}{12} = 100 \cdot \frac{2}{3} \approx 66{,}7\text{ Hz}$. **Correto.**
     - $I = 14$ ($u = 12$): $100 \cdot \frac{12}{16} = 100 \cdot \frac{3}{4} = 75\text{ Hz}$. **Correto.**
     - $I = 18$ ($u = 16$): $100 \cdot \frac{16}{20} = 100 \cdot \frac{4}{5} = 80\text{ Hz}$. **Correto.**
     - $I = 38$ ($u = 36$): $100 \cdot \frac{36}{40} = 100 \cdot \frac{9}{10} = 90\text{ Hz}$. **Correto.**
   - *Item (c):* Deslocamento horizontal de $2$ unidades para a direita; assíntota horizontal em $r = 100\text{ Hz}$. **Correto.**

---

## 4. Checklist de Conformidade Editorial e Pedagógica

| Critério avaliado | Status | Análise detalhada |
|---|:---:|---|
| **Dica e solução completa em cada exercício** | **OK** | Todos os 16 exercícios contam com `<hint><title>Ver dica</title>...</hint>` e `<solution collapsible="true" collapsed="true">` contendo o desenvolvimento dedutivo passo a passo e checagens explícitas por substituição reversa. |
| **Pelo menos um exemplo biológico por seção** | **OK** | **Seção 1:** Curvas de sintonia de orientação em V1, sigmoide $f$–$I$, canais ativados por ligante (Hill/Michaelis–Menten) e faixa de resposta fisiológica $[0, 200]\text{ Hz}$.<br>**Seção 2:** Cascata biofísica estímulo $\to$ corrente $\to$ potencial $\to$ taxa de disparo axonal, e saturação sináptica de neurotransmissores.<br>**Seção 3:** Decodificação de corrente e concentração, ambiguidade de neurônio único e justificativa biológica para codificação em população cortical (*population coding*).<br>**Seção 4:** Modulação atencional de ganho (*gain modulation*), atividade espontânea aditiva, alteração de excitabilidade por anestésicos e modelo de Naka–Rushton. |
| **Afirmações de neurociência de livro-texto** | **OK** | Todos os valores e formulações seguem os cânones da área (Dayan & Abbott, *Theoretical Neuroscience*; Kandel et al., *Principles of Neural Science*): potenciais basais e de limiar ($-70\text{ mV}$, $-55\text{ mV}$), resistências de entrada ($80\text{--}100\text{ M}\Omega$), taxas de disparo ($0\text{--}200\text{ Hz}$), larguras de sintonia ($\sigma \approx 15^\circ\text{--}20^\circ$) e largura total à meia altura ($\text{FWHM} \approx 2{,}355\,\sigma$). |
| **Sequenciamento pedagógico de conceitos** | **OK** | Progressão exemplar: primeiro introduz o conceito intuitivo e formal de função com o teste da reta vertical; apresenta os 3 modelos de referência; constrói a composição e a decomposição em camadas (antecipando cálculo e redes neurais); formaliza a inversa a partir da decodificação e da injetividade; e encerra com leitura de assíntotas e transformações geométricas. Nenhum conceito surge sem preparação prévia. |
| **Scripts de figuras e saídas gráficas** | **OK** | Os dois scripts em `conteudo/modulo-01/fig/` ([sigmoide.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/fig/sigmoide.py) e [curva-sintonia.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/fig/curva-sintonia.py)) estão perfeitamente implementados, usam `plt.rcParams['svg.fonttype'] = 'none'`, geram arquivos SVG válidos com fundo transparente e traduzem exatamente os dados do texto e das legendas da aula. A aula não possui blocos executáveis de código `<code>` no corpo (dispensáveis no Módulo 1). |
| **Consistência de notação matemática e unidades** | **OK** | Uso rigoroso de vírgula para números decimais na prosa e fórmulas ($0{,}5$, $0{,}1$, $1{,}5$), ponto em código Python, intervalos adequadamente delimitados por ponto e vírgula na presença de decimais ($[0{,}2;\, 10{,}2]\text{ nA}$), conjuntos com `\mathbb{R}`, funções especiais padronizadas ($\exp$, $\ln$, $\log$) e unidades científicas consistentes ($\text{mV}$, $\text{nA}$, $\text{pA}$, $\text{Hz}$, $\mu\text{M}$, $\text{M}\Omega$). |
| **Cobertura de todos os subtemas pedidos** | **OK** | Cobertura integral dos 4 subtemas estipulados no guia oficial: `sec:1-3-1 Introdução` (curva de sintonia gaussiana, sigmoide $f$–$I$ e equação de Hill); `sec:1-3-2 Composição de função` (cadeia estímulo $\to$ potencial $\to$ taxa); `sec:1-3-3 Inversa` (decodificação e necessidade de injetividade); `sec:1-3-4 Gráfico` (transformações: translações, escalas, reflexões e saturação por assíntotas). |
| **Tamanho dentro do padrão** | **OK** | A aula contém aproximadamente 4.250 palavras, perfeitamente posicionada dentro da faixa estipulada de 2.500 a 5.000 palavras para capítulos com 4 subtemas. |
| **Conformidade técnica Delta v0.6.0** | **OK** | Todos os atributos possuem valores explícitos, identificadores em ASCII sem acentos, metadados com link de retorno ao guia (`index.html#tema-1-3`), sumários locais e de projeto (`<toc/>`, `<toc scope="project" depth="1"/>`), `<intuition>` localizadas exclusivamente dentro de definições e proposições, caixas `<box>`, seções de Resumo e Para ir além. |

---

## 5. Contas Conferidas

Lista completa dos identificadores de exemplos resolvidos e exercícios propostos cujas contas foram integralmente recalculadas e validadas:

- **Exemplos (8/8):**
  - [exm:1-3-sintonia-sigmoide](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-03.dlt#L111-L148) (Seção 1 · Curva de sintonia gaussiana e sigmoide $f$–$I$)
  - [exm:1-3-hill-relu](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-03.dlt#L150-L176) (Seção 1 · Equação de Hill e função linear com limiar)
  - [exm:1-3-cadeia-neural](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-03.dlt#L302-L336) (Seção 2 · Cadeia estímulo $\to$ potencial $\to$ taxa de disparo)
  - [exm:1-3-ordem-decomposicao](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-03.dlt#L338-L365) (Seção 2 · Domínio da composição e decomposição em 3 camadas)
  - [exm:1-3-inversa-sigmoide-hill](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-03.dlt#L513-L542) (Seção 3 · Decodificação de corrente na sigmoide e ligante em Hill)
  - [exm:1-3-inversa-gaussiana](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-03.dlt#L544-L572) (Seção 3 · Ambiguidade de neurônio único e inversa no flanco direito)
  - [exm:1-3-transformacoes-sintonia](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-03.dlt#L714-L731) (Seção 4 · Transformações em modelos neurais: ganho, linha de base, largura e limiar)
  - [exm:1-3-leitura-reflexao](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-03.dlt#L733-L749) (Seção 4 · Leitura de assíntota e simetria da inversa em torno de $y = x$)

- **Exercícios (16/16):**
  - [exr:1-3-1-1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-03.dlt#L186-L202) (Seção 1 · Domínio natural e teste da reta vertical)
  - [exr:1-3-1-2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-03.dlt#L204-L220) (Seção 1 · Curva de sintonia de neurônio em V1)
  - [exr:1-3-1-3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-03.dlt#L222-L248) (Seção 1 · Receptor sináptico de Michaelis–Menten)
  - [exr:1-3-1-4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-03.dlt#L250-L270) (Seção 1 · Domínio matemático versus domínio fisiológico)
  - [exr:1-3-2-1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-03.dlt#L376-L398) (Seção 2 · Calculando composições nas duas ordens)
  - [exr:1-3-2-2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-03.dlt#L400-L410) (Seção 2 · Domínio de funções compostas)
  - [exr:1-3-2-3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-03.dlt#L412-L429) (Seção 2 · Decompondo unidade de rede neural)
  - [exr:1-3-2-4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-03.dlt#L431-L466) (Seção 2 · Cascata sináptica completa: ligante $\to$ corrente $\to$ potencial $\to$ taxa)
  - [exr:1-3-3-1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-03.dlt#L583-L602) (Seção 3 · Injetividade e inversas simples)
  - [exr:1-3-3-2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-03.dlt#L604-L621) (Seção 3 · Decodificando concentração na equação de Hill)
  - [exr:1-3-3-3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-03.dlt#L623-L645) (Seção 3 · Restrição de domínio na parábola e no flanco esquerdo)
  - [exr:1-3-3-4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-03.dlt#L647-L672) (Seção 3 · Decodificação na sigmoide e crítica $f^{-1} \ne 1/f$)
  - [exr:1-3-4-1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-03.dlt#L759-L775) (Seção 4 · Transformações a partir de parábola base)
  - [exr:1-3-4-2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-03.dlt#L777-L792) (Seção 4 · Modulação aditiva versus multiplicativa na curva de sintonia)
  - [exr:1-3-4-3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-03.dlt#L794-L810) (Seção 4 · Lendo e deslocando a sigmoide $f$–$I$ e sua inversa)
  - [exr:1-3-4-4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-03.dlt#L812-L847) (Seção 4 · Miniatura do projeto final: curva de Naka–Rushton com limiar)

---

## 6. Conclusão da Revisão

A aula [tema-03.dlt](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-03.dlt) está **plenamente aprovada**. Trata-se de um capítulo modelar para a trilha, que estabelece com clareza conceitual e riqueza de conexões biológicas as fundações necessárias para o estudo do Cálculo Real (Módulo 2) e dos modelos de Machine Learning e Redes Neurais (Módulos 8 e 9). As sugestões apontadas na Tabela de Problemas e Observações tratam apenas de refinamentos cosméticos de formatação e padronização visual, podendo ser incorporadas em revisões editoriais futuras sem prejuízo da compilação e publicação imediatas.
