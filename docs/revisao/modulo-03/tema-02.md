# Relatório de Revisão Técnica — Módulo 03 · Tema 02 (Diferencial em Várias Variáveis)

- **Arquivo revisado:** [tema-02.dlt](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-02.dlt)
- **Script de figura associado:** [gradiente-ativacao.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/fig/gradiente-ativacao.py)
- **Figura gerada:** [gradiente-ativacao.svg](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/fig/gradiente-ativacao.svg)
- **Documentos de referência:** [PADRAO-AULAS.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/PADRAO-AULAS.md), [DELTA-COLA.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/DELTA-COLA.md), [Guia.txt](file:///home/al.pedro.alberti/trilha-neuro-computacional/referencias/Guia.txt) e [index.html](file:///home/al.pedro.alberti/trilha-neuro-computacional/index.html)
- **Data da revisão:** 14 de novembro de 2026
- **Perfil do revisor:** Matemático, Neurocientista Computacional e Professor de Alunos de Ciências Biológicas

---

## 1. Veredito

**APROVAR**

A aula cumpre com rigor e excelência todos os requisitos matemáticos, neurobiológicos, didáticos e de conformidade editorial estabelecidos pelo padrão da Trilha de Neurociência Computacional.

Todas as contas dos 12 exemplos e dos 18 exercícios (3 por seção) foram integralmente recalculadas analítica e numericamente, confirmando total exatidão. Nenhum erro matemático foi encontrado. A contextualização biológica é autêntica e realista ao longo de todas as 6 seções (mapas de ativação cortical em coordenadas milimétricas, biofísica de canais iônicos sob a lei de Ohm e equação de Nernst, quimiotaxia e navegação de cones de crescimento axonais, campos receptivos visuais bidimensionais e sensibilidade eletrofisiológica). A notação exigida para os Módulos 3, 4 e 5 (vetores em negrito minúsculo $\mathbf{x}$, matrizes em negrito maiúsculo $\mathbf{A}$, escalares em itálico e o operador gradiente $\nabla f$ sem negrito) foi respeitada com precisão uniforme em 100% das fórmulas.

A ligação conceitual com a passada direta (*forward pass*) e reversa (*backward pass*) na regra da cadeia constrói a base exata do *backpropagation* sem recorrer anacronicamente a redes neurais, preparando perfeitamente os alunos para os Módulos 4 (<mark>Otimização</mark>) e 9 (<mark>Deep Learning</mark>). O script Python da figura executa perfeitamente de forma autocontida e gera um arquivo SVG vetorial leve e legível. A estrutura XML Delta atende integralmente às regras duras de compilação.

Foram catalogadas 3 observações pontuais de aprimoramento pedagógico na tabela a seguir, sem impacto impeditivo.

---

## 2. Tabela de Problemas e Observações

| Severidade | Local | Trecho | Correção sugerida |
|---|---|---|---|
| Pedagógico | Subtema 5 (`sec:3-2-5`), `exr:3-2-5-1`, linhas ~873–874 | `D_{\mathbf{u}} f(2, 1) = \frac{140}{13} \approx 10{,}77` e `\|\nabla f(2, 1)\| = \sqrt{116} = 2\sqrt{29} \approx 10{,}77` | Como tanto $140/13 \approx 10{,}7692$ quanto $\sqrt{116} \approx 10{,}7703$ arredondam para $10{,}77$ com duas casas decimais, um aluno de Biologia pode achar que a direção $\mathbf{u}$ atinge exatamente o valor máximo ou que os dois números são idênticos. Na realidade, o ângulo entre $\mathbf{v} = (5, 12)$ e $\nabla f(2, 1) = (4, 10)$ é muito pequeno ($\theta \approx 0{,}82^\circ$, pois $\cos\theta \approx 0{,}9999$). Sugere-se explicitar na solução que, embora coincidam com duas casas decimais, vale estritamente $140/13 \approx 10{,}7692 < \sqrt{116} \approx 10{,}7703$, confirmando que a derivada direcional em $\mathbf{u}$ é estritamente menor que a taxa máxima teórica $\|\nabla f\|$. |
| Pedagógico | Subtema 4 (`sec:3-2-4`), `exr:3-2-4-1`, linha ~683 | `Calcule o gradiente $\nabla f(x, y)$ de $f(x, y) = x^2 e^y + 3xy^2$ e o gradiente $\nabla g(x, y, z)$ de $g(x, y, z) = \ln(x + 2y) + z^3 y$ (...)` | O exercício pede o cálculo de gradientes em 2D e 3D no início de uma seção cujo título no guia é "Derivadas parciais", logo após a seção "Gradiente". Embora didaticamente válido para integrar as primeiras derivadas antes de calcular derivadas segundas e matriz Hessiana no item (b), convém pontuar no enunciado que o cálculo do vetor gradiente serve aqui como etapa preparatória obrigatória para a obtenção das derivadas parciais de segunda ordem. |
| Pedagógico | Subtema 1 (`sec:3-2-1`), `def:3-2-derivada-parcial`, linha ~89 | `<intuition>Calcular $f_x$ na prática não exige nenhuma fórmula nova: basta olhar para $y$ (e $z$, se houver) como se fosse um número constante (...)</intuition>` | A analogia de "congelar" variáveis é clara e acessível. Para enriquecer a ponte com a prática biológica, sugere-se incluir uma menção explícita ao procedimento experimental de controle de variáveis ("manter temperatura, pH e oxigenação fixos para medir o efeito exclusivo da concentração de substrato"), conectando a derivada parcial à experiência cotidiana de laboratório dos biólogos. |

---

## 3. Recálculo e Auditoria de Todas as Contas

Todas as contas, limites, demonstrações, aproximações lineares e sistemas analíticos da aula foram recalculados passo a passo:

### 3.1 Subtema 1: Introdução (`sec:3-2-1`)

1. **[Exemplo 3.2.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-02.dlt#L93-L121) (`exm:3-2-mecanico-parciais`):**
   - Item (a): $f(x, y) = 3x^2 y - y^3 + 5x$.
     - Derivada parcial em $x$: $f_x(x, y) = \frac{\partial}{\partial x}(3x^2 y - y^3 + 5x) = 6xy + 5$.
     - Derivada parcial em $y$: $f_y(x, y) = \frac{\partial}{\partial y}(3x^2 y - y^3 + 5x) = 3x^2 - 3y^2$.
     - Avaliação no ponto $(1, 2)$:
       $$f_x(1, 2) = 6(1)(2) + 5 = 12 + 5 = 17,$$
       $$f_y(1, 2) = 3(1)^2 - 3(2)^2 = 3(1) - 3(4) = 3 - 12 = -9.$$
       **Correto.**
   - Item (b): $h(x, y) = x e^{2y}$.
     - $\frac{\partial h}{\partial x} = e^{2y} \cdot \frac{d}{dx}(x) = e^{2y}$.
     - $\frac{\partial h}{\partial y} = x \cdot \frac{\partial}{\partial y}(e^{2y}) = x(2e^{2y}) = 2x e^{2y}$.
     **Correto.**
   - Item (c): Curvas de nível de $q(x, y) = x^2 + 4y^2$:
     - Para $c = 4$: $x^2 + 4y^2 = 4 \iff \frac{x^2}{4} + \frac{y^2}{1} = 1$ (elipse com semieixos $a = 2$ em $x$ e $b = 1$ em $y$).
     - Para $c = 16$: $x^2 + 4y^2 = 16 \iff \frac{x^2}{16} + \frac{y^2}{4} = 1$ (elipse concêntrica com semieixos $a = 4$ e $b = 2$).
     **Correto.**

2. **[Exemplo 3.2.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-02.dlt#L123-L155) (`exm:3-2-mapa-corrente`):**
   - Item (a): Mapa de ativação cortical $Z(x, y) = 4\exp\!\left(-\frac{(x - 2)^2 + (y - 1)^2}{8}\right)$:
     - Domínio: a função exponencial e os polinômios estão definidos para todo $(x, y) \in \mathbb{R}^2$, logo $D = \mathbb{R}^2$.
     - Imagem: como $-\frac{(x-2)^2 + (y-1)^2}{8} \le 0$ para todo $(x, y)$, o expoente atinge o máximo $0$ apenas em $(2, 1)$, onde $e^0 = 1 \implies Z = 4$. Quando $(x, y) \to \infty$, o expoente tende a $-\infty$ e $e^{\dots} \to 0^+$. Portanto, $\text{Im}(Z) = (0, 4]$.
     - Curvas de nível $Z(x, y) = c$ ($0 < c < 4$):
       $$4\exp\!\left(-\frac{(x - 2)^2 + (y - 1)^2}{8}\right) = c \iff (x - 2)^2 + (y - 1)^2 = 8\ln\!\left(\frac{4}{c}\right).$$
       Como $0 < c < 4 \implies \frac{4}{c} > 1 \implies \ln(4/c) > 0$, trata-se de circunferências concêntricas de centro $(2, 1)$ e raio $R = \sqrt{8\ln(4/c)}$.
     - Derivadas parciais:
       $$Z_x(x, y) = 4e^{\dots} \cdot \left(-\frac{2(x - 2)}{8}\right) = \frac{2 - x}{4}\,Z(x, y),$$
       $$Z_y(x, y) = 4e^{\dots} \cdot \left(-\frac{2(y - 1)}{8}\right) = \frac{1 - y}{4}\,Z(x, y).$$
     - Avaliação em $(0, -1)$:
       $$(0 - 2)^2 + (-1 - 1)^2 = 4 + 4 = 8 \implies Z(0, -1) = 4e^{-8/8} = 4e^{-1} \approx 1{,}4715... \approx 1{,}47\text{ u.a.}$$
       $$Z_x(0, -1) = \frac{2 - 0}{4}(4e^{-1}) = 2e^{-1} \approx 0{,}7357... \approx 0{,}74\text{ u.a./mm},$$
       $$Z_y(0, -1) = \frac{1 - (-1)}{4}(4e^{-1}) = \frac{2}{4}(4e^{-1}) = 2e^{-1} \approx 0{,}74\text{ u.a./mm}.$$
       **Correto.**
   - Item (b): Corrente iônica $I(g, V, E) = g(V - E) = gV - gE$:
     $$\frac{\partial I}{\partial g} = V - E, \qquad \frac{\partial I}{\partial V} = g, \qquad \frac{\partial I}{\partial E} = -g.$$
     **Correto.**

3. **[Exercício 3.2.1.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-02.dlt#L162-L184) (`exr:3-2-1-1`):**
   - Item (a): $f(x, y) = 2x^3 - 4xy^2 + 7y$:
     $$f_x(x, y) = 6x^2 - 4y^2, \qquad f_y(x, y) = -8xy + 7.$$
     **Correto.**
   - Item (b): $g(x, y, z) = x e^{yz} + z^2$ em $(1, 0, 2)$:
     $$g_x = e^{yz} \implies g_x(1, 0, 2) = e^0 = 1,$$
     $$g_y = x z e^{yz} \implies g_y(1, 0, 2) = 1(2)e^0 = 2,$$
     $$g_z = x y e^{yz} + 2z \implies g_z(1, 0, 2) = 1(0)e^0 + 2(2) = 4.$$
     **Correto.**

4. **[Exercício 3.2.1.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-02.dlt#L186-L210) (`exr:3-2-1-2`):**
   - Item (a): $R(x, y) = 20\exp\left(-\frac{x^2}{2} - \frac{y^2}{8}\right) = c$:
     $$-\frac{x^2}{2} - \frac{y^2}{8} = \ln\left(\frac{c}{20}\right) \iff \frac{x^2}{2} + \frac{y^2}{8} = \ln\left(\frac{20}{c}\right) = k > 0.$$
     $$\frac{x^2}{2k} + \frac{y^2}{8k} = 1.$$
     Semieixo em $x$: $\sqrt{2k}$; semieixo em $y$: $\sqrt{8k} = 2\sqrt{2k}$. Elipses alongadas em $y$ com razão de eixos $2:1$. **Correto.**
   - Item (b): Derivadas parciais:
     $$R_x(x, y) = -x R(x, y), \qquad R_y(x, y) = -\frac{y}{4} R(x, y).$$
     Em $(1, 2)$: expoente $= -\frac{1}{2} - \frac{4}{8} = -1 \implies R(1, 2) = 20e^{-1} \approx 7{,}36\text{ Hz}$.
     $$R_x(1, 2) = -1(20e^{-1}) = -20e^{-1} \approx -7{,}36\text{ Hz/grau},$$
     $$R_y(1, 2) = -\frac{2}{4}(20e^{-1}) = -10e^{-1} \approx -3{,}68\text{ Hz/grau}.$$
     **Correto.**

5. **[Exercício 3.2.1.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-02.dlt#L212-L225) (`exr:3-2-1-3`):**
   - Função $f(x, y) = x^2 y + 3y$ em $(1, 2)$: $f(1, 2) = 1^2(2) + 3(2) = 8$.
   - Por definição para $f_x(1, 2)$:
     $$f(1 + h, 2) = (1 + h)^2(2) + 3(2) = 2(1 + 2h + h^2) + 6 = 8 + 4h + 2h^2,$$
     $$f_x(1, 2) = \lim_{h \to 0} \frac{8 + 4h + 2h^2 - 8}{h} = \lim_{h \to 0}(4 + 2h) = 4.$$
   - Por definição para $f_y(1, 2)$:
     $$f(1, 2 + h) = 1^2(2 + h) + 3(2 + h) = 2 + h + 6 + 3h = 8 + 4h,$$
     $$f_y(1, 2) = \lim_{h \to 0} \frac{8 + 4h - 8}{h} = \lim_{h \to 0} 4 = 4.$$
   - Regras mecânicas: $f_x(x, y) = 2xy \implies f_x(1, 2) = 4$; $f_y(x, y) = x^2 + 3 \implies f_y(1, 2) = 1 + 3 = 4$. Coincidem perfeitamente. **Correto.**

---

### 3.2 Subtema 2: Diferenciabilidade e continuidade (`sec:3-2-2`)

1. **[Exemplo 3.2.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-02.dlt#L251-L273) (`exm:3-2-contraexemplo-limite`):**
   - Função $f(x, y) = \frac{xy}{x^2 + y^2}$ para $(x, y) \ne (0, 0)$ e $f(0, 0) = 0$.
   - Item (a): ao longo de $y = mx$ ($x \ne 0$):
     $$f(x, mx) = \frac{x(mx)}{x^2 + m^2 x^2} = \frac{m}{1 + m^2}.$$
     Para $m = 0$ ($y = 0$), $f \to 0$; para $m = 1$ ($y = x$), $f \to \frac{1}{2}$; para $m = -1$ ($y = -x$), $f \to -\frac{1}{2}$. Como os limites dependem do caminho, $\lim_{(x, y)\to(0,0)} f(x, y)$ não existe.
   - Item (b): parciais na origem:
     $$f_x(0, 0) = \lim_{h \to 0} \frac{f(h, 0) - f(0, 0)}{h} = \lim_{h \to 0} \frac{0 - 0}{h} = 0,$$
     $$f_y(0, 0) = \lim_{h \to 0} \frac{f(0, h) - f(0, 0)}{h} = \lim_{h \to 0} \frac{0 - 0}{h} = 0.$$
     Ambas existem e são nulas, embora $f$ seja descontínua. **Correto.**

2. **[Teorema 3.2.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-02.dlt#L289-L297) (`thm:3-2-dif-cont`):**
   - Demonstração: $f(a + h, b + k) - f(a, b) = f_x(a, b)h + f_y(a, b)k + \sqrt{h^2 + k^2}\varepsilon(h, k)$. Como $\lim_{(h,k)\to(0,0)}\varepsilon(h,k)=0$, todos os termos tendem a $0$, logo $\lim_{(h,k)\to(0,0)} f(a+h, b+k) = f(a, b)$. Demonstração rigorosa e correta.

3. **[Exemplo 3.2.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-02.dlt#L306-L333) (`exm:3-2-aprox-corrente`):**
   - $I(g, V) = g(V + 70)$, com $(g_0, V_0) = (10\text{ nS}, -50\text{ mV})$:
     - $I(10, -50) = 10(-50 + 70) = 10(20) = 200\text{ pA}$.
     - $I_g(g, V) = V + 70 \implies I_g(10, -50) = 20\text{ pA/nS}$.
     - $I_V(g, V) = g \implies I_V(10, -50) = 10\text{ pA/mV}$.
     - Aproximação linear: $L(g, V) = 200 + 20(g - 10) + 10(V + 50)$.
   - Perturbação $\Delta g = 1\text{ nS}$, $\Delta V = 2\text{ mV}$:
     - $\Delta I_{\text{lin}} = 20(1) + 10(2) = 40\text{ pA} \implies I_{\text{aprox}} = 240\text{ pA}$.
     - Valor exato: $I(11, -48) = 11(-48 + 70) = 11(22) = 242\text{ pA}$.
     - Variação exata: $242 - 200 = 42\text{ pA}$.
     - Erro da aproximação: $242 - 240 = 2\text{ pA} = \Delta g \cdot \Delta V = 1 \cdot 2$.
     **Correto.**

4. **[Exercício 3.2.2.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-02.dlt#L343-L365) (`exr:3-2-2-1`):**
   - $f(x, y) = x^2 + 3xy - y^2$ em $(2, 1)$:
     - $f(2, 1) = 2^2 + 3(2)(1) - 1^2 = 4 + 6 - 1 = 9$.
     - $f_x = 2x + 3y \implies f_x(2, 1) = 4 + 3 = 7$.
     - $f_y = 3x - 2y \implies f_y(2, 1) = 6 - 2 = 4$.
     - $L(x, y) = 9 + 7(x - 2) + 4(y - 1)$.
   - Em $(2{,}1;\, 0{,}9)$ ($h = 0{,}1$, $k = -0{,}1$):
     - $L(2{,}1;\, 0{,}9) = 9 + 7(0{,}1) + 4(-0{,}1) = 9 + 0{,}7 - 0{,}4 = 9{,}3$.
     - Valor exato: $2{,}1^2 + 3(2{,}1)(0{,}9) - 0{,}9^2 = 4{,}41 + 5{,}67 - 0{,}81 = 9{,}27$.
     - Erro: $|9{,}30 - 9{,}27| = 0{,}03$.
     **Correto.**

5. **[Exercício 3.2.2.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-02.dlt#L367-L385) (`exr:3-2-2-2`):**
   - Item (a): $\lim_{(x, y) \to (0, 0)} \frac{x^2 - y^2}{x^2 + y^2}$. Ao longo de $y = 0$: $\frac{x^2}{x^2} = 1 \to 1$. Ao longo de $x = 0$: $\frac{-y^2}{y^2} = -1 \to -1$. Como $1 \ne -1$, o limite não existe.
   - Item (b): $\lim_{(x, y) \to (0, 0)} \frac{x^2 y}{x^2 + y^2}$. Como $0 \le x^2 \le x^2 + y^2$, temos $0 \le \frac{x^2}{x^2 + y^2} \le 1$. Multiplicando por $|y|$: $0 \le \left|\frac{x^2 y}{x^2 + y^2}\right| \le |y|$. Como $|y| \to 0$, pelo teorema do confronto o limite vale $0$.
   **Correto.**

6. **[Exercício 3.2.2.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-02.dlt#L387-L408) (`exr:3-2-2-3`):**
   - Item (a): $Z_x = \frac{2-x}{4}Z$ e $Z_y = \frac{1-y}{4}Z$ são contínuas em $\mathbb{R}^2$. Pelo Teorema 3.2.2, $Z$ é diferenciável em todo $\mathbb{R}^2$.
   - Item (b): $Z(0, -1) = 4e^{-1}$, $Z_x(0, -1) = Z_y(0, -1) = 2e^{-1}$.
     Para $(0{,}2;\, -0{,}8)$, temos $h = 0{,}2$ e $k = 0{,}2$:
     $$Z(0{,}2;\, -0{,}8) \approx 4e^{-1} + 2e^{-1}(0{,}2) + 2e^{-1}(0{,}2) = 4{,}8e^{-1}.$$
     Como $e^{-1} \approx 0{,}3678794$, $4{,}8 \cdot 0{,}3678794 \approx 1{,}7658... \approx 1{,}77\text{ u.a.}$ (valor exato: $4e^{-0{,}81} \approx 1{,}7794... \approx 1{,}78\text{ u.a.}$).
     **Correto.**

---

### 3.3 Subtema 3: Gradiente (`sec:3-2-3`)

1. **[Exemplo 3.2.5](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-02.dlt#L462-L483) (`exm:3-2-gradiente-cortical`):**
   - $\nabla Z(x, y) = \frac{Z(x, y)}{4}(2 - x, 1 - y)$.
   - Como $\frac{Z(x, y)}{4} > 0$, $\nabla Z$ aponta paralelamente a $(2 - x, 1 - y) = (2, 1) - (x, y)$, ou seja, diretamente para o pico $(2, 1)$.
   - Em $(0, -1)$: $Z(0, -1) = 4e^{-1} \implies \nabla Z(0, -1) = (2e^{-1}, 2e^{-1})\text{ u.a./mm}$.
     $$\|\nabla Z(0, -1)\| = \sqrt{(2e^{-1})^2 + (2e^{-1})^2} = 2\sqrt{2}\,e^{-1} \approx 1{,}0405... \approx 1{,}04\text{ u.a./mm}.$$
   - No pico $(2, 1)$: $\nabla Z(2, 1) = \mathbf{0}$.
   **Correto.**

2. **[Exemplo 3.2.6](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-02.dlt#L485-L506) (`exm:3-2-quimiotaxia`):**
   - $C(x, y) = 10\exp\!\left(-\frac{x^2 + y^2}{4}\right)$:
     $$\nabla C(x, y) = -\frac{C(x, y)}{2}(x, y).$$
   - Em $(2, 0)$: $C(2, 0) = 10e^{-4/4} = 10e^{-1}\text{ nmol/L}$.
     $$\nabla C(2, 0) = -\frac{10e^{-1}}{2}(2, 0) = (-10e^{-1},\; 0)\text{ nmol/(L}\cdot\text{mm)}.$$
     Sentido atraído: $(-1, 0)$ (para a fonte $(0, 0)$), taxa $10e^{-1} \approx 3{,}68\text{ nmol/(L}\cdot\text{mm)}$.
     Sentido repelido: $(1, 0)$ (afastamento da fonte).
     **Correto.**

3. **[Exercício 3.2.3.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-02.dlt#L513-L535) (`exr:3-2-3-1`):**
   - Item (a): $f(x, y) = x^2 y - 3y^2 + 4x \implies \nabla f = (2xy + 4, x^2 - 6y)$.
     Em $(1, 2)$: $\nabla f(1, 2) = (2(1)(2) + 4, 1^2 - 6(2)) = (8, -11)$. **Correto.**
   - Item (b): $g(x, y, z) = x^2 + 2yz - e^{x - z} \implies \nabla g = (2x - e^{x - z}, 2z, 2y + e^{x - z})$.
     Em $(1, 3, 1)$ ($x - z = 0$): $\nabla g(1, 3, 1) = (2(1) - 1, 2(1), 2(3) + 1) = (1, 2, 7)$. **Correto.**

4. **[Exercício 3.2.3.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-02.dlt#L537-L562) (`exr:3-2-3-2`):**
   - $J(w_1, w_2) = (w_1 - 3)^2 + 2(w_2 + 1)^2 \implies \nabla J = (2(w_1 - 3), 4(w_2 + 1))$.
   - Em $\mathbf{w} = (1, 1)$: $J(1, 1) = (-2)^2 + 2(2)^2 = 4 + 8 = 12$; $\nabla J(1, 1) = (-4, 8)$.
   - Passo com $\eta = 0{,}25$:
     $$\mathbf{w}_{\text{novo}} = (1, 1) - 0{,}25(-4, 8) = (1 - (-1), 1 - 2) = (2, -1).$$
     Novo custo: $J(2, -1) = (2 - 3)^2 + 2(-1 + 1)^2 = 1 + 0 = 1 < 12$. Redução verificada. **Correto.**

5. **[Exercício 3.2.3.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-02.dlt#L564-L587) (`exr:3-2-3-3`):**
   - $C(x, y, z) = 100(1 + x^2 + y^2 + z^2)^{-1}$:
     $$\nabla C(x, y, z) = -\frac{200}{(1 + x^2 + y^2 + z^2)^2}\,(x, y, z).$$
   - Em $P = (1, 2, 2)$: $1 + 1^2 + 2^2 + 2^2 = 10 \implies 10^2 = 100$.
     $$\nabla C(1, 2, 2) = -\frac{200}{100}(1, 2, 2) = (-2, -4, -4)\;\mu\text{M/mm}.$$
     $$\|\nabla C(1, 2, 2)\| = \sqrt{(-2)^2 + (-4)^2 + (-4)^2} = \sqrt{4 + 16 + 16} = \sqrt{36} = 6\;\mu\text{M/mm}.$$
     Como $\nabla C(P) = 2(-1, -2, -2) = 2\bigl((0,0,0) - (1,2,2)\bigr)$, o gradiente aponta diretamente para a origem. **Correto.**

---

### 3.4 Subtema 4: Derivadas parciais (`sec:3-2-4`)

1. **[Exemplo 3.2.7](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-02.dlt#L625-L647) (`exm:3-2-schwarz-hessiana`):**
   - $f(x, y) = x^3 y^2 + \sin(2x) + e^{3y}$:
     - $f_x = 3x^2 y^2 + 2\cos(2x)$, $f_y = 2x^3 y + 3e^{3y}$.
     - $f_{xx} = 6xy^2 - 4\sin(2x)$, $f_{xy} = 6x^2 y$.
     - $f_{yx} = 6x^2 y$, $f_{yy} = 2x^3 + 9e^{3y}$.
     - Verificação de Schwarz: $f_{xy} = f_{yx} = 6x^2 y$.
   - Em $(0, 0)$: $f_{xx}(0, 0) = 0$, $f_{xy} = f_{yx} = 0$, $f_{yy}(0, 0) = 9$.
     $$\mathbf{H}_f(0, 0) = \begin{pmatrix} 0 & 0 \\ 0 & 9 \end{pmatrix}.$$
     **Correto.**

2. **[Exemplo 3.2.8](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-02.dlt#L649-L673) (`exm:3-2-nernst-sensibilidade`):**
   - $E(c_{\text{ext}}, c_{\text{int}}) = \frac{RT}{zF}\ln\left(\frac{c_{\text{ext}}}{c_{\text{int}}}\right)$ com $\frac{RT}{F} = 26{,}7\text{ mV}$, $z = 1$, $c_{\text{ext}} = 5\text{ mM}$, $c_{\text{int}} = 140\text{ mM}$:
     - $E_K = 26{,}7\ln(5/140) = -26{,}7\ln(28) \approx -26{,}7(3{,}3322) \approx -88{,}97... \approx -89\text{ mV}$.
     - Sensibilidades:
       $$\frac{\partial E}{\partial c_{\text{ext}}} = \frac{26{,}7}{5} = +5{,}34\text{ mV/mM},$$
       $$\frac{\partial E}{\partial c_{\text{int}}} = -\frac{26{,}7}{140} \approx -0{,}1907... \approx -0{,}191\text{ mV/mM}.$$
       Razão de magnitudes: $5{,}34 / 0{,}1907 \approx 28 = 140/5$.
       **Correto.**

3. **[Exercício 3.2.4.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-02.dlt#L680-L702) (`exr:3-2-4-1`):**
   - Item (a):
     - $f(x, y) = x^2 e^y + 3xy^2 \implies \nabla f = (2xe^y + 3y^2, x^2 e^y + 6xy)$.
     - $g(x, y, z) = \ln(x + 2y) + z^3 y \implies \nabla g = \left(\frac{1}{x + 2y}, \frac{2}{x + 2y} + z^3, 3z^2 y\right)$.
   - Item (b):
     - $f_{xx} = 2e^y$, $f_{xy} = 2xe^y + 6y$, $f_{yx} = 2xe^y + 6y$, $f_{yy} = x^2 e^y + 6x$.
     - Em $(1, 0)$: $f_{xx}(1, 0) = 2$, $f_{xy} = f_{yx} = 2$, $f_{yy}(1, 0) = 1 + 6 = 7$.
     $$\mathbf{H}_f(1, 0) = \begin{pmatrix} 2 & 2 \\ 2 & 7 \end{pmatrix}.$$
     **Correto.**

4. **[Exercício 3.2.4.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-02.dlt#L704-L729) (`exr:3-2-4-2`):**
   - $\text{Na}^+$, $z = 1$, $c_{\text{ext}} = 145\text{ mM}$, $c_{\text{int}} = 15\text{ mM}$:
     - Item (a): $\frac{\partial E}{\partial c_{\text{ext}}} = \frac{26{,}7}{145} \approx +0{,}1841... \approx +0{,}184\text{ mV/mM}$; $\frac{\partial E}{\partial c_{\text{int}}} = -\frac{26{,}7}{15} = -1{,}78\text{ mV/mM}$.
     - Item (b): $\Delta c_{\text{int}} = 3\text{ mM} \implies \Delta E \approx (-1{,}78) \cdot 3 = -5{,}34\text{ mV}$.
     - Item (c): $\frac{\partial^2 E}{\partial c_{\text{int}}^2} = \frac{\partial}{\partial c_{\text{int}}}(-26{,}7 c_{\text{int}}^{-1}) = \frac{26{,}7}{c_{\text{int}}^2} > 0$.
     **Correto.**

5. **[Exercício 3.2.4.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-02.dlt#L730-L754) (`exr:3-2-4-3`):**
   - Item (a): $Z_{xx} = \frac{(x-2)^2 - 4}{16}Z$, $Z_{xy} = \frac{(x-2)(y-1)}{16}Z$, $Z_{yy} = \frac{(y-1)^2 - 4}{16}Z$.
     No pico $(2, 1)$ com $Z(2, 1) = 4$:
     $Z_{xx}(2, 1) = \frac{-4}{16}(4) = -1$, $Z_{xy}(2, 1) = 0$, $Z_{yy}(2, 1) = -1$.
     $$\mathbf{H}_Z(2, 1) = \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix}.$$
   - Item (b): $\phi(x, y, z) = x e^{-y} + \sin(xz)$:
     $$\nabla \phi(x, y, z) = \bigl(e^{-y} + z\cos(xz),\; -x e^{-y},\; x\cos(xz)\bigr).$$
     **Correto.**

---

### 3.5 Subtema 5: Derivada direcional (`sec:3-2-5`)

1. **[Teorema 3.2.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-02.dlt#L778-L790) e [Corolário 3.2.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-02.dlt#L794-L809):**
   - Demonstrações de $D_{\mathbf{u}} f = \nabla f \cdot \mathbf{u} = \|\nabla f\|\cos\theta$, valor máximo $\|\nabla f\|$, mínimo $-\|\nabla f\|$ e ortogonalidade às curvas de nível ($\cos\theta = 0 \iff \theta = \pi/2$). Ambas rigorosas e corretas.

2. **[Exemplo 3.2.9](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-02.dlt#L811-L835) (`exm:3-2-direcional-3d`):**
   - $f(x, y, z) = x^2 y - y z^2 + 3x$ em $P = (1, 2, -1)$ na direção de $\mathbf{v} = (2, -1, 2)$:
     - $\|\mathbf{v}\| = \sqrt{4 + 1 + 4} = 3 \implies \mathbf{u} = (2/3, -1/3, 2/3)$.
     - $\nabla f = (2xy + 3, x^2 - z^2, -2yz) \implies \nabla f(1, 2, -1) = (7, 0, 4)$.
     - $D_{\mathbf{u}} f = (7, 0, 4) \cdot (2/3, -1/3, 2/3) = \frac{14}{3} + 0 + \frac{8}{3} = \frac{22}{3} \approx 7{,}33$.
     - Taxa máxima: $\|\nabla f(P)\| = \sqrt{49 + 0 + 16} = \sqrt{65} \approx 8{,}0622... \approx 8{,}06$, na direção $\frac{1}{\sqrt{65}}(7, 0, 4)$.
     **Correto.**

3. **[Exemplo 3.2.10](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-02.dlt#L837-L856) (`exm:3-2-eletrodo-cortical`):**
   - $Z(x, y)$ em $(0, -1)$ com $\nabla Z(0, -1) = (2e^{-1}, 2e^{-1})$:
     - Item (a): $\mathbf{v} = (3, 4) \implies \|\mathbf{v}\| = 5 \implies \mathbf{u} = (0{,}6;\, 0{,}8)$.
       $$D_{\mathbf{u}} Z = (2e^{-1}, 2e^{-1}) \cdot (0{,}6;\, 0{,}8) = 2e^{-1}(1{,}4) = 2{,}8e^{-1} \approx 1{,}0300... \approx 1{,}03\text{ u.a./mm}.$$
     - Item (b): $\mathbf{w} = (-1, 1) \implies \mathbf{u}_\perp = (-1/\sqrt{2}, 1/\sqrt{2})$.
       $$D_{\mathbf{u}_\perp} Z = (2e^{-1}, 2e^{-1}) \cdot (-1/\sqrt{2}, 1/\sqrt{2}) = 0\text{ u.a./mm}.$$
     **Correto.**

4. **[Exercício 3.2.5.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-02.dlt#L863-L876) (`exr:3-2-5-1`):**
   - $f(x, y) = x^2 y + 2y^3$ em $(2, 1)$ na direção de $\mathbf{v} = (5, 12)$:
     - $\|\mathbf{v}\| = \sqrt{25 + 144} = 13 \implies \mathbf{u} = (5/13, 12/13)$.
     - $\nabla f = (2xy, x^2 + 6y^2) \implies \nabla f(2, 1) = (4, 10)$.
     - $D_{\mathbf{u}} f(2, 1) = (4, 10) \cdot (5/13, 12/13) = \frac{20 + 120}{13} = \frac{140}{13} \approx 10{,}7692... \approx 10{,}77$.
     - Taxa máxima: $\|\nabla f(2, 1)\| = \sqrt{16 + 100} = \sqrt{116} = 2\sqrt{29} \approx 10{,}7703... \approx 10{,}77$.
     **Correto.**

5. **[Exercício 3.2.5.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-02.dlt#L878-L900) (`exr:3-2-5-2`):**
   - $G(x, y) = 8 - 0{,}5x^2 - y^2$ em $(2, 1)$ na direção de $\mathbf{v} = (-4, 3)$:
     - $\nabla G = (-x, -2y) \implies \nabla G(2, 1) = (-2, -2)$.
     - $\|\mathbf{v}\| = 5 \implies \mathbf{u} = (-0{,}8;\, 0{,}6)$.
     - Item (a): $D_{\mathbf{u}} G(2, 1) = (-2, -2) \cdot (-0{,}8;\, 0{,}6) = 1{,}6 - 1{,}2 = +0{,}4\text{ mmol/(L}\cdot\text{mm)}$.
     - Item (b): taxa máxima $=\|\nabla G(2, 1)\| = \sqrt{4 + 4} = 2\sqrt{2} \approx 2{,}8284... \approx 2{,}83\text{ mmol/(L}\cdot\text{mm)}$, na direção $\hat{\mathbf{d}} = (-1/\sqrt{2}, -1/\sqrt{2})$.
     **Correto.**

6. **[Exercício 3.2.5.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-02.dlt#L902-L925) (`exr:3-2-5-3`):**
   - $h(x, y, z) = x e^y + y z^2$ em $P = (2, 0, 1)$:
     - Item (a): $\nabla h = (e^y, x e^y + z^2, 2yz) \implies \nabla h(2, 0, 1) = (1, 2(1) + 1, 0) = (1, 3, 0)$.
     - Item (b): $\mathbf{v} = (1, -2, 2) \implies \|\mathbf{v}\| = 3 \implies \mathbf{u} = (1/3, -2/3, 2/3)$.
       $$D_{\mathbf{u}} h(P) = (1, 3, 0) \cdot (1/3, -2/3, 2/3) = \frac{1}{3} - \frac{6}{3} + 0 = -\frac{5}{3}.$$
     - Item (c): $\mathbf{w} = (w_1, w_2, 0)$ com $(1, 3, 0) \cdot (w_1, w_2, 0) = 0 \implies w_1 + 3w_2 = 0 \implies w_1 = -3w_2$.
       Vetor diretor: $(-3, 1, 0)$, de norma $\sqrt{9 + 1} = \sqrt{10}$. Normalizando: $\mathbf{w} = \left(-\frac{3}{\sqrt{10}}, \frac{1}{\sqrt{10}}, 0\right)$.
     **Correto.**

---

### 3.6 Subtema 6: Regra da cadeia (`sec:3-2-6`)

1. **[Exemplo 3.2.11](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-02.dlt#L982-L1015) (`exm:3-2-forward-backward`):**
   - Cadeia: $u = w_1 x_1 + w_2 x_2$, $v = e^u$, $L = (v - y)^2$ com $x_1 = 2, x_2 = -3, y = 5, w_1 = 3, w_2 = 2$:
     - Item (a) — Passada direta (*forward pass*):
       $$u = 3(2) + 2(-3) = 6 - 6 = 0,$$
       $$v = e^0 = 1,$$
       $$L = (1 - 5)^2 = (-4)^2 = 16.$$
     - Item (b) — Passada reversa (*backward pass*):
       $$\frac{\partial L}{\partial v} = 2(v - y) = 2(1 - 5) = -8,$$
       $$\frac{dv}{du} = e^u = e^0 = 1 \implies \frac{\partial L}{\partial u} = \frac{\partial L}{\partial v}\cdot\frac{dv}{du} = (-8)(1) = -8.$$
       Reaproveitando $\frac{\partial L}{\partial u} = -8$ com $\frac{\partial u}{\partial w_1} = x_1 = 2$ e $\frac{\partial u}{\partial w_2} = x_2 = -3$:
       $$\frac{\partial L}{\partial w_1} = (-8)(2) = -16, \qquad \frac{\partial L}{\partial w_2} = (-8)(-3) = 24.$$
     - Item (c) — Conferência direta: $L(w_1, w_2) = (e^{2w_1 - 3w_2} - 5)^2$:
       $$\frac{\partial L}{\partial w_1} = 2(e^0 - 5)e^0(2) = 2(-4)(1)(2) = -16,$$
       $$\frac{\partial L}{\partial w_2} = 2(e^0 - 5)e^0(-3) = 2(-4)(1)(-3) = 24.$$
       Coincidência absoluta entre os dois métodos. **Correto.**

2. **[Exemplo 3.2.12](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-02.dlt#L1017-L1030) (`exm:3-2-corrente-temporal`):**
   - $I(g, V) = g(V + 70)$, com $g(t) = 2t + 4\text{ nS}$, $V(t) = -60 + 5t^2\text{ mV}$ em $t = 2\text{ ms}$:
     - $g(2) = 8\text{ nS}$, $g'(2) = 2\text{ nS/ms}$.
     - $V(2) = -60 + 5(4) = -40\text{ mV}$, $V'(2) = 10(2) = 20\text{ mV/ms}$.
     - $\frac{\partial I}{\partial g} = V + 70 = -40 + 70 = 30\text{ pA/nS}$.
     - $\frac{\partial I}{\partial V} = g = 8\text{ pA/mV}$.
     - Pela regra da cadeia:
       $$\frac{dI}{dt}\Big|_{t=2} = 30(2) + 8(20) = 60 + 160 = 220\text{ pA/ms}.$$
     - Conferência direta: $I(t) = (2t + 4)(5t^2 + 10) = 10t^3 + 20t^2 + 20t + 40$.
       $I'(t) = 30t^2 + 40t + 20 \implies I'(2) = 30(4) + 40(2) + 20 = 120 + 80 + 20 = 220\text{ pA/ms}$.
       **Correto.**

3. **[Exercício 3.2.6.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-02.dlt#L1037-L1059) (`exr:3-2-6-1`):**
   - Item (a): $f(x, y) = x^2 y + 3y$ e $\mathbf{r}(t) = (t^2, 2t + 1)$ em $t = 1$:
     - $\mathbf{r}(1) = (1, 3)$, $\mathbf{r}'(1) = (2, 2)$.
     - $\nabla f(x, y) = (2xy, x^2 + 3) \implies \nabla f(1, 3) = (6, 4)$.
     - $\frac{df}{dt}|_{t=1} = (6, 4) \cdot (2, 2) = 12 + 8 = 20$.
   - Item (b): $z = x e^y$ com $x(s, t) = s^2 + t$ e $y(s, t) = s - 2t$ em $(s, t) = (2, 1)$:
     - $x(2, 1) = 4 + 1 = 5$, $y(2, 1) = 2 - 2 = 0$.
     - $z_x = e^0 = 1$, $z_y = 5e^0 = 5$.
     - $x_s = 4, x_t = 1, y_s = 1, y_t = -2$.
     - $\frac{\partial z}{\partial s} = 1(4) + 5(1) = 9$; $\frac{\partial z}{\partial t} = 1(1) + 5(-2) = -9$.
     **Correto.**

4. **[Exercício 3.2.6.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-02.dlt#L1060-L1080) (`exr:3-2-6-2`):**
   - Sonda com $\mathbf{r}(t) = (t, t - 1)\text{ mm}$, velocidade $\mathbf{r}'(t) = (1, 1)\text{ mm/s}$:
     - Item (a): em $t = 0\text{ s}$, $\mathbf{r}(0) = (0, -1)\text{ mm}$, onde $\nabla Z = (2e^{-1}, 2e^{-1})\text{ u.a./mm}$:
       $$\frac{dZ}{dt}\Big|_{t=0} = (2e^{-1}, 2e^{-1}) \cdot (1, 1) = 4e^{-1} \approx 1{,}47\text{ u.a./s}.$$
     - Item (b): em $t = 2\text{ s}$, $\mathbf{r}(2) = (2, 1)\text{ mm}$ (pico), onde $\nabla Z = (0, 0)$:
       $$\frac{dZ}{dt}\Big|_{t=2} = (0, 0) \cdot (1, 1) = 0\text{ u.a./s}.$$
     **Correto.**

5. **[Exercício 3.2.6.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-02.dlt#L1082-L1112) (`exr:3-2-6-3`):**
   - Cadeia: $u = w_1 x_1 + w_2 x_2$, $v = u^2 + 1$, $L = \frac{1}{2}(v - y)^2$ com $x_1 = 3, x_2 = -1, y = 9, w_1 = 1, w_2 = 1$:
     - Item (a) — Passada direta: $u = 1(3) + 1(-1) = 2$, $v = 2^2 + 1 = 5$, $L = \frac{1}{2}(5 - 9)^2 = \frac{16}{2} = 8$.
     - Item (b) — Passada reversa:
       $$\frac{\partial L}{\partial v} = v - y = 5 - 9 = -4,$$
       $$\frac{dv}{du} = 2u = 4 \implies \frac{\partial L}{\partial u} = (-4)(4) = -16.$$
       $$\frac{\partial L}{\partial w_1} = (-16)(3) = -48, \qquad \frac{\partial L}{\partial w_2} = (-16)(-1) = 16.$$
     - Item (c) — Conferência direta: $L(w_1, w_2) = \frac{1}{2}\bigl((3w_1 - w_2)^2 - 8\bigr)^2$:
       $$\frac{\partial L}{\partial w_1} = \bigl((3w_1 - w_2)^2 - 8\bigr) \cdot 2(3w_1 - w_2) \cdot 3 \implies (4 - 8)(4)(3) = -48,$$
       $$\frac{\partial L}{\partial w_2} = \bigl((3w_1 - w_2)^2 - 8\bigr) \cdot 2(3w_1 - w_2) \cdot (-1) \implies (-4)(4)(-1) = 16.$$
       Coincidência exata. **Correto.**

**Declaração conclusiva sobre a matemática:** Nenhum erro matemático encontrado.

---

## 4. Auditoria dos Critérios Editoriais e Pedagógicos

### 4.1 Subtemas do Guia e Estrutura Geral

O tema coberto é o Tema 3.2 — Diferencial em várias variáveis (Nível: Intermediário), com 6 seções numeradas exatamente na ordem estipulada pelo guia oficial ([Guia.txt](file:///home/al.pedro.alberti/trilha-neuro-computacional/referencias/Guia.txt)):
1. `sec:3-2-1`: **Introdução** (funções de várias variáveis, domínio, imagem, gráficos, curvas de nível, mapas de contorno e introdução operacional às derivadas parciais);
2. `sec:3-2-2`: **Diferenciabilidade e continuidade** (limite em $\mathbb{R}^2$, descontinuidade por caminhos distintos, plano tangente, aproximação linear e teoremas fundamentais);
3. `sec:3-2-3`: **Gradiente** (definição do campo gradiente, interpretação geométrica, conexão direta com gradiente descendente e mapa de contorno da ativação cortical com figura);
4. `sec:3-2-4`: **Derivadas parciais** (segunda ordem, matriz Hessiana $2 \times 2$, teorema de Schwarz/Clairaut e sensibilidade paramétrica na biofísica);
5. `sec:3-2-5`: **Derivada direcional** (definição por limite, fórmula pelo produto escalar $\nabla f \cdot \mathbf{u}$, demonstração analítica das direções de máximo/mínimo crescimento e ortogonalidade);
6. `sec:3-2-6`: **Regra da cadeia** (trajetórias, duas variáveis independentes, diagrama de árvore e ligação conceitual rigorosa ao *backpropagation* via *forward* e *backward pass*).

A aula fecha com as seções obrigatórias "Resumo" (`sec:3-2-resumo`) com 7 itens substanciais e "Para ir além" (`sec:3-2-alem`) apontando os materiais do módulo (Diomara Pinto e vídeos de visualização).

### 4.2 Exercícios: Dicas e Soluções

A aula contém exatamente 18 exercícios (3 por seção temática), atendendo rigorosamente à gradação "Básico", "Intermediário" e "Avançado":
- Todos os 18 exercícios trazem `<hint><title>Ver dica</title>...</hint>` com pistas reais e pertinentes;
- Todos os 18 exercícios trazem `<solution collapsible="true" collapsed="true">...</solution>` com resolução completa, demonstrando todo o desenvolvimento analítico, substituição de valores e interpretação do resultado, nunca apenas a resposta final.

### 4.3 Contextualização Biológica

Cada uma das 6 seções possui exemplos e exercícios biológicos detalhados com parâmetros fisiológicos realistas:
- **Subtema 1:** Mapa de ativação cortical gaussiano em milímetros (`exm:3-2-mapa-corrente`), corrente iônica através de canais dependente de condutância e potenciais (`exm:3-2-mapa-corrente`) e campo receptivo bidimensional de neurônio visual em graus de ângulo visual (`exr:3-2-1-2`);
- **Subtema 2:** Ponto de operação e linearização de corrente sináptica em $\text{nS}$, $\text{mV}$ e $\text{pA}$ (`exm:3-2-aprox-corrente`) e estimativa linear da ativação cortical (`exr:3-2-2-3`);
- **Subtema 3:** Guiamento axonal por quimiotaxia e gradiente de moléculas-guia para cones de crescimento (`exm:3-2-quimiotaxia`), gradiente do mapa cortical apontando para o pico (`exm:3-2-gradiente-cortical`) e difusão tridimensional de fator trófico glial no parênquima cerebral (`exr:3-2-3-3`);
- **Subtema 4:** Sensibilidade do potencial de equilíbrio de Nernst do $\text{K}^+$ com concentrações fisiológicas clássicas ($5\text{ mM}$ ext / $140\text{ mM}$ int) a $37\,^\circ\text{C}$ (`exm:3-2-nernst-sensibilidade`) e do $\text{Na}^+$ ($145\text{ mM}$ ext / $15\text{ mM}$ int) (`exr:3-2-4-2`);
- **Subtema 5:** Eletrodo exploratório navegando sobre o mapa cortical em direções arbitrárias (`exm:3-2-eletrodo-cortical`) e quimiotaxia bacteriana em gradiente bidimensional de glicose (`exr:3-2-5-2`);
- **Subtema 6:** Dinâmica temporal de corrente sináptica com condutância e voltagem variando no tempo (`exm:3-2-corrente-temporal`) e sonda registrando ativação cortical ao longo de uma trajetória temporal paramétrica $\mathbf{r}(t)$ (`exr:3-2-6-2`).

### 4.4 Afirmações de Neurociência

Todas as afirmações de neurociência e biofísica estão em perfeita consonância com a literatura padrão (Kandel et al., *Principles of Neural Science*; Dayan & Abbott, *Theoretical Neuroscience*):
- Equação de Nernst com constante térmica $RT/F \approx 26{,}7\text{ mV}$ a $37\,^\circ\text{C}$, concentrações intra e extracelulares de mamíferos para $\text{K}^+$ ($140/5\text{ mM}$) e $\text{Na}^+$ ($15/145\text{ mM}$), potenciais de repouso e reversão em torno de $-70\text{ mV}$;
- Consistência dimensional em eletrofisiologia: $1\text{ nS} \times 1\text{ mV} = 1\text{ pA}$;
- Mecanismo de guiamento axonal mediado por gradientes de quimioatração e quimiorepulsão detectados pelo cone de crescimento;
- Não há citações inventadas, números de página espúrios ou links inexistentes.

### 4.5 Causalidade Conceitual e Pré-requisitos

Nenhum conceito é empregado antes de ser definido:
- A aula inicia revisando a transição de funções vetoriais (Tema 3.1) para funções escalares de várias variáveis;
- As derivadas parciais são introduzidas antes de serem combinadas na aproximação linear e no plano tangente;
- O gradiente é definido apenas após a formalização das derivadas parciais e da diferenciabilidade;
- A Hessiana e as derivadas de ordem superior são apresentadas na seção de derivadas parciais após o estudante já ter fluência nas primeiras derivadas;
- A derivada direcional é construída a partir do produto escalar e do gradiente;
- Menções a tópicos futuros (gradiente descendente e otimização no Módulo 4, matrizes no Módulo 5, *backpropagation* no Módulo 9) são expressamente contextualizadas como antecipações pedagógicas.

### 4.6 Código Python e Figura

- O script [gradiente-ativacao.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/fig/gradiente-ativacao.py) é autocontido, não depende de bibliotecas além de `numpy` e `matplotlib`, adota `plt.rcParams["svg.fonttype"] = "none"`, tem rótulos em português com unidades corretas ($\text{mm}$), formata eixos transparentes e salva a imagem vetorial diretamente em [gradiente-ativacao.svg](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/fig/gradiente-ativacao.svg);
- O código roda como está, sem qualquer erro de execução;
- A tag `<figure>` na aula aponta corretamente para `src="fig/gradiente-ativacao.svg"`, arquivo que existe e compila sem avisos.

### 4.7 Consistência Notacional

- **Vetores:** grafados sistematicamente em negrito minúsculo ($\mathbf{x}$, $\mathbf{h}$, $\mathbf{a}$, $\mathbf{w}$, $\mathbf{u}$, $\mathbf{v}$, $\mathbf{r}(t)$, $\mathbf{r}'(t)$, $\mathbf{0}$, $\hat{\mathbf{d}}$);
- **Matrizes:** a matriz Hessiana é grafada em negrito maiúsculo ($\mathbf{H}_f$, $\mathbf{H}_Z$);
- **Gradiente:** o operador nabla aparece estritamente sem negrito ($\nabla f$, $\nabla Z$, $\nabla C$, $\nabla J$, $\nabla g$, $\nabla \phi$, $\nabla h$);
- **Decimais:** separador decimal por vírgula em toda a prosa e matemática ($0{,}5$, $1{,}47$, $26{,}7$, $-0{,}191$), e ponto em código Python (`4.0`, `2.0`, `1.0`, `8.0`).

### 4.8 Extensão do Texto

- A aula possui aproximadamente 4 450 palavras de prosa (desconsiderando tags XML de marcação e equações puras em KaTeX);
- Está perfeitamente situada dentro da faixa preconizada pelo padrão (2 500 a 5 000 palavras para temas densos);
- **A aula NÃO ultrapassa o teto de 5 500 palavras.**

---

## 5. Conclusão da Revisão

A aula `conteudo/modulo-03/tema-02.dlt` representa um material didático de altíssimo nível, combinando rigor formal impecável, contas 100% conferidas e uma abordagem biológica realista que atende perfeitamente ao perfil do estudante de Ciências Biológicas em transição para a Neurociência Computacional. O veredito é **APROVAR**.
