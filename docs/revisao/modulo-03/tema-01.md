# Relatório de Revisão Técnica — Módulo 03 · Tema 01 (Funções Vetoriais)

- **Arquivo revisado:** [tema-01.dlt](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-01.dlt)
- **Script de figura associado:** [trajetoria-estados.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/fig/trajetoria-estados.py)
- **Documentos de referência:** [PADRAO-AULAS.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/PADRAO-AULAS.md), [DELTA-COLA.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/DELTA-COLA.md), [Guia.txt](file:///home/al.pedro.alberti/trilha-neuro-computacional/referencias/Guia.txt) e [index.html](file:///home/al.pedro.alberti/trilha-neuro-computacional/index.html)
- **Data da revisão:** 14 de novembro de 2026
- **Perfil do revisor:** Matemático, Neurocientista Computacional e Professor de Alunos de Ciências Biológicas

---

## 1. Veredito

**APROVAR**

A aula cumpre rigorosamente todos os requisitos matemáticos, neurobiológicos e editoriais estipulados para a Trilha de Neurociência Computacional. Todas as contas de exemplos e exercícios foram recalculadas analítica e numericamente, confirmando total exatidão. A progressão didática constrói a transição do Cálculo de uma variável para o espaço multivariável com clareza exemplar, utilizando metáforas biológicas autênticas (populações corticais e hipocampais, cinemática flagelar tridimensional e rastreamento comportamental de roedores) sem concessões no rigor analítico. A notação exigida para os Módulos 3 a 5 (vetores em negrito minúsculo $\mathbf{x}$, matrizes em negrito maiúsculo $\mathbf{A}$, escalares em itálico e $\nabla f$ sem negrito) foi respeitada com precisão absoluta. A estrutura XML em formato Delta compila de maneira estrita, com identificadores normalizados, soluções recolhidas e o script Python de figura gerando o SVG de forma autocontida.

Foram catalogadas apenas 3 observações pontuais de aprimoramento pedagógico na tabela a seguir, sem impacto impeditivo.

---

## 2. Tabela de Problemas e Observações

| Severidade | Local | Trecho | Correção sugerida |
|---|---|---|---|
| Pedagógico | Subseção 3 (`sub:3-1-1-c`), `exm:3-1-velocidade-neural`, linha ~403 | `L = \int_0^{1/f} 20\pi f\,dt = 20\pi f \cdot \frac{1}{f} = 20\pi \approx 62{,}83\text{ Hz}` | O comprimento de arco no espaço de estados neural possui unidade de taxa de disparo ($\text{Hz}$), decorrente da integração da rapidez ($\text{Hz/s}$) no tempo ($\text{s}$). Alunos de Biologia habituados à ideia geométrica de comprimento métrico ($\text{m}$ ou $\text{cm}$) podem estranhar um "comprimento em Hertz". Sugere-se explicitar em nota que o comprimento da trajetória em espaços de fase/estados assume a unidade física dos eixos que definem o espaço. |
| Pedagógico | Subseção 3 (`sub:3-1-1-c`), `prop:3-1-regras-derivacao`, linha ~342 | `(f\mathbf{u})'(t) = f'(t)\mathbf{u}(t) + f(t)\mathbf{u}'(t)` | Na Subseção 2 (`exm:3-1-trajetoria-neural`), a letra $f$ foi empregada para denotar frequência temporal em Hertz ($f = 2\text{ Hz}$). Na regra do produto por função escalar, $f(t)$ passa a representar uma função real qualquer. Embora o contexto formal elimine ambiguidades para quem já domina cálculo, sugere-se pontuar que $f(t)$ designa uma função escalar arbitrária (ou usar a notação clássica $c(t)$ ou $\lambda(t)$) para evitar momentânea confusão com frequência. |
| Pedagógico | Subseção 3 (`sub:3-1-1-c`), `exm:3-1-helice-bacteria`, linha ~412 | `\mathbf{r}(t) = \bigl(3\cos(2t),\; 3\sin(2t),\; 8t\bigr), \qquad t \in [0, \pi]` | Ao derivar o argumento $2t$, surge o fator $2$ por aplicação da regra da cadeia. Recomenda-se registrar explicitamente que a constante $2$ tem dimensão de velocidade angular ($\text{rad/s}$), esclarecendo a homogeneidade dimensional que converte a posição em micrômetros ($\mu\text{m}$) na rapidez em $\mu\text{m/s}$ e aceleração em $\mu\text{m/s}^2$. |

---

## 3. Recálculo e Auditoria de Todas as Contas

Todas as expressões analíticas, contas numéricas, demonstrações e soluções foram recalculadas passo a passo:

### 3.1 Subseção 1: Vetores no plano e no espaço (`sub:3-1-1-a`)

1. **[Exemplo 3.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-01.dlt#L102-L126) (`exm:3-1-estado-populacao`):**
   - Item (a): Norma de $\mathbf{r}_A = (12, 30, 5)\text{ Hz}$:
     $$\|\mathbf{r}_A\| = \sqrt{12^2 + 30^2 + 5^2} = \sqrt{144 + 900 + 25} = \sqrt{1\,069} \approx 32{,}695565... \approx 32{,}70\text{ Hz}.$$
     **Correto.**
   - Item (b): Vetor deslocamento $\Delta\mathbf{r} = \mathbf{r}_B - \mathbf{r}_A$:
     $$\Delta\mathbf{r} = (15 - 12,\, 26 - 30,\, 5 - 5) = (3, -4, 0)\text{ Hz}.$$
     Norma euclidiana do deslocamento:
     $$\|\Delta\mathbf{r}\| = \sqrt{3^2 + (-4)^2 + 0^2} = \sqrt{9 + 16 + 0} = \sqrt{25} = 5\text{ Hz}.$$
     **Correto.**
   - Item (c): Vetor unitário $\hat{\mathbf{d}}$ na direção de $\Delta\mathbf{r}$:
     $$\hat{\mathbf{d}} = \frac{\Delta\mathbf{r}}{\|\Delta\mathbf{r}\|} = \frac{1}{5}(3, -4, 0) = (0{,}6;\, -0{,}8;\, 0).$$
     Conferência de unitariedade:
     $$\|\hat{\mathbf{d}}\| = \sqrt{0{,}6^2 + (-0{,}8)^2 + 0^2} = \sqrt{0{,}36 + 0{,}64} = \sqrt{1} = 1.$$
     **Correto.**

2. **[Exemplo 3.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-01.dlt#L128-L150) (`exm:3-1-produto-escalar`):**
   - Item (a): Perpendicularidade entre $\mathbf{u} = (3, 4)$ e $\mathbf{v} = (-4, 3)$:
     $$\mathbf{u} \cdot \mathbf{v} = 3 \cdot (-4) + 4 \cdot 3 = -12 + 12 = 0.$$
     Como ambos são não nulos, o ângulo entre eles é $\theta = \frac{\pi}{2}\text{ rad} = 90^\circ$.
     **Correto.**
   - Item (b): Ângulo entre $\mathbf{a} = (1, \sqrt{3})$ e $\mathbf{b} = (2, 0)$:
     $$\mathbf{a} \cdot \mathbf{b} = 1 \cdot 2 + \sqrt{3} \cdot 0 = 2.$$
     Normas:
     $$\|\mathbf{a}\| = \sqrt{1^2 + (\sqrt{3})^2} = \sqrt{1 + 3} = 2, \qquad \|\mathbf{b}\| = \sqrt{2^2 + 0^2} = 2.$$
     Cálculo do cosseno e do ângulo:
     $$\cos\theta = \frac{\mathbf{a} \cdot \mathbf{b}}{\|\mathbf{a}\|\,\|\mathbf{b}\|} = \frac{2}{2 \cdot 2} = \frac{1}{2} \implies \theta = \arccos\left(\frac{1}{2}\right) = \frac{\pi}{3}\text{ rad} = 60^\circ.$$
     **Correto.**

3. **[Exercício 3.1.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-01.dlt#L152-L177) (`exr:3-1-1-1`):**
   - Item (a): Para $\mathbf{u} = (6, -8)$ e $\mathbf{v} = (-1, 3)$:
     $$2\mathbf{v} = (-2, 6) \implies \mathbf{u} + 2\mathbf{v} = (6 + (-2),\, -8 + 6) = (4, -2).$$
     **Correto.**
   - Item (b): Norma e vetor unitário:
     $$\|\mathbf{u}\| = \sqrt{6^2 + (-8)^2} = \sqrt{36 + 64} = \sqrt{100} = 10.$$
     $$\hat{\mathbf{u}} = \frac{1}{10}(6, -8) = (0{,}6;\, -0{,}8).$$
     **Correto.**
   - Item (c): Produto escalar e classificação angular:
     $$\mathbf{u} \cdot \mathbf{v} = 6 \cdot (-1) + (-8) \cdot 3 = -6 - 24 = -30.$$
     Como $\mathbf{u} \cdot \mathbf{v} < 0$, temos $\cos\theta < 0$, caracterizando ângulo obtuso ($> 90^\circ$).
     **Correto.**

4. **[Exercício 3.1.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-01.dlt#L179-L200) (`exr:3-1-1-2`):**
   - Item (a): Variação de taxas no hipocampo $\mathbf{r}_0 = (5, 8, 4)\text{ Hz}$ para $\mathbf{r}_1 = (11, 16, 4)\text{ Hz}$:
     $$\Delta\mathbf{r} = (11 - 5,\, 16 - 8,\, 4 - 4) = (6, 8, 0)\text{ Hz}.$$
     $$\|\Delta\mathbf{r}\| = \sqrt{6^2 + 8^2 + 0^2} = \sqrt{36 + 64} = \sqrt{100} = 10\text{ Hz}.$$
     **Correto.**
   - Item (b): Ortogonalidade com $\mathbf{w} = (4, -3, 7)$:
     $$\Delta\mathbf{r} \cdot \mathbf{w} = 6 \cdot 4 + 8 \cdot (-3) + 0 \cdot 7 = 24 - 24 + 0 = 0.$$
     Produto escalar nulo confirma perpendicularidade.
     **Correto.**

---

### 3.2 Subseção 2: Funções vetoriais e curvas paramétricas (`sub:3-1-1-b`)

1. **[Exemplo 3.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-01.dlt#L231-L260) (`exm:3-1-trajetoria-neural`):**
   - Item (a): Oscilação sustentada com $f = 2\text{ Hz}$ ao redor de $\mathbf{c} = (20, 20)\text{ Hz}$:
     $$\mathbf{r}(t) - \mathbf{c} = \bigl(10\cos(4\pi t),\, 10\sin(4\pi t)\bigr).$$
     Distância ao centro:
     $$\|\mathbf{r}(t) - \mathbf{c}\| = \sqrt{100\cos^2(4\pi t) + 100\sin^2(4\pi t)} = 10\text{ Hz}.$$
     Trajetória circular de raio $R = 10\text{ Hz}$.
     Período fundamental: $4\pi T = 2\pi \implies T = \frac{1}{2} = 0{,}5\text{ s}$.
     Verificação dos pontos de orientação:
     - em $t = 0\text{ s}$: $\mathbf{r}(0) = (20 + 10,\, 20 + 0) = (30, 20)\text{ Hz}$;
     - em $t = 0{,}125\text{ s}$: $4\pi(0{,}125) = \frac{\pi}{2} \implies \mathbf{r}(0{,}125) = (20 + 0,\, 20 + 10) = (20, 30)\text{ Hz}$.
     Sentido anti-horário confirmado.
     **Correto.**
   - Item (b): Regime amortecido $\mathbf{r}(t) - \mathbf{c} = \bigl(10e^{-t}\cos(2\pi t),\, 10e^{-t}\sin(2\pi t)\bigr)$:
     Distância instantânea ao ponto fixo:
     $$\|\mathbf{r}(t) - \mathbf{c}\| = \sqrt{100e^{-2t}\bigl(\cos^2(2\pi t) + \sin^2(2\pi t)\bigr)} = 10e^{-t}\text{ Hz}.$$
     Avaliação nos ciclos:
     - $t = 0\text{ s}$: $\mathbf{r}(0) = (30, 20)\text{ Hz}$, distância $10\text{ Hz}$;
     - $t = 1\text{ s}$: $\cos(2\pi) = 1, \sin(2\pi) = 0 \implies \mathbf{r}(1) = (20 + 10e^{-1},\, 20)$.
       Como $e^{-1} \approx 0{,}36787944...$, temos $10e^{-1} \approx 3{,}68\text{ Hz}$ e $\mathbf{r}(1) \approx (23{,}68;\, 20)\text{ Hz}$;
     - $t = 2\text{ s}$: $\cos(4\pi) = 1, \sin(4\pi) = 0 \implies \mathbf{r}(2) = (20 + 10e^{-2},\, 20)$.
       Como $e^{-2} \approx 0{,}13533528...$, temos $10e^{-2} \approx 1{,}35\text{ Hz}$ e $\mathbf{r}(2) \approx (21{,}35;\, 20)\text{ Hz}$.
     Convergência espiral para $(20, 20)\text{ Hz}$.
     **Correto.**

2. **[Exercício 3.1.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-01.dlt#L274-L303) (`exr:3-1-1-3`):**
   - Curva $\mathbf{r}(t) = (t^2 - 4t + 10,\; 3t + 5)$, $t \ge 0$.
   - Item (a): Passagem por $(7, 14)$:
     $$r_1(t) = 7 \iff t^2 - 4t + 3 = 0 \iff (t - 1)(t - 3) = 0 \implies t = 1 \quad \text{ou} \quad t = 3.$$
     Testando na segunda componente $r_2(t) = 3t + 5$:
     - $r_2(1) = 3(1) + 5 = 8 \ne 14 \implies \mathbf{r}(1) = (7, 8)$;
     - $r_2(3) = 3(3) + 5 = 14 \implies \mathbf{r}(3) = (7, 14)$.
     Instante único: $t = 3\text{ s}$.
     **Correto.**
   - Item (b): Passagem por $(7, 20)$:
     $$r_2(t) = 20 \iff 3t + 5 = 20 \iff 3t = 15 \iff t = 5\text{ s}.$$
     Avaliando a primeira componente:
     $$r_1(5) = 5^2 - 4(5) + 10 = 25 - 20 + 10 = 15 \ne 7.$$
     Não existe $t$ comum; a trajetória nunca passa por $(7, 20)\text{ Hz}$.
     **Correto.**
   - Item (c): Eliminação do parâmetro $t$:
     $$r_2 = 3t + 5 \implies t = \frac{r_2 - 5}{3} \quad (\text{com } r_2 \ge 5 \text{ pois } t \ge 0).$$
     $$r_1 = \left(\frac{r_2 - 5}{3}\right)^2 - 4\left(\frac{r_2 - 5}{3}\right) + 10 = \frac{1}{9}r_2^2 - \frac{22}{9}r_2 + \frac{175}{9}.$$
     Curva parabólica no plano de estados.
     **Correto.**

---

### 3.3 Subseção 3: Limite, derivada e velocidade (`sub:3-1-1-c`)

1. **[Demonstração da Proposição 3.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-01.dlt#L346-L355) (`prop:3-1-regras-derivacao`):**
   - Regra do produto escalar:
     $$(\mathbf{u} \cdot \mathbf{v})'(t) = \frac{d}{dt}\sum_{i=1}^n u_i(t) v_i(t) = \sum_{i=1}^n \bigl(u_i'(t) v_i(t) + u_i(t) v_i'(t)\bigr) = \mathbf{u}'(t) \cdot \mathbf{v}(t) + \mathbf{u}(t) \cdot \mathbf{v}'(t).$$
   - Corolário para norma constante $\|\mathbf{r}(t)\| = R$:
     $$\mathbf{r}(t) \cdot \mathbf{r}(t) = R^2 \implies \frac{d}{dt}\bigl(\mathbf{r}(t) \cdot \mathbf{r}(t)\bigr) = 2\mathbf{r}'(t) \cdot \mathbf{r}(t) = 0 \implies \mathbf{r}'(t) \cdot \mathbf{r}(t) = 0.$$
     Velocidade perpendicular à posição em curvas esféricas/circulares.
     **Correto.**

2. **[Exemplo 3.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-01.dlt#L371-L407) (`exm:3-1-velocidade-neural`):**
   - Item (a): Derivada de $\mathbf{r}(t) = \bigl(20 + 10\cos(2\pi f t),\; 20 + 10\sin(2\pi f t)\bigr)$:
     $$r_1'(t) = 10\bigl(-\sin(2\pi f t)\bigr) \cdot 2\pi f = -20\pi f \sin(2\pi f t),$$
     $$r_2'(t) = 10\bigl(\cos(2\pi f t)\bigr) \cdot 2\pi f = 20\pi f \cos(2\pi f t).$$
     Rapidez:
     $$\|\mathbf{r}'(t)\| = \sqrt{(-20\pi f \sin)^2 + (20\pi f \cos)^2} = \sqrt{400\pi^2 f^2 (\sin^2 + \cos^2)} = 20\pi f\text{ Hz/s}.$$
     Para $f = 2\text{ Hz}$:
     $$\|\mathbf{r}'(t)\| = 40\pi \approx 125{,}6637... \approx 125{,}66\text{ Hz/s}.$$
     **Correto.**
   - Item (b): Verificação direta de ortogonalidade com $\mathbf{r}(t) - \mathbf{c}$:
     $$\mathbf{r}'(t) \cdot \bigl(\mathbf{r}(t) - \mathbf{c}\bigr) = \bigl(-20\pi f \sin(2\pi f t)\bigr)\bigl(10\cos(2\pi f t)\bigr) + \bigl(20\pi f \cos(2\pi f t)\bigr)\bigl(10\sin(2\pi f t)\bigr)$$
     $$= -200\pi f \sin(2\pi f t)\cos(2\pi f t) + 200\pi f \cos(2\pi f t)\sin(2\pi f t) = 0.$$
     **Correto.**
   - Item (c): Comprimento de arco em um ciclo $t \in [0, 1/f]$:
     $$L = \int_0^{1/f} 20\pi f\,dt = 20\pi f [t]_0^{1/f} = 20\pi f \cdot \frac{1}{f} = 20\pi \approx 62{,}83185... \approx 62{,}83\text{ Hz}.$$
     Coincide com a fórmula elementar $2\pi R = 2\pi \cdot 10 = 20\pi\text{ Hz}$.
     **Correto.**

3. **[Exemplo 3.5](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-01.dlt#L409-L432) (`exm:3-1-helice-bacteria`):**
   - Posição helicoidal $\mathbf{r}(t) = \bigl(3\cos(2t),\; 3\sin(2t),\; 8t\bigr)\;\mu\text{m}$, $t \in [0, \pi]$.
   - Item (a): Velocidade, rapidez e aceleração:
     $$\mathbf{r}'(t) = \bigl(-6\sin(2t),\; 6\cos(2t),\; 8\bigr)\;\mu\text{m/s}.$$
     $$\|\mathbf{r}'(t)\| = \sqrt{(-6\sin(2t))^2 + (6\cos(2t))^2 + 8^2} = \sqrt{36(\sin^2 + \cos^2) + 64} = \sqrt{100} = 10\;\mu\text{m/s}.$$
     $$\mathbf{r}''(t) = \bigl(-12\cos(2t),\; -12\sin(2t),\; 0\bigr)\;\mu\text{m/s}^2.$$
     **Correto.**
   - Item (b): Comprimento total percorrido em uma volta completa ($t \in [0, \pi]$):
     $$L = \int_0^\pi \|\mathbf{r}'(t)\|\,dt = \int_0^\pi 10\,dt = 10\pi \approx 31{,}4159... \approx 31{,}42\;\mu\text{m}.$$
     **Correto.**

4. **[Exercício 3.1.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-01.dlt#L443-L471) (`exr:3-1-1-4`):**
   - Curva da pata do animal $\mathbf{r}(t) = \left(2t,\; t^2,\; \frac{t^3}{3}\right)\text{ cm}$, $t \in [0, 3]\text{ s}$.
   - Item (a): Derivadas primeira e segunda:
     $$\mathbf{r}'(t) = (2,\; 2t,\; t^2), \qquad \mathbf{r}''(t) = (0,\; 2,\; 2t).$$
     Para $t = 1\text{ s}$:
     $$\mathbf{r}'(1) = (2, 2, 1)\text{ cm/s}, \qquad \|\mathbf{r}'(1)\| = \sqrt{2^2 + 2^2 + 1^2} = \sqrt{4 + 4 + 1} = \sqrt{9} = 3\text{ cm/s}.$$
     $$\mathbf{r}''(1) = (0, 2, 2)\text{ cm/s}^2.$$
     **Correto.**
   - Item (b): Simplificação algébrica da rapidez:
     $$\|\mathbf{r}'(t)\| = \sqrt{2^2 + (2t)^2 + (t^2)^2} = \sqrt{4 + 4t^2 + t^4} = \sqrt{(t^2 + 2)^2}.$$
     Como $t^2 + 2 \ge 2 > 0$ para todo $t \in \mathbb{R}$, resulta:
     $$\|\mathbf{r}'(t)\| = t^2 + 2\text{ cm/s}.$$
     **Correto.**
   - Item (c): Comprimento de arco em $[0, 3]$:
     $$L = \int_0^3 (t^2 + 2)\,dt = \left[\frac{t^3}{3} + 2t\right]_0^3 = \left(\frac{27}{3} + 6\right) - 0 = 9 + 6 = 15\text{ cm}.$$
     **Correto.**

5. **[Exercício 3.1.5](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/tema-01.dlt#L473-L507) (`exr:3-1-1-5`):**
   - Trajetória $r_1(t) = 10 + 3t^2 - t^3$ e $r_2(t) = 20 + 4t$, $t \in [0, 2]\text{ s}$.
   - Item (a): Vetores velocidade e aceleração:
     $$\mathbf{r}'(t) = (6t - 3t^2,\; 4)\text{ Hz/s}, \qquad \mathbf{r}''(t) = (6 - 6t,\; 0)\text{ Hz/s}^2.$$
     **Correto.**
   - Item (b): Otimização da rapidez ao quadrado $s(t) = \mathbf{r}'(t) \cdot \mathbf{r}'(t)$:
     Pela regra do produto escalar:
     $$s'(t) = 2\mathbf{r}'(t) \cdot \mathbf{r}''(t) = 2\bigl((6t - 3t^2)(6 - 6t) + 4 \cdot 0\bigr).$$
     Fatorando os polinômios:
     $$6t - 3t^2 = 3t(2 - t), \qquad 6 - 6t = 6(1 - t).$$
     $$s'(t) = 2 \cdot 3t(2 - t) \cdot 6(1 - t) = 36t(2 - t)(1 - t).$$
     No intervalo aberto $(0, 2)$, a única raiz é $t = 1\text{ s}$.
     Análise do sinal de $s'(t)$:
     - para $t \in (0, 1)$: $t > 0$, $2 - t > 0$, $1 - t > 0 \implies s'(t) > 0$ (rapidez estritamente crescente);
     - para $t \in (1, 2)$: $t > 0$, $2 - t > 0$, $1 - t < 0 \implies s'(t) < 0$ (rapidez estritamente decrescente).
     Portanto, $t = 1\text{ s}$ é o ponto de máximo global estrito em $[0, 2]$.
     **Correto.**
   - Item (c): Estado e velocidade no instante ótimo $t = 1\text{ s}$:
     $$\mathbf{r}'(1) = \bigl(6(1) - 3(1)^2,\; 4\bigr) = (3, 4)\text{ Hz/s},$$
     $$\|\mathbf{r}'(1)\| = \sqrt{3^2 + 4^2} = \sqrt{25} = 5\text{ Hz/s},$$
     $$\mathbf{r}(1) = \bigl(10 + 3(1)^2 - 1^3,\; 20 + 4(1)\bigr) = (12, 24)\text{ Hz}.$$
     Conferência nos extremos:
     - em $t = 0$: $\mathbf{r}'(0) = (0, 4) \implies \|\mathbf{r}'(0)\| = 4\text{ Hz/s} < 5\text{ Hz/s}$;
     - em $t = 2$: $\mathbf{r}'(2) = (12 - 12, 4) = (0, 4) \implies \|\mathbf{r}'(2)\| = 4\text{ Hz/s} < 5\text{ Hz/s}$.
     **Correto.**

6. **Auditoria Analítica do Script de Figura [trajetoria-estados.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/fig/trajetoria-estados.py):**
   - Curva: $\mathbf{r}(t) = \bigl(20 + 10e^{-t}\cos(2\pi t),\, 20 + 10e^{-t}\sin(2\pi t)\bigr)$.
   - Derivada de $r_1(t)$ via regra do produto:
     $$\frac{dr_1}{dt} = \frac{d}{dt}\bigl[10e^{-t}\cos(2\pi t)\bigr] = -10e^{-t}\cos(2\pi t) - 20\pi e^{-t}\sin(2\pi t) = -10e^{-t}\bigl(\cos(2\pi t) + 2\pi\sin(2\pi t)\bigr).$$
     No script (linha 20): `dr1 = -fator * (c + 2.0 * np.pi * s)`. **Idêntico.**
   - Derivada de $r_2(t)$:
     $$\frac{dr_2}{dt} = \frac{d}{dt}\bigl[10e^{-t}\sin(2\pi t)\bigr] = -10e^{-t}\sin(2\pi t) + 20\pi e^{-t}\cos(2\pi t) = 10e^{-t}\bigl(2\pi\cos(2\pi t) - \sin(2\pi t)\bigr).$$
     No script (linha 21): `dr2 = fator * (2.0 * np.pi * c - s)`. **Idêntico.**

**Nenhum erro matemático encontrado.**

---

## 4. Verificações Específicas do Padrão Editorial

### 4.1 Estrutura e Exercícios
- **Dicas e Soluções completas:** Todos os 5 exercícios (`exr:3-1-1-1` a `exr:3-1-1-5`) contêm `<hint>` detalhado e `<solution collapsible="true" collapsed="true">` com dedução analítica passo a passo, justificativas conceituais e conferências auxiliares.
- **Graduação dos exercícios:** Os títulos seguem estritamente a gradação contratual ("Básico", "Intermediário" e "Avançado"), cobrindo desde operações aritméticas com vetores até otimização diferencial de rapidez em trajetórias não lineares.

### 4.2 Exemplos Biológicos por Subseção
- **Abertura:** Medição populacional simultânea de disparos neuronais e voxels de neuroimagem funcional (fMRI).
- **Subseção 1 (`sub:3-1-1-a`):** Estado de três neurônios corticais diante de estímulo visual (`exm:3-1-estado-populacao`) e coordenadas de atividade no hipocampo (`exr:3-1-1-2`).
- **Subseção 2 (`sub:3-1-1-b`):** Dinâmica de oscilação sustentada e retorno amortecido ao repouso em par excitatório–inibitório (`exm:3-1-trajetoria-neural`), visualização em espaço de estados (`fig:3-1-trajetoria-estados`) e evolução temporal em tarefa motora (`exr:3-1-1-3`).
- **Subseção 3 (`sub:3-1-1-c`):** Velocidade e perímetro de ciclo em oscilação neural (`exm:3-1-velocidade-neural`), natação flagelar tridimensional helicoidal em meio viscoso (`exm:3-1-helice-bacteria`), cinemática tridimensional de pata de roedor (`exr:3-1-1-4`) e resposta cortical a pulso sensorial (`exr:3-1-1-5`).
- Cada divisão possui pelo menos um exemplo e exercício com contexto biológico quantitativo realista.

### 4.3 Afirmações de Neurociência e Biologia
- Os valores de frequência ($10$ a $30\text{ Hz}$), potencial de base de repouso populacional ($20\text{ Hz}$) e dinâmicas oscilatórias espirais amortecidas correspondem fielmente aos modelos clássicos de circuitos locais de Wilson–Cowan e Dayan & Abbott (*Theoretical Neuroscience*).
- A cinemática da bactéria flagelada condiz com a biofísica clássica de micro-organismos (Purcell / Berg). Não há artigos fictícios, números espúrios de página ou alegações arbitrárias.

### 4.4 Sequência Lógica e Apresentação Prévia
- A ordem de apresentação é estritamente pedagógica: vetor geométrico/algébrico $\to$ norma e produto escalar $\to$ função vetorial dependente do tempo $\to$ trajetória no espaço de estados $\to$ campo vetorial como conceito de transição $\to$ limites e derivadas componente a componente $\to$ cinemática (velocidade, rapidez, aceleração) $\to$ regra do produto escalar $\to$ comprimento de arco via integral de Riemann. Nenhum conceito é exigido antes de sua formalização.

### 4.5 Código Python e Figura
- O arquivo [trajetoria-estados.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-03/fig/trajetoria-estados.py) é autocontido, importa unicamente `pathlib`, `matplotlib` e `numpy`, utiliza `plt.rcParams["svg.fonttype"] = "none"` para leveza vetorial e salva o SVG diretamente no caminho relativo esperado (`fig/trajetoria-estados.svg`). O arquivo SVG correspondente existe e está integro.

### 4.6 Consistência de Notação
- **Vetores:** Formatados invariavelmente em negrito minúsculo ($\mathbf{u}$, $\mathbf{v}$, $\mathbf{r}$, $\Delta\mathbf{r}$, $\mathbf{w}$, $\mathbf{a}$, $\mathbf{b}$, $\mathbf{p}$, $\mathbf{c}$, $\mathbf{e}_1$, $\mathbf{e}_2$, $\mathbf{e}_3$, $\hat{\mathbf{v}}$, $\hat{\mathbf{d}}$, $\mathbf{r}'(t)$, $\mathbf{r}''(t)$).
- **Campos e Matrizes:** Campo vetorial em negrito maiúsculo ($\mathbf{F}(\mathbf{x})$); matrizes ausentes nesta aula introdutória, reservadas aos Módulos 3.2, 4 e 5.
- **Escalares:** Letras em itálico ($t$, $x$, $y$, $z$, $c$, $f$, $L$, $R$, $\theta$).
- **Gradiente:** Mencionado em texto como $\nabla f(x, y)$, estritamente sem negrito no operador $\nabla$, conforme regra contratual.
- **Decimais:** Vírgula com proteção de chaves no LaTeX ($32{,}70$; $0{,}6$; $0{,}5$) e ponto em código Python.

### 4.7 Cobertura do Guia e Extensão
- **Subtema único:** "Introdução e visualização" do Tema 3.1 Funções Vetoriais (Nível Básico).
- **Conteúdos cobertos:** Vetores em $\mathbb{R}^n$, norma euclidiana, vetor unitário, produto escalar, função vetorial, curvas paramétricas (reta, círculo, hélice), espaço de estados de 2–3 neurônios, noção introdutória de campo vetorial, limites, continuidade, derivada componente a componente, cinemática vetorial (velocidade, rapidez, aceleração), regra do produto escalar e comprimento de arco por integral definida.
- **Extensão do texto:** O documento possui aproximadamente 3 350 palavras de prosa técnica, perfeitamente situado na faixa estipulada de 2 800 a 4 000 palavras.

---

## 5. Conclusão

O material apresenta excelência pedagógica e matemática, estando apto para compilação definitiva sem necessidade de alterações no arquivo-fonte. A aula atende perfeitamente ao perfil de alunos de Biologia em transição para a Neurociência Computacional.