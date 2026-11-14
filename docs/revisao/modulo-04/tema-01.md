# Relatório de Revisão Técnica — Módulo 04 · Tema 01 (Espaço de variáveis)

- **Arquivo revisado:** [tema-01.dlt](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-01.dlt)
- **Script de figura associado:** [paisagem-custo.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/fig/paisagem-custo.py) (gera [paisagem-custo.svg](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/fig/paisagem-custo.svg))
- **Documentos de referência:** [PADRAO-AULAS.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/PADRAO-AULAS.md) e [DELTA-COLA.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/DELTA-COLA.md)
- **Data da revisão:** 14 de novembro de 2026
- **Perfil do revisor:** Matemático, Neurocientista Computacional e Professor de Alunos de Ciências Biológicas

---

## 1. Veredito

**APROVAR**

A aula atende rigorosamente a todos os critérios matemáticos, biofísicos, pedagógicos e estruturais do projeto. Todas as contas de todos os exemplos e de todas as soluções dos 16 exercícios foram integralmente recalculadas e conferidas à mão e passo a passo — **nenhum erro matemático foi encontrado**. O código Python em NumPy é autocontido, funcional e produz com exatidão as saídas indicadas nos comentários. A progressão conceitual é exemplar para alunos de Ciências Biológicas, com analogias consistentes, exemplos autênticos de neurociência teórica (Dayan & Abbott; Hodgkin & Huxley) e respeito integral às normas de sintaxe do Delta v0.6.0.

Foram identificadas 4 observações de polimento pedagógico e de formato, nenhuma de caráter impeditivo para publicação.

---

## 2. Tabela de Problemas e Observações

| Severidade | Local | Trecho | Correção sugerida |
|---|---|---|---|
| Pedagógico | Seção 1 (`sec:4-1-1`), [exm:4-1-retificado](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-01.dlt#L87-L89), linha ~88 | `A região viável é o quadrante aberto à direita e fechado na base:` | No plano $(g, \theta)$ com ganho $g$ no eixo horizontal e limiar $\theta$ no eixo vertical, a condição $g > 0$ significa que a fronteira aberta é a vertical à esquerda ($g = 0$), enquanto a base $\theta = 0$ é fechada ($\theta \ge 0$). Dizer "aberto à direita" pode induzir o estudante de Biologia a pensar em um limitante superior aberto para $g$. Sugere-se: `A região viável é o primeiro quadrante com fronteira vertical aberta ($g = 0$) e base horizontal fechada ($\theta = 0$):` ou `A região viável é o quadrante delimitado por $g > 0$ e $\theta \ge 0$ (fronteira vertical aberta e base fechada):`. |
| Pedagógico | Seção 2 (`sec:4-1-2`), [exm:4-1-contraste-custo](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-01.dlt#L281-L293), linha ~291 | `\frac{4}{4}b^2` | Na expansão algébrica detalhada de $J(a, b)$, são listadas explicitamente as somas $\sum x_i$, $\sum x_i^2$, $\sum y_i$, $\sum x_i y_i$ e $\sum y_i^2$, mas não se menciona explicitamente a soma dos termos unitários $\sum_{i=1}^4 1 = 4$. Para estudantes com matemática de ensino médio enferrujada, explicitar na lista de somatórios que $\sum_{i=1}^m 1 = m = 4$ torna a origem do termo $\frac{4}{4}b^2$ imediatamente transparente. |
| Pedagógico | Seção 3 (`sec:4-1-3`), [exr:4-1-3-4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-01.dlt#L587), linha ~587 | `$\cos\theta = \frac{\mathbf{a} \cdot \mathbf{b}}{\|\mathbf{a}\|\,\|\mathbf{b}\|}$` | Como os símbolos escalares $a$ e $b$ são usados intensivamente ao longo de quase toda a aula como parâmetros do modelo linear ($\hat{y} = ax + b$), o uso dos símbolos vetoriais genéricos $\mathbf{a}$ e $\mathbf{b}$ na dica pode causar uma distração visual momentânea. Sugere-se usar diretamente os vetores nomeados na resolução: `$\cos\theta = \frac{\mathbf{d} \cdot \mathbf{v}}{\|\mathbf{d}\|\,\|\mathbf{v}\|}$` ou a fórmula genérica neutra `$\cos\theta = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\|\,\|\mathbf{v}\|}$`. |
| Formato | Script [paisagem-custo.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/fig/paisagem-custo.py#L69-L70), linhas 69–70 | `ax_cont.set_xlabel("Inclinação a (Hz por unidade de contraste)", ...)` e `ax_cont.set_ylabel("Intercepto b (Hz)", ...)` | No painel esquerdo (`ax_dados`), as variáveis $x$ e $y$ foram formatadas em modo matemático LaTeX (`"$x$"` e `"$y$"`). No painel direito (`ax_cont`), $a$ e $b$ foram digitadas em texto puro sem cifrões. Para padronização tipográfica interna no SVG gerado, sugere-se: `"Inclinação $a$ (Hz por unidade de contraste)"` e `"Intercepto $b$ (Hz)"`. |

---

## 3. Recálculo e Auditoria Integral de Contas

Todas as contas foram refeitas passo a passo à mão:

### 3.1 Seção 1: Configurações como pontos (`sec:4-1-1`)

1. **[Exemplo 4.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-01.dlt#L75-L103) (`exm:4-1-retificado`):**
   - Modelo $r(I) = g \, \max(0,\, I - \theta)$.
   - $\mathbf{w}_A = (40;\; 0{,}2)$:
     - $I = 0{,}4\text{ nA} \implies r(0{,}4) = 40 \max(0,\, 0{,}4 - 0{,}2) = 40 \cdot 0{,}2 = 8\text{ Hz}$. **Correto.**
     - $I = 0{,}8\text{ nA} \implies r(0{,}8) = 40 \max(0,\, 0{,}8 - 0{,}2) = 40 \cdot 0{,}6 = 24\text{ Hz}$. **Correto.**
   - $\mathbf{w}_B = (25;\; 0{,}5)$:
     - $I = 0{,}4\text{ nA} \implies r(0{,}4) = 25 \max(0,\, 0{,}4 - 0{,}5) = 25 \cdot 0 = 0\text{ Hz}$. **Correto.**
     - $I = 0{,}8\text{ nA} \implies r(0{,}8) = 25 \max(0,\, 0{,}8 - 0{,}5) = 25 \cdot 0{,}3 = 7{,}5\text{ Hz}$. **Correto.**
2. **[Exemplo 4.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-01.dlt#L105-L126) (`exm:4-1-sintonia-estados`):**
   - Curva de sintonia gaussiana $r(\phi) = r_{\max} \exp\!\left(-\frac{(\phi - \phi_0)^2}{2\sigma^2}\right)$.
   - $\mathbf{w}_1 = (60;\; 90;\; 15)$ em $\phi = 90^\circ$:
     - $\phi - \phi_0 = 0 \implies r(90^\circ) = 60 \exp(0) = 60\text{ Hz}$. **Correto.**
   - $\mathbf{w}_2 = (60;\; 60;\; 15)$ em $\phi = 90^\circ$:
     - $\phi - \phi_0 = 30^\circ \implies \frac{30^2}{2 \cdot 15^2} = \frac{900}{2 \cdot 225} = \frac{900}{450} = 2$.
     - $r(90^\circ) = 60 e^{-2} \approx 60 \cdot 0{,}135335 = 8{,}1201... \approx 8{,}12\text{ Hz}$. **Correto.**
3. **[Exercício 4.1.1.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-01.dlt#L133-L147) (`exr:4-1-1-1`):**
   - Item (a): $I_{\text{sin}}(t) = I_0 e^{-t/\tau} \implies \mathbf{w} = (I_0, \tau) \in \mathbb{R}^2$, dimensão $n = 2$, $\Omega = \{(I_0, \tau) \in \mathbb{R}^2 : I_0 > 0 \text{ e } \tau > 0\}$. **Correto.**
   - Item (b): $R(C) = R_{\max}\frac{C^h}{K^h + C^h} \implies \mathbf{w} = (R_{\max}, K, h) \in \mathbb{R}^3$, dimensão $n = 3$, $\Omega = \{(R_{\max}, K, h) \in \mathbb{R}^3 : R_{\max} \ge 0,\; K > 0,\; h > 0\}$. **Correto.**
4. **[Exercício 4.1.1.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-01.dlt#L149-L169) (`exr:4-1-1-2`):**
   - Item (a): $r(I) = 30 \max(0,\, I - 0{,}3)$.
     - $I = 0{,}1 \implies 30 \cdot 0 = 0\text{ Hz}$;
     - $I = 0{,}3 \implies 30 \cdot 0 = 0\text{ Hz}$;
     - $I = 0{,}7 \implies 30 \cdot 0{,}4 = 12\text{ Hz}$. **Correto.**
   - Item (b): Descola em $I = 0{,}4\text{ nA} \implies \theta = 0{,}4\text{ nA}$; inclinação $50\text{ Hz/nA} \implies g = 50\text{ Hz/nA}$. Ponto $\mathbf{w} = (50;\; 0{,}4)$. **Correto.**
5. **[Exercício 4.1.1.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-01.dlt#L171-L189) (`exr:4-1-1-3`):**
   - Item (a): $\mathbf{w}_1 = (120, 36)$ e $\mathbf{w}_2 = (117, 40)$ têm coordenadas estritamente positivas, logo pertencem a $\Omega$. O ponto $\mathbf{w}_3 = (120, -5)$ possui $\bar{g}_{\text{K}} = -5 < 0$, violando a viabilidade física. **Correto.**
   - Item (b): $\mathbf{w}_2 - \mathbf{w}_1 = (117 - 120,\, 40 - 36) = (-3,\, 4)$.
     - $\|\mathbf{w}_2 - \mathbf{w}_1\| = \sqrt{(-3)^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5\text{ mS/cm}^2$. **Correto.**
6. **[Exercício 4.1.1.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-01.dlt#L191-L212) (`exr:4-1-1-4`):**
   - Item (a): 3 neurônios, conexões direcionadas $3 \times 2 = 6$ pesos $w_{ij}$ e $3$ limiares $\theta_i$, totalizando $9$ parâmetros ($\mathbb{R}^9$). O espaço de estados das taxas $(r_1, r_2, r_3)$ tem dimensão $3$. **Correto.**
   - Item (b): Convenção $w_{ij}$ (efeito do pré $j$ no pós $i$):
     - Pré 1 excitatório: $w_{21} \ge 0$, $w_{31} \ge 0$.
     - Pré 2 inibitório: $w_{12} \le 0$, $w_{32} \le 0$.
     - Pré 3 inibitório: $w_{13} \le 0$, $w_{23} \le 0$. **Correto.**

---

### 3.2 Seção 2: A função custo como paisagem (`sec:4-1-2`)

1. **[Exemplo 4.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-01.dlt#L253-L297) (`exm:4-1-contraste-custo`):**
   - Dados: $(0{,}2;\; 21), (0{,}4;\; 27), (0{,}6;\; 43), (0{,}8;\; 49)$.
   - Item (a): Reta por $(0{,}2;\; 21)$ e $(0{,}4;\; 27)$ tem $a = \frac{27 - 21}{0{,}4 - 0{,}2} = 30$ e $b = 21 - 30(0{,}2) = 15$. Em $x = 0{,}6$, $\hat{y} = 30(0{,}6) + 15 = 33 \ne 43$, provando a não colinearidade dos 4 pontos. **Correto.**
   - Item (b): Avaliação de $J(a, b) = \frac{1}{4}\sum_{i=1}^4 (ax_i + b - y_i)^2$:
     - $\mathbf{w}_1 = (40, 10)$: previsões $18, 26, 34, 42$; erros $-3, -1, -9, -7$; quadrados $9, 1, 81, 49$; soma $140$; $J = \frac{140}{4} = 35$. **Correto.**
     - $\mathbf{w}_2 = (40, 15)$: previsões $23, 31, 39, 47$; erros $+2, +4, -4, -2$; quadrados $4, 16, 16, 4$; soma $40$; $J = \frac{40}{4} = 10$. **Correto.**
     - $\mathbf{w}_3 = (50, 10)$: previsões $20, 30, 40, 50$; erros $-1, +3, -3, +1$; quadrados $1, 9, 9, 1$; soma $20$; $J = \frac{20}{4} = 5$. **Correto.**
   - Item (c): Somatórios:
     - $\sum x_i = 0{,}2 + 0{,}4 + 0{,}6 + 0{,}8 = 2{,}0$;
     - $\sum x_i^2 = 0{,}04 + 0{,}16 + 0{,}36 + 0{,}64 = 1{,}20$;
     - $\sum y_i = 21 + 27 + 43 + 49 = 140$;
     - $\sum x_i y_i = 4{,}2 + 10{,}8 + 25{,}8 + 39{,}2 = 80{,}0$;
     - $\sum y_i^2 = 441 + 729 + 1\,849 + 2\,401 = 5\,420$.
     - Coeficientes divididos por $m = 4$:
       $a^2$: $\frac{1{,}20}{4} = 0{,}3$;
       $ab$: $\frac{2 \cdot 2{,}0}{4} = 1{,}0$;
       $b^2$: $\frac{4}{4} = 1{,}0$;
       $a$: $-\frac{2 \cdot 80{,}0}{4} = -40$;
       $b$: $-\frac{2 \cdot 140}{4} = -70$;
       constante: $\frac{5\,420}{4} = 1\,355$.
       $$J(a, b) = 0{,}3a^2 + ab + b^2 - 40a - 70b + 1\,355.$$
       Conferência em $(50, 10)$: $0{,}3(2\,500) + 500 + 100 - 2\,000 - 700 + 1\,355 = 750 + 600 - 2\,700 + 1\,355 = 1\,350 - 2\,700 + 1\,355 = 5$. **Correto.**
2. **[Exemplo 4.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-01.dlt#L301-L313) (`exm:4-1-custo-quadratico`):**
   - $L(w_1, w_2) = 12 - (w_1 - 2)^2 - 4(w_2 - 5)^2 \implies J(w_1, w_2) = (w_1 - 2)^2 + 4(w_2 - 5)^2 - 12$.
   - $J_{w_1} = 2(w_1 - 2) = 0 \implies w_1 = 2$.
   - $J_{w_2} = 8(w_2 - 5) = 0 \implies w_2 = 5$.
   - $J(2, 5) = -12$ (mínimo global pois quadrados $\ge 0$) $\implies L(2, 5) = 12$ (máximo global). **Correto.**
3. **[Exercício 4.1.2.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-01.dlt#L320-L333) (`exr:4-1-2-1`):**
   - Dados $(0, 3), (1, 5), (2, 5), (3, 7)$.
   - $\mathbf{w}_A = (2, 2)$: previsões $2, 4, 6, 8$; erros $-1, -1, 1, 1$; quadrados $1, 1, 1, 1$; $J(2, 2) = \frac{4}{4} = 1$. **Correto.**
   - $\mathbf{w}_B = (1, 3)$: previsões $3, 4, 5, 6$; erros $0, -1, 0, -1$; quadrados $0, 1, 0, 1$; $J(1, 3) = \frac{2}{4} = 0{,}5$. **Correto.**
   - $J(1, 3) = 0{,}5 < 1 \implies (1, 3)$ ajusta melhor. **Correto.**
4. **[Exercício 4.1.2.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-01.dlt#L335-L348) (`exr:4-1-2-2`):**
   - $L(\tau, g) = 10 - 2(\tau - 3)^2 - (g - 4)^2 \implies J(\tau, g) = 2(\tau - 3)^2 + (g - 4)^2 - 10$.
   - $\frac{\partial J}{\partial \tau} = 4(\tau - 3) = 0 \implies \tau = 3$; $\frac{\partial J}{\partial g} = 2(g - 4) = 0 \implies g = 4$.
   - Mínimo de $J = -10$, máximo de $L = 10$ no ponto $(3, 4)$. **Correto.**
5. **[Exercício 4.1.2.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-01.dlt#L350-L368) (`exr:4-1-2-3`):**
   - Modelo A: erros $(1, -1, 0, 10)$:
     - $\text{EAM}_A = \frac{1 + 1 + 0 + 10}{4} = \frac{12}{4} = 3{,}00\text{ Hz}$. **Correto.**
     - $\text{EQM}_A = \frac{1 + 1 + 0 + 100}{4} = \frac{102}{4} = 25{,}50\text{ Hz}^2$. **Correto.**
   - Modelo B: erros $(3, -3, 3, -4)$:
     - $\text{EAM}_B = \frac{3 + 3 + 3 + 4}{4} = \frac{13}{4} = 3{,}25\text{ Hz}$. **Correto.**
     - $\text{EQM}_B = \frac{9 + 9 + 9 + 16}{4} = \frac{43}{4} = 10{,}75\text{ Hz}^2$. **Correto.**
   - Comparação: EAM escolhe A ($3{,}00 < 3{,}25$); EQM escolhe B ($10{,}75 < 25{,}50$). **Correto.**
6. **[Exercício 4.1.2.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-01.dlt#L370-L395) (`exr:4-1-2-4`):**
   - $J(w_1, w_2) = 2w_1^2 + w_2^2 - 8w_1 + 6w_2 + 20$.
   - Item (a): $J_{w_1} = 4w_1 - 8 = 0 \implies w_1 = 2$; $J_{w_2} = 2w_2 + 6 = 0 \implies w_2 = -3$. Ponto crítico $(2, -3)$. **Correto.**
   - Item (b): $2(w_1^2 - 4w_1) = 2\bigl((w_1 - 2)^2 - 4\bigr) = 2(w_1 - 2)^2 - 8$.
     $(w_2^2 + 6w_2) = (w_2 + 3)^2 - 9$.
     $J = 2(w_1 - 2)^2 + (w_2 + 3)^2 - 8 - 9 + 20 = 2(w_1 - 2)^2 + (w_2 + 3)^2 + 3$.
     Mínimo global $J(2, -3) = 3$. **Correto.**

---

### 3.3 Seção 3: Curvas de nível (`sec:4-1-3`)

1. **[Exemplo 4.5](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-01.dlt#L445-L478) (`exm:4-1-elipses-contraste`):**
   - Item (a): $J(a, b) = 5 + 0{,}05(a - 50)^2 + \bigl((b - 10) + 0{,}5(a - 50)\bigr)^2$.
     - Expandindo: $5 + 0{,}05(a-50)^2 + (b-10)^2 + (a-50)(b-10) + 0{,}25(a-50)^2$
       $= 5 + 0{,}3(a-50)^2 + (a-50)(b-10) + (b-10)^2$
       $= 5 + 0{,}3(a^2 - 100a + 2\,500) + (ab - 10a - 50b + 500) + (b^2 - 20b + 100)$
       $= 0{,}3a^2 + ab + b^2 - 40a - 70b + (5 + 750 + 500 + 100) = 0{,}3a^2 + ab + b^2 - 40a - 70b + 1\,355$.
       Bate perfeitamente com a <ref to="eq:4-1-custo-polinomio"/>. **Correto.**
   - Item (b): Curva $J(a, b) = 10 \implies 0{,}05(a - 50)^2 + \bigl((b - 10) + 0{,}5(a - 50)\bigr)^2 = 5$.
     - Em $a = 50$: $(b - 10)^2 = 5 \implies b = 10 \pm \sqrt{5} \approx 10 \pm 2{,}236... \approx 10 \pm 2{,}24$. **Correto.**
     - Ao longo do eixo do vale $(b - 10) = -0{,}5(a - 50)$:
       $0{,}05(a - 50)^2 = 5 \implies (a - 50)^2 = 100 \implies a = 50 \pm 10 \implies a \in \{40, 60\}$.
       Pontos $(40, 15)$ e $(60, 5)$, onde $J = 10$. **Correto.**
   - Item (c): Derivadas parciais $J_a = 0{,}6a + b - 40$, $J_b = a + 2b - 70$.
     - Em $(40, 15)$: $J_a = 0{,}6(40) + 15 - 40 = 24 + 15 - 40 = -1$; $J_b = 40 + 30 - 70 = 0$.
     - $\nabla J(40, 15) = (-1, 0) \implies -\nabla J(40, 15) = (1, 0)$. **Correto.**
2. **[Exemplo 4.6](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-01.dlt#L482-L505) (`exm:4-1-dois-vales`):**
   - $J(w_1, w_2) = (w_1^2 - 1)^2 + w_2^2$.
   - $J_{w_1} = 4w_1(w_1^2 - 1) = 0 \implies w_1 \in \{-1, 0, 1\}$; $J_{w_2} = 2w_2 = 0 \implies w_2 = 0$.
   - Pontos críticos: $(-1, 0)$ e $(1, 0)$ com $J = 0$ (mínimos globais); $(0, 0)$ com $J = 1$ (sela).
   - Topologia de contorno: $c = 0{,}5$ (dois laços separados); $c = 1$ (oito/lemniscata); $c = 2$ (laço único abrangente). **Correto.**
3. **[Exercício 4.1.3.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-01.dlt#L512-L526) (`exr:4-1-3-1`):**
   - $J(w_1, w_2) = w_1^2 + 4w_2^2$.
   - $c = 4 \implies \frac{w_1^2}{2^2} + \frac{w_2^2}{1^2} = 1$ (semieixos $2$ e $1$);
   - $c = 16 \implies \frac{w_1^2}{4^2} + \frac{w_2^2}{2^2} = 1$ (semieixos $4$ e $2$). Vale 2 vezes mais longo em $w_1$. **Correto.**
   - Em $(2, 1)$: $\nabla J = (2w_1, 8w_2) = (4, 8) \implies -\nabla J(2, 1) = (-4, -8)$. **Correto.**
4. **[Exercício 4.1.3.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-01.dlt#L528-L548) (`exr:4-1-3-2`):**
   - Ponto $(55, 8)$: $a - 50 = 5$, $b - 10 = -2 \implies J(55, 8) = 5 + 0{,}05(25) + (-2 + 2{,}5)^2 = 5 + 1{,}25 + 0{,}25 = 6{,}5$. Fica no interior da curva $c = 8$. **Correto.**
   - Ponto $(55, 10)$: $a - 50 = 5$, $b - 10 = 0 \implies J(55, 10) = 5 + 1{,}25 + 2{,}5^2 = 5 + 1{,}25 + 6{,}25 = 12{,}5$. Fica entre as curvas $c = 8$ e $c = 15$. **Correto.**
   - Ponto $(50, 12)$: $J_a = 0{,}6(50) + 12 - 40 = 2$; $J_b = 50 + 24 - 70 = 4$. $-\nabla J(50, 12) = (-2, -4)$, com componente horizontal negativa. **Correto.**
5. **[Exercício 4.1.3.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-01.dlt#L550-L578) (`exr:4-1-3-3`):**
   - $J(u, v) = 3u^4 - 4u^3 - 12u^2 + 6v^2$.
   - $J_v = 12v = 0 \implies v = 0$.
   - $J_u = 12u(u^2 - u - 2) = 12u(u+1)(u-2) = 0 \implies u \in \{-1, 0, 2\}$.
   - Valores críticos:
     - $J(-1, 0) = 3(1) - 4(-1) - 12(1) = 3 + 4 - 12 = -5$;
     - $J(0, 0) = 0$;
     - $J(2, 0) = 3(16) - 4(8) - 12(4) = 48 - 32 - 48 = -32$. **Correto.**
   - $(2, 0)$ é mínimo global e $(-1, 0)$ é mínimo local. **Correto.**
   - Em $(-0{,}5;\; 0)$: $J_u(-0{,}5;\; 0) = 12(-0{,}5)(0{,}5)(-2{,}5) = +7{,}5$, $J_v = 0 \implies -\nabla J(-0{,}5;\; 0) = (-7{,}5;\; 0)$, atraindo para a esquerda (vale $(-1, 0)$). **Correto.**
6. **[Exercício 4.1.3.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-01.dlt#L580-L608) (`exr:4-1-3-4`):**
   - $\mathbf{w} = (50, 12)$, $\mathbf{w}^* = (50, 10) \implies \mathbf{d} = (0, -2)$; $\mathbf{v} = -\nabla J(50, 12) = (-2, -4)$.
   - $\mathbf{d} \cdot \mathbf{v} = 0 + 8 = 8$; $\|\mathbf{d}\| = 2$; $\|\mathbf{v}\| = \sqrt{4 + 16} = \sqrt{20} = 2\sqrt{5}$.
   - $\cos\theta = \frac{8}{2 \cdot 2\sqrt{5}} = \frac{2}{\sqrt{5}} = \frac{2\sqrt{5}}{5} \approx 0{,}8944... \implies \theta \approx 26{,}565^\circ \approx 26{,}6^\circ$. **Correto.**
   - Derivadas direcionais com $\nabla J = (2, 4)$:
     - $\mathbf{u}_1 = (0, -1) \implies D_{\mathbf{u}_1} J = (2, 4) \cdot (0, -1) = -4$. **Correto.**
     - $\mathbf{u}_2 = \left(-\frac{1}{\sqrt{5}}, -\frac{2}{\sqrt{5}}\right) \implies D_{\mathbf{u}_2} J = -\frac{2 + 8}{\sqrt{5}} = -\frac{10}{\sqrt{5}} = -2\sqrt{5} \approx -4{,}472... \approx -4{,}47$. **Correto.**
     - Queda inicial $\approx 11{,}8\% \approx 12\%$ mais rápida. **Correto.**

---

### 3.4 Seção 4: Ajustando dois parâmetros a dados (`sec:4-1-4`)

1. **[Exemplo 4.7](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-01.dlt#L630-L657) (`exm:4-1-grade-manual`):**
   - Grade $a \in \{40, 55, 70\}$ e $b \in \{5, 10, 15\}$ com $J = 5 + 0{,}05(a-50)^2 + \bigl((b-10) + 0{,}5(a-50)\bigr)^2$:
     - $a = 40$ ($0{,}05(-10)^2 = 5$, $0{,}5(-10) = -5$):
       $J(40, 5) = 5 + 5 + (-5 - 5)^2 = 110$;
       $J(40, 10) = 5 + 5 + (0 - 5)^2 = 35$;
       $J(40, 15) = 5 + 5 + (5 - 5)^2 = 10$. **Correto.**
     - $a = 55$ ($0{,}05(5)^2 = 1{,}25$, $0{,}5(5) = 2{,}5$):
       $J(55, 5) = 5 + 1{,}25 + (-5 + 2{,}5)^2 = 6{,}25 + 6{,}25 = 12{,}5$;
       $J(55, 10) = 5 + 1{,}25 + (0 + 2{,}5)^2 = 6{,}25 + 6{,}25 = 12{,}5$;
       $J(55, 15) = 5 + 1{,}25 + (5 + 2{,}5)^2 = 6{,}25 + 56{,}25 = 62{,}5$. **Correto.**
     - $a = 70$ ($0{,}05(20)^2 = 20$, $0{,}5(20) = 10$):
       $J(70, 5) = 5 + 20 + (-5 + 10)^2 = 25 + 25 = 50$;
       $J(70, 10) = 5 + 20 + (0 + 10)^2 = 25 + 100 = 125$;
       $J(70, 15) = 5 + 20 + (5 + 10)^2 = 25 + 225 = 250$. **Correto.**
   - Todos os 9 valores da [Tabela 4.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-01.dlt#L644-L656) (`tbl:4-1-grade`) conferem exatamente; menor custo $10{,}0$ em $(40, 15)$. **Correto.**
2. **[Código 4.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-01.dlt#L668-L705) (`cod:4-1-grid-search`):**
   - Eixos: `a_vals` tem 9 pontos em $[30, 70]$ (passo 5: $30, 35, 40, 45, 50, 55, 60, 65, 70$); `b_vals` tem 11 pontos em $[0, 20]$ (passo 2: $0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20$).
   - `J.size = 9 \times 11 = 99` avaliações.
   - Ponto ótimo analítico $(50{,}0;\; 10{,}0)$ pertence aos nós da grade ($a\_vals[4] = 50.0$, $b\_vals[5] = 10.0$), logo o mínimo é atingido exatamente nele, com $J = 5{,}000$. Saídas nos comentários conferem exatamente. **Correto.**
3. **[Exemplo 4.8](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-01.dlt#L709-L727) (`exm:4-1-maldicao`):**
   - Item (a): $n = 2, k = 50 \implies 50^2 = 2\,500$ pontos; $2\,500 \times 0{,}001\text{ s} = 2{,}5\text{ s}$. **Correto.**
   - Item (b): $n = 6, k = 20 \implies 20^6 = 64 \times 10^6 = 64\,000\,000$ pontos; $64\,000\text{ s} = \frac{64\,000}{3\,600}\text{ h} = \frac{160}{9}\text{ h} \approx 17{,}777... \approx 17{,}8\text{ h}$. **Correto.**
   - $n = 1\,000 \implies 2^{1000} = (2^{10})^{100} \approx (10^3)^{100} = 10^{300}$ (mais precisamente $\approx 1{,}07 \times 10^{301} \gg 10^{80}$). **Correto.**
4. **[Exercício 4.1.4.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-01.dlt#L734-L748) (`exr:4-1-4-1`):**
   - Item (a): $n = 3, k = 15 \implies 15^3 = 3\,375$ avaliações. **Correto.**
   - Item (b): $n = 4, k = 15 \implies 15^4 = 50\,625$ avaliações; tempo multiplicado por $15$. **Correto.**
5. **[Exercício 4.1.4.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-01.dlt#L750-L775) (`exr:4-1-4-2`):**
   - Dados $(0, 2), (1, 3), (2, 6)$ e $J(a, b) = \frac{1}{3}\sum (ax_i + b - y_i)^2$.
   - Grade $a \in \{1, 2\}, b \in \{1, 2\}$:
     - $(1, 1)$: previsões $1, 2, 3$; erros $-1, -1, -3$; quadrados $1, 1, 9$; $J = \frac{11}{3} \approx 3{,}67$.
     - $(1, 2)$: previsões $2, 3, 4$; erros $0, 0, -2$; quadrados $0, 0, 4$; $J = \frac{4}{3} \approx 1{,}33$.
     - $(2, 1)$: previsões $1, 3, 5$; erros $-1, 0, -1$; quadrados $1, 0, 1$; $J = \frac{2}{3} \approx 0{,}67$.
     - $(2, 2)$: previsões $2, 4, 6$; erros $0, 1, 0$; quadrados $0, 1, 0$; $J = \frac{1}{3} \approx 0{,}33$.
     - Vencedor da grade: $(2, 2)$ com $J = \frac{1}{3}$. **Correto.**
   - Ponto contínuo exato $(2, 5/3)$:
     - Previsões: $\frac{5}{3}, \frac{11}{3}, \frac{17}{3}$; erros: $-\frac{1}{3}, \frac{2}{3}, -\frac{1}{3}$; quadrados: $\frac{1}{9}, \frac{4}{9}, \frac{1}{9}$; soma: $\frac{6}{9} = \frac{2}{3}$;
     - $J(2, 5/3) = \frac{2/3}{3} = \frac{2}{9} \approx 0{,}222... \approx 0{,}22$.
     - Como $\frac{2}{9} < \frac{1}{3}$, confirma-se que a grade perdeu o mínimo contínuo. **Correto.**
6. **[Exercício 4.1.4.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-01.dlt#L777-L799) (`exr:4-1-4-3`):**
   - `a_vals = np.linspace(35.0, 65.0, 4)`: passo $\frac{65 - 35}{3} = 10 \implies [35.0, 45.0, 55.0, 65.0]$.
   - `b_vals = np.linspace(0.0, 20.0, 6)`: passo $\frac{20 - 0}{5} = 4 \implies [0.0, 4.0, 8.0, 12.0, 16.0, 20.0]$.
   - $4 \times 6 = 24$ avaliações. **Correto.**
   - Custo nos nós mais próximos:
     - $J(45, 12) = 5 + 0{,}05(-5)^2 + \bigl(2 + 0{,}5(-5)\bigr)^2 = 5 + 1{,}25 + 0{,}25 = 6{,}5$.
     - $J(55, 8) = 5 + 0{,}05(5)^2 + \bigl(-2 + 0{,}5(5)\bigr)^2 = 5 + 1{,}25 + 0{,}25 = 6{,}5$.
     - Empate em $6{,}5$. **Correto.**
7. **[Exercício 4.1.4.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-01.dlt#L801-L830) (`exr:4-1-4-4`):**
   - $r_{\max} \in [20, 80]$ passo $1 \implies \frac{80 - 20}{1} + 1 = 61$ valores;
   - $\phi_0 \in [0, 180]$ passo $5 \implies \frac{180 - 0}{5} + 1 = 37$ valores;
   - $\sigma \in [10, 30]$ passo $2 \implies \frac{30 - 10}{2} + 1 = 11$ valores.
   - 1 neurônio: $61 \times 37 \times 11 = 2\,257 \times 11 = 24\,827$ avaliações. **Correto.**
   - 5 neurônios acoplados ($n = 15$): $(24\,827)^5 \approx (2{,}4827 \times 10^4)^5 \approx 94{,}16 \times 10^{20} \approx 9{,}4 \times 10^{21}$ avaliações. **Correto.**

**Conclusão da auditoria matemática:**
Nenhum erro matemático encontrado.

---

## 4. Checklist de Conformidade Editorial e Pedagógica

| Critério avaliado | Status | Análise detalhada |
|---|:---:|---|
| **Dica e solução completa em cada exercício** | **OK** | Todos os 16 exercícios (4 por seção) possuem `<hint><title>Ver dica</title>...</hint>` e `<solution collapsible="true" collapsed="true">` com raciocínio passo a passo e valores conferidos. |
| **Pelo menos um exemplo biológico por seção** | **OK** | **Seção 1:** Modelo linear-retificado de disparo neuronal ($r(I) = g\max(0, I - \theta)$); curvas gaussianas de sintonia de orientação em V1; decaimento de EPSC; cinética de Hill; condutâncias de Hodgkin–Huxley ($\bar{g}_{\text{Na}}, \bar{g}_{\text{K}}$); microcircuito de 3 neurônios com a lei de Dale.<br>**Seção 2:** Neurônio visual com resposta a contraste; modelo de adaptação sensorial; dados eletrofisiológicos com outliers.<br>**Seção 3:** Análise das elipses de custo do neurônio visual; modelos biestáveis de conformação proteica e redes atratoras de Hopfield; modelo de dobramento proteico.<br>**Seção 4:** Modelo passivo de membrana versus canais ativos Hodgkin–Huxley; curvas de sintonia em população acoplada de 5 neurônios corticais. |
| **Afirmações de neurociência de livro-texto** | **OK** | Todos os conceitos, modelos e valores numéricos adotados são clássicos e fidedignos aos livros-texto de referência (Dayan & Abbott, *Theoretical Neuroscience*; Kandel et al., *Principles of Neural Science*; Hodgkin & Huxley, 1952). Não há invenção de referências, páginas ou afirmações heterodoxas. |
| **Sequenciamento pedagógico de conceitos** | **OK** | A aula inicia com a intuição bidimensional de "botões de painel", avança para a formalização da função custo escalar e do erro quadrático médio, traduz o gráfico 3D em curvas de nível bidimensionais relacionando-as ao gradiente de descida, e conclui com a busca em grade computacional que motiva o uso de métodos analíticos e iterativos nos temas seguintes. Todas as referências a temas futuros (<mark>Tema 4.2</mark> e <mark>Tema 4.3</mark>) são explícitas. |
| **Código Python e figuras executáveis** | **OK** | O bloco [cod:4-1-grid-search](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-01.dlt#L668-L705) em NumPy é 100% autocontido, não tem erros de sintaxe ou indexação e roda perfeitamente em qualquer ambiente padrão (como Google Colab). O script [paisagem-custo.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/fig/paisagem-custo.py) gera com precisão o arquivo [paisagem-custo.svg](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/fig/paisagem-custo.svg) incorporado na Seção 3. |
| **Consistência de notação matemática** | **OK** | Vetores em negrito minúsculo ($\mathbf{w}, \mathbf{r}, \mathbf{u}, \mathbf{d}, \mathbf{v}, \mathbf{0}$), escalares em itálico ($w_i, g, \theta, a, b, c$), matrizes em maiúsculo (tabelas NumPy `A, B, J`), símbolo gradiente sem negrito ($\nabla J$), decimais em prosa/KaTeX com vírgula ($0{,}5$; $2{,}24$) e código com ponto (`0.2`, `50.0`). |
| **Cobertura de todos os subtemas pedidos** | **OK** | As quatro seções definidas pelo gestor estão integralmente presentes e organizadas: (1) Configurações como pontos; (2) A função custo como paisagem; (3) Curvas de nível; (4) Ajustando dois parâmetros a dados (busca em grade com numpy). |
| **Tamanho dentro do padrão** | **OK** | O texto em prosa da aula totaliza aproximadamente 4.400 palavras, perfeitamente situado na faixa estipulada de 3.500 a 5.500 palavras. |
| **Conformidade técnica Delta v0.6.0** | **OK** | Estrutura XML estrita: atributos explicitamente valorados (`collapsible="true" collapsed="true"`), tags `<intuition>` empregadas exclusivamente como filhas diretas de `<definition>` e sem `id`, links externos restritos a documentações e vídeos oficiais sancionados, metadados com retorno ao guia (`index.html#tema-4-1`) e ausência de tags não documentadas. |

---

## 5. Conclusão da Revisão

A aula [tema-01.dlt](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-01.dlt) está **aprovada para publicação**. O rigor matemático impecável, a sólida contextualização biofísica e o cuidado didático na transição entre representação geométrica, topografia de contorno e código computacional fornecem uma base de excelência para os próximos temas de otimização da trilha. As 4 observações listadas na Tabela de Problemas e Observações podem ser incorporadas em ciclos oportunos de polimento editorial, sem qualquer impedimento à compilação e publicação imediata.