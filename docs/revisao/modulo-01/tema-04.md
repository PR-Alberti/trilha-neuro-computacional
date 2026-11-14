# Relatório de Revisão Técnica — Módulo 01 · Tema 04 (Trigonometria)

- **Arquivo revisado:** [tema-04.dlt](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-04.dlt)
- **Script de figura revisado:** [senoides-eeg.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/fig/senoides-eeg.py) e figura gerada [senoides-eeg.svg](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/fig/senoides-eeg.svg)
- **Documentos de referência:** [PADRAO-AULAS.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/PADRAO-AULAS.md) e [DELTA-COLA.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/DELTA-COLA.md)
- **Data da revisão:** 14 de novembro de 2026
- **Perfil do revisor:** Matemático, Neurocientista Computacional e Professor de Alunos de Ciências Biológicas

---

## 1. Veredito

**CORRIGIR**

A aula [tema-04.dlt](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-04.dlt) apresenta nível didático, matemático e neurobiológico primoroso. Todos os 12 exemplos e 16 exercícios propostos tiveram suas contas integralmente recalculadas passo a passo, confirmando **100% de exatidão analítica e numérica** (sem qualquer divergência de cálculo). A contextualização biológica é autêntica e fundamentada na literatura clássica (*Dayan & Abbott*, *Kandel et al.*, *Hubel & Wiesel*, *Georgopoulos et al.*, *Berger*), os scripts de figura atendem estritamente às especificações gráficas e a estrutura respeita os padrões do Delta v0.6.0.

No entanto, em observância ao princípio de **Exatidão Inegociável** estipulado no contrato editorial ([PADRAO-AULAS.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/PADRAO-AULAS.md)), o parecer formal é de **CORRIGIR** devido a dois apontamentos centrais:
1. **Erro factual de referência cruzada** na Seção 1 (linha ~94), que atribui a Álgebra Linear ao "Módulo 3" da trilha, quando na arquitetura curricular oficial ela constitui o **Módulo 5** (o Módulo 3 é *Cálculo Multivariável*);
2. **Conceito utilizado antes de ser apresentado** na Seção 4 (linha ~771), onde a função secante ($\sec\theta$) é introduzida na identidade fundamental sem que tenha sido definida em nenhuma seção prévia da aula.

Ambas as correções são cirúrgicas e pontuais (juntamente com pequenas melhorias pedagógicas e de formato tabuladas abaixo), não demandando reestruturação da aula. Uma vez aplicados esses ajustes pontuais pelo autor, a aula estará plenamente apta à aprovação e compilação definitiva.

---

## 2. Tabela de Problemas e Observações

| Severidade | Local | Trecho | Correção sugerida |
|---|---|---|---|
| Erro factual | Seção 1 (`sec:1-4-1`), linha ~94 | `que usaremos na Geometria Analítica (Tema 1.5) e na Álgebra Linear (Módulo 3).` | Álgebra Linear é o **Módulo 5** da trilha (o Módulo 3 é *Cálculo Multivariável*, conforme o `index.html`). Corrigir para: `que usaremos na Geometria Analítica (Tema 1.5) e na Álgebra Linear (Módulo 5).` |
| Pedagógico | Seção 4 (`sec:1-4-4`), `thm:1-4-pitagoras-trig`, linha ~771 (e linha ~777 na demonstração e linha ~977 no Resumo) | `$$1 + \tan^2\theta = \frac{1}{\cos^2\theta} = \sec^2\theta.$$` | A função secante ($\sec\theta$) aparece abruptamente na identidade sem que tenha sido definida anteriormente (a Seção 1 introduziu apenas seno, cosseno e tangente). Para alunos de Biologia sem formação prévia em cálculo, a notação $\sec\theta$ causa estranheza. Sugere-se adicionar uma nota explicativa ou nota de margem (`<sidenote>A função secante é definida como o inverso do cosseno: $\sec\theta = \frac{1}{\cos\theta}$.</sidenote>`) ou grafar a identidade primordialmente como $1 + \tan^2\theta = \frac{1}{\cos^2\theta}$. |
| Pedagógico | Seção 4 (`sec:1-4-4`), `proof of="thm:1-4-soma-arcos"`, linha ~794 | `Considere primeiro o caso $0 < \alpha, \beta$ com $\alpha + \beta < \pi/2$.` | A escrita `$0 < \alpha, \beta$` é uma elipse informal que pode confundir leitores iniciantes habituados a inequações unívocas. Sugere-se explicitar as desigualdades: `Considere primeiro o caso com $0 < \alpha < \pi/2$ e $0 < \beta < \pi/2$ tais que $\alpha + \beta < \pi/2$.` |
| Formato | Seção 1 (`sec:1-4-1`), `def:1-4-razoes-triangulo`, linha ~51 e Seção 2 (`sec:1-4-2`), linhas ~285–288 | `($0^\circ < \theta < 90^\circ$)`, `($0 < \theta < \pi/2$)`, `$x < 0, y > 0$` | Embora estejam inseridos dentro de delimitadores matemáticos `$...$`, para prevenir potenciais alertas de falso positivo em validadores estritos de XML ou linters de KaTeX que possam interceptar caracteres `<` e `>` soltos no código-fonte, sugere-se usar comandos nominais LaTeX (`\lt` e `\gt`) ou escrever por extenso quando fora de fórmulas display: `($0^\circ \lt \theta \lt 90^\circ$)`, etc. |
| Pedagógico | Seção 3 (`sec:1-4-3`), `exm:1-4-orientacao-barra`, linhas ~624–626 e `exr:1-4-3-3`, linha ~709 | `$(\Delta x, \Delta y) = (2\sqrt{3},\, 2)\text{ cm}$`, `$\mathbf{u} = (-3,\, 3\sqrt{3})$` | Para assegurar consistência pedagógica com estudantes de biologia habituados a números decimais com vírgula e manter a convenção das demais aulas da trilha, recomenda-se adotar ponto e vírgula como separador canônico em pares ordenados: `$(2\sqrt{3};\, 2)\text{ cm}$`, `$\mathbf{u} = (-3;\, 3\sqrt{3})$`. |

---

## 3. Auditoria Editorial, Pedagógica e Biofísica

A auditoria verificou sistematicamente todos os requisitos estipulados em [PADRAO-AULAS.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/PADRAO-AULAS.md) e [DELTA-COLA.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/DELTA-COLA.md):

### 3.1 Cobertura Temática e Estrutura dos Subtemas
- **Subtema 1 (`sec:1-4-1`) — Introdução de seno, cosseno e tangente:** Cobertura completa das definições no triângulo retângulo, ângulos complementares, valores exatos dos ângulos notáveis ($30^\circ$, $45^\circ$, $60^\circ$) deduzidos geometricamente com demonstração recolhível, decomposição de segmentos em componentes ortogonais ($\Delta x = L\cos\theta$, $\Delta y = L\operatorname{sen}\theta$) e formulação do ângulo visual ($\tan(\theta/2) = s/(2d)$).
- **Subtema 2 (`sec:1-4-2`) — Círculo trigonométrico:** Definição rigorosa de radianos como razão arco/raio ($\theta = s/R$), equivalência $\pi\text{ rad} = 180^\circ$, extensão das funções ao círculo unitário $x^2 + y^2 = 1$, análise de sinais nos quatro quadrantes, propriedades formais (domínio, imagem, periodicidade $2\pi$ e paridade), equação sinusoidal geral $A\operatorname{sen}(2\pi f t + \varphi) = A\operatorname{sen}(\omega t + \varphi)$ com interpretação física e gráfica de todos os parâmetros, caracterização das cinco bandas clássicas do EEG (delta, teta, alfa, beta e gama) e modelagem de ritmos circadianos (mesor, amplitude e pico).
- **Subtema 3 (`sec:1-4-3`) — Funções trigonométricas inversas:** Conceituação do teste da reta horizontal e necessidade de restrição de domínio, formalização de $\operatorname{arcsen}$, $\arccos$ e $\arctan$ com domínios e imagens estritos, regras e armadilhas de cancelamento de fora para dentro e de dentro para fora, distinção crucial entre orientação de estímulo estático ($[0^\circ, 180^\circ)$) e direção de movimento ($[0^\circ, 360^\circ)$), perda de quadrante por $\arctan(\Delta y/\Delta x)$ e introdução conceitual de `atan2`, e regra psicofísica dos $57\text{ cm}$ para calibração de telas.
- **Subtema 4 (`sec:1-4-4`) — Relações e identidades fundamentais:** Relação fundamental $\operatorname{sen}^2\theta + \cos^2\theta = 1$ e sua forma tangente/secante, identidades de soma e diferença de arcos com demonstração geométrica completa, fórmulas de arco duplo, defasagem de quarto de ciclo entre seno e cosseno ($\cos(\theta - \pi/2) = \operatorname{sen}\theta$), combinação linear de senoides de mesma frequência $a\operatorname{sen}(\omega t) + b\cos(\omega t) = R\operatorname{sen}(\omega t + \varphi)$ com ponte para a análise de Fourier, e curva de sintonia de cosseno de Georgopoulos (1982) no córtex motor com expansão cartesiana.
- **Fechamento:** Seção "Resumo" (`sec:1-4-resumo`) com 9 itens estruturados destacando fórmulas-chave e armadilhas comuns, seguida da seção "Para ir além" (`sec:1-4-alem`), que aponta os materiais nucleares (Khan Academy Pré-Cálculo), aprofundamento em vídeo, *drill* de IA e o projeto final do módulo.

### 3.2 Contextualização Biológica e Neurociência de Livro-Texto
Cada uma das seções apresenta múltiplos exemplos aplicados com parâmetros biofísicos realistas de livro-texto:
- **Seção 1:** Campo receptivo visual em V1 com barra luminosa orientada ($L = 6{,}0\text{ cm}$, $\theta = 30^\circ$ e $60^\circ$); cálculo do ângulo visual de estímulos na retina e dedução da regra prática do polegar estendido cobrindo $\approx 2^\circ$; inserção inclinada de microeletrodo intracortical a $45^\circ$ para desvio de vaso pial com profundidade $\Delta y = 1{,}2\text{ mm}$ e percurso $1{,}2\sqrt{2}\text{ mm}$.
- **Seção 2:** Registro clássico de ritmo alfa occipital por Hans Berger (1929) com amplitude $20\;\mu\text{V}$, frequência $10\text{ Hz}$, janela de aquisição compatível com o tempo de repetição de fMRI ($\text{TR} = 2\text{ s}$); modelagem circadiana da temperatura corporal central humana (mesor $M = 36{,}8\,^\circ\text{C}$, amplitude $A = 0{,}4\,^\circ\text{C}$, pico às $17\text{ h}$ e nadir às $5\text{ h}$ da madrugada); bandas do EEG de livro-texto (delta $0{,}5\text{–}4\text{ Hz}$, teta $4\text{–}8\text{ Hz}$, alfa $8\text{–}13\text{ Hz}$, beta $13\text{–}30\text{ Hz}$, gama $>30\text{ Hz}$); deslocamento circadiano por *jet lag*.
- **Seção 3:** Recuperação da orientação de barras visuais em V1 vs. direção de deslocamento animal no plano; dedução da regra laboratorial dos $57\text{ cm}$ em psicofísica visual (onde $1\text{ cm}$ no centro da tela subtende exatamente $1^\circ$ de ângulo visual); decodificação de múltiplos horários do dia a partir de registros de temperatura circadiana via $\arccos$.
- **Seção 4:** Curva de sintonia de cosseno (*cosine tuning curve*) no córtex motor primário (M1) descrita por Georgopoulos et al. (1982) ($f(s) = r_0 + (r_{\text{max}} - r_0)\cos(s - s_{\text{pref}})$); soma e interferência de fase (construtiva vs. destrutiva) de correntes sinápticas oscilatórias a $10\text{ Hz}$; decomposição da sintonia direcional em coordenadas cartesianas ($c_x\cos s + c_y\operatorname{sen} s$), conectando diretamente à regressão linear e modelos de *encoding*.

### 3.3 Verificação dos Scripts e Figuras
- **Script [senoides-eeg.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/fig/senoides-eeg.py):**
  - Autocontido, escrito em Python padrão com `numpy`, `matplotlib` e `pathlib`;
  - Configura `plt.rcParams["svg.fonttype"] = "none"` na linha 7, garantindo exportação vetorial de fontes limpa e leve;
  - Gera 4 subplots empilhados compartilhando eixos para as frequências representativas: teta ($6\text{ Hz}$), alfa ($10\text{ Hz}$), beta ($20\text{ Hz}$) e gama ($40\text{ Hz}$);
  - Formata o eixo temporal com vírgula decimal (`replace(".", ",")`), rótulos em português ("Tempo $t$ (s)", "Amplitude normalizada") e salva [senoides-eeg.svg](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/fig/senoides-eeg.svg) com fundo transparente;
  - O arquivo SVG gerado existe em disco e coincide rigorosamente com o texto e com a legenda do elemento `<figure src="fig/senoides-eeg.svg" id="fig:1-4-senoides-eeg">`.

### 3.4 Progressão Didática e Notação
- **Pré-requisitos:** Respeita a sequência pedagógica, retomando conceitos de Álgebra (Tema 1.1), Geometria (Tema 1.2) e Funções (Tema 1.3).
- **Sem conceitos anacrônicos desavisados:** Menções à transformada de Fourier e à Álgebra Linear são explicitamente demarcadas com avisos de continuidade ("que veremos mais adiante na trilha"). A única ressalva refere-se à função secante na linha ~771, que não foi formalizada previamente.
- **Notação consistente:**
  - Decimais grafados com vírgula no texto e com chaves na matemática (`$0{,}5$`, `$1{,}2\text{ mm}$`, `$36{,}8\,^\circ\text{C}$`);
  - Vetores em negrito minúsculo ($\mathbf{u}$, $\mathbf{v}$);
  - Rótulos trigonométricos padronizados em português ($\operatorname{sen}\theta$, $\operatorname{arcsen} x$), com nota explícita sobre a notação internacional em inglês (`sin` e `asin`) utilizada em calculadoras e em Python.
- **Extensão do texto:** O documento possui 999 linhas e cerca de 4.400 palavras, enquadrando-se com folga na meta estipulada de 2.500 a 5.000 palavras por tema.
- **Exercícios:** Todos os 16 exercícios contam com classificação graduada ("Básico", "Intermediário", "Avançado"), gatilho `<hint>` com dica e `<solution collapsible="true" collapsed="true">` completa, apresentando raciocínio detalhado, memória algébrica e interpretação biológica.

---

## 4. Memória de Cálculo e Auditoria Passo a Passo

Todas as contas foram integralmente recalculadas. Como **nenhuma divergência numérica foi encontrada** nos exemplos e soluções originais, apresentamos abaixo o registro formal da memória de cálculo de cada item auditado.

### 4.1 Subtema 1: Introdução de seno, cosseno e tangente (`sec:1-4-1`)

1. **[Exemplo 1.4.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-04.dlt#L96-L119) (`exm:1-4-barra-v1`):**
   - $L = 6{,}0\text{ cm}$, $\theta = 30^\circ$.
   - Item (a): $\Delta x = 6{,}0 \cdot \cos 30^\circ = 6{,}0 \cdot \frac{\sqrt{3}}{2} = 3\sqrt{3} \approx 5{,}196 \approx 5{,}20\text{ cm}$. **Correto.**
     $\Delta y = 6{,}0 \cdot \operatorname{sen} 30^\circ = 6{,}0 \cdot \frac{1}{2} = 3{,}00\text{ cm}$. **Correto.**
   - Item (b): $(\Delta x)^2 + (\Delta y)^2 = (3\sqrt{3})^2 + 3^2 = 27 + 9 = 36 = 6{,}0^2$. Recupera $\sqrt{36} = 6{,}0\text{ cm}$. **Correto.**
   - Item (c): Para $\theta = 60^\circ$: $\Delta x = 6{,}0 \cdot \frac{1}{2} = 3{,}00\text{ cm}$; $\Delta y = 6{,}0 \cdot \frac{\sqrt{3}}{2} = 3\sqrt{3} \approx 5{,}20\text{ cm}$. **Correto.**
2. **[Exemplo 1.4.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-04.dlt#L123-L144) (`exm:1-4-angulo-visual`):**
   - Relação: $\tan(\theta/2) = \frac{s}{2d}$.
   - Item (a): $d = 30\text{ cm}$, $\theta = 60^\circ \implies \theta/2 = 30^\circ$.
     $\tan 30^\circ = \frac{\sqrt{3}}{3} = \frac{s}{60} \implies s = \frac{60\sqrt{3}}{3} = 20\sqrt{3} \approx 34{,}64 \approx 34{,}6\text{ cm}$. **Correto.**
   - Item (b): $s = 2{,}1\text{ cm}$, $d = 60\text{ cm}$.
     $\tan(\theta/2) = \frac{2{,}1}{2 \cdot 60} = \frac{2{,}1}{120} = 0{,}0175$.
     Como $\tan 1^\circ \approx 0{,}017455 \approx 0{,}0175$, temos $\theta/2 \approx 1^\circ \implies \theta \approx 2^\circ$. **Correto.**
3. **[Exemplo 1.4.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-04.dlt#L146-L155) (`exm:1-4-microeletrodo`):**
   - $\theta = 45^\circ$, profundidade vertical $\Delta y = 1{,}2\text{ mm}$ (cateto oposto).
   - Trajetória inclinada $L$ (hipotenusa): $L = \frac{\Delta y}{\operatorname{sen} 45^\circ} = \frac{1{,}2}{\sqrt{2}/2} = \frac{2{,}4}{\sqrt{2}} = 1{,}2\sqrt{2} \approx 1{,}697 \approx 1{,}70\text{ mm}$. **Correto.**
   - Deslocamento horizontal $\Delta x$: $\tan 45^\circ = 1 = \frac{\Delta y}{\Delta x} \implies \Delta x = 1{,}2\text{ mm}$. **Correto.**
   - Conferência: $(\Delta x)^2 + (\Delta y)^2 = 1{,}2^2 + 1{,}2^2 = 2{,}88 = (1{,}2\sqrt{2})^2$. **Correto.**
4. **[Exercício 1.4.1.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-04.dlt#L165-L176) (`exr:1-4-1-1`):**
   - Catetos $6\text{ cm}$ e $8\text{ cm}$. Hipotenusa $h = \sqrt{6^2 + 8^2} = \sqrt{36 + 64} = \sqrt{100} = 10\text{ cm}$.
   - Menor ângulo $\theta$ (oposto a $6\text{ cm}$): $\operatorname{sen}\theta = \frac{6}{10} = 0{,}6$; $\cos\theta = \frac{8}{10} = 0{,}8$; $\tan\theta = \frac{6}{8} = 0{,}75$.
   - Conferência: $\frac{0{,}6}{0{,}8} = 0{,}75$. **Correto.**
5. **[Exercício 1.4.1.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-04.dlt#L178-L188) (`exr:1-4-1-2`):**
   - $L = 8{,}0\text{ cm}$, $\theta = 60^\circ$.
   - $\Delta x = 8{,}0 \cdot \cos 60^\circ = 8{,}0 \cdot \frac{1}{2} = 4{,}00\text{ cm}$.
   - $\Delta y = 8{,}0 \cdot \operatorname{sen} 60^\circ = 8{,}0 \cdot \frac{\sqrt{3}}{2} = 4\sqrt{3} \approx 4 \cdot 1{,}732 = 6{,}928 \approx 6{,}93\text{ cm}$.
   - Conferência: $4^2 + (4\sqrt{3})^2 = 16 + 48 = 64 = 8{,}0^2$. **Correto.**
6. **[Exercício 1.4.1.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-04.dlt#L190-L209) (`exr:1-4-1-3`):**
   - $\theta = 30^\circ$, $L = 2{,}0\text{ mm}$.
   - Item (a): $\Delta y = 2{,}0 \cdot \operatorname{sen} 30^\circ = 2{,}0 \cdot \frac{1}{2} = 1{,}0\text{ mm}$. **Correto.**
   - Item (b): $\Delta x = 2{,}0 \cdot \cos 30^\circ = 2{,}0 \cdot \frac{\sqrt{3}}{2} = \sqrt{3} \approx 1{,}73\text{ mm}$. **Correto.**
   - Conferência: $1{,}0^2 + (\sqrt{3})^2 = 1 + 3 = 4 = 2{,}0^2$. **Correto.**
7. **[Exercício 1.4.1.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-04.dlt#L211-L232) (`exr:1-4-1-4`):**
   - $d = 40\text{ cm}$.
   - Item (a): $\theta_1 = 60^\circ \implies \theta_1/2 = 30^\circ$. $s_1 = 2 \cdot 40 \cdot \tan 30^\circ = 80 \cdot \frac{\sqrt{3}}{3} \approx 46{,}19 \approx 46{,}2\text{ cm}$. **Correto.**
   - Item (b): $\theta_2 = 90^\circ \implies \theta_2/2 = 45^\circ$. $s_2 = 2 \cdot 40 \cdot \tan 45^\circ = 80 \cdot 1 = 80{,}0\text{ cm}$. **Correto.**
   - Item (c): $1{,}5 \cdot s_1 = 1{,}5 \cdot 46{,}2 = 69{,}3\text{ cm} \ne 80{,}0\text{ cm}$, justificado pela geometria plana do monitor e pela não linearidade estrita da função tangente. **Correto.**

---

### 4.2 Subtema 2: Círculo trigonométrico (`sec:1-4-2`)

1. **[Exemplo 1.4.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-04.dlt#L336-L351) (`exm:1-4-circulo-valores`):**
   - Item (a): $\theta_1 = \frac{5\pi}{6} = 150^\circ$ (2º quadrante).
     $\cos(5\pi/6) = -\cos(\pi/6) = -\frac{\sqrt{3}}{2}$; $\operatorname{sen}(5\pi/6) = \operatorname{sen}(\pi/6) = \frac{1}{2}$; $\tan(5\pi/6) = \frac{1/2}{-\sqrt{3}/2} = -\frac{\sqrt{3}}{3}$. **Correto.**
   - Item (b): $\theta_2 = -\frac{\pi}{4} = -45^\circ$ (4º quadrante).
     $\cos(-\pi/4) = \cos(\pi/4) = \frac{\sqrt{2}}{2}$; $\operatorname{sen}(-\pi/4) = -\operatorname{sen}(\pi/4) = -\frac{\sqrt{2}}{2}$; $\tan(-\pi/4) = -1$. **Correto.**
2. **[Exemplo 1.4.5](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-04.dlt#L368-L406) (`exm:1-4-eeg-alfa`):**
   - $v(t) = 20 \operatorname{sen}(20\pi t)\;\mu\text{V}$.
   - Item (a): Amplitude $A = 20\;\mu\text{V}$; fase $\varphi = 0$; $\omega = 20\pi \approx 62{,}83\text{ rad/s}$; $f = \frac{20\pi}{2\pi} = 10\text{ Hz}$; $T = \frac{1}{10} = 0{,}1\text{ s} = 100\text{ ms}$. **Correto.**
   - Item (b): Em $\Delta t = 2{,}0\text{ s}$: $f \cdot \Delta t = 10 \cdot 2{,}0 = 20\text{ ciclos}$. Em $\Delta t = 250\text{ ms} = 0{,}25\text{ s}$: $10 \cdot 0{,}25 = 2{,}5\text{ ciclos}$. **Correto.**
   - Item (c):
     - $t_1 = 0{,}025\text{ s}$: argumento $20\pi \cdot 0{,}025 = 0{,}5\pi = \frac{\pi}{2}\text{ rad} = 90^\circ \implies v(0{,}025) = 20 \cdot 1 = +20\;\mu\text{V}$. **Correto.**
     - $t_2 = 0{,}075\text{ s}$: argumento $20\pi \cdot 0{,}075 = 1{,}5\pi = \frac{3\pi}{2}\text{ rad} = 270^\circ \implies v(0{,}075) = 20 \cdot (-1) = -20\;\mu\text{V}$. **Correto.**
3. **[Exemplo 1.4.6](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-04.dlt#L408-L441) (`exm:1-4-circadiano`):**
   - $y(t) = 36{,}8 + 0{,}4\cos\left(\frac{2\pi(t - 17)}{24}\right)$.
   - Item (a):
     - Máximo em $t = 17\text{ h}$: $y_{\text{max}} = 36{,}8 + 0{,}4 = 37{,}2\,^\circ\text{C}$. **Correto.**
     - Mínimo $12\text{ h}$ após/antes do pico ($t = 17 - 12 = 5\text{ h}$): $y_{\text{min}} = 36{,}8 - 0{,}4 = 36{,}4\,^\circ\text{C}$. **Correto.**
   - Item (b):
     - $t = 9\text{ h}$: argumento $\frac{2\pi(9-17)}{24} = -\frac{16\pi}{24} = -\frac{2\pi}{3}$. $\cos(-2\pi/3) = \cos(2\pi/3) = -0{,}5 \implies y(9) = 36{,}8 + 0{,}4(-0{,}5) = 36{,}6\,^\circ\text{C}$. **Correto.**
     - $t = 21\text{ h}$: argumento $\frac{2\pi(21-17)}{24} = \frac{8\pi}{24} = \frac{\pi}{3}$. $\cos(\pi/3) = 0{,}5 \implies y(21) = 36{,}8 + 0{,}4(0{,}5) = 37{,}0\,^\circ\text{C}$. **Correto.**
4. **[Exercício 1.4.2.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-04.dlt#L451-L469) (`exr:1-4-2-1`):**
   - $\alpha = 135^\circ \cdot \frac{\pi}{180^\circ} = \frac{3\pi}{4}\text{ rad}$ (2º quadrante). $\cos(3\pi/4) = -\frac{\sqrt{2}}{2}$; $\operatorname{sen}(3\pi/4) = \frac{\sqrt{2}}{2}$. **Correto.**
   - $\beta = 300^\circ \cdot \frac{\pi}{180^\circ} = \frac{5\pi}{3}\text{ rad}$ (4º quadrante). $\cos(5\pi/3) = \cos(\pi/3) = \frac{1}{2}$; $\operatorname{sen}(5\pi/3) = -\operatorname{sen}(\pi/3) = -\frac{\sqrt{3}}{2}$. **Correto.**
5. **[Exercício 1.4.2.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-04.dlt#L471-L492) (`exr:1-4-2-2`):**
   - Item (a): $f = 6\text{ Hz} \implies T = \frac{1}{6}\text{ s} \approx 0{,}1667\text{ s} \approx 166{,}7\text{ ms}$. Ciclos em $1{,}5\text{ s}$: $6 \cdot 1{,}5 = 9\text{ ciclos}$. **Correto.**
   - Item (b): $f = 40\text{ Hz} \implies T = \frac{1}{40}\text{ s} = 0{,}025\text{ s} = 25\text{ ms}$; $\omega = 2\pi \cdot 40 = 80\pi \approx 251{,}3\text{ rad/s}$. **Correto.**
6. **[Exercício 1.4.2.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-04.dlt#L494-L524) (`exr:1-4-2-3`):**
   - $v(t) = 12\operatorname{sen}(40\pi t - \pi/2)\;\mu\text{V}$.
   - Item (a): $A = 12\;\mu\text{V}$; $\omega = 40\pi\text{ rad/s}$; $f = \frac{40\pi}{2\pi} = 20\text{ Hz}$; $T = \frac{1}{20}\text{ s} = 50\text{ ms}$. **Correto.**
   - Item (b): $40\pi t - \frac{\pi}{2} = 40\pi\left(t - \frac{1}{80}\right) = 40\pi(t - 0{,}0125)$. Deslocamento de $0{,}0125\text{ s} = 12{,}5\text{ ms}$ para a direita (atraso de $T/4$). **Correto.**
   - Item (c): $v(0) = 12\operatorname{sen}(-\pi/2) = -12\;\mu\text{V}$; $v(0{,}025) = 12\operatorname{sen}(\pi - \pi/2) = 12\operatorname{sen}(\pi/2) = +12\;\mu\text{V}$. **Correto.**
7. **[Exercício 1.4.2.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-04.dlt#L526-L546) (`exr:1-4-2-4`):**
   - $t_{\text{pico}} = 23\text{ h} \implies y_{\text{nova}}(t) = 36{,}8 + 0{,}4\cos\left(\frac{2\pi(t - 23)}{24}\right)$.
   - Item (a): Mínimo em $t = 23 - 12 = 11\text{ h}$ da manhã ($36{,}4\,^\circ\text{C}$). **Correto.**
   - Item (b): Antes: $y(5) = 36{,}4\,^\circ\text{C}$ (mínimo). Depois: argumento $\frac{2\pi(5-23)}{24} = -\frac{36\pi}{24} = -\frac{3\pi}{2}$. Como $\cos(-3\pi/2) = 0$, $y_{\text{nova}}(5) = 36{,}8\,^\circ\text{C}$ (subiu $0{,}4\,^\circ\text{C}$, atingindo o mesor). **Correto.**

---

### 4.3 Subtema 3: Funções trigonométricas inversas (`sec:1-4-3`)

1. **[Exemplo 1.4.7](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-04.dlt#L593-L616) (`exm:1-4-cancelamento-exato`):**
   - Item (a): $\operatorname{arcsen}(-\sqrt{3}/2) = -\frac{\pi}{3}\text{ rad}$ (imagem $[-\pi/2, \pi/2]$); $\arccos(-1/2) = \frac{2\pi}{3}\text{ rad}$ (imagem $[0, \pi]$). **Correto.**
   - Item (b): $\operatorname{sen}(5\pi/6) = 1/2 \implies \operatorname{arcsen}(1/2) = \frac{\pi}{6}$; $\cos(3\pi/2) = 0 \implies \arccos(0) = \frac{\pi}{2}$. **Correto.**
2. **[Exemplo 1.4.8](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-04.dlt#L618-L641) (`exm:1-4-orientacao-barra`):**
   - Item (a): $(\Delta x, \Delta y) = (2\sqrt{3}, 2) \implies \frac{\Delta y}{\Delta x} = \frac{2}{2\sqrt{3}} = \frac{\sqrt{3}}{3} \implies \theta = \arctan(\sqrt{3}/3) = 30^\circ \in [0^\circ, 180^\circ)$. **Correto.**
   - Item (b): $(\Delta x, \Delta y) = (4, -4) \implies \frac{\Delta y}{\Delta x} = -1 \implies \arctan(-1) = -45^\circ$. Orientação: $-45^\circ + 180^\circ = 135^\circ \in [0^\circ, 180^\circ)$. **Correto.**
   - Item (c): $(\Delta x, \Delta y) = (-4, -4) \implies \frac{\Delta y}{\Delta x} = +1 \implies \arctan(1) = 45^\circ$. Porém, com $\Delta x < 0$ e $\Delta y < 0$, o vetor aponta para o 3º quadrante: direção de movimento $= 45^\circ + 180^\circ = 225^\circ$. **Correto.**
3. **[Exemplo 1.4.9](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-04.dlt#L643-L666) (`exm:1-4-monitor-angulo-visual`):**
   - $\theta = 2 \arctan\left(\frac{s}{2d}\right)$, com $d = 57\text{ cm}$.
   - Item (a): $s = 1\text{ cm} \implies \frac{s}{2d} = \frac{1}{114} \implies \arctan(1/114) \approx 0{,}5026^\circ \implies \theta = 2 \cdot 0{,}5026^\circ \approx 1{,}005^\circ \approx 1{,}01^\circ \approx 1^\circ$. **Correto.**
   - Item (b): $s = 30\text{ cm} \implies \frac{s}{2d} = \frac{30}{114} = \frac{5}{19} \approx 0{,}2632$. $\arctan(5/19) \approx 0{,}2573\text{ rad} \approx 14{,}74^\circ \implies \theta = 2 \cdot 14{,}74^\circ \approx 29{,}49^\circ \approx 29{,}5^\circ$. **Correto.**
4. **[Exercício 1.4.3.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-04.dlt#L677-L693) (`exr:1-4-3-1`):**
   - $\operatorname{arcsen}(-1/2) = -\frac{\pi}{6}\text{ rad} = -30^\circ$. **Correto.**
   - $\arccos(-\sqrt{2}/2) = \frac{3\pi}{4}\text{ rad} = 135^\circ$. **Correto.**
   - $\arctan(\sqrt{3}) = \frac{\pi}{3}\text{ rad} = 60^\circ$. **Correto.**
5. **[Exercício 1.4.3.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-04.dlt#L695-L705) (`exr:1-4-3-2`):**
   - $\operatorname{sen}(2\pi/3) = \frac{\sqrt{3}}{2} \implies \operatorname{arcsen}(\sqrt{3}/2) = \frac{\pi}{3} \ne \frac{2\pi}{3}$ (pois $\frac{2\pi}{3} \notin [-\pi/2, \pi/2]$). **Correto.**
   - $\cos(-\pi/4) = \frac{\sqrt{2}}{2} \implies \arccos(\sqrt{2}/2) = \frac{\pi}{4} \ne -\frac{\pi}{4}$ (pois imagem de $\arccos$ é $[0, \pi]$). **Correto.**
6. **[Exercício 1.4.3.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-04.dlt#L707-L728) (`exr:1-4-3-3`):**
   - Item (a): $\frac{\Delta y}{\Delta x} = -\sqrt{3} \implies \arctan(-\sqrt{3}) = -60^\circ = -\frac{\pi}{3}\text{ rad}$. **Correto.**
   - Item (b): Orientação de barra em $[0^\circ, 180^\circ)$: $-60^\circ + 180^\circ = 120^\circ$. **Correto.**
   - Item (c): Para $\mathbf{u} = (-3, 3\sqrt{3})$ (2º quadrante): direção $= 180^\circ - 60^\circ = 120^\circ$. Para $\mathbf{v} = (3, -3\sqrt{3})$ (4º quadrante): direção $= 360^\circ - 60^\circ = 300^\circ$. **Correto.**
7. **[Exercício 1.4.3.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-04.dlt#L730-L753) (`exr:1-4-3-4`):**
   - $y(t) = 36{,}8 + 0{,}4\cos\left(\frac{2\pi(t - 17)}{24}\right) = 37{,}0$.
   - Item (a): $\cos\left(\frac{2\pi(t - 17)}{24}\right) = \frac{37{,}0 - 36{,}8}{0{,}4} = \frac{0{,}2}{0{,}4} = \frac{1}{2}$. **Correto.**
   - Item (b): Soluções em um ciclo: $\frac{2\pi(t - 17)}{24} = \pm \frac{\pi}{3} \implies \frac{t - 17}{12} = \pm \frac{1}{3} \implies t - 17 = \pm 4 \implies t_1 = 21\text{ h}$ e $t_2 = 13\text{ h}$. **Correto.**
   - Item (c): Justificativa exata pela restrição de imagem do $\arccos$ a $[0, \pi]$ (capturando apenas a fase descendente pós-pico). **Correto.**

---

### 4.4 Subtema 4: Relações e identidades fundamentais (`sec:1-4-4`)

1. **[Exemplo 1.4.10](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-04.dlt#L834-L846) (`exm:1-4-identidades`):**
   - $\operatorname{sen}\theta = \frac{3}{5}$ no 2º quadrante.
   - $\cos^2\theta = 1 - \frac{9}{25} = \frac{16}{25} \implies \cos\theta = -\frac{4}{5}$. $\tan\theta = \frac{3/5}{-4/5} = -\frac{3}{4}$. **Correto.**
   - $\operatorname{sen}(2\theta) = 2 \cdot \frac{3}{5} \cdot \left(-\frac{4}{5}\right) = -\frac{24}{25}$. **Correto.**
   - $\cos(2\theta) = \left(-\frac{4}{5}\right)^2 - \left(\frac{3}{5}\right)^2 = \frac{16 - 9}{25} = \frac{7}{25}$. **Correto.**
   - Conferência: $\left(-\frac{24}{25}\right)^2 + \left(\frac{7}{25}\right)^2 = \frac{576 + 49}{625} = \frac{625}{625} = 1$. **Correto.**
2. **[Exemplo 1.4.11](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-04.dlt#L848-L861) (`exm:1-4-georgopoulos`):**
   - $f(s) = 30 + 20\cos(s - 45^\circ)$.
   - $s = 45^\circ$: $30 + 20\cos(0^\circ) = 30 + 20 = 50\text{ Hz}$ ($r_{\text{max}}$). **Correto.**
   - $s = 105^\circ$: $30 + 20\cos(60^\circ) = 30 + 20(0{,}5) = 40\text{ Hz}$. **Correto.**
   - $s = 135^\circ$: $30 + 20\cos(90^\circ) = 30 + 0 = 30\text{ Hz}$ ($r_0$, direção ortogonal). **Correto.**
   - $s = 225^\circ$: $30 + 20\cos(180^\circ) = 30 - 20 = 10\text{ Hz}$. **Correto.**
3. **[Exemplo 1.4.12](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-04.dlt#L863-L885) (`exm:1-4-soma-sinais`):**
   - $I_1(t) = 3\operatorname{sen}(20\pi t)$, $I_2(t) = 4\cos(20\pi t)$.
   - Item (a): $R = \sqrt{3^2 + 4^2} = \sqrt{25} = 5\text{ nA}$. $\tan\varphi = \frac{4}{3} \implies \varphi = \arctan(4/3) \approx 0{,}9273\text{ rad} \approx 53{,}1^\circ$.
     $I_{\text{total}}(t) = 5\operatorname{sen}(20\pi t + 0{,}927)\text{ nA}$. **Correto.**
     Conferência em $t = 0$: $3\operatorname{sen}(0) + 4\cos(0) = 4\text{ nA}$; pela fórmula combinada: $5\operatorname{sen}(0{,}927) \approx 5 \cdot \frac{4}{5} = 4\text{ nA}$. **Correto.**
   - Item (b): Explicação rigorosa de defasagem de $\pi/2$ e interferência destrutiva vs. construtiva. **Correto.**
4. **[Exercício 1.4.4.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-04.dlt#L896-L907) (`exr:1-4-4-1`):**
   - $\cos\theta = -\frac{5}{13}$ no 3º quadrante.
   - $\operatorname{sen}^2\theta = 1 - \frac{25}{169} = \frac{144}{169} \implies \operatorname{sen}\theta = -\frac{12}{13}$. **Correto.**
   - $\tan\theta = \frac{-12/13}{-5/13} = \frac{12}{5} = 2{,}4$. **Correto.**
   - $\operatorname{sen}(2\theta) = 2 \left(-\frac{12}{13}\right) \left(-\frac{5}{13}\right) = \frac{120}{169}$. **Correto.**
5. **[Exercício 1.4.4.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-04.dlt#L909-L930) (`exr:1-4-4-2`):**
   - $f(s) = 25 + 15\cos(s - 120^\circ)\text{ Hz}$.
   - Item (a): $s_{\text{pref}} = 120^\circ$; $r_{\text{max}} = 25 + 15 = 40\text{ Hz}$; ortogonal: $r_0 = 25\text{ Hz}$. **Correto.**
   - Item (b):
     - $s = 180^\circ$: $25 + 15\cos(60^\circ) = 25 + 7{,}5 = 32{,}5\text{ Hz}$. **Correto.**
     - $s = 210^\circ$: $25 + 15\cos(90^\circ) = 25 + 0 = 25\text{ Hz}$. **Correto.**
     - $s = 300^\circ$: $25 + 15\cos(180^\circ) = 25 - 15 = 10\text{ Hz}$. **Correto.**
6. **[Exercício 1.4.4.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-04.dlt#L932-L947) (`exr:1-4-4-3`):**
   - $y(t) = \sqrt{3}\operatorname{sen}(12\pi t) + \cos(12\pi t)$.
   - $a = \sqrt{3} > 0$, $b = 1 \implies R = \sqrt{(\sqrt{3})^2 + 1^2} = 2$.
   - $\tan\varphi = \frac{1}{\sqrt{3}} = \frac{\sqrt{3}}{3} \implies \varphi = \frac{\pi}{6}\text{ rad} = 30^\circ$.
   - Forma resultante: $y(t) = 2\operatorname{sen}\left(12\pi t + \frac{\pi}{6}\right)$; $f = \frac{12\pi}{2\pi} = 6\text{ Hz}$ (banda teta); $T = \frac{1}{6}\text{ s} \approx 166{,}7\text{ ms}$. **Correto.**
7. **[Exercício 1.4.4.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-04.dlt#L949-L966) (`exr:1-4-4-4`):**
   - $f(s) = r_0 + (r_{\text{max}} - r_0)\cos(s - s_{\text{pref}})$.
   - Expansão: $\cos(s - s_{\text{pref}}) = \cos s \cos s_{\text{pref}} + \operatorname{sen} s \operatorname{sen} s_{\text{pref}}$.
     $c_x = (r_{\text{max}} - r_0)\cos s_{\text{pref}}$, $c_y = (r_{\text{max}} - r_0)\operatorname{sen} s_{\text{pref}}$. **Correto.**
   - Para $r_0 = 30$, $r_{\text{max}} = 50$, $s_{\text{pref}} = 60^\circ$:
     $c_x = 20\cos 60^\circ = 10\text{ Hz}$; $c_y = 20\operatorname{sen} 60^\circ = 10\sqrt{3} \approx 17{,}32\text{ Hz}$. **Correto.**
   - Conferência em $s = 60^\circ$: $30 + 10\left(\frac{1}{2}\right) + 10\sqrt{3}\left(\frac{\sqrt{3}}{2}\right) = 30 + 5 + 15 = 50\text{ Hz} = r_{\text{max}}$. **Correto.**

---

## 5. Contas Conferidas

Lista completa dos identificadores de exemplos e exercícios auditados, recalculados passo a passo e atestados como **100% corretos**:

### Exemplos (12 de 12)
- [exm:1-4-barra-v1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-04.dlt#L96) — Componentes de uma barra orientada no córtex visual
- [exm:1-4-angulo-visual](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-04.dlt#L123) — Ângulo visual de um estímulo e a regra do polegar
- [exm:1-4-microeletrodo](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-04.dlt#L146) — Inserção inclinada de um microeletrodo cortical
- [exm:1-4-circulo-valores](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-04.dlt#L336) — Calculando valores no círculo trigonométrico por simetria
- [exm:1-4-eeg-alfa](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-04.dlt#L368) — Ritmo alfa no EEG: período, ciclos e fase instantânea
- [exm:1-4-circadiano](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-04.dlt#L408) — Ritmo circadiano da temperatura corporal
- [exm:1-4-cancelamento-exato](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-04.dlt#L593) — Calculando inversas e testando o cancelamento
- [exm:1-4-orientacao-barra](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-04.dlt#L618) — Recuperando orientação e direção a partir de $(\Delta x, \Delta y)$
- [exm:1-4-monitor-angulo-visual](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-04.dlt#L643) — Ângulo visual de um monitor e a regra dos $57\text{ cm}$
- [exm:1-4-identidades](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-04.dlt#L834) — Aplicando a relação fundamental e o arco duplo
- [exm:1-4-georgopoulos](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-04.dlt#L848) — Sintonia de cosseno no córtex motor (Georgopoulos, 1982)
- [exm:1-4-soma-sinais](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-04.dlt#L863) — Soma de duas correntes oscilatórias na mesma frequência

### Exercícios (16 de 16)
- [exr:1-4-1-1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-04.dlt#L165) — Básico — Razões no triângulo retângulo
- [exr:1-4-1-2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-04.dlt#L178) — Básico — Decomposição de barra luminosa em V1
- [exr:1-4-1-3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-04.dlt#L190) — Intermediário — Alcance de um microeletrodo
- [exr:1-4-1-4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-04.dlt#L211) — Avançado — Largura da tela para grandes ângulos visuais
- [exr:1-4-2-1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-04.dlt#L451) — Básico — Conversões e valores no círculo trigonométrico
- [exr:1-4-2-2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-04.dlt#L471) — Básico — Oscilações teta e gama no EEG
- [exr:1-4-2-3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-04.dlt#L494) — Intermediário — Parâmetros e deslocamento de uma onda beta
- [exr:1-4-2-4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-04.dlt#L526) — Avançado — Deslocamento de fase circadiano (jet lag)
- [exr:1-4-3-1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-04.dlt#L677) — Básico — Valores exatos de funções trigonométricas inversas
- [exr:1-4-3-2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-04.dlt#L695) — Básico — Testando limites do cancelamento
- [exr:1-4-3-3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-04.dlt#L707) — Intermediário — Orientação de borda e quadrante de movimento
- [exr:1-4-3-4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-04.dlt#L730) — Avançado — Decodificando horários a partir da temperatura circadiana
- [exr:1-4-4-1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-04.dlt#L896) — Básico — Relação fundamental e arco duplo no 3º quadrante
- [exr:1-4-4-2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-04.dlt#L909) — Básico — Avaliando a curva de sintonia de um neurônio motor
- [exr:1-4-4-3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-04.dlt#L932) — Intermediário — Soma de oscilações teta com ângulo exato
- [exr:1-4-4-4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-01/tema-04.dlt#L949) — Avançado — Decompondo a sintonia de cosseno pela identidade da diferença
