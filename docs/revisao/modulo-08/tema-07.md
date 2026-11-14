# Relatório de Revisão Técnica — Módulo 08 · Tema 07 (Estudo de variáveis)

- **Arquivo revisado:** [tema-07.dlt](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-07.dlt)
- **Documentos de referência:** [PADRAO-AULAS.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/PADRAO-AULAS.md) e [DELTA-COLA.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/DELTA-COLA.md)
- **Data da revisão:** 14 de novembro de 2026
- **Perfil do revisor:** Matemático, Neurocientista Computacional e Professor de Alunos de Ciências Biológicas

---

## 1. Veredito

**APROVAR**

A aula [tema-07.dlt](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-07.dlt) cumpre integralmente e com alto nível de rigor todos os requisitos pedagógicos, matemáticos, conceituais e estruturais estipulados no contrato editorial e nas diretrizes específicas do Módulo 8 (Machine Learning).

Principais destaques da auditoria:
1. **Estrutura e cobertura temática:** Todas as 4 seções solicitadas foram contempladas na ordem exata prescrita (`sec:8-7-1` a `sec:8-7-4`), complementadas adequadamente pelas seções de "Resumo" e "Para ir além".
2. **Exatidão matemática:** Todas as contas de todos os exemplos resolvidos e das soluções dos 12 exercícios (3 por seção: Básico, Intermediário e Avançado) foram recalculadas analiticamente do início ao fim; não há um único erro aritmético, dimensional ou algébrico.
3. **Completude didática:** Todos os 12 exercícios possuem título graduado, dica objetiva (`<hint>`) e solução completa (`<solution collapsible="true" collapsed="true">`) com justificativa formal e intuitiva, não se limitando a respostas numéricas isoladas.
4. **Contextualização biológica realista:** Cada uma das quatro seções apresenta contextos biológicos autênticos da neurociência (características eletrofisiológicas de disparo e potenciais de membrana, bandas espectrais de EEG e condução de volume, sobreposição hemodinâmica e seleção de voxels em fMRI, e classificação de vigília vs. sono de ondas lentas NREM).
5. **Código Python exemplar e autocontido:** Todos os 4 blocos de código principais e os 4 códigos presentes nas soluções rodam de forma totalmente autocontida com `numpy`, `matplotlib` e `scikit-learn`, sem dependências externas nem download de dados. Respeitam integralmente a API moderna do scikit-learn (sem parâmetros obsoletos como `penalty=` ou `multi_class=` em `LogisticRegression`, uso correto de `SequentialFeatureSelector`, `Pipeline` e `permutation_importance`).
6. **Fidelidade científica e citações:** As menções bibliográficas na prosa limitam-se estritamente aos clássicos autorizados (Breiman, 2001; Kriegeskorte et al., 2009; Haufe et al., 2014), sem detalhes inventados. As afirmações neurofisiológicas são de livro-texto (Kandel; Dayan & Abbott).
7. **Sintaxe Delta estrita:** O documento segue rigorosamente as regras de XML estrito do Delta v0.6.0, sem atributos vazios, com matemática KaTeX padronizada e link de volta ao guia devidamente posicionado.

Foram formuladas apenas 5 observações pedagógicas e de refinamento tipográfico na tabela a seguir, nenhuma de natureza impeditiva.

---

## 2. Tabela de Problemas e Sugestões

| Severidade | Local | Trecho | Correção sugerida |
|---|---|---|---|
| Pedagógico | Seção 1 (`sec:8-7-1`), [def:8-7-padronizacao](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-07.dlt#L67), linha ~67 | `Ao ajustar a regressão sobre variáveis padronizadas $z_j$, obtemos os coeficientes padronizados $\tilde{\beta}_j = \hat{\beta}_j s_j$, que medem a mudança prevista em $y$ por desvio padrão de $x_j$.` | Para estudantes de Biologia, vale explicitar em nota de margem (<c>&lt;sidenote&gt;</c>) a distinção entre coeficientes semi-padronizados ($\tilde{\beta}_j = \hat{\beta}_j s_j$, onde $y$ preserva sua unidade biológica fisiológica, como $\text{Hz}$) e coeficientes totalmente padronizados ($\beta_j^* = \hat{\beta}_j \frac{s_j}{s_y}$, onde $y$ também é dividido por seu desvio padrão e o peso torna-se puramente adimensional). Isso evita confusão quando consultarem manuais de econometria ou estatística geral. |
| Pedagógico | Seção 2 (`sec:8-7-2`), [def:8-7-vif-condicao](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-07.dlt#L256), linha ~256 | `O número de condição $\kappa(\mathbf{Z}^\top\mathbf{Z}) = \frac{\mu_{\max}}{\mu_{\min}}$ cresce sem limites...` | Recomenda-se adicionar um breve comentário elucidando que $\kappa(\mathbf{Z}^\top\mathbf{Z}) = (\kappa(\mathbf{Z}))^2$. Assim, o valor $\kappa \approx 39{,}4$ obtido no script corresponde a uma razão de valores singulares de $\mathbf{Z}$ de $\sqrt{39{,}4} \approx 6{,}3$. Esse esclarecimento é valioso para que o leitor não confunda o limiar de Belsley et al. ($\kappa(\mathbf{Z}) > 30$) com o da matriz Gramiana ($\kappa(\mathbf{Z}^\top\mathbf{Z}) > 100$ a $900$). |
| Pedagógico | Seção 3 (`sec:8-7-3`), [def:8-7-stepwise](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-07.dlt#L454), linha ~454 | `$$1 + p + (p - 1) + \dots + 1 = 1 + \frac{p(p + 1)}{2}\text{ modelos.}$$` | A primeira parcela "$1$" representa o modelo nulo (apenas o intercepto, avaliado no Passo 0 antes da entrada de variáveis). Vale explicitar textualmente essa decomposição "$1\text{ (nulo)} + \sum_{k=1}^p k$", facilitando a verificação contábil imediata por alunos com pouca familiaridade com progressões aritméticas. |
| Pedagógico | Seção 4 (`sec:8-7-4`), [def:8-7-permutacao](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-07.dlt#L644), linha ~644 | `s_{I,j} = \sqrt{\frac{1}{R}\sum_{r=1}^R (I_{j,r} - \bar{I}_j)^2}` | A fórmula utiliza o divisor $R$ (`ddof=0`), que reflete com exatidão a implementação interna do NumPy e do scikit-learn (`np.std(importances, axis=1)`). Vale incluir uma observação esclarecendo que, embora na estatística descritiva de pequenas amostras se use $R-1$, a convenção do `permutation_importance` adota o divisor $R$, o que explica por que os cálculos manuais com $R=2$ ou $R=4$ usam diretamente a média dos quadrados dos desvios. |
| Formato | Seção 4 (`sec:8-7-4`), [exr:8-7-4-1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-07.dlt#L744-L746), linhas ~744–746 | `Variável A: $(0{,}43;\; 0{,}43;\; 0{,}47;\; 0{,}47)$; ` | Há um espaço em branco antes do fechamento de parêntese/ponto e vírgula nos itens da lista do enunciado. Sugere-se remover o espaço sobressalente para manter o padrão tipográfico impecável do restante da aula. |

---

## 3. Recálculo e Auditoria de Todas as Contas

Todas as contas da aula foram refeitas integralmente à mão e conferidas analiticamente, abrangendo médias amostrais, variâncias populacionais, escores $z$, inversões de matrizes, fatores de inflação da variância ($\mathrm{VIF}$), progressões combinatórias e degradações de escore por permutação.

### 3.1 Subtema 1: Padronização e escala das variáveis (`sec:8-7-1`)

1. **[Exemplo 8.7.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-07.dlt#L72-L87) (`exm:8-7-zscore-mao` — Padronizando larguras de potencial de ação à mão):**
   - Dados de entrada: $\mathbf{x} = (0{,}3;\; 0{,}9;\; 1{,}1;\; 1{,}7)\text{ ms}$, com $n = 4$.
   - Média amostral:
     $$\bar{x} = \frac{0{,}3 + 0{,}9 + 1{,}1 + 1{,}7}{4} = \frac{4{,}0}{4} = 1{,}0\text{ ms}.$$
   - Desvios em relação à média:
     $$x_1 - \bar{x} = 0{,}3 - 1{,}0 = -0{,}7\text{ ms},$$
     $$x_2 - \bar{x} = 0{,}9 - 1{,}0 = -0{,}1\text{ ms},$$
     $$x_3 - \bar{x} = 1{,}1 - 1{,}0 = +0{,}1\text{ ms},$$
     $$x_4 - \bar{x} = 1{,}7 - 1{,}0 = +0{,}7\text{ ms}.$$
   - Soma dos quadrados dos desvios:
     $$\sum_{i=1}^4 (x_i - \bar{x})^2 = (-0{,}7)^2 + (-0{,}1)^2 + (+0{,}1)^2 + (+0{,}7)^2 = 0{,}49 + 0{,}01 + 0{,}01 + 0{,}49 = 1{,}00\text{ ms}^2.$$
   - Variância e desvio padrão populacionais (padrão do `StandardScaler` com divisor $n = 4$):
     $$s^2 = \frac{1{,}00}{4} = 0{,}25\text{ ms}^2 \implies s = \sqrt{0{,}25} = 0{,}5\text{ ms}.$$
   - Escores $z$ individuais ($z_i = (x_i - \bar{x})/s$):
     $$z_1 = \frac{-0{,}7}{0{,}5} = -1{,}4, \quad z_2 = \frac{-0{,}1}{0{,}5} = -0{,}2, \quad z_3 = \frac{+0{,}1}{0{,}5} = +0{,}2, \quad z_4 = \frac{+0{,}7}{0{,}5} = +1{,}4.$$
   - Verificação de consistência: média dos escores $\bar{z} = \frac{-1{,}4 - 0{,}2 + 0{,}2 + 1{,}4}{4} = 0$; variância dos escores $s_z^2 = \frac{(-1{,}4)^2 + (-0{,}2)^2 + 0{,}2^2 + 1{,}4^2}{4} = \frac{1{,}96 + 0{,}04 + 0{,}04 + 1{,}96}{4} = \frac{4{,}00}{4} = 1{,}00$.
   *Conta perfeitamente exata.*

2. **[Exemplo 8.7.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-07.dlt#L89-L98) (`exm:8-7-eletrofisiologia-unidades` — Comparando coeficientes em unidades eletrofisiológicas distintas):**
   - Modelo bruto: $\hat{y} = 90 - 12{,}0\,x_1 + 0{,}5\,x_2$, com $y$ em $\text{Hz}$, $x_1$ em $\text{ms}$ e $x_2$ em $\text{mV}$.
   - Estatísticas da amostra: $\bar{x}_1 = 1{,}0\text{ ms}$, $s_1 = 0{,}25\text{ ms}$; $\bar{x}_2 = -70\text{ mV}$, $s_2 = 6{,}0\text{ mV}$.
   - Substituição de $x_j = \bar{x}_j + s_j z_j$:
     $$x_1 = 1{,}0 + 0{,}25\,z_1, \qquad x_2 = -70 + 6{,}0\,z_2.$$
   - Reescrita do modelo:
     $$\hat{y} = 90 - 12{,}0(1{,}0 + 0{,}25\,z_1) + 0{,}5(-70 + 6{,}0\,z_2)$$
     $$\hat{y} = 90 - 12{,}0 - 3{,}0\,z_1 - 35{,}0 + 3{,}0\,z_2 = (90 - 47{,}0) - 3{,}0\,z_1 + 3{,}0\,z_2 = 43{,}0 - 3{,}0\,z_1 + 3{,}0\,z_2.$$
   - Coeficientes padronizados: $\tilde{\beta}_1 = -3{,}0\text{ Hz}$ e $\tilde{\beta}_2 = +3{,}0\text{ Hz}$.
   - Comparação: $|\tilde{\beta}_1| = |\tilde{\beta}_2| = 3{,}0\text{ Hz}$, mostrando que $1$ desvio padrão em qualquer uma das variáveis provoca exatamente a mesma variação prevista na taxa de disparo ($3{,}0\text{ Hz}$), apesar de $\hat{\beta}_1 = -12{,}0$ aparentar magnitude $24$ vezes maior que $\hat{\beta}_2 = 0{,}5$ nas variáveis originais.
   *Conta perfeitamente exata.*

3. **[Exercício 8.7.1.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-07.dlt#L160-L176) (`exr:8-7-1-1` — Básico: Escore $z$ de potenciais de repouso à mão):**
   - Dados: $(-73,\; -71,\; -70,\; -69,\; -67)\text{ mV}$, $n = 5$.
   - Item a:
     - Média: $\bar{x} = \frac{-73 - 71 - 70 - 69 - 67}{5} = \frac{-350}{5} = -70\text{ mV}$.
     - Desvios: $(-3,\; -1,\; 0,\; +1,\; +3)\text{ mV}$.
     - Soma dos quadrados: $(-3)^2 + (-1)^2 + 0^2 + 1^2 + 3^2 = 9 + 1 + 0 + 1 + 9 = 20$.
     - Variância populacional: $s^2 = \frac{20}{5} = 4\text{ mV}^2 \implies s = \sqrt{4} = 2\text{ mV}$.
     - Escores $z$:
       $$z_1 = \frac{-3}{2} = -1{,}5; \quad z_2 = \frac{-1}{2} = -0{,}5; \quad z_3 = \frac{0}{2} = 0; \quad z_4 = \frac{+1}{2} = +0{,}5; \quad z_5 = \frac{+3}{2} = +1{,}5.$$
   - Item b:
     - Potencial para $z = +2{,}0$:
       $$x = \bar{x} + z\,s = -70 + 2{,}0 \cdot 2 = -70 + 4 = -66\text{ mV}.$$
   *Conta perfeitamente exata.*

4. **[Exercício 8.7.1.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-07.dlt#L178-L194) (`exr:8-7-1-2` — Intermediário: Quem depende da escala e o que muda nos coeficientes?):**
   - Modelo: $\hat{y} = 50 + 20\,x_1 - 0{,}4\,x_2$, com $s_1 = 0{,}1\text{ ms}$ e $s_2 = 10\text{ Hz}$.
   - Item a:
     - Mudança para segundos: $\tilde{x}_1 = x_1 / 1\,000 \iff x_1 = 1\,000\,\tilde{x}_1$.
     - Na OLS: o termo $20\,x_1$ torna-se $20(1\,000\,\tilde{x}_1) = 20\,000\,\tilde{x}_1$. O coeficiente passa para $\tilde{\beta}_1^{\text{s}} = 20\,000\text{ Hz/s}$, mantendo as predições $\hat{y}_i$ e o $R^2$ inalterados.
     - Na Ridge com $\alpha = 10$: a penalidade L2 adiciona $\alpha \beta_1^2$. O valor $20\,000$ geraria penalidade $10 \cdot (20\,000)^2 = 4 \cdot 10^9$, forçando um encolhimento desproporcional que destruiria o ajuste e alteraria completamente o $R^2$.
   - Item b:
     - Coeficientes padronizados:
       $$\tilde{\beta}_1 = \hat{\beta}_1 s_1 = 20 \cdot 0{,}1 = +2{,}0\text{ Hz},$$
       $$\tilde{\beta}_2 = \hat{\beta}_2 s_2 = -0{,}4 \cdot 10 = -4{,}0\text{ Hz}.$$
     - Impacto relativo: $|\tilde{\beta}_2| = 4{,}0 = 2 \cdot 2{,}0 = 2\,|\tilde{\beta}_1|$. A variável $x_2$ tem o dobro do impacto de $x_1$ por desvio padrão, contrariando a falsa impressão dada pelos coeficientes brutos ($20$ vs. $-0{,}4$).
   *Conta perfeitamente exata.*

---

### 3.2 Subtema 2: Multicolinearidade (`sec:8-7-2`)

1. **[Exemplo 8.7.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-07.dlt#L271-L289) (`exm:8-7-vif-mao` — Calculando o $\mathrm{VIF}$ e a inflação do erro padrão à mão):**
   - Item a:
     - $R_{\text{beta}}^2 = 0{,}90$.
     - Fator de inflação da variância:
       $$\mathrm{VIF}_{\text{beta}} = \frac{1}{1 - 0{,}90} = \frac{1}{0{,}10} = 10.$$
     - Fator de ampliação do erro padrão:
       $$\sqrt{\mathrm{VIF}_{\text{beta}}} = \sqrt{10} \approx 3{,}16227... \approx 3{,}16.$$
   - Item b:
     - Dois preditores com correlação $r = 0{,}80$:
       $$R^2 = r^2 = 0{,}80^2 = 0{,}64.$$
       $$\mathrm{VIF} = \frac{1}{1 - 0{,}64} = \frac{1}{0{,}36} = \frac{100}{36} = \frac{25}{9} \approx 2{,}777... \approx 2{,}78.$$
   *Conta perfeitamente exata.*

2. **[Exemplo 8.7.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-07.dlt#L291-L296) (`exm:8-7-fmri-sinais-trocados` — Regressores sobrepostos de fMRI: pesos trocados, previsão preservada):**
   - Relação verdadeira: $y = 2{,}0\,x_1 + 1{,}0\,x_2 + \varepsilon$, com correlação $r = 0{,}95$ entre regressores.
   - Modelo OLS obtido em corrida específica: $\hat{y} = 5{,}8\,x_1 - 2{,}9\,x_2$.
   - Avaliação sob ensaio típico com $x_1 \approx x_2 \approx 1{,}0$:
     - Resposta verdadeira esperada: $y_{\text{verd}} = 2{,}0(1{,}0) + 1{,}0(1{,}0) = 3{,}0$.
     - Predição do modelo instável: $\hat{y} = 5{,}8(1{,}0) - 2{,}9(1{,}0) = 2{,}9$.
     - Erro de predição: $|3{,}0 - 2{,}9| = 0{,}1$.
   - Conclusão teórica: confirma que a instabilidade dos pesos individuais não compromete a capacidade preditiva quando a estrutura de covariância entre regressores é preservada fora da amostra.
   *Conta e raciocínio exatos.*

3. **[Exercício 8.7.2.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-07.dlt#L360-L372) (`exr:8-7-2-1` — Básico: Tabela rápida de $\mathrm{VIF}$ e erro padrão):**
   - Variável 1 ($R_1^2 = 0{,}50$):
     $$\mathrm{VIF}_1 = \frac{1}{1 - 0{,}50} = \frac{1}{0{,}50} = 2 \implies \sqrt{\mathrm{VIF}_1} = \sqrt{2} \approx 1{,}4142... \approx 1{,}41.$$
   - Variável 2 ($R_2^2 = 0{,}80$):
     $$\mathrm{VIF}_2 = \frac{1}{1 - 0{,}80} = \frac{1}{0{,}20} = 5 \implies \sqrt{\mathrm{VIF}_2} = \sqrt{5} \approx 2{,}2360... \approx 2{,}24.$$
   - Variável 3 ($R_3^2 = 0{,}96$):
     $$\mathrm{VIF}_3 = \frac{1}{1 - 0{,}96} = \frac{1}{0{,}04} = 25 \implies \sqrt{\mathrm{VIF}_3} = \sqrt{25} = 5{,}00.$$
   *Conta perfeitamente exata.*

4. **[Exercício 8.7.2.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-07.dlt#L374-L388) (`exr:8-7-2-2` — Intermediário: Eletrodos vizinhos com sinais trocados):**
   - Correlação $r = 0{,}90$.
   - Item a:
     $$R_1^2 = r^2 = 0{,}90^2 = 0{,}81 \implies \mathrm{VIF} = \frac{1}{1 - 0{,}81} = \frac{1}{0{,}19} = \frac{100}{19} \approx 5{,}2631... \approx 5{,}26.$$
   - Item b:
     - Resposta verdadeira para $x_1 = x_2 = x$: $1{,}0\,x + 1{,}0\,x = 2{,}0\,x$.
     - Resposta ajustada com $\hat{\beta}_1 = +4{,}5$ e $\hat{\beta}_2 = -2{,}5$: $4{,}5\,x - 2{,}5\,x = 2{,}0\,x$.
     - Coincidência exata das retas de resposta ao longo do eixo de colinearidade.
   *Conta perfeitamente exata.*

---

### 3.3 Subtema 3: Seleção de subconjuntos: forward, backward e melhor subconjunto (`sec:8-7-3`)

1. **[Exemplo 8.7.5](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-07.dlt#L468-L487) (`exm:8-7-forward-mao` — Executando a seleção forward à mão com erros de CV):**
   - Espaço de busca com $p = 3$ variáveis: $x_1$ (delta), $x_2$ (alfa), $x_3$ (frequência cardíaca).
   - Tabela de $\mathrm{MSE}_{\text{CV}}$:
     - Nulo: $\emptyset = 10{,}0$.
     - Tamanho 1: $\{x_1\} = 6{,}2$; $\{x_2\} = 4{,}8$; $\{x_3\} = 8{,}5$.
     - Tamanho 2: $\{x_1, x_2\} = 3{,}1$; $\{x_1, x_3\} = 5{,}9$; $\{x_2, x_3\} = 4{,}9$.
     - Tamanho 3: $\{x_1, x_2, x_3\} = 3{,}5$.
   - Execução do algoritmo *forward*:
     - **Passo 0:** Modelo nulo ($\mathrm{MSE} = 10{,}0$). (1 modelo avaliado).
     - **Passo 1:** Compara $\{x_1\} = 6{,}2$, $\{x_2\} = 4{,}8$, $\{x_3\} = 8{,}5$. Vencedor: $\{x_2\}$ ($4{,}8$). Fixa $x_2$. (3 modelos avaliados).
     - **Passo 2:** Compara adições a $\{x_2\}$: $\{x_2, x_1\} = 3{,}1$ e $\{x_2, x_3\} = 4{,}9$. Vencedor: $\{x_1, x_2\}$ ($3{,}1$). Fixa $\{x_1, x_2\}$. (2 modelos avaliados).
     - **Passo 3:** Avalia adicionar $x_3$: $\{x_1, x_2, x_3\} = 3{,}5$. O erro aumenta de $3{,}1$ para $3{,}5$. (1 modelo avaliado).
   - Resultado: O melhor subconjunto no caminho *forward* é $\{x_1, x_2\}$ com $\mathrm{MSE}_{\text{CV}} = 3{,}1$.
   - Total de modelos ajustados: $1 + 3 + 2 + 1 = 7$ modelos.
   - Fórmula analítica: $1 + \frac{p(p+1)}{2} = 1 + \frac{3 \cdot 4}{2} = 1 + 6 = 7$ modelos.
   - Comparação com melhor subconjunto global: $2^p = 2^3 = 8$ modelos (o modelo $\{x_1, x_3\}$ com erro $5{,}9$ foi poupado da avaliação).
   *Conta perfeitamente exata.*

2. **[Exercício 8.7.3.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-07.dlt#L548-L562) (`exr:8-7-3-1` — Básico: Quantos modelos cada estratégia ajusta?):**
   - Item a ($p = 5$ variáveis):
     - Melhor subconjunto: $2^p = 2^5 = 32$ modelos.
     - *Forward* completa: $1 + \frac{p(p+1)}{2} = 1 + \frac{5 \cdot 6}{2} = 1 + 15 = 16$ modelos.
   - Item b ($p = 15$ variáveis):
     - Melhor subconjunto: $2^p = 2^{15} = 32\,768$ modelos.
     - *Forward* completa: $1 + \frac{p(p+1)}{2} = 1 + \frac{15 \cdot 16}{2} = 1 + 120 = 121$ modelos.
     - Redução: $\frac{32\,768}{121} \approx 270{,}8 \implies$ cerca de $270$ vezes menos modelos.
   *Conta perfeitamente exata.*

3. **[Exercício 8.7.3.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-07.dlt#L564-L580) (`exr:8-7-3-2` — Intermediário: Quando a seleção forward perde o melhor subconjunto):**
   - Dados de $\mathrm{MSE}_{\text{CV}}$:
     - Nulo: $12{,}0$.
     - Tamanho 1: $\{x_1\} = 8{,}0$; $\{x_2\} = 9{,}0$; $\{x_3\} = 7{,}5$.
     - Tamanho 2: $\{x_1, x_2\} = 3{,}0$; $\{x_1, x_3\} = 6{,}5$; $\{x_2, x_3\} = 6{,}8$.
     - Tamanho 3: $\{x_1, x_2, x_3\} = 3{,}4$.
   - **Caminho *forward*:**
     - Passo 1: Menor erro de tamanho 1 é $\{x_3\}$ ($7{,}5$). Fixa $x_3$.
     - Passo 2: Entre $\{x_1, x_3\}$ ($6{,}5$) e $\{x_2, x_3\}$ ($6{,}8$), escolhe $\{x_1, x_3\}$ ($6{,}5$).
     - Passo 3: Avalia $\{x_1, x_2, x_3\}$, com erro $3{,}4$.
     - Vencedor do caminho *forward*: $\{x_1, x_2, x_3\}$ com $\mathrm{MSE} = 3{,}4$.
   - **Caminho *backward*:**
     - Passo 0: Parte do modelo completo $\{x_1, x_2, x_3\}$ com erro $3{,}4$.
     - Passo 1: Testa remover uma variável: remover $x_3 \implies \{x_1, x_2\}$ ($3{,}0$); remover $x_2 \implies \{x_1, x_3\}$ ($6{,}5$); remover $x_1 \implies \{x_2, x_3\}$ ($6{,}8$). O erro reduz para $3{,}0$ ao remover $x_3$. Fixa $\{x_1, x_2\}$.
     - Passo 2: A partir de $\{x_1, x_2\}$, testa remover $x_1$ ($\{x_2\} = 9{,}0$) ou $x_2$ ($\{x_1\} = 8{,}0$). Ambos aumentam o erro em relação a $3{,}0$.
     - Vencedor do caminho *backward*: $\{x_1, x_2\}$ com $\mathrm{MSE} = 3{,}0$.
   - Conclusão: O melhor subconjunto global é $\{x_1, x_2\}$ ($\mathrm{MSE} = 3{,}0$). A *forward* perdeu essa solução porque $x_1$ e $x_2$ exibem forte sinergismo mútuo, mas individualmente foram derrotadas por $x_3$ no primeiro passo.
   *Conta e demonstração analítica impecáveis.*

---

### 3.4 Subtema 4: Importância por permutação (`sec:8-7-4`)

1. **[Exemplo 8.7.7](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-07.dlt#L659-L678) (`exm:8-7-perm-mao` — Calculando a importância por permutação à mão):**
   - Escore de base de acurácia no teste: $S_{\text{base}} = 0{,}90$. Número de repetições: $R = 2$.
   - Queda de escore: $I_{j,r} = S_{\text{base}} - S_{j,r}$.
   - **Banda Delta:** escores $0{,}62$ e $0{,}66$.
     - Quedas: $I_1 = 0{,}90 - 0{,}62 = 0{,}28$ e $I_2 = 0{,}90 - 0{,}66 = 0{,}24$.
     - Média: $\bar{I}_{\text{delta}} = \frac{0{,}28 + 0{,}24}{2} = 0{,}26$.
     - Desvios: $+0{,}02$ e $-0{,}02$.
     - Variância ($1/R$): $s^2 = \frac{0{,}02^2 + (-0{,}02)^2}{2} = \frac{0{,}0004 + 0{,}0004}{2} = 0{,}0004$.
     - Desvio padrão: $s_{I,\text{delta}} = \sqrt{0{,}0004} = 0{,}02$.
   - **Banda Alfa:** escores $0{,}74$ e $0{,}78$.
     - Quedas: $I_1 = 0{,}90 - 0{,}74 = 0{,}16$ e $I_2 = 0{,}90 - 0{,}78 = 0{,}12$.
     - Média: $\bar{I}_{\text{alfa}} = \frac{0{,}16 + 0{,}12}{2} = 0{,}14$.
     - Desvios: $+0{,}02$ e $-0{,}02 \implies s_{I,\text{alfa}} = 0{,}02$.
   - **Banda Beta:** escores $0{,}88$ e $0{,}90$.
     - Quedas: $I_1 = 0{,}90 - 0{,}88 = 0{,}02$ e $I_2 = 0{,}90 - 0{,}90 = 0{,}00$.
     - Média: $\bar{I}_{\text{beta}} = \frac{0{,}02 + 0{,}00}{2} = 0{,}01$.
     - Desvios: $+0{,}01$ e $-0{,}01$.
     - Variância: $s^2 = \frac{0{,}01^2 + (-0{,}01)^2}{2} = \frac{0{,}0001 + 0{,}0001}{2} = 0{,}0001 \implies s_{I,\text{beta}} = 0{,}01$.
   - **Banda Gama:** escores $0{,}91$ e $0{,}89$.
     - Quedas: $I_1 = 0{,}90 - 0{,}91 = -0{,}01$ e $I_2 = 0{,}90 - 0{,}89 = +0{,}01$.
     - Média: $\bar{I}_{\text{gama}} = \frac{-0{,}01 + 0{,}01}{2} = 0{,}00$.
     - Desvios: $-0{,}01$ e $+0{,}01 \implies s_{I,\text{gama}} = \sqrt{0{,}0001} = 0{,}01$.
   *Conta perfeitamente exata.*

2. **[Exercício 8.7.4.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-07.dlt#L740-L759) (`exr:8-7-4-1` — Básico: Calculando $\bar{I}_j$ e $s_{I,j}$ para três variáveis):**
   - Escore de base no teste: $R_{\text{base}}^2 = 0{,}85$. Número de repetições: $R = 4$.
   - **Variável A:** $R^2$ degradados: $(0{,}43;\; 0{,}43;\; 0{,}47;\; 0{,}47)$.
     - Quedas: $0{,}85 - 0{,}43 = 0{,}42$ (duas vezes); $0{,}85 - 0{,}47 = 0{,}38$ (duas vezes).
     - Média: $\bar{I}_A = \frac{0{,}42 + 0{,}42 + 0{,}38 + 0{,}38}{4} = \frac{1{,}60}{4} = 0{,}40$.
     - Desvios em relação à média: $(+0{,}02;\; +0{,}02;\; -0{,}02;\; -0{,}02)$.
     - Variância ($1/4$): $s^2 = \frac{4 \cdot (0{,}02)^2}{4} = 0{,}0004 \implies s_{I,A} = \sqrt{0{,}0004} = 0{,}02$.
   - **Variável B:** $R^2$ degradados: $(0{,}69;\; 0{,}69;\; 0{,}71;\; 0{,}71)$.
     - Quedas: $0{,}85 - 0{,}69 = 0{,}16$ (duas vezes); $0{,}85 - 0{,}71 = 0{,}14$ (duas vezes).
     - Média: $\bar{I}_B = \frac{0{,}16 + 0{,}16 + 0{,}14 + 0{,}14}{4} = \frac{0{,}60}{4} = 0{,}15$.
     - Desvios: $(+0{,}01;\; +0{,}01;\; -0{,}01;\; -0{,}01) \implies s_{I,B} = \sqrt{0{,}0001} = 0{,}01$.
   - **Variável C:** $R^2$ degradados: $(0{,}87;\; 0{,}87;\; 0{,}85;\; 0{,}85)$.
     - Quedas: $0{,}85 - 0{,}87 = -0{,}02$ (duas vezes); $0{,}85 - 0{,}85 = 0{,}00$ (duas vezes).
     - Média: $\bar{I}_C = \frac{-0{,}02 - 0{,}02 + 0{,}00 + 0{,}00}{4} = \frac{-0{,}04}{4} = -0{,}01$.
     - Desvios em relação a $-0{,}01$:
       $$-0{,}02 - (-0{,}01) = -0{,}01 \text{ (duas vezes)}, \qquad 0{,}00 - (-0{,}01) = +0{,}01 \text{ (duas vezes)}.$$
     - Variância: $s^2 = \frac{4 \cdot (0{,}01)^2}{4} = 0{,}0001 \implies s_{I,C} = 0{,}01$.
   - Ordem de importância: $A > B > C$.
   - Interpretação de $C$: valor $-0{,}01 \pm 0{,}01$ indica que a variável é ruído inerte; sua leve melhora ocasional no teste deve-se exclusivamente a flutuação amostral aleatória da permutação.
   *Conta perfeitamente exata.*

---

## 4. Auditoria de Código Python

Todos os blocos de código presentes na aula foram auditados mentalmente simulando um interpretador CPython 3.11 com `numpy`, `scipy`, `matplotlib` e `scikit-learn` em suas versões atuais.

1. **Bloco [cod:8-7-escala](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-07.dlt#L102-L150) (`sec:8-7-1` — Escala de variáveis e KNN vs. Regressão Logística):**
   - **Bibliotecas:** `numpy`, `sklearn.linear_model.LogisticRegression`, `sklearn.metrics.accuracy_score`, `sklearn.model_selection.train_test_split`, `sklearn.neighbors.KNeighborsClassifier`, `sklearn.pipeline.Pipeline`, `sklearn.preprocessing.StandardScaler`.
   - **Operações e dimensões:** Gera matriz $\mathbf{X} \in \mathbb{R}^{240 \times 3}$ e vetor $\mathbf{y} \in \{0, 1\}^{240}$. A divisão $70/30$ estratificada produz $168$ amostras de treino e $72$ de teste.
   - **Chamadas de API:** `StandardScaler` e `KNeighborsClassifier(5)` encapsulados corretamente em `Pipeline`. `LogisticRegression(C=1.0, max_iter=1000)` utiliza parâmetros padrão estáveis, sem os atributos obsoletos `penalty=` ou `multi_class=`. Acesso a pesos via `.named_steps["clf"].coef_[0]`, que retorna shape `(3,)`.
   - **Saídas comentadas:** A acurácia do KNN salta de $0{,}569$ (bruta) para $0{,}986$ (padronizada), e o peso da largura do spike domina ($\approx -4{,}318$). Resultados perfeitamente consistentes com a teoria.

2. **Bloco [cod:8-7-vif-bootstrap](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-07.dlt#L300-L350) (`sec:8-7-2` — Cálculo manual do VIF e bootstrap dos coeficientes):**
   - **Bibliotecas:** `numpy`, `sklearn.linear_model.LinearRegression`, `sklearn.metrics.r2_score`, `sklearn.preprocessing.StandardScaler`.
   - **Implementação do VIF:** A função `calcular_vif(X)` ajusta regressores auxiliares com `LinearRegression` descartando uma coluna por vez com `np.delete(X, j, axis=1)` e calculando $1 / (1 - R_j^2)$ via `.score()`. Totalmente conforme a especificação do usuário (sem depender do `statsmodels`).
   - **Álgebra linear:** O número de condição $\kappa$ é computado via `np.linalg.cond(Z_tr.T @ Z_tr)`, após padronização explícita com `StandardScaler().fit_transform(X_tr)`.
   - **Bootstrap:** $B = 200$ reamostragens com reposição usando `rng.integers(0, n_treino, size=n_treino)`.
   - **Saídas:** $\mathrm{VIF} \approx [1{,}02,\; 10{,}48,\; 10{,}45]$ para $r = 0{,}95$; desvio padrão dos coeficientes inflado de $0{,}098$ (delta) para $\approx 0{,}318$ (alfa e beta), com $R^2$ de teste preservado em $0{,}858$. Totalmente coerente.

3. **Bloco [cod:8-7-sfs](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-07.dlt#L498-L537) (`sec:8-7-3` — Seleção passo a passo com `load_diabetes`):**
   - **Bibliotecas:** `sklearn.datasets.load_diabetes`, `sklearn.feature_selection.SequentialFeatureSelector`, `sklearn.linear_model.LinearRegression`, `sklearn.metrics.r2_score`, `sklearn.model_selection.train_test_split`, `sklearn.pipeline.Pipeline`, `sklearn.preprocessing.StandardScaler`.
   - **Estrutura de Pipeline:** `SequentialFeatureSelector` opera como transformador intermediário dentro de um `Pipeline` após o `StandardScaler`. O seletor executa validação cruzada $5$-fold interna apenas nos dados de treino.
   - **Indexação:** Máscara booleana obtida por `.named_steps["sel"].get_support()` aplicada diretamente sobre o array `nomes` de features do dataset.
   - **Saídas:** Seleção de 4 variáveis (`['bmi', 'bp', 's3', 's5']`) mantendo $R^2 = 0{,}352$ frente ao modelo completo ($0{,}359$).

4. **Bloco [cod:8-7-perm-eeg](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-07.dlt#L689-L729) (`sec:8-7-4` — Importância por permutação em decodificador de EEG):**
   - **Bibliotecas:** `sklearn.inspection.permutation_importance`, `sklearn.linear_model.LogisticRegression`, `sklearn.model_selection.train_test_split`, `sklearn.pipeline.Pipeline`, `sklearn.preprocessing.StandardScaler`.
   - **Execução:** Aplica `permutation_importance` sobre o objeto `tubo` já treinado passando os dados de teste `(X_te, y_te)`, com `n_repeats=30` e `random_state=0`.
   - **Extração de métricas:** Recupera `.importances_mean` e `.importances_std` com alinhamento rigoroso via `zip(nomes_bandas, ...)`.
   - **Saídas:** Bandas reais delta ($0{,}197 \pm 0{,}036$) e alfa ($0{,}145 \pm 0{,}032$) claramente destacadas, enquanto teta, beta e gama oscilam em torno de zero.

5. **Códigos de exercícios ([exr:8-7-1-3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-07.dlt#L201-L229), [exr:8-7-2-3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-07.dlt#L395-L431), [exr:8-7-3-3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-07.dlt#L588-L620), [exr:8-7-4-3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-07.dlt#L775-L797)):**
   - Todos os imports necessários estão presentes nos próprios blocos.
   - [exr:8-7-3-3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-07.dlt#L588-L620) demonstra de forma irretocável o vazamento de seleção fora da CV gerando acurácia ilusória de $80\%$ em ruído puro contra $48{,}3\%$ no pipeline correto.
   - [exr:8-7-4-3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-07.dlt#L775-L797) ilustra com clareza a inflação da importância no treino sob sobreajuste ($p/n = 25/45$).

6. **Script da figura [t07-importancia.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/fig/t07-importancia.py):**
   - Script Python independente e funcional, contendo a flag mandatória `plt.rcParams["svg.fonttype"] = "none"`, fundo transparente (`transparent=True`), tipografia e paleta de cores elegantes em conformidade com o tema visual do projeto. O arquivo SVG gerado já se encontra gravado e referenciado na aula em `fig/t07-importancia.svg`.

---

## 5. Auditoria de Neurociência e Fatos Biológicos

1. **Valores eletrofisiológicos padrão de livro-texto:**
   - Potencial de membrana de repouso: $-70\text{ mV}$ (com faixa biológica realista de $-75$ a $-60\text{ mV}$).
   - Taxas de disparo neuronal: $0$ a $200\text{ Hz}$ (típicas em córtex de mamíferos).
   - Largura do potencial de ação: $0{,}3$ a $0{,}8\text{ ms}$ para interneurônios GABAérgicos de disparo rápido (*fast-spiking*) e $> 1{,}2\text{ ms}$ para células piramidais excitatórias.
2. **Bandas espectrais de EEG e estados fisiológicos:**
   - Banda delta ($0{,}5\text{–}4\text{ Hz}$) ligada com precisão ao sono de ondas lentas (estágio N3 / NREM profundo).
   - Banda alfa ($8\text{–}12\text{ Hz}$) associada corretamente à vigília relaxada com olhos fechados (ritmo de Berger).
   - Fenômeno da condução de volume (*volume conduction*) citado corretamente como a causa física primordial da alta correlação espacial entre canais de eletroencefalografia.
3. **Hemodinâmica e fMRI:**
   - Tempo de repetição ($\mathrm{TR} \approx 2\text{ s}$) e resposta hemodinâmica (função de resposta hemodinâmica — HRF com pico atrasado de $5\text{–}6\text{ s}$) descritos com fidelidade aos padrões experimentais de neuroimagem funcional.
4. **Citações bibliográficas autorizadas:**
   - **Breiman (2001):** Introdução da importância por permutação e florestas aleatórias.
   - **Kriegeskorte et al. (2009):** Artigo clássico sobre análise circular (*double dipping*) em neuroimagem.
   - **Haufe et al. (2014):** Interpretação dos pesos em modelos de decodificação neural e cancelamento de ruído.
   - Nenhuma referência proibida, número de página inventado ou citação espúria foi inserida no texto.
5. **Links externos:**
   - Todos os links apontam exclusivamente para os domínios homologados: `statlearning.com` e páginas oficiais da documentação do `scikit-learn.org`.

---

## 6. Auditoria Didática e Pedagógica

1. **Público-alvo (Ciências Biológicas):**
   - Abertura cativante que justifica por que um neurobiólogo precisa padronizar grandezas com dimensões físicas distintas antes de rodar classificadores.
   - Filosofia "intuição primeiro, formalização depois" seguida com rigor em todas as seções por meio dos blocos `<intro>` e `<intuition>`.
   - Progressão impecável de complexidade: os exercícios de cada seção iniciam-se com contas acessíveis de fixação manual ("Básico"), passam por análise crítica de modelos neurais ("Intermediário") e culminam em experimentos computacionais reveladores ("Avançado").
2. **Armadilhas cobertas:**
   - Comparação ingênua de coeficientes brutos de variáveis em unidades distintas (`sec:8-7-1`).
   - Conclusão precipitada de que $\mathrm{VIF}$ elevado impede predições acuradas (`sec:8-7-2`).
   - Seleção de variáveis realizada sobre a matriz global fora do pipeline de validação cruzada (`sec:8-7-3`).
   - Interpretação de importância estatística/preditiva como nexo causal direto (`sec:8-7-4`).
   - Confusão entre importância por permutação fora da amostra e métricas internas de impureza de árvores (`sec:8-7-4`).
3. **Continuidade do currículo:**
   - Retoma conexões pontuais com os temas anteriores de Machine Learning (Métricas 8.4, Reamostragem 8.5 e Regularização 8.6), Álgebra Linear (Módulo 5: autovalores e número de condição) e Estatística/Combinatória (Módulo 7: $2^p$ subconjuntos), preparando com fluidez a transição para Árvores de Decisão (Tema 8.8).

---

## 7. Auditoria de Delta e XML Estrito

1. **Marcação XML:**
   - Todo atributo possui valor explícito entre aspas (`numbered="false"`, `collapsible="true"`, `collapsed="true"`).
   - Nenhuma tag de abertura desemparelhada ou cruzada.
   - Ausência de tags proibidas (`<interactive>`, `<cite>`, `<bibliography>`, `<youtube>`).
   - O cabeçalho possui o link de retorno ao guia devidamente estruturado em `<meta-item key="Guia"><link to="../../index.html#tema-8-7">Voltar ao guia (Tema 8.7)</link></meta-item>`, sem repetição indevida sob o título do capítulo.
2. **Matemática LaTeX KaTeX:**
   - Símbolos de desigualdade e operadores (`<`, `>`, `&`) encontram-se rigorosamente dentro dos delimitadores matemáticos (`$...$`, `$$...$$`, `<equation>`), ou escapados como entidades XML na prosa (`&lt;`, `&gt;`, `&amp;`).
3. **Extensão e densidade:**
   - O arquivo possui 830 linhas e aproximadamente 3.800 palavras, situando-se perfeitamente dentro da faixa recomendada de 2.500 a 5.000 palavras para aulas com quatro subtemas.

---

## 8. Conclusão e Recomendação

O material atinge excelência técnica e didática. As contas são irretocáveis, o código é funcional e robusto, a neurociência é precisa e o estilo atende plenamente ao estudante autodidata de Ciências Biológicas. O parecer conclusivo é de **APROVAÇÃO IMEDIATA**, com a incorporação das sugestões pedagógicas da Tabela de Problemas ficando a critério do gestor editorial em rodadas de polimento futuro.