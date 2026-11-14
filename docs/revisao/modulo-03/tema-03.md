# Relatório de Revisão Técnica — Módulo 03 · Tema 03 (Integrais Múltiplas)

- **Arquivo revisado:** [tema-03.dlt](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-03.dlt)
- **Script de figura associado:** [densidade-conjunta.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/fig/densidade-conjunta.py)
- **Figura gerada:** [densidade-conjunta.svg](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/fig/densidade-conjunta.svg)
- **Documentos de referência:** [PADRAO-AULAS.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/PADRAO-AULAS.md), [DELTA-COLA.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/DELTA-COLA.md), [Guia.txt](file:///home/al.pedro.alberti/trilha-neuro-computacional/referencias/Guia.txt) e [index.html](file:///home/al.pedro.alberti/trilha-neuro-computacional/index.html)
- **Data da revisão:** 14 de novembro de 2026
- **Perfil do revisor:** Matemático, Neurocientista Computacional e Professor de Alunos de Ciências Biológicas

---

## 1. Veredito

**APROVAR**

A aula cumpre integralmente os requisitos matemáticos, biológicos, pedagógicos e editoriais estipulados para a Trilha de Neurociência Computacional. Todas as contas de exemplos, teoremas, demonstrações e exercícios foram recalculadas analítica e numericamente, com **exatidão absoluta** em cada passagem. A transição pedagógica da integral simples para integrais duplas e triplas é construída com intuição sólida ("densidade vezes área" e "densidade vezes volume"), aplicando contextos biológicos e neurobiológicos realistas (contagem de corpos neuronais em fatias e blocos corticais, densidade de carga em bicamada lipídica, densidade sináptica, latências de disparo via processos pontuais e campos receptivos visuais gaussianos). 

A probabilidade conjunta como volume sob uma superfície é tratada de forma geométrica e rigorosa, preparando perfeitamente os alunos para o Módulo 7 (Estatística e Probabilidade) e Módulo 8 (Machine Learning). A notação do documento respeita estritamente o padrão dos Módulos 3 a 5 (escalares em itálico, decimais com vírgula e proteção de chaves no LaTeX, operadores matemáticos formatados e XML estrito compatível com o compilador Delta).

Foram registradas na tabela a seguir apenas 4 observações de aprimoramento pedagógico e de formato, de caráter não impeditivo.

---

## 2. Tabela de Problemas e Observações

| Severidade | Local | Trecho | Correção sugerida |
|---|---|---|---|
| Pedagógico | Subtema 2 (`sec:3-3-2`), `exm:3-3-iterada-tripla`, linha ~213 | `\int_0^2 \left(2 + \frac{8}{3}y\right)dy = \left[2y + \frac{4}{3}y^2\right]_0^2 = \frac{28}{3}` | Na ordem $dx\,dy$, a solução pula a passagem aritmética intermediária $4 + \frac{16}{3}$, presente na ordem anterior ($dy\,dx$). Para estudantes de Biologia com base matemática enferrujada, explicitar `\left[2y + \frac{4}{3}y^2\right]_0^2 = 4 + \frac{16}{3} = \frac{28}{3}` reforça a simetria operacional entre as duas ordens de Fubini. |
| Pedagógico | Subtema 4 (`sec:3-3-4`), `exr:3-3-4-2`, linha ~556 | `\frac{\partial(x, y)}{\partial(u, v)} = \left(\frac{1}{2}\right)\left(-\frac{1}{2}\right) - \left(\frac{1}{2}\right)\left(\frac{1}{2}\right) = -\frac{1}{2}` | Alunos de graduação costumam derivar $u(x, y) = x + y$ e $v(x, y) = x - y$ em relação a $x$ e $y$, obtendo determinante $-2$. Sugere-se adicionar uma breve observação de que $\left|\frac{\partial(x, y)}{\partial(u, v)}\right| = \left|\frac{\partial(u, v)}{\partial(x, y)}\right|^{-1} = |-2|^{-1} = \frac{1}{2}$, alertando para nunca multiplicar pelo jacobiano da transformação inversa. |
| Pedagógico | Subtema 2 (`sec:3-3-2`), `def:3-3-tripla-media`, linha ~179 | `B = [a_1, b_1] \times [a_2, b_2] \times [a_3, b_3]` | O uso de índices numéricos nos intervalos pode gerar confusão temporária com pontos de amostragem discretos ($x_i, y_j, z_k$). Sugere-se explicitar brevemente na prosa que $[a_1, b_1]$ corresponde a $x \in [a, b]$, $[a_2, b_2]$ a $y \in [c, d]$ e $[a_3, b_3]$ a $z \in [p, q]$. |
| Formato | Subtema 3 (`sec:3-3-3`), `prop:3-3-propriedades`, linha ~318 | `\text{vol}(E) = \iiint_E 1\,dV` | O símbolo $E$ é introduzido para denotar um sólido tridimensional arbitrário, enquanto no Subtema 2 usou-se $B$ para bloco retangular. Recomenda-se registrar em nota que $E$ designa uma região tridimensional qualquer em $\mathbb{R}^3$, análoga ao domínio plano $D$ em $\mathbb{R}^2$. |

---

## 3. Recálculo e Auditoria de Todas as Contas

Todas as expressões analíticas, contas numéricas, demonstrações de teoremas e proposições, bem como as soluções dos exercícios, foram recalculadas passo a passo.

### 3.1 Subtema 1: Introdução (`sec:3-3-1`)

1. **[Exemplo 3.3.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-03.dlt#L64-L76) (`exm:3-3-riemann-2x2`):**
   - Função: $f(x, y) = 1 + x^2 y$ no retângulo $R = [0, 2] \times [0, 2]$.
   - Grade $2 \times 2$: $\Delta x = \frac{2 - 0}{2} = 1$, $\Delta y = \frac{2 - 0}{2} = 1$, $\Delta A = 1 \cdot 1 = 1$.
   - Subintervalos: $x \in [0, 1], [1, 2]$; $y \in [0, 1], [1, 2]$.
   - Centros dos quatro subquadrados:
     - $(x_1^*, y_1^*) = (0{,}5;\, 0{,}5) \implies f(0{,}5;\, 0{,}5) = 1 + (0{,}5)^2(0{,}5) = 1 + 0{,}125 = 1{,}125$;
     - $(x_2^*, y_1^*) = (1{,}5;\, 0{,}5) \implies f(1{,}5;\, 0{,}5) = 1 + (1{,}5)^2(0{,}5) = 1 + 2{,}25 \cdot 0{,}5 = 2{,}125$;
     - $(x_1^*, y_2^*) = (0{,}5;\, 1{,}5) \implies f(0{,}5;\, 1{,}5) = 1 + (0{,}5)^2(1{,}5) = 1 + 0{,}25 \cdot 1{,}5 = 1{,}375$;
     - $(x_2^*, y_2^*) = (1{,}5;\, 1{,}5) \implies f(1{,}5;\, 1{,}5) = 1 + (1{,}5)^2(1{,}5) = 1 + 2{,}25 \cdot 1{,}5 = 4{,}375$.
   - Soma de Riemann dupla:
     $$S_{2, 2} = (1{,}125 + 2{,}125 + 1{,}375 + 4{,}375) \cdot 1 = 9{,}000 = 9.$$
   - Valor exato por integral iterada:
     $$\iint_R (1 + x^2 y)\,dA = \int_0^2 \left(2 + 2x^2\right)dx = \left[2x + \frac{2x^3}{3}\right]_0^2 = 4 + \frac{16}{3} = \frac{28}{3} \approx 9{,}333.$$
     Erro relativo da partição $2 \times 2$: $\frac{|9 - 28/3|}{28/3} = \frac{1/3}{28/3} = \frac{1}{28} \approx 3{,}57\%$.
     **Correto.**

2. **[Exemplo 3.3.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-03.dlt#L78-L91) (`exm:3-3-densidade-tecido`):**
   - Densidade superficial: $\rho(x, y) = 800 + 100(x + y)\text{ células/mm}^2$ em $R = [0, 2] \times [0, 2]\text{ mm}$.
   - Grade $2 \times 2 \implies \Delta A = 1\text{ mm}^2$.
   - Valores nos quatro centros:
     - $\rho(0{,}5;\, 0{,}5) = 800 + 100(1{,}0) = 900\text{ células/mm}^2$;
     - $\rho(1{,}5;\, 0{,}5) = 800 + 100(2{,}0) = 1\,000\text{ células/mm}^2$;
     - $\rho(0{,}5;\, 1{,}5) = 800 + 100(2{,}0) = 1\,000\text{ células/mm}^2$;
     - $\rho(1{,}5;\, 1{,}5) = 800 + 100(3{,}0) = 1\,100\text{ células/mm}^2$.
   - Estimativa total:
     $$N \approx (900 + 1\,000 + 1\,000 + 1\,100) \cdot 1 = 4\,000\text{ células}.$$
     (Por linearidade, a regra do ponto médio coincide com o valor exato $\iint_R \rho\,dA = 4\,000$).
     **Correto.**

3. **[Exercício 3.3.1.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-03.dlt#L101-L115) (`exr:3-3-1-1`):**
   - Função: $f(x, y) = x + 2y$ em $R = [0, 2] \times [0, 2]$ com $\Delta x = \Delta y = 1$, $\Delta A = 1$.
   - Item (a) — Cantos superiores direitos:
     - subquadrados: $[0, 1] \times [0, 1] \to (1, 1)$, $f = 1 + 2 = 3$;
     - $[1, 2] \times [0, 1] \to (2, 1)$, $f = 2 + 2 = 4$;
     - $[0, 1] \times [1, 2] \to (1, 2)$, $f = 1 + 4 = 5$;
     - $[1, 2] \times [1, 2] \to (2, 2)$, $f = 2 + 4 = 6$.
     - Soma: $S_{\text{sup}} = (3 + 4 + 5 + 6) \cdot 1 = 18$.
     **Correto.**
   - Item (b) — Cantos inferiores esquerdos:
     - $[0, 1] \times [0, 1] \to (0, 0)$, $f = 0 + 0 = 0$;
     - $[1, 2] \times [0, 1] \to (1, 0)$, $f = 1 + 0 = 1$;
     - $[0, 1] \times [1, 2] \to (0, 1)$, $f = 0 + 2 = 2$;
     - $[1, 2] \times [1, 2] \to (1, 1)$, $f = 1 + 2 = 3$.
     - Soma: $S_{\text{inf}} = (0 + 1 + 2 + 3) \cdot 1 = 6$.
     (A média entre $S_{\text{sup}}$ e $S_{\text{inf}}$ é $\frac{18 + 6}{2} = 12$, exata).
     **Correto.**

4. **[Exercício 3.3.1.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-03.dlt#L117-L131) (`exr:3-3-1-2`):**
   - $R = [0, 4] \times [0, 2]\;\mu\text{m}$, $\sigma(x, y) = 2 + 0{,}5\,xy\text{ fC}/\mu\text{m}^2$.
   - Divisão $2 \times 2$: $\Delta x = 2\;\mu\text{m}$, $\Delta y = 1\;\mu\text{m} \implies \Delta A = 2 \cdot 1 = 2\;\mu\text{m}^2$.
   - Subintervalos: $x \in [0, 2], [2, 4]$ (pontos médios $x = 1, 3$); $y \in [0, 1], [1, 2]$ (pontos médios $y = 0{,}5; 1{,}5$).
   - Pontos médios:
     - $(1;\, 0{,}5) \implies \sigma = 2 + 0{,}5(1)(0{,}5) = 2 + 0{,}25 = 2{,}25\text{ fC}/\mu\text{m}^2$;
     - $(3;\, 0{,}5) \implies \sigma = 2 + 0{,}5(3)(0{,}5) = 2 + 0{,}75 = 2{,}75\text{ fC}/\mu\text{m}^2$;
     - $(1;\, 1{,}5) \implies \sigma = 2 + 0{,}5(1)(1{,}5) = 2 + 0{,}75 = 2{,}75\text{ fC}/\mu\text{m}^2$;
     - $(3;\, 1{,}5) \implies \sigma = 2 + 0{,}5(3)(1{,}5) = 2 + 2{,}25 = 4{,}25\text{ fC}/\mu\text{m}^2$.
   - Carga total:
     $$Q \approx (2{,}25 + 2{,}75 + 2{,}75 + 4{,}25) \cdot 2 = 12{,}00 \cdot 2 = 24\text{ fC}.$$
     **Correto.**

5. **[Exercício 3.3.1.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-03.dlt#L133-L141) (`exr:3-3-1-3`):**
   - Bloco $B = [0, 2]^3\text{ mm}$, $\rho(x, y, z) = 40\,000 + 5\,000\,z\text{ neurônios/mm}^3$.
   - Partição $2 \times 2 \times 2 = 8$ cubos de lado $1\text{ mm}$ ($\Delta V = 1\text{ mm}^3$).
   - Como $\rho$ independe de $x$ e $y$:
     - 4 cubos da camada inferior ($z \in [0, 1]$, centro $z = 0{,}5$): $\rho = 40\,000 + 2\,500 = 42\,500/\text{mm}^3$;
     - 4 cubos da camada superior ($z \in [1, 2]$, centro $z = 1{,}5$): $\rho = 40\,000 + 7\,500 = 47\,500/\text{mm}^3$.
   - Total estimado:
     $$N \approx 4(42\,500 \cdot 1) + 4(47\,500 \cdot 1) = 170\,000 + 190\,000 = 360\,000\text{ neurônios}.$$
     **Correto.**

---

### 3.2 Subtema 2: Integral dupla e tripla (retângulo e paralelepípedo) (`sec:3-3-2`)

1. **[Exemplo 3.3.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-03.dlt#L202-L221) (`exm:3-3-iterada-tripla`):**
   - Item (a) — Ordem $dy\,dx$ para $\iint_R (1 + x^2 y)\,dA$ em $[0, 2]^2$:
     $$\int_0^2 (1 + x^2 y)\,dy = \left[y + \frac{x^2 y^2}{2}\right]_0^2 = 2 + 2x^2.$$
     $$\int_0^2 (2 + 2x^2)\,dx = \left[2x + \frac{2x^3}{3}\right]_0^2 = 4 + \frac{16}{3} = \frac{28}{3} \approx 9{,}333.$$
     Ordem $dx\,dy$:
     $$\int_0^2 (1 + x^2 y)\,dx = \left[x + \frac{x^3 y}{3}\right]_0^2 = 2 + \frac{8}{3}y.$$
     $$\int_0^2 \left(2 + \frac{8}{3}y\right)dy = \left[2y + \frac{4}{3}y^2\right]_0^2 = 4 + \frac{4}{3}(4) = 4 + \frac{16}{3} = \frac{28}{3}.$$
     Ambas as ordens concordam.
     **Correto.**
   - Item (b) — Integral tripla em $B = [0, 1] \times [0, 2] \times [0, 1]$:
     $$\int_0^1 (x + 2y + 3z)\,dz = \left[xz + 2yz + \frac{3}{2}z^2\right]_0^1 = x + 2y + \frac{3}{2}.$$
     $$\int_0^2 \left(x + 2y + \frac{3}{2}\right)dy = \left[xy + y^2 + \frac{3}{2}y\right]_0^2 = 2x + 4 + 3 = 2x + 7.$$
     $$\int_0^1 (2x + 7)\,dx = \left[x^2 + 7x\right]_0^1 = 1 + 7 = 8.$$
     Volume de $B$: $\text{vol}(B) = (1 - 0)(2 - 0)(1 - 0) = 2$.
     Valor médio: $\bar{f} = \frac{8}{2} = 4$.
     **Correto.**

2. **[Exemplo 3.3.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-03.dlt#L223-L241) (`exm:3-3-prob-conjunta`):**
   - Item (a) — Constante de normalização de $p(x, y) = c(x + y)$ em $[0, 1]^2$:
     $$\int_0^1 \!\int_0^1 (x + y)\,dy\,dx = \int_0^1 \left[xy + \frac{y^2}{2}\right]_0^1 dx = \int_0^1 \left(x + \frac{1}{2}\right)dx = \left[\frac{x^2}{2} + \frac{x}{2}\right]_0^1 = 1 \implies c = 1.$$
     Probabilidade em $[0;\, 0{,}5]^2$:
     $$P = \int_0^{1/2} \left(\frac{x}{2} + \frac{1}{8}\right)dx = \left[\frac{x^2}{4} + \frac{x}{8}\right]_0^{1/2} = \frac{1}{16} + \frac{1}{16} = \frac{1}{8} = 0{,}125.$$
     **Correto.**
   - Item (b) — Latências independentes $p(x, y) = \lambda_1\lambda_2 e^{-\lambda_1 x - \lambda_2 y}$ em $[0, a] \times [0, b]$:
     Pela separabilidade:
     $$P = \left(\int_0^a \lambda_1 e^{-\lambda_1 x}\,dx\right)\left(\int_0^b \lambda_2 e^{-\lambda_2 y}\,dy\right) = \left[-e^{-\lambda_1 x}\right]_0^a \cdot \left[-e^{-\lambda_2 y}\right]_0^b = (1 - e^{-\lambda_1 a})(1 - e^{-\lambda_2 b}).$$
     **Correto.**

3. **[Exercício 3.3.2.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-03.dlt#L251-L267) (`exr:3-3-2-1`):**
   - $f(x, y) = 6x^2 y - 2y = (6x^2 - 2)y$ em $R = [0, 2] \times [1, 3]$.
   - Item (a):
     $$\int_0^2 (6x^2 - 2)\,dx = \left[2x^3 - 2x\right]_0^2 = 16 - 4 = 12.$$
     $$\int_1^3 y\,dy = \left[\frac{y^2}{2}\right]_1^3 = \frac{9 - 1}{2} = 4.$$
     $$\iint_R f\,dA = 12 \cdot 4 = 48.$$
     **Correto.**
   - Item (b): $\text{área}(R) = (2 - 0)(3 - 1) = 4 \implies \bar{f} = \frac{48}{4} = 12$.
     **Correto.**

4. **[Exercício 3.3.2.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-03.dlt#L269-L285) (`exr:3-3-2-2`):**
   - $p(x, y) = k\,xy^2$ em $R = [0, 2] \times [0, 1]$.
   - Item (a):
     $$1 = k \left(\int_0^2 x\,dx\right)\left(\int_0^1 y^2\,dy\right) = k \cdot \left[\frac{x^2}{2}\right]_0^2 \cdot \left[\frac{y^3}{3}\right]_0^1 = k \cdot 2 \cdot \frac{1}{3} = \frac{2k}{3} \implies k = \frac{3}{2}.$$
     **Correto.**
   - Item (b):
     $$P(0 \le X \le 1,\; 0 \le Y \le 1) = \frac{3}{2}\left(\int_0^1 x\,dx\right)\left(\int_0^1 y^2\,dy\right) = \frac{3}{2} \cdot \frac{1}{2} \cdot \frac{1}{3} = \frac{1}{4} = 0{,}25.$$
     Avaliação de $p(2, 1)$: $p(2, 1) = \frac{3}{2}(2)(1)^2 = 3 > 1$. Válido, pois a densidade pode exceder a unidade sem que a probabilidade acumulada (volume) ultrapasse $1$.
     **Correto.**

5. **[Exercício 3.3.2.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-03.dlt#L287-L298) (`exr:3-3-2-3`):**
   - $B = [0, 2] \times [0, 1] \times [0, 1]\text{ mm}$, $\rho(x, y, z) = 10^8(1 + 3xy^2 z)\text{ sinapses/mm}^3$.
   - Fator $10^8$ em evidência:
     $$\int_0^1 (1 + 3xy^2 z)\,dz = \left[z + \frac{3}{2}xy^2 z^2\right]_0^1 = 1 + \frac{3}{2}xy^2.$$
     $$\int_0^1 \left(1 + \frac{3}{2}xy^2\right)dy = \left[y + \frac{1}{2}xy^3\right]_0^1 = 1 + \frac{1}{2}x.$$
     $$\int_0^2 \left(1 + \frac{1}{2}x\right)dx = \left[x + \frac{x^2}{4}\right]_0^2 = 2 + 1 = 3.$$
     Total: $3 \times 10^8$ sinapses.
     **Correto.**

---

### 3.3 Subtema 3: Propriedades de integrais múltiplas (`sec:3-3-3`)

1. **[Exemplo 3.3.5](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-03.dlt#L342-L362) (`exm:3-3-troca-ordem`):**
   - Item (a) — Triângulo de vértices $(0, 0)$, $(1, 0)$ e $(1, 1)$, $\iint_D 6x^2 y\,dA$:
     - Tipo I ($0 \le x \le 1$, $0 \le y \le x$):
       $$\int_0^1 \!\left(\int_0^x 6x^2 y\,dy\right)dx = \int_0^1 \left[3x^2 y^2\right]_0^x dx = \int_0^1 3x^4\,dx = \left[\frac{3x^5}{5}\right]_0^1 = \frac{3}{5}.$$
     - Tipo II ($0 \le y \le 1$, $y \le x \le 1$):
       $$\int_0^1 \!\left(\int_y^1 6x^2 y\,dx\right)dy = \int_0^1 \left[2x^3 y\right]_y^1 dy = \int_0^1 (2y - 2y^4)\,dy = \left[y^2 - \frac{2y^5}{5}\right]_0^1 = 1 - \frac{2}{5} = \frac{3}{5}.$$
     Ambas as parametrizações coincidem.
     **Correto.**
   - Item (b) — Inversão de $\int_0^1 \!\left(\int_x^1 e^{y^2}\,dy\right)dx$:
     - Domínio: $0 \le x \le 1$, $x \le y \le 1 \implies$ triângulo de vértices $(0, 0)$, $(0, 1)$, $(1, 1)$.
     - Descrição horizontal (Tipo II): $0 \le y \le 1$, $0 \le x \le y$.
     - Integral invertida:
       $$\int_0^1 \!\left(\int_0^y e^{y^2}\,dx\right)dy = \int_0^1 y\,e^{y^2}\,dy.$$
       Com $u = y^2$, $du = 2y\,dy \implies y\,dy = \frac{du}{2}$:
       $$\left[\frac{1}{2}e^{y^2}\right]_0^1 = \frac{e^1 - e^0}{2} = \frac{e - 1}{2}.$$
     **Correto.**

2. **[Exemplo 3.3.6](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-03.dlt#L364-L381) (`exm:3-3-latencia-e-mapa`):**
   - Item (a) — Probabilidade $P(X < Y)$ com $p(x, y) = \lambda_1\lambda_2 e^{-\lambda_1 x - \lambda_2 y}$ ($x, y \ge 0$):
     $$\int_0^\infty \lambda_1 e^{-\lambda_1 x}\!\left(\int_x^\infty \lambda_2 e^{-\lambda_2 y}\,dy\right)dx = \int_0^\infty \lambda_1 e^{-\lambda_1 x}\left[-e^{-\lambda_2 y}\right]_x^\infty dx = \int_0^\infty \lambda_1 e^{-\lambda_1 x} e^{-\lambda_2 x}\,dx$$
     $$= \lambda_1 \int_0^\infty e^{-(\lambda_1 + \lambda_2)x}\,dx = \lambda_1 \left[-\frac{e^{-(\lambda_1 + \lambda_2)x}}{\lambda_1 + \lambda_2}\right]_0^\infty = \frac{\lambda_1}{\lambda_1 + \lambda_2}.$$
     **Correto.**
   - Item (b) — Valor médio de $Z = 12(1 - x - y)$ em $D = \{x \ge 0, y \ge 0, x + y \le 1\}$:
     - Área: $\text{área}(D) = \frac{1 \cdot 1}{2} = \frac{1}{2}\text{ mm}^2$.
     - Integral dupla ($0 \le x \le 1$, $0 \le y \le 1 - x$):
       $$\int_0^{1-x} 12\bigl[(1 - x) - y\bigr]\,dy = 12\left[(1 - x)y - \frac{y^2}{2}\right]_0^{1-x} = 12\left[(1 - x)^2 - \frac{(1 - x)^2}{2}\right] = 6(1 - x)^2.$$
       $$\int_0^1 6(1 - x)^2\,dx = 6\left[-\frac{(1 - x)^3}{3}\right]_0^1 = 6\left(0 - \left(-\frac{1}{3}\right)\right) = 2.$$
     - Valor médio: $\bar{f} = \frac{2}{1/2} = 4$.
     **Correto.**

3. **[Exercício 3.3.3.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-03.dlt#L391-L405) (`exr:3-3-3-1`):**
   - Região limitada por $y = x^2$, $y = 0$, $x = 2$ ($0 \le x \le 2$, $0 \le y \le x^2$).
   - Item (a):
     $$\text{área}(D) = \int_0^2 \!\left(\int_0^{x^2} dy\right)dx = \int_0^2 x^2\,dx = \left[\frac{x^3}{3}\right]_0^2 = \frac{8}{3}.$$
     **Correto.**
   - Item (b):
     $$\int_0^2 \!\left(\int_0^{x^2} (x + 2y)\,dy\right)dx = \int_0^2 \left[xy + y^2\right]_0^{x^2} dx = \int_0^2 (x^3 + x^4)\,dx = \left[\frac{x^4}{4} + \frac{x^5}{5}\right]_0^2 = 4 + \frac{32}{5} = \frac{52}{5} = 10{,}4.$$
     **Correto.**

4. **[Exercício 3.3.3.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-03.dlt#L407-L417) (`exr:3-3-3-2`):**
   - Inversão da ordem de $\int_0^4 \!\left(\int_{\sqrt{y}}^2 \frac{1}{x^3 + 1}\,dx\right)dy$:
     - Região: $0 \le y \le 4$, $\sqrt{y} \le x \le 2 \implies 0 \le x \le 2$, $0 \le y \le x^2$.
     - Integral na nova ordem:
       $$\int_0^2 \!\left(\int_0^{x^2} \frac{1}{x^3 + 1}\,dy\right)dx = \int_0^2 \frac{x^2}{x^3 + 1}\,dx.$$
     - Substituição $u = x^3 + 1$, $du = 3x^2\,dx$ ($x = 0 \implies u = 1$; $x = 2 \implies u = 9$):
       $$\int_1^9 \frac{du}{3u} = \frac{1}{3}\bigl[\ln u\bigr]_1^9 = \frac{\ln 9}{3} = \frac{\ln(3^2)}{3} = \frac{2\ln 3}{3}.$$
     **Correto.**

5. **[Exercício 3.3.3.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-03.dlt#L419-L433) (`exr:3-3-3-3`):**
   - Densidade conjunta $p(x, y) = 2e^{-x - 2y}$ para $x, y \ge 0$.
   - Item (a) — $P(Y \ge X + 1)$:
     $$P = \int_0^\infty e^{-x}\!\left(\int_{x+1}^\infty 2e^{-2y}\,dy\right)dx = \int_0^\infty e^{-x} \left[-e^{-2y}\right]_{x+1}^\infty dx = \int_0^\infty e^{-x} e^{-2(x+1)}\,dx$$
     $$= e^{-2}\int_0^\infty e^{-3x}\,dx = e^{-2}\left[-\frac{e^{-3x}}{3}\right]_0^\infty = \frac{e^{-2}}{3} \approx \frac{0{,}135335}{3} \approx 0{,}0451 \approx 0{,}045.$$
     **Correto.**
   - Item (b) — Comparação com $P(X < Y)$:
     Pela fórmula $\frac{\lambda_1}{\lambda_1 + \lambda_2} = \frac{1}{1 + 2} = \frac{1}{3} \approx 0{,}333$.
     Como o evento $\{Y \ge X + 1\}$ é subconjunto próprio de $\{Y > X\} = \{X < Y\}$ e a densidade é estritamente positiva, a probabilidade é estritamente menor ($\frac{e^{-2}}{3} < \frac{1}{3}$), demonstrando a aditividade e monotonicidade da integral.
     **Correto.**

---

### 3.4 Subtema 4: Mudança de variáveis (`sec:3-3-4`)

1. **[Demonstração da Proposição 3.3.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-03.dlt#L470-L474) (`prop:3-3-polares`):**
   - $x(r, \theta) = r\cos\theta$, $y(r, \theta) = r\sin\theta$.
   - Derivadas parciais:
     $$\frac{\partial x}{\partial r} = \cos\theta, \quad \frac{\partial x}{\partial \theta} = -r\sin\theta, \quad \frac{\partial y}{\partial r} = \sin\theta, \quad \frac{\partial y}{\partial \theta} = r\cos\theta.$$
   - Determinante jacobiano:
     $$\frac{\partial(x, y)}{\partial(r, \theta)} = (\cos\theta)(r\cos\theta) - (-r\sin\theta)(\sin\theta) = r\cos^2\theta + r\sin^2\theta = r(\cos^2\theta + \sin^2\theta) = r.$$
     Como $r \ge 0$, $|r| = r \implies dA = r\,dr\,d\theta$.
     **Correto.**

2. **[Demonstração do Teorema 3.3.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-03.dlt#L485-L492) (`thm:3-3-gaussiana`):**
   - Definição: $I = \int_{-\infty}^\infty e^{-x^2}\,dx = \int_{-\infty}^\infty e^{-y^2}\,dy$.
   - Produto em $\mathbb{R}^2$ via separabilidade e conversão polar:
     $$I^2 = \iint_{\mathbb{R}^2} e^{-(x^2 + y^2)}\,dA = \int_0^{2\pi} \!\left(\int_0^\infty e^{-r^2} r\,dr\right)d\theta.$$
     Com $u = r^2$, $du = 2r\,dr \implies r\,dr = \frac{du}{2}$:
     $$\int_0^\infty e^{-r^2} r\,dr = \frac{1}{2}\int_0^\infty e^{-u}\,du = \frac{1}{2}\left[-e^{-u}\right]_0^\infty = \frac{1}{2}.$$
     $$I^2 = \int_0^{2\pi} \frac{1}{2}\,d\theta = 2\pi \cdot \frac{1}{2} = \pi \implies I = \sqrt{\pi}.$$
   - Normalização da curva gaussiana geral:
     Substituição $w = \frac{x - \mu}{\sqrt{2}\,\sigma} \implies dx = \sqrt{2}\,\sigma\,dw$:
     $$\int_{-\infty}^\infty \frac{1}{\sqrt{2\pi}\,\sigma} e^{-\frac{(x - \mu)^2}{2\sigma^2}}\,dx = \frac{\sqrt{2}\,\sigma}{\sqrt{2\pi}\,\sigma} \int_{-\infty}^\infty e^{-w^2}\,dw = \frac{1}{\sqrt{\pi}} \cdot \sqrt{\pi} = 1.$$
     **Correto.**

3. **[Exemplo 3.3.7](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-03.dlt#L494-L508) (`exm:3-3-linear-e-anel`):**
   - Item (a) — Área da elipse $\frac{x^2}{4} + \frac{y^2}{9} \le 1$:
     Mudança $x = 2u$, $y = 3v \implies \frac{(2u)^2}{4} + \frac{(3v)^2}{9} = u^2 + v^2 \le 1$ (disco unitário $S$, área $\pi$).
     Jacobiano:
     $$\frac{\partial(x, y)}{\partial(u, v)} = \det\begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix} = 2 \cdot 3 - 0 = 6.$$
     $$\text{área}(E) = \iint_S 6\,du\,dv = 6 \cdot \text{área}(S) = 6\pi.$$
     **Correto.**
   - Item (b) — Integral no anel $1 \le x^2 + y^2 \le 4$:
     Em coordenadas polares: $1 \le r \le 2$, $0 \le \theta \le 2\pi$. Integrando $x^2 + y^2 = r^2$ e $dA = r\,dr\,d\theta$:
     $$\iint_D (x^2 + y^2)\,dA = \int_0^{2\pi}\!d\theta \cdot \int_1^2 r^3\,dr = 2\pi \left[\frac{r^4}{4}\right]_1^2 = 2\pi\left(\frac{16 - 1}{4}\right) = 2\pi \cdot \frac{15}{4} = \frac{15\pi}{2}.$$
     **Correto.**

4. **[Exemplo 3.3.8](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-03.dlt#L510-L532) (`exm:3-3-campo-receptivo`):**
   - Sensibilidade gaussiana: $f(x, y) = A \exp\left(-\frac{x^2 + y^2}{2\sigma^2}\right)$.
   - Item (a) — Resposta total $T$ em $\mathbb{R}^2$:
     Com $u = \frac{r^2}{2\sigma^2} \implies du = \frac{r}{\sigma^2}\,dr \implies r\,dr = \sigma^2\,du$:
     $$T = \int_0^{2\pi}\!d\theta \cdot A \int_0^\infty e^{-\frac{r^2}{2\sigma^2}} r\,dr = 2\pi A \sigma^2 \int_0^\infty e^{-u}\,du = 2\pi\sigma^2 A.$$
     Para densidade unitária ($T = 1$), temos $A = \frac{1}{2\pi\sigma^2}$.
     **Correto.**
   - Item (b) — Fração dentro dos discos de raio $R$:
     $$T(R) = 2\pi A \sigma^2 \int_0^{\frac{R^2}{2\sigma^2}} e^{-u}\,du = 2\pi\sigma^2 A \left(1 - e^{-\frac{R^2}{2\sigma^2}}\right) \implies \frac{T(R)}{T} = 1 - e^{-\frac{R^2}{2\sigma^2}}.$$
     - Para $R = \sigma$: $1 - e^{-1/2} = 1 - \frac{1}{\sqrt{e}} \approx 1 - 0{,}60653 = 0{,}39347 \approx 39{,}3\%$;
     - Para $R = 2\sigma$: $1 - e^{-2} \approx 1 - 0{,}135335 = 0{,}864665 \approx 86{,}5\%$.
     Valores idênticos aos gerados no script da figura.
     **Correto.**

5. **[Exercício 3.3.4.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-03.dlt#L542-L549) (`exr:3-3-4-1`):**
   - Região: primeiro quadrante do círculo $x^2 + y^2 \le 9$ ($0 \le r \le 3$, $0 \le \theta \le \frac{\pi}{2}$).
   - Função: $\sqrt{x^2 + y^2} = r$. Elemento de área: $dA = r\,dr\,d\theta$.
   - Cálculo:
     $$\iint_D \sqrt{x^2 + y^2}\,dA = \int_0^{\pi/2}\!d\theta \int_0^3 r^2\,dr = \frac{\pi}{2} \left[\frac{r^3}{3}\right]_0^3 = \frac{\pi}{2} \cdot \frac{27}{3} = \frac{9\pi}{2}.$$
     **Correto.**

6. **[Exercício 3.3.4.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-03.dlt#L551-L561) (`exr:3-3-4-2`):**
   - $x = \frac{u + v}{2}$, $y = \frac{u - v}{2}$ em $D = \{|x| + |y| \le 1\}$, com $S = [-1, 1]^2$.
   - Derivadas e jacobiano:
     $$x_u = \frac{1}{2}, \quad x_v = \frac{1}{2}, \quad y_u = \frac{1}{2}, \quad y_v = -\frac{1}{2}.$$
     $$\frac{\partial(x, y)}{\partial(u, v)} = \left(\frac{1}{2}\right)\left(-\frac{1}{2}\right) - \left(\frac{1}{2}\right)\left(\frac{1}{2}\right) = -\frac{1}{4} - \frac{1}{4} = -\frac{1}{2} \implies \left|\frac{\partial(x, y)}{\partial(u, v)}\right| = \frac{1}{2}.$$
   - Integrando $(x + y)^2 = u^2$:
     $$\iint_D (x + y)^2\,dA = \frac{1}{2}\left(\int_{-1}^1 u^2\,du\right)\left(\int_{-1}^1 dv\right) = \frac{1}{2} \cdot \left[\frac{u^3}{3}\right]_{-1}^1 \cdot 2 = \frac{1}{2} \cdot \frac{2}{3} \cdot 2 = \frac{2}{3}.$$
     **Correto.**

7. **[Exercício 3.3.4.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-03.dlt#L563-L571) (`exr:3-3-4-3`):**
   - Centro excitatório de célula ganglionar: $s(x, y) = 4e^{-(x^2 + y^2)}$ em $D = \{x^2 + y^2 \le 1\}\text{ mm}$.
   - Coordenadas polares ($0 \le r \le 1$, $0 \le \theta \le 2\pi$), com $u = r^2$, $r\,dr = \frac{du}{2}$:
     $$E = \int_0^{2\pi}\!d\theta \cdot 4 \int_0^1 e^{-r^2} r\,dr = 2\pi \cdot 4 \cdot \frac{1}{2}\int_0^1 e^{-u}\,du = 4\pi\left[-e^{-u}\right]_0^1 = 4\pi(1 - e^{-1}).$$
     Aproximação decimal: $4\pi(1 - 0{,}367879) = 4\pi(0{,}632121) \approx 7{,}9436 \approx 7{,}94$.
     **Correto.**

8. **[Exercício 3.3.4.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-03.dlt#L573-L589) (`exr:3-3-4-4`):**
   - $p(x, y) = c\,e^{-\frac{x^2 + y^2}{2\sigma^2}}$.
   - Item (a) — Constante de normalização:
     $$\iint_{\mathbb{R}^2} p\,dA = 2\pi\sigma^2 c = 1 \implies c = \frac{1}{2\pi\sigma^2}.$$
     **Correto.**
   - Item (b) — Raio mediano $R$ ($50\%$ da massa):
     $$P(X^2 + Y^2 \le R^2) = 1 - e^{-\frac{R^2}{2\sigma^2}} = \frac{1}{2} \implies e^{-\frac{R^2}{2\sigma^2}} = \frac{1}{2}.$$
     $$-\frac{R^2}{2\sigma^2} = -\ln 2 \implies R^2 = 2\sigma^2\ln 2 \implies R = \sigma\sqrt{2\ln 2} \approx \sigma\sqrt{1{,}386294} \approx 1{,}1774\,\sigma \approx 1{,}177\,\sigma.$$
     **Correto.**

---

### 3.5 Auditoria do Script de Figura e Verificação Numérica

O script [densidade-conjunta.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/fig/densidade-conjunta.py) foi auditado:
- **Configuração vetorial:** Utiliza `plt.rcParams["svg.fonttype"] = "none"`, garantindo que os textos sejam preservados como glifos vetoriais abertos sem conversão pesada para caminhos (`path`), mantendo o SVG extremamente leve e nítido.
- **Autocontenção:** Importa estritamente `math`, `pathlib.Path`, `matplotlib.patches`, `matplotlib.pyplot` e `numpy`, sem dependências externas não padronizadas.
- **Fórmulas de probabilidade:**
  - Painel esquerdo: `prob_ret = (math.erf(1.0 / math.sqrt(2.0))) ** 2`. Como $\int_{-1}^1 \frac{1}{\sqrt{2\pi}}e^{-x^2/2}\,dx = \text{erf}(1/\sqrt{2}) \approx 0{,}6826895$, o produto bidimensional em $[-1, 1]^2$ resulta em $0{,}6826895^2 \approx 0{,}466065 \approx 46{,}6\%$.
  - Painel direito: `prob_r1 = 1.0 - math.exp(-0.5) \approx 39{,}3\%` e `prob_r2 = 1.0 - math.exp(-2.0) \approx 86{,}5\%`.
  - As legendas e caixas de texto refletem perfeitamente a vírgula decimal exigida no português do Brasil (`replace(".", ",")`).
- O arquivo [densidade-conjunta.svg](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/fig/densidade-conjunta.svg) existe no diretório correto e é referenciado adequadamente no Delta via `src="fig/densidade-conjunta.svg"`.

---

**Nenhum erro matemático encontrado.**

---

## 4. Verificações Específicas do Padrão Editorial

### 4.1 Estrutura e Exercícios
- **Dicas e Soluções completas:** Todos os 13 exercícios (`exr:3-3-1-1` a `exr:3-3-4-4`) contêm `<hint>` direcionado e `<solution collapsible="true" collapsed="true">` com deduções analíticas completas, etapas intermediárias, justificativas conceituais e conferências auxiliares.
- **Gradação dos exercícios:** Todos os títulos seguem rigorosamente os prefixos estipulados ("Básico", "Intermediário" e "Avançado"), cobrindo desde somas de Riemann manuais com cantos e fatiamento pelo Teorema de Fubini até inversão de ordem em regiões curvas e mudanças não lineares de coordenadas em campos receptivos.

### 4.2 Exemplos Biológicos por Subtema
- **Abertura:** Densidade de corpos celulares em fatias corticais, carga em bicamada lipídica, rastreamento de animais em arena, latências de disparo neuronal e normalização gaussiana em campos receptivos visuais.
- **Subtema 1 (`sec:3-3-1`):** Contagem de neurônios em fatia cortical fina de mamífero (`exm:3-3-densidade-tecido`), densidade superficial de carga em bicamada lipídica (`exr:3-3-1-2`) e densidade volumétrica neuronal em bloco cortical tridimensional (`exr:3-3-1-3`).
- **Subtema 2 (`sec:3-3-2`):** Rastreamento de roedor em arena e latências de disparos de dois neurônios independentes (`exm:3-3-prob-conjunta`), probabilidade espacial em arena comportamental com densidade pontual superior à unidade (`exr:3-3-2-2`) e contagem total de sinapses em bloco cortical volumétrico (`exr:3-3-2-3`).
- **Subtema 3 (`sec:3-3-3`):** Ordem cronológica de potenciais de ação entre neurônios e média de sinal em mapa cortical triangular (`exm:3-3-latencia-e-mapa`), bem como janela de coincidência temporal mínima entre spikes (`exr:3-3-3-3`).
- **Subtema 4 (`sec:3-3-4`):** Sensibilidade de campo receptivo visual gaussiano e frações energéticas em raios $1\sigma$ e $2\sigma$ (`exm:3-3-campo-receptivo`), centro excitatório de célula ganglionar da retina (`exr:3-3-4-3`) e raio de $50\%$ de ativação gaussiana (`exr:3-3-4-4`).
- Todas as quatro divisões possuem pelo menos um exemplo e um exercício biológico realisticamente calibrados.

### 4.3 Afirmações de Neurociência e Biologia
- A densidade neuronal no córtex de mamíferos ($10^4$ a $10^5\text{ neurônios/mm}^3$, com valores típicos entre $40\,000$ e $100\,000/\text{mm}^3$) e a densidade sináptica cortical ($\sim 10^8$ a $10^9\text{ sinapses/mm}^3$) são fatos canônicos consolidados na literatura clássica (Braitenberg & Schüz; Kandel et al., *Principles of Neural Science*; Dayan & Abbott, *Theoretical Neuroscience*).
- O tratamento de latências e intervalos entre disparos como variáveis exponenciais e processos pontuais de Poisson reflete fielmente o Capítulo 1 de Dayan & Abbott.
- A modelagem de campos receptivos visuais por filtros gaussianos circulares (e centros excitatórios de células ganglionares) está alinhada ao Capítulo 2 de Dayan & Abbott e Kandel (Capítulo 25).
- Não há citações apócrifas, inventadas ou números de páginas fabricados.

### 4.4 Sequência Lógica e Apresentação Prévia
- A ordenação didática é exemplar: soma de Riemann dupla no retângulo $\to$ volume/densidade $\to$ Teorema de Fubini e caso separável $\to$ integral tripla em paralelepípedos e valor médio $\to$ probabilidade conjunta como volume $\to$ propriedades fundamentais $\to$ regiões gerais (Tipo I e Tipo II) $\to$ inversão da ordem de integração $\to$ mudança de variáveis e determinante jacobiano $\to$ coordenadas polares ($dA = r\,dr\,d\theta$) $\to$ dedução bidimensional da integral da curva gaussiana ($\int_{-\infty}^\infty e^{-x^2}\,dx = \sqrt{\pi}$).
- Nenhum conceito de módulos futuros é invocado sem a devida contextualização preparatória (matrizes e determinantes gerais são apontados para o Módulo 5, e a teoria formal de probabilidade para o Módulo 7).

### 4.5 Código Python
- O script [densidade-conjunta.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/fig/densidade-conjunta.py) roda de maneira autônoma, emprega boas práticas em Python (`pathlib`, tipagem auxiliar e funções organizadas), manipula a formatação visual com rigor (cores padronizadas da paleta Slate/Indigo/Teal) e exporta a figura vetorial sem dependências ocultas.

### 4.6 Consistência de Notação
- **Escalares:** Formatados em itálico ($x, y, z, u, v, r, \theta, \lambda_1, \lambda_2, \sigma, \mu, c, k, A, T$).
- **Matrizes e Vetores:** A matriz jacobiana dentro da fórmula de determinante é apresentada explicitamente como $\det \begin{pmatrix} \dots \end{pmatrix}$. Variáveis aleatórias são maiúsculas em itálico ($X, Y$), padrão em probabilidade matemática. Vetores e matrizes em negrito não foram necessários nem violados no corpo da aula.
- **Operador Gradiente:** Não utilizado indevidamente com negrito (mencionado conceitualmente em temas anteriores como $\nabla f$).
- **Decimais:** Vírgula padronizada com chaves no ambiente matemático ($0{,}5$, $1{,}5$, $1{,}125$, $46{,}6\%$, $39{,}3\%$, $86{,}5\%$) e ponto em código Python.

### 4.7 Cobertura do Guia, Subtemas e Extensão
- **Subtemas cobertos:**
  1. Introdução (`sec:3-3-1`);
  2. Integral dupla e tripla no retângulo e paralelepípedo, e Probabilidade conjunta como volume (`sec:3-3-2`);
  3. Propriedades de integrais múltiplas (`sec:3-3-3`);
  4. Mudança de variáveis: polares, jacobiano e integral da gaussiana (`sec:3-3-4`).
- A ordem exigida pelo Guia de Estudos e pelo padrão do projeto foi cumprida rigorosamente.
- **Extensão do texto:**
  - O texto possui aproximadamente **4 400 palavras de prosa técnica** (descontando cabeçalhos puramente estruturais de XML e código).
  - O tamanho-alvo estabelecido é de **3 500 a 5 500 palavras**.
  - A aula encontra-se **perfeitamente dentro do padrão**, não ficando nem abaixo nem acima do intervalo estipulado.

---

## 5. Conclusão

A aula do Tema 3.3 (Integrais Múltiplas) atinge o ápice de excelência matemática e didática do Módulo 3. A integração de áreas e volumes deixa de ser um mero exercício mecânico e passa a ser uma ferramenta palpável de biofísica e neurociência estatística. O arquivo [tema-03.dlt](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-03.dlt) está pronto para compilação definitiva pelo gestor técnico, sem necessidade de alterações estruturais prévias.
