# Relatório de Revisão Técnica — Módulo 01 · Tema 02 (Geometria)

- **Arquivo revisado:** [tema-02.dlt](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-02.dlt)
- **Script de figura revisado:** [barras-orientadas.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/fig/barras-orientadas.py)
- **Documentos de referência:** [PADRAO-AULAS.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/PADRAO-AULAS.md) e [DELTA-COLA.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/DELTA-COLA.md)
- **Data da revisão:** 14 de novembro de 2026
- **Perfil do revisor:** Matemático, Neurocientista Computacional e Professor de Alunos de Ciências Biológicas

---

## 1. Veredito

**APROVAR**

A aula `tema-02.dlt` apresenta qualidade técnica, matemática e pedagógica exemplar. Todas as deduções, exemplos e soluções dos 12 exercícios foram integralmente recalculados e auditados, revelando **$100\%$ de exatidão analítica e numérica** (sem qualquer divergência). A estrutura textual respeita estritamente o contrato editorial ([PADRAO-AULAS.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/PADRAO-AULAS.md)) e as regras duras de XML estrito do Delta v0.6.0 ([DELTA-COLA.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/DELTA-COLA.md)).

As pontes com a biologia celular (microscopia óptica e eletrônica, câmaras de contagem, razão superfície/volume em difusão, pavimentação hexagonal epitelial) e com a neurociência de sistemas (eletrofisiologia e seletividade de orientação em células simples de V1 segundo Hubel & Wiesel) são precisas, autênticas e de livro-texto (Kandel; Dayan & Abbott; Alberts). O script de figura em Python [barras-orientadas.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/fig/barras-orientadas.py) é executável, enxuto, perfeitamente alinhado às legendas e gera a ilustração em conformidade com os padrões do projeto.

Foram catalogadas apenas 3 sugestões pontuais de polimento pedagógico e de formatação na tabela a seguir, nenhuma de caráter impeditivo.

---

## 2. Tabela de Problemas e Observações

| Severidade | Local | Trecho | Correção sugerida |
|---|---|---|---|
| Pedagógico | Seção 1 (`sec:1-2-1`), `exr:1-2-1-3`, linha ~222 | `($1\text{ cm} = 10\text{ mm} = 10^7\text{ nm}$)` | Para alunos de Biologia em transição da notação decimal para potências de $10$, a passagem direta de $10\text{ mm}$ para $10^7\text{ nm}$ omite a etapa intermediária de conversão. Sugere-se explicitar o produto de potências: `($1\text{ cm} = 10\text{ mm} = 10 \cdot 10^6\text{ nm} = 10^7\text{ nm}$)`. |
| Pedagógico | Seção 1 (`sec:1-2-1`), `exr:1-2-1-4`, linha ~257 | `passa de $\frac{3}{1\;\mu\text{m}} = 3\;\mu\text{m}^{-1}$ na bactéria para $\frac{3}{10\;\mu\text{m}} = 0{,}3\;\mu\text{m}^{-1}$ na célula eucariótica.` | O expoente negativo na unidade ($\mu\text{m}^{-1}$) costuma gerar confusão inicial em estudantes de ciências da vida. Sugere-se acrescentar uma nota breve entre parênteses esclarecendo o significado físico: `(isto é, $3\;\mu\text{m}^2$ de membrana por $\mu\text{m}^3$ de volume na bactéria, contra apenas $0{,}3\;\mu\text{m}^2/\mu\text{m}^3$ na célula eucariótica)`. |
| Formato | Seção 3 (`sec:1-2-3`), `fig:1-2-barras`, linha ~597 | `alt="Quatro painéis circulares representando o campo receptivo de uma célula simples em V1..."` | O texto do atributo `alt` possui 286 caracteres. Embora seja rico e acessível, linters estritos de acessibilidade web recomendam manter o atributo `alt` sintético (abaixo de 125–150 caracteres), delegando a descrição anatômica detalhada à `<caption>` (já presente e excelente). Sugere-se encurtar o `alt` para: `alt="Campos receptivos de célula simples em V1 e barras de estímulo em diferentes orientações"`. |

---

## 3. Recálculo e Auditoria de Contas

Todas as fórmulas, deduções teóricas, exemplos numéricos e soluções de exercícios foram recalculados passo a passo de forma independente. Não foi encontrada **nenhuma divergência numérica ou algébrica**.

### 3.1 Subtema 1: Introdução, Escalas e Semelhança (`sec:1-2-1`)

1. **[Exemplo 1.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-02.dlt#L121-L145) (`exm:1-2-microscopia` — Barra de escala em microscopia óptica):**
   - Item (a): Diâmetro aparente $d_{\text{ap}} = 3\text{ cm} = 30\text{ mm} = 30 \times 10^3\;\mu\text{m} = 30\,000\;\mu\text{m}$.
     Com aumento linear $k = 1\,000$: $d_{\text{real}} = \frac{30\,000\;\mu\text{m}}{1\,000} = 30\;\mu\text{m}$. **Correto.**
   - Item (b): Razão de áreas escala com $k^2 = (10^3)^2 = 10^6$ ($1\,000\,000$ de vezes). **Correto.**
   - Item (c): Barra real de $10\;\mu\text{m}$ na fotografia: $L_{\text{barra}} = 10\;\mu\text{m} \cdot 1\,000 = 10\,000\;\mu\text{m} = 10\text{ mm} = 1\text{ cm}$. **Correto.**
2. **[Exemplo 1.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-02.dlt#L147-L168) (`exm:1-2-neubauer` — Retículo de contagem celular):**
   - Item (a): Lado $l = 0{,}25\text{ mm}$. Perímetro $P = 4 \cdot 0{,}25\text{ mm} = 1{,}0\text{ mm} = 1\,000\;\mu\text{m}$. **Correto.**
   - Item (b): Área em $\text{mm}^2$: $A = (0{,}25\text{ mm})^2 = 0{,}0625\text{ mm}^2 = 6{,}25 \times 10^{-2}\text{ mm}^2$.
     Conversão para $\mu\text{m}^2$: $(6{,}25 \times 10^{-2}) \cdot 10^6\;\mu\text{m}^2 = 62\,500\;\mu\text{m}^2$.
     Conferência direta: $l = 250\;\mu\text{m} \implies A = (250\;\mu\text{m})^2 = 62\,500\;\mu\text{m}^2$. **Correto.**
3. **[Exercício 1.2.1.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-02.dlt#L179-L195) (`exr:1-2-1-1` — Básico: Classificação de ângulos e perímetro):**
   - Item (a): $35^\circ$ (agudo, $< 90^\circ$); $90^\circ$ (reto); $128^\circ$ (obtuso, entre $90^\circ$ e $180^\circ$); $180^\circ$ (raso). **Correto.**
   - Item (b): Pentágono de lados $3, 4, 5, 4, 2\text{ cm}$: $P = 3 + 4 + 5 + 4 + 2 = 18\text{ cm} = 180\text{ mm}$. **Correto.**
4. **[Exercício 1.2.1.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-02.dlt#L197-L209) (`exr:1-2-1-2` — Básico: Conversão de áreas em campo microscópico):**
   - Campo $2{,}0\text{ mm} \times 1{,}5\text{ mm}$: $A = 2{,}0 \cdot 1{,}5 = 3{,}0\text{ mm}^2$.
   - Em $\mu\text{m}^2$: $3{,}0 \cdot 10^6 = 3{,}0 \times 10^6\;\mu\text{m}^2$.
   - Em $\text{cm}^2$: $\frac{3{,}0}{100} = 0{,}03\text{ cm}^2 = 3{,}0 \times 10^{-2}\text{ cm}^2$. **Correto.**
5. **[Exercício 1.2.1.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-02.dlt#L211-L237) (`exr:1-2-1-3` — Intermediário: Barra de escala na microscopia eletrônica):**
   - Item (a): Barra de $2{,}0\text{ cm} = 2{,}0 \times 10^7\text{ nm}$ para $100\text{ nm}$ reais:
     $k = \frac{2{,}0 \times 10^7}{10^2} = 2{,}0 \times 10^5 = 200\,000\times$. **Correto.**
   - Item (b): Fenda de $4{,}0\text{ mm} = 4{,}0 \times 10^6\text{ nm}$ na imagem:
     $d_{\text{real}} = \frac{4{,}0 \times 10^6\text{ nm}}{2{,}0 \times 10^5} = 20\text{ nm}$. **Correto.**
   - Item (c): Razão de áreas $k^2 = (2{,}0 \times 10^5)^2 = 4{,}0 \times 10^{10}$ ($40$ bilhões de vezes). **Correto.**
6. **[Exercício 1.2.1.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-02.dlt#L239-L264) (`exr:1-2-1-4` — Avançado: Razão superfície/volume e limite celular):**
   - Item (a): $\frac{A}{V} = \frac{4\pi r^2}{\frac{4}{3}\pi r^3} = 4\pi r^2 \cdot \frac{3}{4\pi r^3} = \frac{3}{r}$. **Correto.**
   - Item (b): $r_1 = 1\;\mu\text{m}$, $r_2 = 10\;\mu\text{m} \implies k = 10$.
     Área aumenta por $k^2 = 100$; volume aumenta por $k^3 = 1\,000$.
     Razão $\frac{A}{V}$ cai de $\frac{3}{1} = 3\;\mu\text{m}^{-1}$ para $\frac{3}{10} = 0{,}3\;\mu\text{m}^{-1}$ (redução por um fator de $10$). **Correto.**
   - Item (c): Demanda metabólica cresce com o volume ($r^3$), suprimento por difusão cresce com a área ($r^2$), logo a razão cai com $1/r$, impondo limite ao raio celular em ausência de especializações de transporte. **Correto.**

---

### 3.2 Subtema 2: Áreas Clássicas, Pitágoras e Polígonos (`sec:1-2-2`)

1. **[Deduções e Demonstrações](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-02.dlt#L294-L348) (`thm:1-2-pitagoras`, `prop:1-2-equilatero-hexagono`, `prop:1-2-soma-angulos-poligono`):**
   - Teorema de Pitágoras via quadrado de lado $(a+b)$:
     $(a+b)^2 = 4 \cdot \frac{ab}{2} + c^2 \iff a^2 + 2ab + b^2 = 2ab + c^2 \iff a^2 + b^2 = c^2$. **Correto.**
   - Triângulo equilátero de lado $l$:
     $h^2 + (l/2)^2 = l^2 \implies h^2 = l^2 - l^2/4 = 3l^2/4 \implies h = \frac{l\sqrt{3}}{2}$.
     Área $A_{\triangle} = \frac{l \cdot h}{2} = \frac{l^2\sqrt{3}}{4}$. **Correto.**
   - Hexágono regular: $6 \cdot \frac{l^2\sqrt{3}}{4} = \frac{3\sqrt{3}}{2}l^2$. **Correto.**
   - Soma dos ângulos internos: $S_i = (n - 2) \cdot 180^\circ$; no regular $\alpha_n = \frac{(n-2)\cdot 180^\circ}{n}$. **Correto.**
2. **[Exemplo 2.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-02.dlt#L352-L384) (`exm:1-2-tecido` — Decomposição de corte histológico):**
   - Regiões:
     1. Triângulo retângulo: $A_1 = \frac{3 \cdot 4}{2} = 6\text{ mm}^2$. Hipotenusa: $\sqrt{3^2 + 4^2} = 5\text{ mm}$.
     2. Quadrado: $A_2 = 4 \cdot 4 = 16\text{ mm}^2$. Lado superior: $4\text{ mm}$.
     3. Trapézio retângulo: $B = 4\text{ mm}$, $b = 1\text{ mm}$, $h_{\text{trap}} = 4\text{ mm}$.
        $A_3 = \frac{(4 + 1) \cdot 4}{2} = 10\text{ mm}^2$. Lado inclinado: $\sqrt{4^2 + (4-1)^2} = \sqrt{16 + 9} = 5\text{ mm}$.
   - Área total: $A_{\text{total}} = 6 + 16 + 10 = 32\text{ mm}^2$. **Correto.**
   - Perímetro externo: base inferior ($3 + 4 + 4 = 11\text{ mm}$) + borda direita ($1\text{ mm}$) + topo inclinado direito ($5\text{ mm}$) + topo quadrado ($4\text{ mm}$) + topo inclinado esquerdo ($5\text{ mm}$) $= 11 + 1 + 5 + 4 + 5 = 26\text{ mm}$. **Correto.**
3. **[Exemplo 2.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-02.dlt#L386-L409) (`exm:1-2-epitelio` — Monocamada epitelial e mosaico hexagonal):**
   - Item (a): $\alpha_6 = \frac{(6-2)\cdot 180^\circ}{6} = 120^\circ$. No vértice: $3 \cdot 120^\circ = 360^\circ$ (encaixe perfeito sem frestas). **Correto.**
   - Item (b): Célula de lado $l = 8\;\mu\text{m}$:
     $A_{\text{célula}} = \frac{3\sqrt{3}}{2} \cdot 8^2 = 96\sqrt{3}\;\mu\text{m}^2 \approx 96 \cdot 1{,}732 = 166{,}272 \approx 166{,}3\;\mu\text{m}^2$. **Correto.**
     Monocamada com $500$ células:
     $A_{\text{total}} = 500 \cdot 96\sqrt{3} = 48\,000\sqrt{3}\;\mu\text{m}^2 \approx 48\,000 \cdot 1{,}732 = 83\,136\;\mu\text{m}^2 \approx 8{,}31 \times 10^4\;\mu\text{m}^2 \approx 0{,}083\text{ mm}^2$. **Correto.**
4. **[Exercício 1.2.2.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-02.dlt#L420-L440) (`exr:1-2-2-1` — Básico: Círculo e octógono regular):**
   - Item (a): $r = 5\text{ cm} \implies C = 2\pi(5) = 10\pi\text{ cm} \approx 31{,}4\text{ cm}$; $A = \pi(5)^2 = 25\pi\text{ cm}^2 \approx 78{,}5\text{ cm}^2$. **Correto.**
   - Item (b): $n = 8 \implies S_i = (8 - 2)\cdot 180^\circ = 6 \cdot 180^\circ = 1\,080^\circ$; $\alpha_8 = \frac{1\,080^\circ}{8} = 135^\circ$. **Correto.**
5. **[Exercício 1.2.2.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-02.dlt#L442-L452) (`exr:1-2-2-2` — Básico: Distância euclidiana de microeletrodo):**
   - Catetos $a = 80\;\mu\text{m}$, $b = 60\;\mu\text{m} \implies d^2 = 80^2 + 60^2 = 6\,400 + 3\,600 = 10\,000 \implies d = 100\;\mu\text{m}$. **Correto.**
6. **[Exercício 1.2.2.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-02.dlt#L454-L476) (`exr:1-2-2-3` — Intermediário: Triângulo equilátero vs. quadrado de mesmo perímetro):**
   - Item (a): Lado $l = 6\text{ cm} \implies h = \frac{6\sqrt{3}}{2} = 3\sqrt{3}\text{ cm} \approx 5{,}196 \approx 5{,}20\text{ cm}$;
     $A_{\triangle} = \frac{6^2\sqrt{3}}{4} = 9\sqrt{3}\text{ cm}^2 \approx 9 \cdot 1{,}732 = 15{,}588 \approx 15{,}59\text{ cm}^2$. **Correto.**
   - Item (b): Perímetro $P = 3 \cdot 6 = 18\text{ cm}$. Quadrado: lado $l_q = \frac{18}{4} = 4{,}5\text{ cm}$; área $A_q = (4{,}5)^2 = 20{,}25\text{ cm}^2$.
     Comparação: $20{,}25 > 15{,}59$ (o quadrado encerra maior área com o mesmo contorno). **Correto.**
7. **[Exercício 1.2.2.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-02.dlt#L478-L512) (`exr:1-2-2-4` — Avançado: Pavimentação do plano e otimização de perímetro):**
   - Item (a): Condição de pavimentação por polígonos regulares: $\frac{360^\circ}{\alpha_n} = m \in \mathbb{N}$ com $m \ge 3$.
     - $n = 3$: $\alpha_3 = 60^\circ \implies m = 6$ (possível).
     - $n = 4$: $\alpha_4 = 90^\circ \implies m = 4$ (possível).
     - $n = 5$: $\alpha_5 = 108^\circ \implies 360/108 = 3{,}33$ (impossível).
     - $n = 6$: $\alpha_6 = 120^\circ \implies m = 3$ (possível).
     - $n \ge 7$: $\alpha_n > 120^\circ \implies 3\alpha_n > 360^\circ$ e $2\alpha_n < 360^\circ$, nenhum inteiro $m$ atende. Logo, apenas $n \in \{3, 4, 6\}$ pavimentam. **Correto.**
   - Item (b): Perímetro fixo $P = 24\;\mu\text{m}$:
     - Triângulo ($n = 3$): $l_3 = 8\;\mu\text{m} \implies A_3 = \frac{8^2\sqrt{3}}{4} = 16\sqrt{3} \approx 27{,}71\;\mu\text{m}^2$.
     - Quadrado ($n = 4$): $l_4 = 6\;\mu\text{m} \implies A_4 = 6^2 = 36\;\mu\text{m}^2$.
     - Hexágono ($n = 6$): $l_6 = 4\;\mu\text{m} \implies A_6 = \frac{3\sqrt{3}}{2} \cdot 4^2 = 24\sqrt{3} \approx 24 \cdot 1{,}732 = 41{,}568 \approx 41{,}57\;\mu\text{m}^2$.
     O hexágono maximiza a área interna ($41{,}57 > 36 > 27{,}71$), minimizando o custo metabólico de membrana por área útil. **Correto.**

---

### 3.3 Subtema 3: Relações Básicas de Ângulos e Orientação em V1 (`sec:1-2-3`)

1. **[Deduções e Demonstrações](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-02.dlt#L535-L583) (`prop:1-2-opv`, `thm:1-2-triangulo-angulos`):**
   - Ângulos opostos pelo vértice: $\alpha + \gamma = 180^\circ$ e $\beta + \gamma = 180^\circ \implies \alpha = \beta$. **Correto.**
   - Soma dos ângulos internos do triângulo: paralela ao lado $BC$ passando pelo vértice $A$ cria ângulos alternos internos congruentes a $\beta$ e $\gamma$, formando ângulo raso com $\alpha$: $\alpha + \beta + \gamma = 180^\circ$. **Correto.**
   - Ângulo externo: $e_\gamma + \gamma = 180^\circ \implies e_\gamma = \alpha + \beta$. **Correto.**
2. **[Exemplo 3.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-02.dlt#L601-L613) (`exm:1-2-v1` — Seletividade de orientação em V1):**
   - Eixo preferido $\theta_{\text{pref}} = 45^\circ$. Aplicação de $\Delta\theta = \min\bigl(|\theta - 45^\circ|,\; 180^\circ - |\theta - 45^\circ|\bigr)$:
     - Barra a $45^\circ$: $|45^\circ - 45^\circ| = 0^\circ \implies \Delta\theta = 0^\circ$ (resposta máxima).
     - Barra a $90^\circ$: $|90^\circ - 45^\circ| = 45^\circ \le 90^\circ \implies \Delta\theta = 45^\circ$.
     - Barra a $135^\circ$: $|135^\circ - 45^\circ| = 90^\circ \implies \Delta\theta = 90^\circ$ (perpendicular/ortogonal).
     - Barra a $0^\circ$: $|0^\circ - 45^\circ| = 45^\circ \le 90^\circ \implies \Delta\theta = 45^\circ$. **Correto.**
3. **[Exemplo 3.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-02.dlt#L615-L635) (`exm:1-2-tratos-paralelos` — Fibras paralelas, transversal e triângulo):**
   - Item (a): Ângulo colateral interno suplementar a $62^\circ$: $180^\circ - 62^\circ = 118^\circ$. **Correto.**
   - Item (b): Triângulo com ângulos $62^\circ$ e $48^\circ$:
     Terceiro interno: $\gamma = 180^\circ - (62^\circ + 48^\circ) = 180^\circ - 110^\circ = 70^\circ$.
     Ângulo externo correspondente: $e_\gamma = 62^\circ + 48^\circ = 110^\circ$ ($= 180^\circ - 70^\circ$). **Correto.**
4. **[Exercício 1.2.3.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-02.dlt#L646-L662) (`exr:1-2-3-1` — Básico: Complemento, suplemento e OPV):**
   - Item (a): Ângulo $37^\circ$: complemento $= 90^\circ - 37^\circ = 53^\circ$; suplemento $= 180^\circ - 37^\circ = 143^\circ$. **Correto.**
   - Item (b): Retas concorrentes com um ângulo de $124^\circ$: OPV $= 124^\circ$; dois adjacentes suplementares $= 180^\circ - 124^\circ = 56^\circ$ cada. Soma $= 124^\circ + 56^\circ + 124^\circ + 56^\circ = 360^\circ$. **Correto.**
5. **[Exercício 1.2.3.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-02.dlt#L664-L681) (`exr:1-2-3-2` — Básico: Diferença de orientação em V1 com suplementares):**
   - $\theta_{\text{pref}} = 20^\circ$:
     - Item (a): Barra a $160^\circ$: diferença bruta $|160^\circ - 20^\circ| = 140^\circ > 90^\circ \implies \Delta\theta = 180^\circ - 140^\circ = 40^\circ$. **Correto.**
     - Item (b): Barra a $110^\circ$: diferença bruta $|110^\circ - 20^\circ| = 90^\circ \implies \Delta\theta = 90^\circ$ (perpendicular). **Correto.**
6. **[Exercício 1.2.3.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-02.dlt#L683-L705) (`exr:1-2-3-3` — Intermediário: Paralelas, transversal e triângulo com incógnita):**
   - Item (a): Colaterais internos: $(3x + 15^\circ) + (7x + 15^\circ) = 180^\circ \implies 10x + 30^\circ = 180^\circ \implies 10x = 150^\circ \implies x = 15^\circ$.
     Ângulo agudo: $3(15^\circ) + 15^\circ = 60^\circ$; obtuso: $7(15^\circ) + 15^\circ = 120^\circ$. Conferência: $60^\circ + 120^\circ = 180^\circ$. **Correto.**
   - Item (b): Triângulo com ângulos $60^\circ$ e $45^\circ$:
     Interno no terceiro vértice: $\gamma = 180^\circ - (60^\circ + 45^\circ) = 180^\circ - 105^\circ = 75^\circ$.
     Externo: $e_\gamma = 60^\circ + 45^\circ = 105^\circ$ ($= 180^\circ - 75^\circ$). **Correto.**
7. **[Exercício 1.2.3.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-02.dlt#L707-L732) (`exr:1-2-3-4` — Avançado: Soma dos ângulos externos em polígonos):**
   - Item (a): Triângulo: $e_1 = \beta + \gamma$, $e_2 = \alpha + \gamma$, $e_3 = \alpha + \beta \implies \sum e_i = 2(\alpha + \beta + \gamma) = 2 \cdot 180^\circ = 360^\circ$. **Correto.**
   - Item (b): Polígono convexo de $n$ lados: $\sum_{k=1}^n e_k = \sum_{k=1}^n (180^\circ - \alpha_k) = n \cdot 180^\circ - (n - 2)\cdot 180^\circ = 2 \cdot 180^\circ = 360^\circ$. **Correto.**
   - Item (c): Hexágono regular ($n = 6$): $e = \frac{360^\circ}{6} = 60^\circ$. Conferência via ângulo interno: $180^\circ - 120^\circ = 60^\circ$. **Correto.**

---

## 4. Auditoria do Script de Figura Python

O script [barras-orientadas.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/fig/barras-orientadas.py) foi auditado linha a linha:

1. **Estrutura e Execução:** Código autocontido em Python 3, dependendo unicamente de `matplotlib` e `numpy`. Contém a diretiva obrigatória `plt.rcParams["svg.fonttype"] = "none"`, garantindo que os textos sejam exportados como elementos de texto vetorial (mantendo o SVG leve e nítido).
2. **Caminho e Destino:** Salva o arquivo em `conteudo/modulo-01/fig/barras-orientadas.svg` usando `Path(__file__).resolve().parent / "barras-orientadas.svg"`, exatamente onde a tag `<figure src="fig/barras-orientadas.svg">` do tema a localiza.
3. **Fidelidade Gráfica e Neurocientífica:**
   - O painel 1 ilustra a barra a $45^\circ$ (orientação preferida, com arco indicativo de $45^\circ$).
   - O painel 2 ilustra a barra a $90^\circ$ com eixo tracejado a $45^\circ$ e arco de $\Delta\theta = 45^\circ$.
   - O painel 3 ilustra a barra a $135^\circ$ com símbolo de ângulo reto ($90^\circ$) em relação ao eixo preferido (condição ortogonal).
   - O painel 4 ilustra a barra horizontal a $0^\circ$ com arco de $\Delta\theta = 45^\circ$.
   - As convenções visuais, cores e rótulos correspondem com rigor absoluto ao que o texto e a `<caption>` de [fig:1-2-barras](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-02.dlt#L597-L599) expõem.

---

## 5. Checklist de Conformidade Editorial e Pedagógica

| Critério avaliado | Status | Análise detalhada |
|---|:---:|---|
| **Dica e solução completa em cada exercício** | **OK** | Todos os 12 exercícios dispõem de `<hint><title>Ver dica</title>...</hint>` com orientação metodológica sem dar a resposta direta, e `<solution collapsible="true" collapsed="true">` estruturada passo a passo, incluindo etapas algébricas, conversões de unidade e conferência explícita. |
| **Pelo menos um exemplo biológico por seção** | **OK** | **Seção 1:** Microscopia óptica e escala de aumento ($k$ e $k^2$); contagem celular em câmara de Neubauer; microscopia eletrônica de fenda sináptica química ($\approx 20\text{ nm}$); lei de escala alométrica de superfície/volume ($A/V = 3/r$) e limite de difusão.<br>**Seção 2:** Decomposição geométrica de corte histológico plano; mosaico epitelial e empacotamento hexagonal; posicionamento euclidiano de microeletrodo de registro neural.<br>**Seção 3:** Seletividade de orientação de barras em células simples de V1 (Hubel & Wiesel); organização de feixes e tratos de fibras nervosas paralelas em cortes cerebrais; contorno poligonal de células biológicas. |
| **Afirmações de neurociência de livro-texto** | **OK** | Seletividade de orientação em V1, trabalhos clássicos de Hubel & Wiesel (1959, 1962; Prêmio Nobel de 1981), distinção neurofisiológica entre direção ($0^\circ$ a $360^\circ$) e orientação ($0^\circ$ a $180^\circ$), dimensões da fenda sináptica ($\approx 20\text{ nm}$) e profundidades típicas de eletrodos em micrômetros seguem fielmente Kandel et al. (*Principles of Neural Science*, caps. 10 e 25) e Dayan & Abbott (*Theoretical Neuroscience*, cap. 1). |
| **Sequenciamento pedagógico de conceitos** | **OK** | A progressão inicia nos elementos primitivos da reta e ângulos básicos, avança para conversão de unidades e áreas clássicas, introduz Pitágoras e triangulação de polígonos, e culmina nas propriedades de paralelas e soma de ângulos em triângulos. Onde uma propriedade de soma de ângulos é usada antes da demonstração formal (na prova de Pitágoras e polígonos), há aviso explícito e link cruzado apontando para o Subtema 3. |
| **Código Python e figuras executáveis** | **OK** | O script [barras-orientadas.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/fig/barras-orientadas.py) é executável, não apresenta erros de sintaxe ou de importação, e produz com fidelidade o arquivo SVG referenciado. O arquivo `.dlt` não contém blocos de código desnecessários (em conformidade com a diretriz de reservar código aos módulos aplicados). |
| **Consistência de notação matemática** | **OK** | Uso padronizado de vírgula decimal na prosa ($0{,}5$, $1{,}5$, $166{,}3$), notação científica no padrão $c \times 10^k$, símbolos de grau ($^\circ$), medidas físicas com espaço fino (`\text{ mm}`, `\;\mu\text{m}`, `\text{ nm}`), notação geométrica clássica ($\overline{AB}$, $AB$, $\alpha_n$, $S_i$) e delimitadores matemáticos KaTeX sem quebras inválidas. |
| **Cobertura de todos os subtemas pedidos** | **OK** | Cobre integralmente os 3 subtemas exigidos no plano curricular do Módulo 1: (1) *Introdução* (com semelhança e escala em microscopia); (2) *Áreas e ângulos de figuras planas clássicas* (com corte de tecido, soma de áreas celulares e Pitágoras); (3) *Relações básicas de ângulos* (com orientação de barras em campos receptivos de V1, Hubel e Wiesel). |
| **Tamanho dentro do padrão** | **OK** | A aula totaliza aproximadamente 4.350 palavras, posicionando-se perfeitamente no intervalo estipulado de 2.500 a 5.000 palavras para temas com três subtemas. |
| **Conformidade técnica Delta v0.6.0** | **OK** | XML estrito com todos os atributos explicitamente valorados (`collapsible="true" collapsed="true"`, `numbered="false"`), identificadores em formato padronizado sem caracteres acentuados, uso correto de `<intro>`, `<eyebrow>`, `<remark>`, `<proof>`, metadados com link ao guia (`<link to="../../index.html#tema-1-2">`) e sumário flutuante do projeto (`<toc scope="project" depth="1"/>`). |

---

## 6. Contas Conferidas

Abaixo estão listados todos os identificadores de exemplos teóricos, demonstrações e exercícios cujas contas foram integralmente recalculadas e consideradas **corretas**:

### Exemplos e Demonstrações
- `prop:1-2-semelhanca` (lei de escala para comprimentos $k$ e áreas $k^2$)
- `exm:1-2-microscopia` (aumento de microscopia óptica, diâmetro celular e barra de escala)
- `exm:1-2-neubauer` (perímetro e conversão de área em câmara de contagem)
- `thm:1-2-pitagoras` (dedução algébrica via quadrado $(a+b)^2$)
- `prop:1-2-equilatero-hexagono` (altura e área do triângulo equilátero e do hexágono regular)
- `prop:1-2-soma-angulos-poligono` (fórmula $(n-2)\cdot 180^\circ$ e ângulo regular)
- `exm:1-2-tecido` (decomposição de corte histológico: triângulo, quadrado e trapézio)
- `exm:1-2-epitelio` (área da célula epitelial hexagonal e monocamada com 500 células)
- `prop:1-2-opv` (demonstração de congruência de ângulos opostos pelo vértice)
- `thm:1-2-triangulo-angulos` (soma dos ângulos internos e teorema do ângulo externo)
- `exm:1-2-v1` (diferença de orientação $\Delta\theta$ para barras a $45^\circ$, $90^\circ$, $135^\circ$ e $0^\circ$)
- `exm:1-2-tratos-paralelos` (fibras nervosas paralelas, ângulo colateral e terceiro ângulo de triângulo)

### Exercícios
- `exr:1-2-1-1` (classificação de ângulos e perímetro do pentágono: $18\text{ cm} = 180\text{ mm}$)
- `exr:1-2-1-2` (área retangular de campo: $3{,}0\text{ mm}^2 = 3{,}0 \times 10^6\;\mu\text{m}^2 = 0{,}03\text{ cm}^2$)
- `exr:1-2-1-3` (micrografia eletrônica: $k = 200\,000\times$, fenda $= 20\text{ nm}$, área $= 4 \times 10^{10}\times$)
- `exr:1-2-1-4` (razão $A/V = 3/r$, comparação bactéria vs. eucarioto e limite de difusão)
- `exr:1-2-2-1` (placa de Petri: $C = 10\pi\text{ cm}$, $A = 25\pi\text{ cm}^2$; octógono: $S_i = 1\,080^\circ$, $\alpha_8 = 135^\circ$)
- `exr:1-2-2-2` (distância de microeletrodo via Pitágoras: $\sqrt{80^2 + 60^2} = 100\;\mu\text{m}$)
- `exr:1-2-2-3` (triângulo equilátero vs. quadrado de mesmo perímetro $18\text{ cm}$: $15{,}59\text{ cm}^2$ vs. $20{,}25\text{ cm}^2$)
- `exr:1-2-2-4` (pavimentação por polígonos regulares $n=3,4,6$ e maximização de área hexagonal com $P = 24\;\mu\text{m}$)
- `exr:1-2-3-1` (complemento $53^\circ$, suplemento $143^\circ$ de $37^\circ$; ângulos de retas concorrentes $124^\circ$ e $56^\circ$)
- `exr:1-2-3-2` (diferença de orientação em V1 para $\theta_{\text{pref}} = 20^\circ$: $40^\circ$ e $90^\circ$)
- `exr:1-2-3-3` (equação de colaterais internos $x = 15^\circ$, ângulos $60^\circ$ e $120^\circ$; triângulo com $75^\circ$ e $105^\circ$)
- `exr:1-2-3-4` (soma de ângulos externos de triângulo e polígono de $n$ lados $= 360^\circ$; giro no hexágono $= 60^\circ$)
