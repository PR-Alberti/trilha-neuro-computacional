# Relatório de Revisão Técnica — Módulo 01 · Tema 05 (Geometria Analítica)

- **Arquivo revisado:** [tema-05.dlt](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-05.dlt)
- **Script de figura revisado:** [curva-iv.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/fig/curva-iv.py)
- **Figura gerada:** [curva-iv.svg](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/fig/curva-iv.svg)
- **Documentos de referência:** [PADRAO-AULAS.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/PADRAO-AULAS.md) e [DELTA-COLA.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/DELTA-COLA.md)
- **Data da revisão:** 14 de novembro de 2026
- **Perfil do revisor:** Matemático, Neurocientista Computacional e Professor de Alunos de Ciências Biológicas

---

## 1. Veredito

**APROVAR**

A aula [tema-05.dlt](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-05.dlt) apresenta qualidade técnica, matemática e pedagógica de nível excepcional. Todas as deduções, exemplos guiados e soluções dos 12 exercícios foram integralmente recalculados e auditados de forma independente, constatando **$100\%$ de exatidão analítica e numérica** (sem qualquer divergência). A estrutura textual respeita com fidelidade o contrato editorial ([PADRAO-AULAS.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/PADRAO-AULAS.md)) e a gramática XML estrita do Delta v0.6.0 ([DELTA-COLA.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/DELTA-COLA.md)).

As articulações com a neurociência celular e de sistemas são autênticas e rigorosamente baseadas na literatura de livro-texto (Dayan & Abbott; Kandel et al.; Hodgkin & Huxley):
- o uso da distância euclidiana para formalizar a separação entre respostas neurais no **espaço de atividade** (*activity space*), preparando a transição natural para os vetores de disparo no Módulo 5 (Álgebra Linear);
- a modelagem das curvas corrente-voltagem ($I$-$V$) ôhmicas lineares ($I = g(V - E)$), identificando a condutância como inclinação e o cruzamento horizontal como potencial de reversão, com dedução biofísica e geométrica exata do potencial de repouso estacionário da membrana ($-70\text{ mV}$);
- a formalização de campos receptivos centro-periferia (*center-surround*) de células ganglionares retinianas e esferas de tolerância populacional via equações e inequações quadráticas do círculo e da esfera.

O script de suporte em Python [curva-iv.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/fig/curva-iv.py) é autocontido, segue todas as convenções do projeto (fundo transparente, tipografia sem fontes embutidas pesadas, rótulos em português) e reproduz com fidelidade milimétrica os parâmetros apresentados no texto.

Foram catalogadas apenas 4 observações de polimento pedagógico e de formatação na tabela a seguir, nenhuma delas de caráter impeditivo.

---

## 2. Tabela de Problemas e Observações

| Severidade | Local | Trecho | Correção sugerida |
|---|---|---|---|
| Pedagógico | Seção 2 (`sec:1-5-2`), `exm:1-5-curva-iv`, linha ~398 | `Como a corrente líquida é nula, $-70\text{ mV}$ é exatamente o potencial de repouso estacionário dessa célula!` | Para estudantes de Biologia, pode parecer paradoxal que haja correntes contínuas não nulas de potássio ($+500\text{ pA}$) e de sódio ($-500\text{ pA}$) no repouso sem que os gradientes de concentração se esgotem. Sugere-se acrescentar uma breve frase de contextualização biológica: `(Vale lembrar que, em neurônios vivos, esse fluxo iônico passivo contínuo é compensado pelo transporte ativo da bomba de $\text{Na}^+/\text{K}^+$-ATPase consumindo ATP, mantendo os gradientes químicos estáveis ao longo do tempo).` |
| Pedagógico | Seção 2 (`sec:1-5-2`), `exr:1-5-2-3`, linha ~476 | `$$I - 200 = 4(V - 20) \implies I(V) = 4V + 120\text{ pA}.$$` | Na expressão $I(V) = 4V + 120\text{ pA}$, o termo $4V$ combina condutância em $\text{nS}$ com voltagem em $\text{mV}$, gerando corrente em $\text{pA}$. Para evitar que alunos menos experientes em análise dimensional tentem converter $V$ para Volts antes de substituir, sugere-se explicitar as unidades operacionais: `$$I(V) = 4V + 120\text{ pA} \quad \text{(para } V \text{ em mV e } I \text{ em pA)}.$$` |
| Pedagógico | Seção 3 (`sec:1-5-3`), `def:1-5-circulo`, linha ~525 | `O <strong>círculo</strong> (ou circunferência) de centro $C = (a, b)$ e raio $r > 0$...` | No ensino médio tradicional brasileiro, muitos alunos aprendem a distinção rígida entre a borda (*circunferência*, $(x-a)^2 + (y-b)^2 = r^2$) e a região bidimensional preenchida (*disco* ou *círculo*, $(x-a)^2 + (y-b)^2 \le r^2$). Embora o texto logo aponte essa distinção (interior, borda, exterior), sugere-se explicitar a terminologia na abertura para tranquilizar o leitor: `O <strong>círculo</strong> (frequentemente chamado de <strong>circunferência</strong> quando nos referimos apenas à curva de contorno) de centro $C = (a, b)$ e raio $r > 0$...` |
| Formato | Seção 3 (`sec:1-5-3`), `prop:1-5-forma-geral-circulo`, linha ~557 | `<item>se $K = 0$, reduz-se a um <strong>único ponto</strong> $\left(-\dfrac{D}{2},\; -\dfrac{E}{2}\right)$; </item>` | Há um espaço em branco supérfluo antes do fechamento da tag `</item>`. Sugere-se remover o espaço: `<item>se $K = 0$, reduz-se a um <strong>único ponto</strong> $\left(-\dfrac{D}{2},\; -\dfrac{E}{2}\right);</item>`. |

---

## 3. Recálculo e Auditoria de Contas

Todas as fórmulas, deduções teóricas, exemplos numéricos e soluções de exercícios foram recalculados passo a passo de forma independente. Não foi constatada **nenhuma divergência numérica ou algébrica**.

### 3.1 Subtema 1: Introdução (`sec:1-5-1`)

1. **[Proposição 1.5.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-05.dlt#L71-L87) (`prop:1-5-distancia-2d` — Distância euclidiana no plano):**
   - Catetos do triângulo retângulo auxiliar formado por $P(x_1, y_1)$, $Q(x_2, y_2)$ e $R(x_2, y_1)$:
     $\Delta x = x_2 - x_1 \implies \text{comprimento } |\Delta x|$, e $\Delta y = y_2 - y_1 \implies \text{comprimento } |\Delta y|$.
   - Pitágoras: $d(P, Q)^2 = |\Delta x|^2 + |\Delta y|^2 = (x_2 - x_1)^2 + (y_2 - y_1)^2$.
   - Como $d \ge 0$, extrai-se a raiz quadrada principal: $d(P, Q) = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$. **Dedução correta.**

2. **[Definição 1.5.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-05.dlt#L91-L100) (`def:1-5-ponto-medio` — Ponto médio de segmento):**
   - Coordenadas dadas pela média aritmética em cada eixo: $M = \left(\frac{x_1 + x_2}{2},\; \frac{y_1 + y_2}{2}\right)$. **Definição correta.**

3. **[Proposição 1.5.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-05.dlt#L104-L117) (`prop:1-5-distancia-3d` — Distância e ponto médio em $\mathbb{R}^3$):**
   - Projeção no plano $z = z_1$: ponto $Q'(x_2, y_2, z_1)$.
   - Distância basal: $d(P, Q')^2 = (x_2 - x_1)^2 + (y_2 - y_1)^2$.
   - Segmento vertical $Q'Q$ ortogonal ao plano $z = z_1$ com comprimento $|z_2 - z_1|$.
   - Triângulo $PQ'Q$ retângulo em $Q'$: $d(P, Q)^2 = d(P, Q')^2 + |z_2 - z_1|^2 = (x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2$.
   - $d(P, Q) = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2}$. **Dedução correta.**

4. **[Exemplo 1.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-05.dlt#L121-L142) (`exm:1-5-fatia` — Neurônios em fatia cortical):**
   - Dados: $A = (-40, 20)\;\mu\text{m}$ e $B = (80, 70)\;\mu\text{m}$.
   - Item (a): $A$ tem $x = -40 < 0$ e $y = 20 > 0 \implies$ II quadrante; $B$ tem $x = 80 > 0$ e $y = 70 > 0 \implies$ I quadrante. **Correto.**
   - Item (b): $\Delta x = 80 - (-40) = 120\;\mu\text{m}$, $\Delta y = 70 - 20 = 50\;\mu\text{m}$.
     $$d(A, B) = \sqrt{120^2 + 50^2} = \sqrt{14\,400 + 2\,500} = \sqrt{16\,900} = 130\;\mu\text{m}.$$
     (Tríade pitagórica 5-12-13 multiplicada por 10). **Correto.**
   - Item (c): Ponto médio:
     $$M = \left(\frac{-40 + 80}{2},\; \frac{20 + 70}{2}\right) = \left(\frac{40}{2},\; \frac{90}{2}\right) = (20, 45)\;\mu\text{m}.$$
     Conferência: $d(A, M) = \sqrt{(20 - (-40))^2 + (45 - 20)^2} = \sqrt{60^2 + 25^2} = \sqrt{3\,600 + 625} = \sqrt{4\,225} = 65\;\mu\text{m} = \frac{130}{2}\;\mu\text{m}$. **Correto.**

5. **[Exemplo 1.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-05.dlt#L144-L163) (`exm:1-5-espaco-atividade` — Distância entre padrões de disparo):**
   - Item (a): $P_A = (10, 20)\text{ Hz}$, $P_B = (16, 28)\text{ Hz}$.
     $\Delta r_1 = 16 - 10 = 6\text{ Hz}$, $\Delta r_2 = 28 - 20 = 8\text{ Hz}$.
     $$d(P_A, P_B) = \sqrt{6^2 + 8^2} = \sqrt{36 + 64} = \sqrt{100} = 10\text{ Hz}.$$ **Correto.**
   - Item (b): $Q_A = (10, 20, 15)\text{ Hz}$, $Q_B = (16, 28, 39)\text{ Hz}$, $Q_C = (12, 23, 21)\text{ Hz}$.
     $$d(Q_A, Q_B) = \sqrt{(16-10)^2 + (28-20)^2 + (39-15)^2} = \sqrt{6^2 + 8^2 + 24^2} = \sqrt{36 + 64 + 576} = \sqrt{676} = 26\text{ Hz}.$$
     $$d(Q_A, Q_C) = \sqrt{(12-10)^2 + (23-20)^2 + (21-15)^2} = \sqrt{2^2 + 3^2 + 6^2} = \sqrt{4 + 9 + 36} = \sqrt{49} = 7\text{ Hz}.$$
     Como $26\text{ Hz} > 7\text{ Hz}$, os estímulos A e B separam-se muito melhor do que A e C. **Correto.**

6. **[Exercício 1.5.1.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-05.dlt#L174-L195) (`exr:1-5-1-1` — Básico: Quadrantes, distância e ponto médio):**
   - Dados: $A = (-2, 7)$ e $B = (4, -1)$.
   - Item (a): $A \in$ II quadrante ($x < 0, y > 0$); $B \in$ IV quadrante ($x > 0, y < 0$). **Correto.**
   - Item (b): $\Delta x = 4 - (-2) = 6$, $\Delta y = -1 - 7 = -8$.
     $$d(A, B) = \sqrt{6^2 + (-8)^2} = \sqrt{36 + 64} = \sqrt{100} = 10.$$ **Correto.**
   - Item (c): $M = \left(\frac{-2 + 4}{2},\; \frac{7 - 1}{2}\right) = (1, 3)$.
     Conferência: $d(A, M) = \sqrt{(1 - (-2))^2 + (3 - 7)^2} = \sqrt{3^2 + (-4)^2} = \sqrt{25} = 5 = \frac{10}{2}$. **Correto.**

7. **[Exercício 1.5.1.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-05.dlt#L197-L215) (`exr:1-5-1-2` — Básico: Eletrodos em matriz cortical MEA):**
   - Dados: $E_1 = (150, 200)\;\mu\text{m}$, $E_2 = (450, 600)\;\mu\text{m}$.
   - Item (a): $\Delta x = 450 - 150 = 300\;\mu\text{m}$, $\Delta y = 600 - 200 = 400\;\mu\text{m}$.
     $$d(E_1, E_2) = \sqrt{300^2 + 400^2} = \sqrt{90\,000 + 160\,000} = \sqrt{250\,000} = 500\;\mu\text{m}.$$ **Correto.**
   - Item (b): Ponto médio:
     $$M = \left(\frac{150 + 450}{2},\; \frac{200 + 600}{2}\right) = \left(\frac{600}{2},\; \frac{800}{2}\right) = (300, 400)\;\mu\text{m}.$$ **Correto.**

8. **[Exercício 1.5.1.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-05.dlt#L217-L232) (`exr:1-5-1-3` — Intermediário: Ponto equidistante sobre o eixo $x$):**
   - Dados: $P = (x, 0)$, $A = (1, 4)$, $B = (7, 2)$.
   - Equação: $d(P, A)^2 = d(P, B)^2 \implies (x - 1)^2 + (0 - 4)^2 = (x - 7)^2 + (0 - 2)^2$.
   - Expansão: $x^2 - 2x + 1 + 16 = x^2 - 14x + 49 + 4 \implies x^2 - 2x + 17 = x^2 - 14x + 53$.
   - Simplificação: $12x = 36 \implies x = 3 \implies P = (3, 0)$.
   - Conferência: $d(P, A) = \sqrt{(3 - 1)^2 + (-4)^2} = \sqrt{4 + 16} = \sqrt{20}$; $d(P, B) = \sqrt{(3 - 7)^2 + (-2)^2} = \sqrt{16 + 4} = \sqrt{20}$. **Correto.**

9. **[Exercício 1.5.1.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-05.dlt#L234-L255) (`exr:1-5-1-4` — Avançado: Espaço de atividade 3D e projeção 2D):**
   - Dados: $S_0 = (20, 15, 30)\text{ Hz}$, $S_1 = (24, 18, 42)\text{ Hz}$, $S_2 = (28, 21, 30)\text{ Hz}$.
   - Item (a) em $\mathbb{R}^3$:
     $$d(S_0, S_1) = \sqrt{(24-20)^2 + (18-15)^2 + (42-30)^2} = \sqrt{4^2 + 3^2 + 12^2} = \sqrt{16 + 9 + 144} = \sqrt{169} = 13\text{ Hz}.$$
     $$d(S_0, S_2) = \sqrt{(28-20)^2 + (21-15)^2 + (30-30)^2} = \sqrt{8^2 + 6^2 + 0^2} = \sqrt{64 + 36} = \sqrt{100} = 10\text{ Hz}.$$
     Logo, $S_1$ é a resposta mais distante em 3D ($13\text{ Hz} > 10\text{ Hz}$). **Correto.**
   - Item (b) em $\mathbb{R}^2$ projetado $(r_1, r_2)$:
     $$d_{2\text{D}}(S_0, S_1) = \sqrt{4^2 + 3^2} = \sqrt{25} = 5\text{ Hz}.$$
     $$d_{2\text{D}}(S_0, S_2) = \sqrt{8^2 + 6^2} = \sqrt{100} = 10\text{ Hz}.$$
     A ordem inverte-se porque a diferenciação primária de $S_1$ estava carreada na coordenada $r_3$ ($42 - 30 = 12\text{ Hz}$), anulada pela perda do eletrodo. **Correto.**

---

### 3.2 Subtema 2: Equação da Reta (`sec:1-5-2`)

1. **[Proposição 1.5.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-05.dlt#L288-L309) (`prop:1-5-equacoes-reta` — Formas da reta):**
   - Forma ponto-inclinação: $\frac{y - y_0}{x - x_0} = m \iff y - y_0 = m(x - x_0)$.
   - Forma reduzida: fazendo $(x_0, y_0) = (0, b)$, obtém-se $y = mx + b$. **Dedução correta.**

2. **[Proposição 1.5.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-05.dlt#L313-L339) (`prop:1-5-paralelas-perp` — Condições de paralelismo e perpendicularidade):**
   - Paralelas: $\tan\alpha_1 = \tan\alpha_2 \iff m_1 = m_2$.
   - Perpendiculares: transladando retas para a origem, $y = m_1 x$ e $y = m_2 x$. Tomando $O = (0, 0)$, $P = (1, m_1)$ e $Q = (1, m_2)$:
     Ângulo reto $\iff d(O, P)^2 + d(O, Q)^2 = d(P, Q)^2$.
     $$(1 + m_1^2) + (1 + m_2^2) = (1 - 1)^2 + (m_2 - m_1)^2$$
     $$2 + m_1^2 + m_2^2 = m_2^2 - 2m_1 m_2 + m_1^2 \implies 2 = -2m_1 m_2 \implies m_1 m_2 = -1.$$ **Dedução correta.**

3. **[Exemplo 1.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-05.dlt#L343-L368) (`exm:1-5-reta-basica` — Reta por dois pontos, perpendicular e interseção):**
   - Dados: $A = (1, 3)$, $B = (5, 11)$, $C = (4, 4)$.
   - Item (a): $m_r = \frac{11 - 3}{5 - 1} = \frac{8}{4} = 2$.
     Equação: $y - 3 = 2(x - 1) \implies y = 2x + 1$.
     Conferência em $B$: $2(5) + 1 = 11$.
     Ângulo: $\alpha = \arctan(2) \approx 63{,}435^\circ \approx 63{,}4^\circ$. **Correto.**
   - Item (b): Reta perpendicular $s$: $m_s = -\frac{1}{m_r} = -\frac{1}{2}$.
     Passando por $C(4, 4)$: $y - 4 = -\frac{1}{2}(x - 4) \implies y = -\frac{1}{2}x + 6$.
     Interseção: $2x + 1 = -\frac{1}{2}x + 6 \implies \frac{5}{2}x = 5 \implies x = 2$.
     $y = 2(2) + 1 = 5$.
     Conferência em $s$: $-\frac{1}{2}(2) + 6 = 5 \implies P = (2, 5)$. **Correto.**

4. **[Exemplo 1.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-05.dlt#L372-L401) (`exm:1-5-curva-iv` — Curvas $I$-$V$ de canais iônicos):**
   - Parâmetros: $g_{\text{K}} = 25\text{ nS}$, $E_{\text{K}} = -90\text{ mV}$; $g_{\text{Na}} = 4\text{ nS}$, $E_{\text{Na}} = +55\text{ mV}$.
   - Unidades: $1\text{ nS} \times 1\text{ mV} = 10^{-9}\text{ S} \times 10^{-3}\text{ V} = 10^{-12}\text{ A} = 1\text{ pA}$.
   - Item (a):
     $I_{\text{K}}(V) = 25(V - (-90)) = 25(V + 90) = 25V + 2\,250\text{ pA}$.
     $I_{\text{Na}}(V) = 4(V - 55) = 4V - 220\text{ pA}$.
     Inclinações: $g_{\text{K}} = 25\text{ nS}$, $g_{\text{Na}} = 4\text{ nS}$.
     Interceptos horizontais ($I = 0$): $V = E_{\text{K}} = -90\text{ mV}$, $V = E_{\text{Na}} = +55\text{ mV}$. **Correto.**
   - Item (b): Avaliação em $V = -70\text{ mV}$:
     $$I_{\text{K}}(-70) = 25(-70 + 90) = 25 \cdot 20 = +500\text{ pA}.$$
     $$I_{\text{Na}}(-70) = 4(-70 - 55) = 4 \cdot (-125) = -500\text{ pA}.$$
     $$I_{\text{total}}(-70) = +500 + (-500) = 0\text{ pA}.$$
     Corrente líquida nula $\implies V = -70\text{ mV}$ é o potencial de repouso. **Correto.**

5. **[Exercício 1.5.2.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-05.dlt#L418-L438) (`exr:1-5-2-1` — Básico: Reta por dois pontos, horizontal e vertical):**
   - Dados: $A = (2, -3)$, $B = (6, 5)$.
   - Item (a): $m = \frac{5 - (-3)}{6 - 2} = \frac{8}{4} = 2$.
     $y - (-3) = 2(x - 2) \implies y + 3 = 2x - 4 \implies y = 2x - 7$.
     Conferência em $B$: $2(6) - 7 = 5$. **Correto.**
   - Item (b): Reta horizontal por $A$: $y = -3$ ($m = 0$, função constante).
     Reta vertical por $A$: $x = 2$ (sem inclinação definida, não é gráfico de função). **Correto.**

6. **[Exercício 1.5.2.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-05.dlt#L440-L461) (`exr:1-5-2-2` — Básico: Paralelas, perpendiculares e interseção):**
   - Reta de referência: $r: y = 3x - 4$.
   - Item (a): Reta $s$ paralela por $(2, 5) \implies m_s = 3$:
     $y - 5 = 3(x - 2) \implies y = 3x - 1$. **Correto.**
   - Item (b): Reta $t$ perpendicular por $(3, 4) \implies m_t = -\frac{1}{3}$:
     $y - 4 = -\frac{1}{3}(x - 3) \implies y = -\frac{1}{3}x + 5$.
     Interseção com $r$: $3x - 4 = -\frac{1}{3}x + 5 \implies \frac{10}{3}x = 9 \implies x = \frac{27}{10} = 2{,}7$.
     $y = 3(2{,}7) - 4 = 8{,}1 - 4 = 4{,}1$.
     Conferência em $t$: $-\frac{1}{3}(2{,}7) + 5 = -0{,}9 + 5 = 4{,}1 \implies (2{,}7;\; 4{,}1)$. **Correto.**

7. **[Exercício 1.5.2.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-05.dlt#L463-L485) (`exr:1-5-2-3` — Intermediário: Curva $I$-$V$ experimental em patch-clamp):**
   - Dados: $(V_1, I_1) = (-60\text{ mV}, -120\text{ pA})$, $(V_2, I_2) = (+20\text{ mV}, +200\text{ pA})$.
   - Item (a): Condutância:
     $$g = \frac{I_2 - I_1}{V_2 - V_1} = \frac{200 - (-120)}{20 - (-60)} = \frac{320\text{ pA}}{80\text{ mV}} = 4\text{ nS}.$$
     Equação: $I - 200 = 4(V - 20) \implies I(V) = 4V + 120\text{ pA}$.
     Conferência em $V_1$: $4(-60) + 120 = -240 + 120 = -120\text{ pA}$. **Correto.**
   - Item (b): Potencial de reversão $I(E) = 0$:
     $$4E + 120 = 0 \implies 4E = -120 \implies E = -30\text{ mV}.$$
     Forma fatorada: $I(V) = 4(V - (-30)) = 4(V + 30)\text{ pA}$. **Correto.**

8. **[Exercício 1.5.2.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-05.dlt#L487-L511) (`exr:1-5-2-4` — Avançado: Canais em paralelo e potencial de ação):**
   - Item (a): Condição de corrente nula:
     $$g_{\text{K}}(V_{\text{eq}} - E_{\text{K}}) + g_{\text{Na}}(V_{\text{eq}} - E_{\text{Na}}) = 0$$
     $$(g_{\text{K}} + g_{\text{Na}}) V_{\text{eq}} = g_{\text{K}} E_{\text{K}} + g_{\text{Na}} E_{\text{Na}} \implies V_{\text{eq}} = \frac{g_{\text{K}} E_{\text{K}} + g_{\text{Na}} E_{\text{Na}}}{g_{\text{K}} + g_{\text{Na}}}.$$
     Geometricamente, $I_{\text{K}}(V) = -I_{\text{Na}}(V)$, correspondendo ao cruzamento de $y = I_{\text{K}}(V)$ com a reta refletida $y = -I_{\text{Na}}(V)$. **Correto.**
   - Item (b): Parâmetros: $g_{\text{K}} = 25\text{ nS}$, $g_{\text{Na}} = 100\text{ nS}$, $E_{\text{K}} = -90\text{ mV}$, $E_{\text{Na}} = +55\text{ mV}$.
     $$V_{\text{eq}}' = \frac{25(-90) + 100(55)}{25 + 100} = \frac{-2\,250 + 5\,500}{125} = \frac{3\,250}{125} = +26\text{ mV}.$$
     Conferência: $I_{\text{K}}(26) = 25(26 - (-90)) = 25(116) = +2\,900\text{ pA}$.
     $I_{\text{Na}}(26) = 100(26 - 55) = 100(-29) = -2\,900\text{ pA}$.
     Soma $= 0\text{ pA}$. O potencial varia de $-70\text{ mV}$ para $+26\text{ mV}$, caracterizando forte **despolarização**. **Correto.**

---

### 3.3 Subtema 3: Equação do Círculo (`sec:1-5-3`)

1. **[Proposição 1.5.5](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-05.dlt#L546-L568) (`prop:1-5-forma-geral-circulo` — Forma geral e completamento de quadrados):**
   - Partindo de $x^2 + y^2 + Dx + Ey + F = 0$:
     $$(x^2 + Dx) + (y^2 + Ey) = -F.$$
   - Somando $\left(\frac{D}{2}\right)^2 = \frac{D^2}{4}$ e $\left(\frac{E}{2}\right)^2 = \frac{E^2}{4}$ em ambos os membros:
     $$\left(x + \frac{D}{2}\right)^2 + \left(y + \frac{E}{2}\right)^2 = \frac{D^2 + E^2 - 4F}{4} = K.$$
   - Se $K > 0$, centro $C = \left(-\frac{D}{2},\; -\frac{E}{2}\right)$ e $r = \sqrt{K}$; se $K = 0$, ponto único; se $K < 0$, conjunto vazio em $\mathbb{R}^2$. **Dedução correta.**

2. **[Exemplo 1.5](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-05.dlt#L578-L608) (`exm:1-5-completar-quadrados` — Completamento e interseção reta-círculo):**
   - Item (a): $x^2 + y^2 - 6x + 4y - 12 = 0$.
     $$(x^2 - 6x + 9) + (y^2 + 4y + 4) = 12 + 9 + 4 = 25 \implies (x - 3)^2 + (y + 2)^2 = 25.$$
     Círculo de centro $C = (3, -2)$ e raio $r = \sqrt{25} = 5$. **Correto.**
   - Item (b): Interseção com $y = x - 4$:
     $$(x - 3)^2 + (x - 4 + 2)^2 = 25 \implies (x - 3)^2 + (x - 2)^2 = 25$$
     $$x^2 - 6x + 9 + x^2 - 4x + 4 = 25 \implies 2x^2 - 10x - 12 = 0 \implies x^2 - 5x - 6 = 0.$$
     Bhaskara: $\Delta = (-5)^2 - 4(1)(-6) = 25 + 24 = 49$.
     $x = \frac{5 \pm 7}{2} \implies x_1 = 6, \quad x_2 = -1$.
     Ordenadas: $y_1 = 6 - 4 = 2 \implies (6, 2)$; $y_2 = -1 - 4 = -5 \implies (-1, -5)$.
     Conferência no círculo: $(6 - 3)^2 + (2 + 2)^2 = 9 + 16 = 25$; $(-1 - 3)^2 + (-5 + 2)^2 = 16 + 9 = 25$. **Correto.**

3. **[Exemplo 1.6](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-05.dlt#L610-L635) (`exm:1-5-campo-receptivo` — Campo receptivo centro-periferia na retina):**
   - Dados: Centro $C = (3, -1)$, $r_{\text{c}} = 2\text{ mm}$, $r_{\text{p}} = 5\text{ mm}$.
   - Item (a): $d^2 = (x - 3)^2 + (y + 1)^2$.
     Centro: $d^2 \le 4$; Periferia: $4 < d^2 \le 25$; Fora: $d^2 > 25$. **Correto.**
   - Item (b):
     $P_1 = (4, 0)$: $(4-3)^2 + (0+1)^2 = 1 + 1 = 2 \le 4 \implies$ Centro ($d = \sqrt{2} \approx 1{,}41\text{ mm}$).
     $P_2 = (6, 3)$: $(6-3)^2 + (3+1)^2 = 9 + 16 = 25 \implies 4 < 25 \le 25 \implies$ Periferia ($d = 5\text{ mm}$).
     $P_3 = (-2, 4)$: $(-2-3)^2 + (4+1)^2 = 25 + 25 = 50 > 25 \implies$ Fora ($d = \sqrt{50} \approx 7{,}07\text{ mm}$). **Correto.**

4. **[Exemplo 1.7](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-05.dlt#L637-L658) (`exm:1-5-esfera-atividade` — Círculo e esfera de tolerância no espaço de disparo):**
   - Item (a): Centro $R_0 = (20, 30)\text{ Hz}$, $r = 5\text{ Hz}$.
     Círculo de borda: $(r_1 - 20)^2 + (r_2 - 30)^2 = 25$.
     Disco fechado: $(r_1 - 20)^2 + (r_2 - 30)^2 \le 25$. **Correto.**
   - Item (b): Centro em 3D $R_0 = (20, 30, 15)\text{ Hz}$, raio $r = 5\text{ Hz}$.
     $R_1 = (22, 33, 19)$: $(22-20)^2 + (33-30)^2 + (19-15)^2 = 4 + 9 + 16 = 29 > 25 \implies$ Fora ($d = \sqrt{29} \approx 5{,}39\text{ Hz}$).
     $R_2 = (23, 34, 15)$: $(23-20)^2 + (34-30)^2 + (15-15)^2 = 9 + 16 + 0 = 25 \le 25 \implies$ Sobre a superfície ($d = 5\text{ Hz}$). **Correto.**

5. **[Exercício 1.5.3.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-05.dlt#L670-L690) (`exr:1-5-3-1` — Básico: Centro, raio e posição de pontos):**
   - Círculo: $(x + 4)^2 + (y - 3)^2 = 25$.
   - Item (a): $C = (-4, 3)$, $r = \sqrt{25} = 5$. **Correto.**
   - Item (b):
     $P = (-1, 7)$: $(-1 + 4)^2 + (7 - 3)^2 = 9 + 16 = 25 \implies$ Sobre o círculo.
     $Q = (0, 1)$: $(0 + 4)^2 + (1 - 3)^2 = 16 + 4 = 20 < 25 \implies$ Dentro do círculo.
     $R = (2, 3)$: $(2 + 4)^2 + (3 - 3)^2 = 36 + 0 = 36 > 25 \implies$ Fora do círculo. **Correto.**

6. **[Exercício 1.5.3.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-05.dlt#L692-L716) (`exr:1-5-3-2` — Intermediário: Completando quadrados na forma geral):**
   - Item (a): $x^2 + y^2 + 8x - 6y + 9 = 0$.
     $(x^2 + 8x + 16) + (y^2 - 6y + 9) = -9 + 16 + 9 = 16 \implies (x + 4)^2 + (y - 3)^2 = 16$.
     Como $16 > 0$, é um círculo com centro $C = (-4, 3)$ e raio $r = \sqrt{16} = 4$. **Correto.**
   - Item (b): $x^2 + y^2 - 2x + 4y + 10 = 0$.
     $(x^2 - 2x + 1) + (y^2 + 4y + 4) = -10 + 1 + 4 = -5 \implies (x - 1)^2 + (y + 2)^2 = -5$.
     Como soma de quadrados reais não pode ser $-5 < 0$, conjunto vazio em $\mathbb{R}^2$. **Correto.**

7. **[Exercício 1.5.3.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-05.dlt#L718-L736) (`exr:1-5-3-3` — Intermediário: Campo receptivo e círculo unitário):**
   - Item (a): Centro $(2, 5)\text{ mm}$, centro excitatório $r_{\text{c}} = 1{,}5\text{ mm}$ ($r_{\text{c}}^2 = 2{,}25$), periferia $r_{\text{p}} = 4\text{ mm}$ ($r_{\text{p}}^2 = 16$).
     Estímulo em $(3, 3)\text{ mm}$: $d^2 = (3 - 2)^2 + (3 - 5)^2 = 1 + 4 = 5$.
     Como $2{,}25 < 5 \le 16$, o estímulo cai na **periferia** inibitória ($d = \sqrt{5} \approx 2{,}24\text{ mm}$). **Correto.**
   - Item (b): Ângulo $\theta = 150^\circ$.
     $\cos 150^\circ = -\cos 30^\circ = -\frac{\sqrt{3}}{2}$, $\operatorname{sen} 150^\circ = \operatorname{sen} 30^\circ = \frac{1}{2}$.
     Ponto: $P = \left(-\frac{\sqrt{3}}{2},\; \frac{1}{2}\right)$.
     Conferência: $x^2 + y^2 = \left(-\frac{\sqrt{3}}{2}\right)^2 + \left(\frac{1}{2}\right)^2 = \frac{3}{4} + \frac{1}{4} = 1$. **Correto.**

8. **[Exercício 1.5.3.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-05.dlt#L738-L767) (`exr:1-5-3-4` — Avançado: Reta tangente ao círculo):**
   - Círculo: $x^2 + y^2 = 25$, ponto $P = (3, 4)$.
   - Item (a): Inclinação radial de $O(0, 0)$ a $P(3, 4)$: $m_{OP} = \frac{4 - 0}{3 - 0} = \frac{4}{3}$.
     Reta tangente perpendicular: $m_t = -\frac{1}{m_{OP}} = -\frac{3}{4}$.
     Passando por $P(3, 4)$: $y - 4 = -\frac{3}{4}(x - 3) \implies y = -\frac{3}{4}x + \frac{25}{4}$. **Correto.**
   - Item (b): Substituição em $x^2 + y^2 = 25$:
     $$x^2 + \left(\frac{25 - 3x}{4}\right)^2 = 25 \implies 16x^2 + (625 - 150x + 9x^2) = 400$$
     $$25x^2 - 150x + 225 = 0 \implies x^2 - 6x + 9 = 0.$$
     Discriminante de Bhaskara: $\Delta = (-6)^2 - 4(1)(9) = 36 - 36 = 0$.
     Como $\Delta = 0$, há raiz real única: $x = \frac{6}{2} = 3 \implies y = -\frac{3}{4}(3) + \frac{25}{4} = \frac{16}{4} = 4$.
     Ponto único de contato em $P = (3, 4)$. **Correto.**

---

### 3.4 Auditoria do Script de Figura (`conteudo/modulo-01/fig/curva-iv.py`)

- **Equações e parâmetros no script:**
  - $g_{\text{K}} = 25{,}0\text{ nS}$, $E_{\text{K}} = -90{,}0\text{ mV}$.
  - $g_{\text{Na}} = 4{,}0\text{ nS}$, $E_{\text{Na}} = +55{,}0\text{ mV}$.
  - $V_{\text{rep}} = \frac{25(-90) + 4(55)}{25 + 4} = \frac{-2\,250 + 220}{29} = \frac{-2\,030}{29} = -70{,}0\text{ mV}$.
  - Correntes no repouso: $I_{\text{K}}(-70) = 25(-70 - (-90)) = +500\text{ pA}$; $I_{\text{Na}}(-70) = 4(-70 - 55) = -500\text{ pA}$; $I_{\text{total}} = 0\text{ pA}$.
- **Conformidade técnica do script:**
  - Define `plt.rcParams["svg.fonttype"] = "none"` para evitar fontes SVG pesadas em curvas;
  - Utiliza fundo transparente (`fig.patch.set_alpha(0.0)`, `ax.patch.set_alpha(0.0)`);
  - Salva o arquivo diretamente em `conteudo/modulo-01/fig/curva-iv.svg` via `pathlib.Path`;
  - Rótulos dos eixos, títulos e anotações inteiramente em português com notação matemática consistente;
  - Alinhamento total com o elemento `<figure src="fig/curva-iv.svg" ...>` e sua legenda na aula.

---

## 4. Checklist de Conformidade Editorial e Pedagógica

| Critério avaliado | Status | Análise detalhada |
|---|:---:|---|
| **Dica e solução completa em cada exercício** | **OK** | Todos os 12 exercícios possuem `<hint><title>Ver dica</title>...</hint>` e `<solution collapsible="true" collapsed="true">` contendo o raciocínio formal passo a passo e a conferência dos resultados. |
| **Pelo menos um exemplo biológico por seção** | **OK** | **Seção 1:** Imagem de microscopia confocal de fatia cortical em micrômetros (`exm:1-5-fatia`) e espaço de atividade de taxas de disparo (`exm:1-5-espaco-atividade`), além de matrizes MEA (`exr:1-5-1-2`) e projeções neurais 3D para 2D (`exr:1-5-1-4`).<br>**Seção 2:** Curvas $I$-$V$ lineares de canais iônicos com potencial de reversão e repouso a $-70\text{ mV}$ (`exm:1-5-curva-iv`), patch-clamp (`exr:1-5-2-3`) e influxo de sódio na despolarização do potencial de ação (`exr:1-5-2-4`).<br>**Seção 3:** Campos receptivos centro-periferia em células ganglionares da retina (`exm:1-5-campo-receptivo` e `exr:1-5-3-3`) e esfera de tolerância de disparo populacional (`exm:1-5-esfera-atividade`). |
| **Afirmações de neurociência de livro-texto** | **OK** | Todas as convenções de sinal e valores numéricos são rigorosamente canônicos: potencial de repouso ($-70\text{ mV}$), potenciais de reversão ($E_{\text{K}} = -90\text{ mV}$, $E_{\text{Na}} = +55\text{ mV}$), condutâncias da ordem de $\text{nS}$, correntes em $\text{pA}$, taxas de disparo entre $0$ e $200\text{ Hz}$, e estrutura centro-periferia retiniana de Kuffler (Dayan & Abbott, cap. 2 e 5; Kandel et al., cap. 6, 7 e 26). |
| **Sequenciamento pedagógico de conceitos** | **OK** | Nenhum conceito é presumido sem apresentação prévia. A geometria analítica parte do plano cartesiano e Pitágoras (Temas 1.1 e 1.2), conecta a inclinação da reta à função afim e à tangente (Temas 1.3 e 1.4), introduz o círculo a partir da distância euclidiana e retoma Bhaskara (Tema 1.1) para as interseções, antecipando de forma elegante a reta tangente e secante para o Módulo 2 (Cálculo Real) e os vetores para o Módulo 5 (Álgebra Linear). |
| **Código Python e scripts de figura** | **OK** | O script [curva-iv.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/fig/curva-iv.py) roda sem erros, possui tipagem limpa e gera a figura SVG referenciada com precisão. O corpo da aula não possui blocos `<code>` desnecessários, respeitando a diretriz de reservar código embutido para os módulos aplicados (4, 5, 6, 7, 8 e 9). |
| **Consistência de notação matemática** | **OK** | Emprego rigoroso de vírgula decimal na prosa e na matemática ($0{,}5$, $63{,}4^\circ$, $2{,}7$), ponto e vírgula na separação de coordenadas com vírgula decimal ($(2{,}7;\; 4{,}1)$), conjuntos em $\mathbb{R}^2$ e $\mathbb{R}^3$, e padronização vetorial anunciada para $\mathbf{x}$. |
| **Cobertura de todos os subtemas pedidos** | **OK** | Cobre com completude e profundidade os 3 subtemas da ementa oficial: Subtema 1 (Introdução e distância euclidiana como distância entre padrões de atividade), Subtema 2 (Equação da reta, inclinação como condutância e $I = g(V - E)$) e Subtema 3 (Equação do círculo, completamento de quadrados e campos receptivos). |
| **Tamanho dentro do padrão** | **OK** | O texto possui aproximadamente 3.850 palavras (801 linhas no `.dlt`), perfeitamente ajustado à faixa estipulada de 2.500 a 5.000 palavras. |
| **Conformidade técnica Delta v0.6.0** | **OK** | XML estrito válido: todos os atributos possuem valores explícitos, caracteres especiais na prosa usam entidades, `<intuition>` empregada unicamente como filha direta de resultados sem `id`, soluções recolhidas por padrão (`collapsible="true" collapsed="true"`), e metadados com retorno ao guia conformes à especificação. |

---

## 5. Contas Conferidas

Abaixo estão listados todos os identificadores de definições, proposições, exemplos e exercícios que tiveram suas deduções algébricas e contas numéricas auditadas, refeitas e atestadas como **corretas**:

- `prop:1-5-distancia-2d` (dedução da distância euclidiana 2D via Pitágoras)
- `def:1-5-ponto-medio` (definição analítica do ponto médio)
- `prop:1-5-distancia-3d` (dedução da distância euclidiana e ponto médio em 3D)
- `exm:1-5-fatia` (itens a, b, c — quadrantes, distância $130\;\mu\text{m}$ e ponto médio $(20, 45)\;\mu\text{m}$)
- `exm:1-5-espaco-atividade` (itens a, b — distância 2D de $10\text{ Hz}$ e distâncias 3D de $26\text{ Hz}$ e $7\text{ Hz}$)
- `exr:1-5-1-1` (itens a, b, c — quadrantes II e IV, distância $10$ e ponto médio $(1, 3)$)
- `exr:1-5-1-2` (itens a, b — distância entre eletrodos $500\;\mu\text{m}$ e ponto médio $(300, 400)\;\mu\text{m}$)
- `exr:1-5-1-3` (ponto equidistante sobre eixo $x$ em $P = (3, 0)$ com conferência de distâncias $\sqrt{20}$)
- `exr:1-5-1-4` (itens a, b — distâncias em 3D de $13\text{ Hz}$ e $10\text{ Hz}$, distâncias projetadas em 2D de $5\text{ Hz}$ e $10\text{ Hz}$)
- `def:1-5-inclinacao` (definição de inclinação e relação com $\tan\alpha$)
- `prop:1-5-equacoes-reta` (dedução das formas ponto-inclinação e reduzida)
- `prop:1-5-paralelas-perp` (dedução de paralelismo e de perpendicularidade $m_1 m_2 = -1$ via Pitágoras)
- `exm:1-5-reta-basica` (itens a, b — reta $y = 2x + 1$, ângulo $\approx 63{,}4^\circ$, reta perpendicular $y = -\frac{1}{2}x + 6$ e interseção em $(2, 5)$)
- `exm:1-5-curva-iv` (itens a, b — retas $I_{\text{K}}$ e $I_{\text{Na}}$, cancelamento das correntes em $+500\text{ pA}$ e $-500\text{ pA}$ no repouso de $-70\text{ mV}$)
- `exr:1-5-2-1` (itens a, b — reta $y = 2x - 7$, horizontal $y = -3$ e vertical $x = 2$)
- `exr:1-5-2-2` (itens a, b — reta paralela $y = 3x - 1$, perpendicular $y = -\frac{1}{3}x + 5$ e interseção em $(2{,}7;\; 4{,}1)$)
- `exr:1-5-2-3` (itens a, b — condutância $g = 4\text{ nS}$, equação $I(V) = 4V + 120\text{ pA}$ e potencial de reversão $E = -30\text{ mV}$)
- `exr:1-5-2-4` (itens a, b — dedução da média ponderada de condutâncias e novo potencial de equilíbrio em $+26\text{ mV}$)
- `def:1-5-circulo` (equação reduzida do círculo e classificação de regiões)
- `prop:1-5-forma-geral-circulo` (dedução do completamento de quadrados e discriminante de existência $K$)
- `exm:1-5-completar-quadrados` (itens a, b — centro $(3, -2)$, raio $5$ e pontos de interseção $(6, 2)$ e $(-1, -5)$ com reta secante)
- `exm:1-5-campo-receptivo` (itens a, b — inequações de centro, anel periférico e fora, com classificação exata de $P_1, P_2, P_3$)
- `exm:1-5-esfera-atividade` (itens a, b — equações de círculo e esfera de raio $5\text{ Hz}$, com classificação dos padrões $R_1$ fora e $R_2$ sobre a borda)
- `exr:1-5-3-1` (itens a, b — centro $(-4, 3)$, raio $5$, pontos sobre, dentro e fora)
- `exr:1-5-3-2` (itens a, b — completamento de quadrados resultando em círculo com centro $(-4, 3)$ e $r = 4$, e conjunto vazio com soma de quadrados igual a $-5$)
- `exr:1-5-3-3` (itens a, b — classificação de ponto no campo receptivo periférico com $d^2 = 5$ e verificação trigonométrica no círculo unitário com $\theta = 150^\circ$)
- `exr:1-5-3-4` (itens a, b — inclinação radial $m = \frac{4}{3}$, reta tangente $y = -\frac{3}{4}x + \frac{25}{4}$ e Bhaskara com $\Delta = 0$ confirmando tangência em $(3, 4)$)
- `fig:1-5-curva-iv` / `curva-iv.py` (cálculo de $V_{\text{rep}} = -70{,}0\text{ mV}$, correntes $+500\text{ pA}$ e $-500\text{ pA}$, e geração do SVG)
