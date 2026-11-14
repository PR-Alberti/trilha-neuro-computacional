# Relatório de Revisão Técnica — Módulo 04 · Tema 02 (Minimização e maximização)

- **Arquivo revisado:** [tema-02.dlt](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-02.dlt)
- **Script de figura associado:** [minimo-sela.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/fig/minimo-sela.py) (gera [minimo-sela.svg](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/fig/minimo-sela.svg))
- **Documentos de referência:** [PADRAO-AULAS.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/PADRAO-AULAS.md) e [DELTA-COLA.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/DELTA-COLA.md)
- **Data da revisão:** 14 de novembro de 2026
- **Perfil do revisor:** Matemático, Neurocientista Computacional e Professor de Alunos de Ciências Biológicas

---

## 1. Veredito

**APROVAR**

A aula cumpre rigorosamente todos os requisitos matemáticos, biológicos, pedagógicos, de escopo e de formatação exigidos pelas diretrizes do projeto. Todas as contas de todos os 9 exemplos desenvolvidos e das soluções de todos os 16 exercícios propostos foram integralmente recalculadas à mão, passo a passo — **nenhum erro matemático foi encontrado**. Os dados experimentais do neurônio visual do Tema 4.1 foram retomados com exatidão, deduzindo-se analiticamente a solução $(a^*, b^*) = (50, 10)$ com custo mínimo $J = 5$, comprovado como mínimo global único via Hessiana. O script de figura em Python é autocontido e gera perfeitamente a ilustração vetorial requerida. A notação matemática respeita estritamente o padrão estipulado ($\mathbf{x}$ para vetores, $\mathbf{A}$ e $\mathbf{H}$ para matrizes, escalares em itálico e $\nabla f$ sem negrito). A extensão da prosa é de aproximadamente 5 250 palavras, situando-se rigorosamente dentro do teto estipulado de até ~5 500 palavras de prosa (não ultrapassa o padrão).

Foram apontadas 4 observações de natureza pedagógica e de formato, nenhuma de caráter impeditivo para publicação.

---

## 2. Tabela de Problemas e Observações

| Severidade | Local | Trecho | Correção sugerida |
|---|---|---|---|
| Pedagógico | Seção 2 (`sec:4-2-2`), [thm:4-2-teste-hessiana](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-02.dlt#L363-L365), linhas 363–365 | `...aproximação quadrática $\frac{1}{2}\bigl(f_{xx}(\Delta x)^2 + 2f_{xy}\Delta x\,\Delta y + f_{yy}(\Delta y)^2\bigr)$. Quando $f_{xx} \ne 0$, completar o quadrado dentro dos parênteses transforma essa expressão em: $$f_{xx}\left(\Delta x + \frac{f_{xy}}{f_{xx}}\Delta y\right)^2 + \frac{D}{f_{xx}}(\Delta y)^2.$$` | A fórmula destacada corresponde à transformação do polinômio quadrático que estava *dentro* dos parênteses/colchetes, omitindo o fator global $\frac{1}{2}$ da aproximação de Taylor citada na frase anterior. Para um aluno de Biologia não ficar com a impressão de que o fator $\frac{1}{2}$ foi esquecido ou se cancelou, sugere-se precisar o texto: `Quando $f_{xx} \ne 0$, completar o quadrado na expressão entre parênteses resulta em:` ou incluir explicitamente o fator $\frac{1}{2}$ na equação em destaque: `$$\frac{1}{2}\left[f_{xx}\left(\Delta x + \frac{f_{xy}}{f_{xx}}\Delta y\right)^2 + \frac{D}{f_{xx}}(\Delta y)^2\right].$$` |
| Pedagógico | Seção 1 (`sec:4-2-1`), [exr:4-2-1-4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-02.dlt#L288), linha ~288 | `$$R''(x) = 20\left(-\frac{1}{2}e^{-x/2}\right)\left(1 - \frac{x}{2}\right) + 20e^{-x/2}\left(-\frac{1}{2}\right) = -10e^{-x/2}\left(1 - \frac{x}{2} + 1\right) = 10e^{-x/2}\left(\frac{x}{2} - 2\right).$$` | A igualdade final é exata porque $-10(2 - x/2) = 10(x/2 - 2)$. Contudo, a passagem direta da expressão intermediária $-10e^{-x/2}(2 - x/2)$ para $10e^{-x/2}(x/2 - 2)$ com a troca simultânea de sinal e inversão da ordem pode gerar hesitação em alunos com base algébrica elementar. Sugere-se explicitar a etapa intermediária: `$-10e^{-x/2}\left(2 - \frac{x}{2}\right) = 10e^{-x/2}\left(\frac{x}{2} - 2\right)$`. |
| Formato | Seção 2 (`sec:4-2-2`), [def:4-2-hessiana](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-02.dlt#L340-L345), linhas 340–345 | `$$\mathbf{H}(x_0, y_0) = \begin{pmatrix} f_{xx}(x_0, y_0) & f_{xy}(x_0, y_0) \\ f_{yx}(x_0, y_0) & f_{yy}(x_0, y_0) \end{pmatrix}.$$` | A matriz Hessiana é definida diretamente no ponto fixado $(x_0, y_0)$, enquanto nos exemplos posteriores (ex.: [exm:4-2-polinomio-2d](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-02.dlt#L382)) e na Seção 3 ([eq:4-2-hessiana-mq](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-02.dlt#L533)) calcula-se primeiro a função matricial $\mathbf{H}(x, y)$ para depois avaliá-la nos pontos críticos específicos. Sugere-se definir primeiro $\mathbf{H}(x, y)$ em coordenadas genéricas no domínio e em seguida destacar a avaliação $\mathbf{H}(x_0, y_0)$ no ponto crítico. |
| Formato | Seção 4 (`sec:4-2-4`), [thm:4-2-lagrange](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-02.dlt#L724-L729), linhas 724–729 | `$$\begin{cases} f_x(x, y) = \lambda g_x(x, y), \\ f_y(x, y) = \lambda g_y(x, y), \\ g(x, y) = c. \end{cases}$$` | No enunciado do teorema e na equação destacada ([eq:4-2-lagrange](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-02.dlt#L724-L727)), as grandezas são avaliadas no ponto candidato $(x_0, y_0)$ ($\nabla f(x_0, y_0) = \lambda \nabla g(x_0, y_0)$). No sistema por coordenadas que fecha o teorema, usam-se as variáveis genéricas $(x, y)$. Para total harmonia formal, sugere-se enunciar explicitamente: `Escrevendo por coordenadas para determinar as incógnitas $(x, y, \lambda)$ cujo par $(x, y)$ fornece o candidato $(x_0, y_0)$:` ou manter a indexação com $(x_0, y_0)$ no sistema. |

---

## 3. Recálculo e Auditoria Integral de Contas

Todas as contas dos exemplos, deduções e soluções dos exercícios foram integralmente refeitas à mão, passo a passo.

### 3.1 Seção 1: Pontos críticos em uma variável (`sec:4-2-1`)

1. **[Exemplo 4.2.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-02.dlt#L121-L137) (`exm:4-2-sintonia-1d`):**
   - Função de sintonia: $r(\theta) = r_{\max} \exp\!\left(-\frac{(\theta - \theta_0)^2}{2\sigma^2}\right)$.
   - Derivada primeira pela regra da cadeia:
     $$r'(\theta) = r_{\max} \exp\!\left(-\frac{(\theta - \theta_0)^2}{2\sigma^2}\right) \cdot \left(-\frac{2(\theta - \theta_0)}{2\sigma^2}\right) = -r(\theta)\,\frac{\theta - \theta_0}{\sigma^2}.$$
     Como $r(\theta) > 0$ para todo $\theta$, $r'(\theta) = 0 \iff \theta - \theta_0 = 0 \iff \theta = \theta_0$. **Correto.**
   - Derivada segunda pela regra do produto:
     $$r''(\theta) = -r'(\theta)\,\frac{\theta - \theta_0}{\sigma^2} - r(\theta)\,\frac{1}{\sigma^2}.$$
     Em $\theta = \theta_0$, como $r'(\theta_0) = 0$ e $r(\theta_0) = r_{\max}$:
     $$r''(\theta_0) = 0 - \frac{r_{\max}}{\sigma^2} = -\frac{r_{\max}}{\sigma^2} < 0 \implies \text{máximo local (e global)}.$$
   - Caso numérico: $r_{\max} = 60\text{ Hz}$, $\theta_0 = 90^\circ$, $\sigma = 15^\circ$:
     $$r''(90^\circ) = -\frac{60}{15^2} = -\frac{60}{225} = -\frac{4}{15} \approx -0{,}267\text{ Hz}/(\text{grau})^2.$$
     Contas e unidades exatas. **Correto.**

2. **[Exemplo 4.2.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-02.dlt#L139-L160) (`exm:4-2-cubica-fechada`):**
   - $f(x) = x^3 - 6x^2 + 9x + 4$ em $[0, 5]$.
   - $f'(x) = 3x^2 - 12x + 9 = 3(x^2 - 4x + 3) = 3(x - 1)(x - 3) = 0 \implies x = 1$ e $x = 3$ (ambos em $(0, 5)$).
   - $f''(x) = 6x - 12$:
     - $x = 1$: $f''(1) = -6 < 0 \implies$ máximo local, $f(1) = 1 - 6 + 9 + 4 = 8$. **Correto.**
     - $x = 3$: $f''(3) = +6 > 0 \implies$ mínimo local, $f(3) = 27 - 54 + 27 + 4 = 4$. **Correto.**
   - Avaliação nas bordas de $[0, 5]$:
     - $f(0) = 4$;
     - $f(5) = 5^3 - 6(25) + 9(5) + 4 = 125 - 150 + 45 + 4 = 24$. **Correto.**
   - Extremos globais em $[0, 5]$: máximo global vale $24$ (em $x = 5$); mínimo global vale $4$ (em $x = 0$ e $x = 3$). **Correto.**

3. **[Exemplo 4.2.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-02.dlt#L161-L180) (`exm:4-2-forrageamento-polinomio`):**
   - $G(t) = -t^3 + 3t^2 + 9t$ em $[0, 4]$.
   - $G'(t) = -3t^2 + 6t + 9 = -3(t^2 - 2t - 3) = -3(t - 3)(t + 1) = 0 \implies t = 3$ e $t = -1$.
     Como o domínio é $[0, 4]$, $t = -1$ é descartado, restando $t = 3 \in (0, 4)$.
   - $G''(t) = -6t + 6 \implies G''(3) = -18 + 6 = -12 < 0 \implies$ máximo local.
   - Comparação com as bordas:
     - $G(0) = 0\text{ mg/min}$;
     - $G(3) = -27 + 27 + 27 = 27\text{ mg/min}$;
     - $G(4) = -64 + 48 + 36 = 20\text{ mg/min}$.
   - Máximo global: $27\text{ mg/min}$ em $t^* = 3\text{ min}$. **Correto.**

4. **[Exercício 4.2.1.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-02.dlt#L192-L219) (`exr:4-2-1-1`):**
   - $f(x) = x^3 - 3x + 2$.
   - Item (a): $f'(x) = 3x^2 - 3 = 3(x - 1)(x + 1) = 0 \implies x = -1$ e $x = 1$.
     $f''(x) = 6x$.
     $x = -1$: $f''(-1) = -6 < 0 \implies$ máximo local, $f(-1) = -1 + 3 + 2 = 4$.
     $x = 1$: $f''(1) = 6 > 0 \implies$ mínimo local, $f(1) = 1 - 3 + 2 = 0$. **Correto.**
   - Item (b): No intervalo fechado $[-2, 3]$:
     $f(-2) = (-8) - 3(-2) + 2 = -8 + 6 + 2 = 0$;
     $f(-1) = 4$;
     $f(1) = 0$;
     $f(3) = 27 - 9 + 2 = 20$.
     Máximo global: $20$ (em $x = 3$); mínimo global: $0$ (em $x = -2$ e $x = 1$). **Correto.**

5. **[Exercício 4.2.1.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-02.dlt#L221-L240) (`exr:4-2-1-2`):**
   - $A(T) = -T^2 + 74T - 1\,269$ em $[30, 45]$.
   - $A'(T) = -2T + 74 = 0 \implies T = 37\,^\circ\text{C} \in (30, 45)$.
   - $A''(T) = -2 < 0 \implies$ máximo local.
   - Avaliação:
     - $A(30) = -900 + 2\,220 - 1\,269 = 51$;
     - $A(37) = -1\,369 + 2\,738 - 1\,269 = 100$;
     - $A(45) = -2\,025 + 3\,330 - 1\,269 = 36$.
   - Atividade máxima: $100$ em $T = 37\,^\circ\text{C}$; menor atividade: $36$ na borda $T = 45\,^\circ\text{C}$. **Correto.**

6. **[Exercício 4.2.1.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-02.dlt#L242-L271) (`exr:4-2-1-3`):**
   - $p(x) = 3x^4 - 4x^3$ em $\mathbb{R}$.
   - Item (a): $p'(x) = 12x^3 - 12x^2 = 12x^2(x - 1) = 0 \implies x = 0$ e $x = 1$.
     $p''(x) = 36x^2 - 24x$.
     $x = 0$: $p''(0) = 0$ (inconclusivo).
     $x = 1$: $p''(1) = 12 > 0 \implies$ mínimo local, $p(1) = 3 - 4 = -1$. **Correto.**
   - Item (b): Estudo de sinal de $p'(x) = 12x^2(x - 1)$:
     Para $x \ne 0$, $12x^2 > 0$. Para $x < 0$, $x - 1 < 0 \implies p'(x) < 0$.
     Para $0 < x < 1$, $x - 1 < 0 \implies p'(x) < 0$.
     Como $p$ decresce antes e continua decrescendo após $x = 0$, $x = 0$ é ponto de inflexão horizontal ($p(0) = 0$). **Correto.**
   - Item (c): Como $p'(x) < 0$ para $x < 1$ e $p'(x) > 0$ para $x > 1$, $x = 1$ é o mínimo global em $\mathbb{R}$, com $p(1) = -1$. **Correto.**

7. **[Exercício 4.2.1.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-02.dlt#L273-L304) (`exr:4-2-1-4`):**
   - $R(x) = 20xe^{-x/2}$ em $[0, 6]$.
   - Item (a): $R'(x) = 20e^{-x/2} + 20x\left(-\frac{1}{2}e^{-x/2}\right) = 20e^{-x/2}\left(1 - \frac{x}{2}\right)$.
     $R''(x) = -10e^{-x/2}\left(1 - \frac{x}{2}\right) + 20e^{-x/2}\left(-\frac{1}{2}\right) = -10e^{-x/2}\left(2 - \frac{x}{2}\right) = 10e^{-x/2}\left(\frac{x}{2} - 2\right)$. **Correto.**
   - Item (b): $R'(x) = 0 \iff 1 - \frac{x}{2} = 0 \iff x = 2 \in (0, 6)$.
     $R''(2) = 10e^{-1}(1 - 2) = -10e^{-1} < 0 \implies$ máximo local. **Correto.**
   - Item (c): Avaliação:
     - $R(0) = 0$;
     - $R(2) = 40e^{-1} \approx 40 / 2{,}71828 \approx 14{,}72\text{ Hz}$;
     - $R(6) = 120e^{-3} \approx 120 / 20{,}0855 \approx 5{,}97\text{ Hz}$.
     Como $R'(x) < 0$ para $x > 2$, $R(6) < R(2)$. Máximo global: $40e^{-1} \approx 14{,}72\text{ Hz}$ (em $x = 2$); mínimo global: $0\text{ Hz}$ (em $x = 0$). **Correto.**

---

### 3.2 Seção 2: Pontos críticos em duas variáveis e a Hessiana (`sec:4-2-2`)

1. **[Exemplo 4.2.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-02.dlt#L371-L389) (`exm:4-2-polinomio-2d`):**
   - $f(x, y) = x^3 - 3x + y^2$.
   - Gradiente nulo: $f_x = 3x^2 - 3 = 0 \implies x = \pm 1$; $f_y = 2y = 0 \implies y = 0$.
     Pontos críticos: $P_1 = (1, 0)$ e $P_2 = (-1, 0)$.
   - Segundas derivadas: $f_{xx} = 6x$, $f_{xy} = 0$, $f_{yy} = 2$.
     Determinante: $D(x, y) = (6x)(2) - 0 = 12x$.
   - Classificação:
     - Em $P_1 = (1, 0)$: $D(1, 0) = 12 > 0$ e $f_{xx}(1, 0) = 6 > 0 \implies$ mínimo local, com $f(1, 0) = -2$.
     - Em $P_2 = (-1, 0)$: $D(-1, 0) = -12 < 0 \implies$ ponto de sela, com $f(-1, 0) = 2$.
   - Não é mínimo global pois $f(x, 0) = x^3 - 3x \to -\infty$ quando $x \to -\infty$. **Correto.**

2. **[Exemplo 4.2.5](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-02.dlt#L391-L411) (`exm:4-2-mapa-cortical`):**
   - $Z(x, y) = 8 - x^2 - 2xy - 2y^2 + 2x$.
   - Gradiente nulo:
     $$Z_x = -2x - 2y + 2 = 0 \implies x + y = 1,$$
     $$Z_y = -2x - 4y = 0 \implies x = -2y.$$
     Substituição: $-2y + y = 1 \implies -y = 1 \implies y = -1 \implies x = 2$.
     Ponto crítico único: $(2, -1)$. **Correto.**
   - Hessiana constante: $Z_{xx} = -2$, $Z_{xy} = -2$, $Z_{yy} = -4$.
     $$D = (-2)(-4) - (-2)^2 = 8 - 4 = 4 > 0.$$
     Como $D = 4 > 0$ e $Z_{xx} = -2 < 0 \implies$ máximo local (e global, pois $Z(x, y) = 10 - \bigl((x - 2) + (y + 1)\bigr)^2 - (y + 1)^2 \le 10$).
   - Valor de pico: $Z(2, -1) = 8 - 4 + 4 - 2 + 4 = 10$. **Correto.**

3. **[Exercício 4.2.2.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-02.dlt#L422-L438) (`exr:4-2-2-1`):**
   - $f(x, y) = x^2 + 4xy + y^2 - 6y$.
   - Gradiente nulo:
     $$f_x = 2x + 4y = 0 \implies x = -2y,$$
     $$f_y = 4x + 2y - 6 = 0 \implies 4(-2y) + 2y - 6 = 0 \implies -6y = 6 \implies y = -1 \implies x = 2.$$
     Ponto crítico único: $(2, -1)$.
   - Segundas derivadas: $f_{xx} = 2$, $f_{xy} = 4$, $f_{yy} = 2$.
     $$D = (2)(2) - 4^2 = 4 - 16 = -12 < 0 \implies \text{ponto de sela}.$$
     Valor: $f(2, -1) = 4 - 8 + 1 + 6 = 3$. **Correto.**

4. **[Exercício 4.2.2.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-02.dlt#L440-L452) (`exr:4-2-2-2`):**
   - $g(x, y) = 2x^2 - 4x + y^2 + 6y + 15$.
   - Gradiente nulo: $g_x = 4x - 4 = 0 \implies x = 1$; $g_y = 2y + 6 = 0 \implies y = -3$.
     Ponto crítico único: $(1, -3)$.
   - Hessiana: $g_{xx} = 4$, $g_{xy} = 0$, $g_{yy} = 2 \implies D = (4)(2) - 0 = 8 > 0$.
     Como $D > 0$ e $g_{xx} = 4 > 0 \implies$ mínimo local e global.
   - Valor mínimo: $g(1, -3) = 2(1) - 4 + 9 - 18 + 15 = 4$.
     Conferência por quadrados completos: $2(x - 1)^2 + (y + 3)^2 + 4 \ge 4$. **Correto.**

5. **[Exercício 4.2.2.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-02.dlt#L454-L474) (`exr:4-2-2-3`):**
   - $E(x, y) = x^4 - 2x^2 + y^2 + 1$.
   - Gradiente nulo: $E_x = 4x(x^2 - 1) = 0 \implies x \in \{-1, 0, 1\}$; $E_y = 2y = 0 \implies y = 0$.
     Três pontos críticos: $(-1, 0)$, $(0, 0)$ e $(1, 0)$.
   - Segundas derivadas: $E_{xx} = 12x^2 - 4$, $E_{xy} = 0$, $E_{yy} = 2$.
     $$D(x, y) = (12x^2 - 4)(2) - 0 = 24x^2 - 8.$$
   - Classificação:
     - $(-1, 0)$: $D = 16 > 0$ e $E_{xx} = 8 > 0 \implies$ mínimo local ($E = 0$);
     - $(1, 0)$: $D = 16 > 0$ e $E_{xx} = 8 > 0 \implies$ mínimo local ($E = 0$);
     - $(0, 0)$: $D = -8 < 0 \implies$ ponto de sela ($E = 1$).
   - Estados estáveis em $(-1, 0)$ e $(1, 0)$ com energia mínima $0$; barreira de transição na sela $(0, 0)$ com altura $1$. **Correto.**

6. **[Exercício 4.2.2.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-02.dlt#L476-L500) (`exr:4-2-2-4`):**
   - Item (a): $R(u, v) = 3u - u^3 - 2v^2 + 4v + 20$.
     $R_u = 3(1 - u^2) = 0 \implies u = \pm 1$; $R_v = -4v + 4 = 0 \implies v = 1$.
     Pontos críticos: $(1, 1)$ e $(-1, 1)$.
     $R_{uu} = -6u$, $R_{uv} = 0$, $R_{vv} = -4 \implies D = (-6u)(-4) - 0 = 24u$.
     - $(1, 1)$: $D = 24 > 0$, $R_{uu} = -6 < 0 \implies$ máximo local, $R(1, 1) = 3 - 1 - 2 + 4 + 20 = 24\text{ Hz}$.
     - $(-1, 1)$: $D = -24 < 0 \implies$ ponto de sela, $R(-1, 1) = -3 + 1 - 2 + 4 + 20 = 20\text{ Hz}$. **Correto.**
   - Item (b): $h(x, y) = x^4 - y^4$.
     $h_x = 4x^3 = 0, h_y = -4y^3 = 0 \implies (0, 0)$ é ponto crítico.
     $h_{xx} = 12x^2 = 0$, $h_{yy} = -12y^2 = 0$, $h_{xy} = 0 \implies D(0, 0) = 0$ (inconclusivo).
     Sobre o eixo $x$ ($y = 0$, $x \ne 0$): $h(x, 0) = x^4 > 0 = h(0, 0)$.
     Sobre o eixo $y$ ($x = 0$, $y \ne 0$): $h(0, y) = -y^4 < 0 = h(0, 0)$.
     Como toda vizinhança contém valores maiores e menores que $h(0, 0)$, $(0, 0)$ é ponto de sela. **Correto.**

---

### 3.3 Seção 3: O mínimo exato de um ajuste: mínimos quadrados (`sec:4-2-3`)

1. **Dedução das equações normais e da matriz Hessiana:**
   - Custo: $J(a, b) = \frac{1}{m}\sum_{i=1}^m (ax_i + b - y_i)^2$.
   - Derivadas de 1ª ordem:
     $$\frac{\partial J}{\partial a} = \frac{2}{m}\left(a\sum x_i^2 + b\sum x_i - \sum x_i y_i\right) = 0 \implies \left(\sum x_i^2\right)a + \left(\sum x_i\right)b = \sum x_i y_i,$$
     $$\frac{\partial J}{\partial b} = \frac{2}{m}\left(a\sum x_i + mb - \sum y_i\right) = 0 \implies \left(\sum x_i\right)a + mb = \sum y_i.$$
     Dividindo por $m$: $a\bar{x} + b = \bar{y} \implies b = \bar{y} - a\bar{x}$. **Correto.**
   - Derivadas de 2ª ordem e determinante:
     $$J_{aa} = \frac{2}{m}\sum x_i^2, \qquad J_{ab} = \frac{2}{m}\sum x_i, \qquad J_{bb} = \frac{2}{m}\sum 1 = 2.$$
     $$D = J_{aa}J_{bb} - J_{ab}^2 = \frac{4}{m}\sum x_i^2 - \frac{4}{m^2}\left(\sum x_i\right)^2 = \frac{4}{m}\left(\sum x_i^2 - m\bar{x}^2\right) = \frac{4}{m}\sum_{i=1}^m (x_i - \bar{x})^2.$$
     Desde que nem todos os $x_i$ sejam iguais, $\sum (x_i - \bar{x})^2 > 0 \implies D > 0$ e $J_{aa} > 0$, provando a convexidade estrita e o mínimo global. **Correto.**

2. **[Exemplo 4.2.6](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-02.dlt#L558-L593) (`exm:4-2-minimos-quadrados-neuronio`):**
   - Dados idênticos ao Tema 4.1: $(0{,}2;\; 21), (0{,}4;\; 27), (0{,}6;\; 43), (0{,}8;\; 49)$, $m = 4$.
   - Somatórios:
     - $\sum x_i = 0{,}2 + 0{,}4 + 0{,}6 + 0{,}8 = 2{,}0 \implies \bar{x} = 0{,}5$;
     - $\sum x_i^2 = 0{,}04 + 0{,}16 + 0{,}36 + 0{,}64 = 1{,}20$;
     - $\sum y_i = 21 + 27 + 43 + 49 = 140 \implies \bar{y} = 35$;
     - $\sum x_i y_i = 4{,}2 + 10{,}8 + 25{,}8 + 39{,}2 = 80{,}0$.
   - Sistema normal:
     $$\begin{cases} 1{,}2a + 2b = 80, \\ 2a + 4b = 140 \implies b = 35 - 0{,}5a. \end{cases}$$
     Substituição: $1{,}2a + 2(35 - 0{,}5a) = 80 \implies 0{,}2a = 10 \implies a^* = 50$.
     $b^* = 35 - 0{,}5(50) = 10$.
   - Hessiana: $J_{aa} = \frac{2}{4}(1{,}20) = 0{,}6$, $J_{ab} = \frac{2}{4}(2{,}0) = 1$, $J_{bb} = 2$.
     $D = (0{,}6)(2) - 1^2 = 0{,}2 > 0$ e $J_{aa} = 0{,}6 > 0 \implies$ mínimo global.
   - Previsões e resíduos de $\hat{y} = 50x + 10$:
     Previsões: $20, 30, 40, 50$; resíduos: $-1, +3, -3, +1$.
     $$J(50, 10) = \frac{(-1)^2 + 3^2 + (-3)^2 + 1^2}{4} = \frac{1 + 9 + 9 + 1}{4} = \frac{20}{4} = 5.$$
     Bate exatamente com os resultados da grade e das curvas de nível do Tema 4.1. **Correto.**

3. **[Exemplo 4.2.7](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-02.dlt#L594-L609) (`exm:4-2-mq-quatro-pontos`):**
   - Pontos: $(0, 1), (1, 3), (2, 4), (3, 4)$, $m = 4$.
   - Somatórios: $\sum x_i = 6$, $\sum x_i^2 = 14$, $\sum y_i = 12$, $\sum x_i y_i = 0 + 3 + 8 + 12 = 23$.
   - Sistema: $14a + 6b = 23$ e $6a + 4b = 12 \implies b = 3 - 1{,}5a$.
     $14a + 6(3 - 1{,}5a) = 23 \implies 5a = 5 \implies a^* = 1 \implies b^* = 1{,}5$.
   - Hessiana: $J_{aa} = 7$, $J_{ab} = 3$, $J_{bb} = 2 \implies D = 14 - 9 = 5 > 0$.
   - Previsões: $1{,}5;\; 2{,}5;\; 3{,}5;\; 4{,}5$; erros: $+0{,}5;\; -0{,}5;\; -0{,}5;\; +0{,}5$.
     $$J(1;\; 1{,}5) = \frac{4 \cdot (0{,}5)^2}{4} = 0{,}25.$$
     Contas exatas. **Correto.**

4. **[Exercício 4.2.3.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-02.dlt#L621-L638) (`exr:4-2-3-1`):**
   - Pontos: $(0, 2), (1, 3), (2, 7)$, $m = 3$.
   - Somatórios: $\sum x_i = 3$, $\sum x_i^2 = 5$, $\sum y_i = 12$, $\sum x_i y_i = 3 + 14 = 17$.
   - Sistema: $5a + 3b = 17$ e $3a + 3b = 12 \implies b = 4 - a$.
     $5a + 3(4 - a) = 17 \implies 2a = 5 \implies a^* = 2{,}5 \implies b^* = 1{,}5$.
   - Hessiana: $J_{aa} = 10/3$, $J_{ab} = 2$, $J_{bb} = 2 \implies D = 20/3 - 4 = 8/3 > 0$.
   - Previsões: $1{,}5;\; 4{,}0;\; 6{,}5$; erros: $-0{,}5;\; +1{,}0;\; -0{,}5$.
     $$J(2{,}5;\; 1{,}5) = \frac{0{,}25 + 1{,}00 + 0{,}25}{3} = \frac{1{,}5}{3} = 0{,}5.$$
     Contas exatas. **Correto.**

5. **[Exercício 4.2.3.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-02.dlt#L640-L660) (`exr:4-2-3-2`):**
   - Dados eletrofisiológicos: $I \in \{0;\; 0{,}2;\; 0{,}4;\; 0{,}6\}\text{ nA}$, $V \in \{-70;\; -58;\; -52;\; -40\}\text{ mV}$, $m = 4$.
   - Somatórios:
     - $\sum I_i = 1{,}2$;
     - $\sum I_i^2 = 0 + 0{,}04 + 0{,}16 + 0{,}36 = 0{,}56$;
     - $\sum V_i = -220$;
     - $\sum I_i V_i = 0{,}2(-58) + 0{,}4(-52) + 0{,}6(-40) = -11{,}6 - 20{,}8 - 24{,}0 = -56{,}4$.
   - Sistema: $0{,}56 R_{\text{in}} + 1{,}2 E_L = -56{,}4$ e $1{,}2 R_{\text{in}} + 4 E_L = -220 \implies E_L = -55 - 0{,}3 R_{\text{in}}$.
     $0{,}56 R_{\text{in}} + 1{,}2(-55 - 0{,}3 R_{\text{in}}) = -56{,}4 \implies 0{,}20 R_{\text{in}} = 9{,}6 \implies R_{\text{in}}^* = 48\text{ M}\Omega$.
     $E_L^* = -55 - 0{,}3(48) = -55 - 14{,}4 = -69{,}4\text{ mV}$.
   - Previsões de $48I - 69{,}4$: $-69{,}4;\; -59{,}8;\; -50{,}2;\; -40{,}6\text{ mV}$.
     Erros: $+0{,}6;\; -1{,}8;\; +1{,}8;\; -0{,}6\text{ mV}$.
     $$J = \frac{0{,}36 + 3{,}24 + 3{,}24 + 0{,}36}{4} = \frac{7{,}2}{4} = 1{,}8\text{ mV}^2.$$
     Contas e unidades físicas perfeitas. **Correto.**

6. **[Exercício 4.2.3.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-02.dlt#L662-L686) (`exr:4-2-3-3`):**
   - Item (a): $J(a) = \frac{1}{m}\sum (ax_i - y_i)^2$.
     $J'(a) = \frac{2}{m}\left(a\sum x_i^2 - \sum x_i y_i\right) = 0 \implies a^* = \frac{\sum x_i y_i}{\sum x_i^2}$.
     $J''(a) = \frac{2}{m}\sum x_i^2 > 0 \implies$ mínimo global. **Correto.**
   - Item (b): Dados $(0{,}1;\; 7), (0{,}2;\; 9), (0{,}3;\; 15)$.
     $\sum I_i^2 = 0{,}01 + 0{,}04 + 0{,}09 = 0{,}14$.
     $\sum I_i \Delta V_i = 0{,}7 + 1{,}8 + 4{,}5 = 7{,}0$.
     $$R_{\text{in}}^* = \frac{7{,}0}{0{,}14} = 50\text{ M}\Omega.$$
     Contas exatas. **Correto.**

7. **[Exercício 4.2.3.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-02.dlt#L688-L705) (`exr:4-2-3-4`):**
   - Item (a): $\hat{y}(\bar{x}) = a^*\bar{x} + b^* = a^*\bar{x} + (\bar{y} - a^*\bar{x}) = \bar{y}$. A reta passa por $(\bar{x}, \bar{y})$.
     $\frac{\partial J}{\partial b} = 0 \implies \sum_{i=1}^m (\hat{y}_i - y_i) = 0$. **Correto.**
   - Item (b): Se $x_i = c$ para todo $i$, $\bar{x} = c \implies x_i - \bar{x} = 0 \implies D = 0$.
     $J(a, b) = \frac{1}{m}\sum (ac + b - y_i)^2$ atinge o mínimo para qualquer par satisfazendo $ac + b = \bar{y}$ (reta de soluções no espaço de parâmetros). **Correto.**

---

### 3.4 Seção 4: Otimização com restrição: multiplicadores de Lagrange (`sec:4-2-4`)

1. **[Exemplo 4.2.8](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-02.dlt#L741-L759) (`exm:4-2-lagrange-produto`):**
   - Maximizar $f(x, y) = xy$ com $x + y = 10$.
   - Método de Lagrange: $\nabla f = (y, x)$, $\nabla g = (1, 1)$.
     $y = \lambda$, $x = \lambda \implies x = y = \lambda$.
     $x + y = 10 \implies 2\lambda = 10 \implies \lambda = 5 \implies (x^*, y^*) = (5, 5)$, com $f(5, 5) = 25$.
     Preço-sombra: se $c = 10{,}1$, ótimo em $(5{,}05;\; 5{,}05)$ dá $f = 25{,}5025 \approx 25 + 5(0{,}1)$. **Correto.**
   - Método direto: $h(x) = x(10 - x) = 10x - x^2 \implies h'(x) = 10 - 2x = 0 \implies x = 5$, $h''(x) = -2 < 0 \implies$ máximo global. **Correto.**

2. **[Exemplo 4.2.9](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-02.dlt#L760-L774) (`exm:4-2-lagrange-atp`):**
   - Maximizar $B(x, y) = \ln x + 2\ln y$ sujeito a $x + y = 9$ ($x, y > 0$).
   - $\nabla B = \left(\frac{1}{x},\; \frac{2}{y}\right)$, $\nabla g = (1, 1)$.
     $\frac{1}{x} = \lambda \implies x = \frac{1}{\lambda}$; $\frac{2}{y} = \lambda \implies y = \frac{2}{\lambda} \implies y = 2x$.
     $x + 2x = 9 \implies 3x = 9 \implies x^* = 3$, $y^* = 6$, $\lambda = 1/3$.
   - Teste direto: $h(x) = \ln x + 2\ln(9 - x) \implies h''(x) = -\frac{1}{x^2} - \frac{2}{(9 - x)^2} < 0 \implies$ máximo global restrito.
   - Valor máximo: $B(3, 6) = \ln 3 + 2\ln 6 = \ln 3 + \ln 36 = \ln 108$. **Correto.**

3. **[Exercício 4.2.4.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-02.dlt#L784-L797) (`exr:4-2-4-1`):**
   - Minimizar $f(x, y) = x^2 + y^2$ com $x + 2y = 10$.
   - $\nabla f = (2x, 2y)$, $\nabla g = (1, 2)$.
     $2x = \lambda \implies x = \lambda/2$; $2y = 2\lambda \implies y = \lambda \implies y = 2x$.
     $x + 2(2x) = 10 \implies 5x = 10 \implies x^* = 2, y^* = 4, \lambda = 4$.
     Valor: $f(2, 4) = 4 + 16 = 20$.
   - Confirmação direta: $x = 10 - 2y \implies h(y) = (10 - 2y)^2 + y^2 = 5y^2 - 40y + 100 = 5(y - 4)^2 + 20 \ge 20$. **Correto.**

4. **[Exercício 4.2.4.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-02.dlt#L799-L810) (`exr:4-2-4-2`):**
   - Maximizar $U(x, y) = 3\ln x + \ln y$ com $x + y = 12$ ($x, y > 0$).
   - $\nabla U = \left(\frac{3}{x},\; \frac{1}{y}\right)$, $\nabla g = (1, 1)$.
     $\frac{3}{x} = \lambda \implies x = \frac{3}{\lambda}$; $\frac{1}{y} = \lambda \implies y = \frac{1}{\lambda} \implies x = 3y$.
     $3y + y = 12 \implies 4y = 12 \implies y^* = 3, x^* = 9, \lambda = 1/3$.
   - Confirmação direta: $h(y) = 3\ln(12 - y) + \ln y \implies h''(y) < 0 \implies$ máximo global restrito. **Correto.**

5. **[Exercício 4.2.4.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-02.dlt#L812-L828) (`exr:4-2-4-3`):**
   - Otimizar $f(x, y) = x + 2y$ sobre $x^2 + y^2 = 5$.
   - $\nabla f = (1, 2)$, $\nabla g = (2x, 2y)$.
     $1 = 2\lambda x \implies x = \frac{1}{2\lambda}$; $2 = 2\lambda y \implies y = \frac{1}{\lambda} = 2x$.
     $x^2 + (2x)^2 = 5 \implies 5x^2 = 5 \implies x = \pm 1$.
     - $x = 1 \implies y = 2$, $\lambda = 1/2$, $f(1, 2) = 1 + 4 = 5$;
     - $x = -1 \implies y = -2$, $\lambda = -1/2$, $f(-1, -2) = -1 - 4 = -5$.
   - Máximo global restrito: $5$ em $(1, 2)$; mínimo global restrito: $-5$ em $(-1, -2)$. **Correto.**

6. **[Exercício 4.2.4.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-02.dlt#L830-L854) (`exr:4-2-4-4`):**
   - Minimizar $C(r_1, r_2) = r_1^2 + 2r_2^2$ com $r_1 + r_2 = 12$.
   - Item (a): $\nabla C = (2r_1, 4r_2)$, $\nabla g = (1, 1)$.
     $2r_1 = \lambda$ e $4r_2 = \lambda \implies 2r_1 = 4r_2 \implies r_1 = 2r_2$.
     $2r_2 + r_2 = 12 \implies 3r_2 = 12 \implies r_2^* = 4\text{ Hz}, r_1^* = 8\text{ Hz}, \lambda = 16$. **Correto.**
   - Item (b): Confirmação direta: $r_1 = 12 - r_2 \implies h(r_2) = (12 - r_2)^2 + 2r_2^2 = 3r_2^2 - 24r_2 + 144$.
     $h'(r_2) = 6r_2 - 24 = 0 \implies r_2 = 4\text{ Hz}$, $h''(r_2) = 6 > 0 \implies$ mínimo global restrito.
     Custo mínimo: $C(8, 4) = 8^2 + 2(4^2) = 64 + 32 = 96$. **Correto.**
   - Item (c): $\lambda = 16$ é a derivada do custo ótimo em relação ao vínculo $c$ ($\frac{dC^*}{dc} = 16$). Se a meta de disparo subir de $12\text{ Hz}$ para $12 + \Delta c\text{ Hz}$, o custo mínimo cresce em aproximadamente $16\,\Delta c$ unidades. **Correto.**

---

**Conclusão da auditoria matemática:**
Nenhum erro matemático encontrado.

---

## 4. Checklist de Conformidade Editorial e Pedagógica

| Critério avaliado | Status | Análise detalhada |
|---|:---:|---|
| **Dica e solução completa em cada exercício** | **OK** | Todos os 16 exercícios (4 por seção) contêm `<hint><title>Ver dica</title>...</hint>` e `<solution collapsible="true" collapsed="true">` completas, com passos detalhados de derivação, fatoração e conferência. |
| **Pelo menos um exemplo biológico por seção** | **OK** | **Seção 1:** Curva de sintonia de orientação em V1 ($r_{\max} = 60\text{ Hz}, \theta_0 = 90^\circ, \sigma = 15^\circ$); forrageamento de abelha em mancha de néctar; atividade de enzima mamífera ($37\,^\circ\text{C}$); dessensibilização bifásica a neuromodulador.<br>**Seção 2:** Mapeamento cortical bidimensional; paisagem de energia livre de enovelamento macromolecular (biestável); taxa de disparo sob duas entradas sinápticas.<br>**Seção 3:** Regressão linear do neurônio visual sensível ao contraste (dados exatos do Tema 4.1); estimativa de resistência de entrada ($R_{\text{in}}$) e potencial de repouso ($E_L$) em eletrofisiologia intracelular passiva.<br>**Seção 4:** Alocação de orçamento de ATP em neurônio entre manutenção de bombas e síntese; alocação de substrato em vias metabólicas; minimização de consumo metabólico em codificação populacional. |
| **Afirmações de neurociência de livro-texto** | **OK** | Todos os conceitos e parâmetros utilizados pertencem aos livros-texto clássicos (Dayan & Abbott, *Theoretical Neuroscience*; Kandel et al., *Principles of Neural Science*). Sem invenção de fontes ou dados não documentados. |
| **Sequenciamento pedagógico de conceitos** | **OK** | A progressão parte de 1 variável (tangente horizontal, Fermat, teste da 2ª derivada e Weierstrass), generaliza para 2 variáveis (gradiente nulo, Hessiana, teste do determinante e ponto de sela), aplica analiticamente aos mínimos quadrados (revelando a convexidade e o mínimo global exato do neurônio do Tema 4.1) e culmina na otimização sob restrições via multiplicadores de Lagrange. Conceitos de módulos posteriores (como matrizes e determinantes gerais do Módulo 5) são expressamente sinalizados antes do uso, conforme a regra de continuidade do padrão editorial. |
| **Código Python e figuras executáveis** | **OK** | A aula é analítica e não contém blocos de código no corpo do texto (preparando o terreno para os algoritmos de descida de gradiente do Tema 4.3). O script [minimo-sela.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/fig/minimo-sela.py) é 100% autocontido, gera de modo reproduzível o gráfico [minimo-sela.svg](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/fig/minimo-sela.svg) e emprega `plt.rcParams['svg.fonttype'] = 'none'` conforme exigido em [DELTA-COLA.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/DELTA-COLA.md). |
| **Consistência de notação matemática** | **OK** | Vetores em negrito minúsculo ($\mathbf{x}_0, \mathbf{0}$), matrizes em negrito maiúsculo ($\mathbf{H}$), escalares em itálico ($x, y, a, b, c, D, \lambda$), símbolo gradiente sem negrito ($\nabla f, \nabla J, \nabla g$), vírgula decimal na prosa e decimais KaTeX formatados com chaves ($0{,}5$; $-0{,}267$). |
| **Cobertura de todos os subtemas pedidos** | **OK** | As quatro seções definidas pelo gestor foram integralmente desenvolvidas: (1) Pontos críticos em uma variável; (2) Pontos críticos em duas variáveis e a Hessiana ($D = f_{xx}f_{yy} - f_{xy}^2$, sela); (3) Mínimos quadrados (equações normais da reta, dados do Tema 4.1); (4) Lagrange introdutório. |
| **Tamanho dentro do padrão** | **OK** | A aula possui aproximadamente 5 250 palavras de prosa (excluindo tags XML e fórmulas KaTeX isoladas), permanecendo rigorosamente abaixo do limite de até ~5 500 palavras de prosa estipulado para temas intermediários com 4 subtemas. A aula **não ultrapassa** o padrão. |
| **Conformidade técnica Delta v0.6.0** | **OK** | XML estrito válido: atributos com valores booleanos explícitos (`collapsible="true" collapsed="true"`), tags `<intuition>` empregadas exclusivamente como filhas diretas de definições, teoremas e proposições sem atributo `id`, links relativos canônicos ao guia (`../../index.html#tema-4-2`), ausência de tags proibidas (`<interactive>`, `<cite>`, `<bibliography>`). |

---

## 5. Conclusão da Revisão

A aula [tema-02.dlt](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-04/tema-02.dlt) está **aprovada para publicação**. Sua precisão matemática é impecável, com todas as contas perfeitamente fechadas, a integração com os dados do Tema 4.1 é completa e a contextualização neurobiológica e fisiológica é autêntica e acessível. As 4 observações pedagógicas e de formato registradas na Tabela de Problemas e Observações representam apenas oportunidades de polimento fino editorial, não obstando a homologação imediata.
