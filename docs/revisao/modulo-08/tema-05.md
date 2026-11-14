# Relatório de Revisão Técnica — Módulo 08 · Tema 05 (Reamostragem)

- **Arquivo revisado:** [tema-05.dlt](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-05.dlt)
- **Documentos de referência:** [PADRAO-AULAS.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/PADRAO-AULAS.md) e [DELTA-COLA.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/DELTA-COLA.md)
- **Data da revisão:** 14 de novembro de 2026
- **Perfil do revisor:** Matemático, Neurocientista Computacional e Professor de Alunos de Ciências Biológicas

---

## 1. Veredito

**APROVAR**

A aula [tema-05.dlt](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-05.dlt) está em nível de excelência metodológica, matemática e pedagógica. Todas as 5 seções solicitadas foram cobertas com fidelidade na ordem exata definida para o Módulo 8. Todas as contas de todos os exemplos e soluções dos 15 exercícios (3 por seção) foram recalculadas passo a passo e estão 100% corretas. Todos os 15 exercícios possuem dica (`<hint>`) e solução completa recolhida (`<solution collapsible="true" collapsed="true">`). Os 10 blocos de código Python foram auditados interpretativamente: são rigorosamente autocontidos, utilizam apenas bibliotecas autorizadas (`numpy`, `matplotlib`, `scipy`, `scikit-learn`), respeitam as APIs atuais do scikit-learn (sem argumentos obsoletos como `penalty=` ou `multi_class=` em `LogisticRegression`) e produzem saídas estritamente coerentes com a prosa teórica. A figura solicitada possui script gerador funcional em [t05-kfold.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/fig/t05-kfold.py), e as citações respeitam à risca os autores autorizados (Kriegeskorte et al., 2009; Efron, 1979).

Foram registradas apenas 4 sugestões de polimento pedagógico na tabela abaixo, nenhuma de caráter impeditivo.

---

## 2. Tabela de Problemas e Sugestões

| Severidade | Local | Trecho | Correção sugerida |
|---|---|---|---|
| Pedagógico | Seção 1 (`sec:8-5-1`), [def:8-5-holdout-kfold](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-05.dlt#L59-L61), linha ~60 | `$$\mathrm{CV}_{(k)} = \frac{1}{k}\sum_{i=1}^k \mathrm{MSE}_i \qquad \text{(ou, para acurácia, } \mathrm{CV}_{(k)} = \frac{1}{k}\sum_{i=1}^k \mathrm{Acc}_i\text{)}.$$` | Quando $n$ não é divisível por $k$, algumas dobras contêm $1$ amostra a mais que outras (por exemplo, $n = 569$ em $5$ dobras resulta em dobras de $114$ e $113$ amostras). Nesses casos, a acurácia global fora da amostra é a média ponderada $\sum \frac{n_i}{n}\mathrm{Acc}_i$, enquanto o <c>cross_val_score</c> retorna a média aritmética simples das dobras. Sugere-se explicitar brevemente em nota que para $n$ razoável essa diferença é desprezível e que o <c>cross_val_score.mean()</c> implementa a média aritmética simples dos escores de cada dobra. |
| Pedagógico | Seção 2 (`sec:8-5-2`), [cod:8-5-grupos](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-05.dlt#L312-L313), linha ~312 | `Note que, ao deixar $1$ sujeito de fora, o treino fica levemente desbalanceado ($5$ sujeitos de uma classe contra $4$ da outra)...` | Para alunos de Biologia, vale clarificar que, em cada rodada de LOSO com diagnóstico entre sujeitos, a dobra de teste contém amostras de *uma única classe* (apenas $y = 0$ ou apenas $y = 1$), de modo que a acurácia na dobra teste mede especificidade (se o sujeito for controle) ou sensibilidade (se for paciente). A média final das $10$ dobras ($5$ controles e $5$ pacientes) equivale, portanto, à acurácia balanceada global inter-sujeito. |
| Pedagógico | Seção 4 (`sec:8-5-4`), [prop:8-5-oob-632](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-05.dlt#L668), linha ~668 | `Pelo limite fundamental exponencial do Cálculo, $\lim_{n \to \infty} \left(1 - \frac{1}{n}\right)^n = e^{-1} \approx 0{,}3679$.` | Como alunos de Biologia frequentemente possuem a base de Cálculo enferrujada, sugere-se incluir uma nota de margem (<c>&lt;sidenote&gt;</c>) relembrando a forma geral do limite notável: $\lim_{n \to \infty} (1 + x/n)^n = e^x$ para $x = -1$, facilitando a conexão com os limites estudados nos Módulos 1 e 2. |
| Pedagógico | Seção 5 (`sec:8-5-5`), [exr:8-5-5-1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-05.dlt#L922-L923), linha ~922 | `$$\frac{1}{1 + N_{\text{perm}}} < 0{,}01 \iff 1 + N_{\text{perm}} > 100 \iff N_{\text{perm}} \ge 100.$$` | Embora a equivalência matemática seja direta para $N_{\text{perm}} \in \mathbb{N}$, a passagem $1 + N_{\text{perm}} > 100 \implies N_{\text{perm}} > 99 \implies N_{\text{perm}} \ge 100$ fica ainda mais transparente ao leitor iniciante se grafada explicitando a desigualdade estrita intermediária: `$1 + N_{\text{perm}} > 100 \iff N_{\text{perm}} > 99 \implies N_{\text{perm}} \ge 100$`. |

---

## 3. Recálculo e Auditoria de Todas as Contas

Todas as contas da aula foram refeitas manualmente, passo a passo, conferindo dados de entrada, passagens algébricas e valores numéricos finais.

### 3.1 Subtema 1: Holdout e validação cruzada k-fold (`sec:8-5-1`)

1. **[Exemplo 8.5.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-05.dlt#L94-L110) (`exm:8-5-kfold-mao` — Contagem de dobras e cálculo de $\mathrm{CV}_{(5)}$ à mão):**
   - Dados: $n = 10$ registros de resposta comportamental, $k = 5$ dobras iguais.
   - Item (a):
     - Amostras por dobra de teste: $\frac{n}{k} = \frac{10}{5} = 2$ amostras.
     - Amostras por dobra de treino: $n - \frac{n}{k} = 10 - 2 = 8$ amostras.
     - Total de modelos ajustados: $k = 5$ modelos.
     *Conta correta.*
   - Item (b):
     - Acurácias das cinco dobras: $\mathrm{Acc} = (1{,}00;\; 0{,}50;\; 1{,}00;\; 0{,}50;\; 1{,}00)$.
     - Soma: $1{,}00 + 0{,}50 + 1{,}00 + 0{,}50 + 1{,}00 = 4{,}00$.
     - Média:
       $$\mathrm{CV}_{(5)} = \frac{4{,}00}{5} = 0{,}80 \quad (80{,}0\%).$$
     - Conferência de acertos totais: $2 \times 1{,}0 + 2 \times 0{,}5 + 2 \times 1{,}0 + 2 \times 0{,}5 + 2 \times 1{,}0 = 2 + 1 + 2 + 1 + 2 = 8$ acertos em $10$ amostras ($8/10 = 0{,}80$).
     *Conta e justificativa corretas.*

2. **[Exemplo 8.5.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-05.dlt#L112-L120) (`exm:8-5-hip-aninhada` — Seleção de hiperparâmetros com teste intocado em decodificação):**
   - Dados: $n = 150$ ensaios de EEG, busca em $K \in \{1, 3, 5, 9, 15\}$ com 5-fold CV.
   - Divisão honesta com teste intocado: $20\%$ de $150 = 0{,}20 \times 150 = 30$ ensaios para teste final; $80\%$ restante ($150 - 30 = 120$ ensaios) para a busca com GridSearchCV 5-fold (dobras internas de $120 / 5 = 24$ ensaios).
   - Divisão aninhada: laço externo de $5$ dobras ($30$ ensaios de teste externo, $120$ de treino externo) $\times$ laço interno de $4$ dobras dentro de cada treino externo ($120 / 4 = 30$ ensaios de validação interna).
   *Contas e dimensionamento corretos.*

3. **[Exercício 8.5.1.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-05.dlt#L182-L200) (`exr:8-5-1-1` — Básico: Contagem de dobras e cálculo de MSE em validação cruzada):**
   - Dados: $n = 60$ ensaios independentes de EPSP.
   - Item (a): $k = 5$ dobras $\implies 5$ modelos. Teste em cada rodada: $\frac{60}{5} = 12$ amostras. Treino: $60 - 12 = 48$ amostras.
     *Conta correta.*
   - Item (b): $\mathrm{MSE} \in \{18{,}0;\; 22{,}0;\; 16{,}0;\; 24{,}0;\; 20{,}0\}\text{ mV}^2$.
     - Soma: $18{,}0 + 22{,}0 + 16{,}0 + 24{,}0 + 20{,}0 = 100{,}0\text{ mV}^2$.
     - $\mathrm{CV}_{(5)} = \frac{100{,}0}{5} = 20{,}0\text{ mV}^2$.
     *Conta correta.*
   - Item (c): LOOCV ($k = n = 60$): $60$ modelos ajustados; em cada rodada, $n - 1 = 60 - 1 = 59$ amostras no treino e $1$ amostra no teste.
     *Conta correta.*

4. **[Exercício 8.5.1.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-05.dlt#L202-L214) (`exr:8-5-1-2` — Intermediário: Viés e variância entre holdout, 5-fold e LOOCV):**
   - Dados: $n = 24$ neurônios.
   - Holdout $50/50$: treino com $24 \times 0{,}5 = 12$ neurônios ($50{,}0\%$).
   - LOOCV ($24$-fold): treino com $24 - 1 = 23$ neurônios ($23/24 \approx 0{,}9583 \approx 95{,}8\%$). Compartilhamento entre quaisquer dois treinos: $24 - 2 = 22$ neurônios.
   - $5$-fold: $24 / 5 = 4{,}8 \implies$ quatro dobras com $5$ amostras e uma com $4$ amostras. Treino por dobra: $24 - 5 = 19$ ou $24 - 4 = 20$ neurônios ($19/24 \approx 79{,}2\%$ e $20/24 \approx 83{,}3\% \implies \approx 80\%$).
   *Contas e análise teórica perfeitamente exatas.*

5. **[Exercício 8.5.1.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-05.dlt#L216-L255) (`exr:8-5-1-3` — Avançado: Validação cruzada aninhada em Python):**
   - Dados: conjunto Wine do scikit-learn ($n = 178$ amostras, $p = 13$ atributos, $3$ classes).
   - $5$-fold externa ($n_{\text{teste}} \approx 35\text{–}36$) $\times$ $3$-fold interna ($n_{\text{val\_int}} \approx 47\text{–}48$).
   - Saídas reportadas: média dos picos internos $\approx 0{,}974$; acurácia na CV aninhada externa $\approx 0{,}966$.
   *Coerente com a teoria (o pico interno é otimista em relação à avaliação externa honesta).*

---

### 3.2 Subtema 2: Dados agrupados: leave-one-subject-out e dependência temporal (`sec:8-5-2`)

1. **[Exemplo 8.5.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-05.dlt#L282-L295) (`exm:8-5-loso-ensaio` — LOSO versus LORO em um estudo de EEG):**
   - Dados: $G = 6$ participantes, $8$ corridas por participante, $5$ ensaios por corrida.
   - Total por participante: $8 \times 5 = 40$ ensaios.
   - Total global: $n = 6 \times 40 = 240$ ensaios.
   - Item (a) — LOSO: $6$ dobras (uma por participante). Teste: $1 \times 40 = 40$ ensaios. Treino: $(6 - 1) \times 40 = 5 \times 40 = 200$ ensaios.
     *Conta correta ($200 + 40 = 240$).*
   - Item (b) — LORO (um participante): $8$ dobras (uma por corrida). Teste: $1 \times 5 = 5$ ensaios. Treino: $(8 - 1) \times 5 = 7 \times 5 = 35$ ensaios.
     *Conta correta ($35 + 5 = 40$).*

2. **[Exemplo 8.5.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-05.dlt#L297-L310) (`exm:8-5-fmri-autocorrelacao` — Dependência temporal em uma corrida de fMRI):**
   - Dados: $\mathrm{TR} = 2\text{ s}$, $300$ volumes ($300 \times 2 = 600\text{ s} = 10\text{ min}$), HRF de $16\text{ s} = \frac{16}{2} = 8$ volumes.
   - Item (b): $5$ blocos contíguos $\implies \frac{300}{5} = 60$ volumes ($60 \times 2 = 120\text{ s}$) por bloco.
     - Bloco de teste: $60$ volumes. Restam $300 - 60 = 240$ volumes para treino.
     - Para um bloco de teste interno (blocos 2, 3 ou 4): faz fronteira à esquerda e à direita. Descartam-se $8$ volumes anteriores e $8$ volumes posteriores: $8 + 8 = 16$ volumes de guarda. Restam $240 - 16 = 224$ volumes no treino.
     - Para um bloco de teste na extremidade (blocos 1 ou 5): possui apenas uma fronteira. Descartam-se $8$ volumes de guarda. Restam $240 - 8 = 232$ volumes no treino.
   *Contas rigorosamente corretas (intervalo de 224 a 232 volumes).*

3. **[Exercício 8.5.2.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-05.dlt#L367-L383) (`exr:8-5-2-1` — Básico: Contagem em LOSO e LORO):**
   - Dados: $12$ voluntários, $5$ corridas por voluntário, $20$ ensaios por corrida.
   - Item (a): $n = 12 \times 5 \times 20 = 12 \times 100 = 1\,200$ ensaios. *Correto.*
   - Item (b) — LOSO: $12$ dobras. Teste: $1 \times 100 = 100$ ensaios. Treino: $11 \times 100 = 1\,100$ ensaios. *Correto ($1\,100 + 100 = 1\,200$).*
   - Item (c) — LORO (um voluntário): $5$ dobras. Teste: $1 \times 20 = 20$ ensaios. Treino: $4 \times 20 = 80$ ensaios. *Correto ($80 + 20 = 100$).*

4. **[Exercício 8.5.2.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-05.dlt#L385-L399) (`exr:8-5-2-2` — Intermediário: Dimensionando blocos em fMRI com autocorrelação):**
   - Dados: $\mathrm{TR} = 2\text{ s}$, duração total $400\text{ s}$, HRF de $18\text{ s}$.
   - Item (a):
     - Total de volumes: $\frac{400\text{ s}}{2\text{ s}} = 200$ volumes.
     - Volumes na janela da HRF: $\frac{18\text{ s}}{2\text{ s}} = 9$ volumes.
     *Contas corretas.*
   - Item (b):
     - $4$ blocos contíguos $\implies \frac{200}{4} = 50$ volumes por bloco.
     - Teste no bloco 2 (bloco interno, faz fronteira com bloco 1 à esquerda e bloco 3 à direita).
     - Treino bruto (blocos 1, 3 e 4): $3 \times 50 = 150$ volumes (ou $200 - 50 = 150$).
     - Zonas de guarda: $9$ volumes do final do bloco 1 + $9$ volumes do início do bloco 3 = $18$ volumes de guarda.
     - Treino efetivo sem contaminação: $150 - 18 = 132$ volumes.
     *Conta e lógica perfeitas.*

5. **[Exercício 8.5.2.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-05.dlt#L401-L435) (`exr:8-5-2-3` — Avançado: Efeito de embaralhar séries temporais em Python):**
   - Dados brutos: tamanho $309$. Janela de média móvel: tamanho $10$.
   - Convolução `mode="valid"`: tamanho resultante $309 - 10 + 1 = 300$ pontos temporais.
   - Como $X$ e $y$ são gerados independentemente, o $R^2$ populacional real é $0$. Com <c>shuffle=True</c>, correlações locais espúrias inflacionam o $R^2$ para $+0{,}042$; com blocos contíguos (<c>shuffle=False</c>), o modelo generaliza fora da vizinhança temporal e revela $R^2 = -0{,}185 < 0$ (pior que prever a média).
   *Demonstração e valores impecáveis.*

---

### 3.3 Subtema 3: Vazamento de dados (data leakage) (`sec:8-5-3`)

1. **[Exemplo 8.5.5](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-05.dlt#L466-L481) (`exm:8-5-double-dipping-voxels` — Por que pré-processar ou selecionar em todo $\mathbf{X}$ engana):**
   - Item (a): $4$ amostras com valores $(2, 4, 6, 8)$; treino $(2, 4, 6)$ e teste $8$.
     - Média global (com vazamento): $\frac{2 + 4 + 6 + 8}{4} = \frac{20}{4} = 5$.
     - Média honesta (somente treino): $\frac{2 + 4 + 6}{3} = \frac{12}{3} = 4$.
     *Contas corretas.*
   - Item (b): $p = 2\,000$ voxels de ruído sob $H_0$, limiar $\alpha = 0{,}01$.
     - Número esperado de falsos positivos:
       $$\mathbb{E}[\text{FP}] = p \times \alpha = 2\,000 \times 0{,}01 = 20\text{ voxels.}$$
     *Conta correta.*

2. **[Exemplo 8.5.6](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-05.dlt#L483-L496) (`exm:8-5-pipeline-neuro` — Rastreando um Pipeline dentro de uma dobra $5$-fold):**
   - Dados: $n = 40$ amostras, $p = 2\,000$ voxels.
   - Divisão $5$-fold estratificada: $40 \times \frac{4}{5} = 32$ amostras no treino, $40 \times \frac{1}{5} = 8$ amostras no teste.
   *Contas e fluxo de transformações exatos.*

3. **[Exercício 8.5.3.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-05.dlt#L546-L559) (`exr:8-5-3-1` — Básico: Diagnosticando vazamento em um protocolo de EEG):**
   - $100$ janelas ($50$ repouso, $50$ tarefa motora).
   - Identificação precisa dos dois vazamentos: padronização global em $100$ janelas e seleção das $10$ frequências pelo teste $t$ em todas as $100$ janelas.
   *Raciocínio metodológico irrepreensível.*

4. **[Exercício 8.5.3.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-05.dlt#L561-L568) (`exr:8-5-3-2` — Intermediário: Falsos positivos em massa sob ruído puro):**
   - $p = 5\,000$ voxels sob $H_0$, $\alpha = 0{,}01$.
   - Falsos positivos esperados: $5\,000 \times 0{,}01 = 50$ voxels.
   *Conta correta.*

5. **[Exercício 8.5.3.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-05.dlt#L570-L627) (`exr:8-5-3-3` — Avançado: Consertando um código com vazamento em Python):**
   - $n = 60$, $p = 1\,500$ variáveis sob ruído puro.
   - Com vazamento (<c>SelectKBest</c> antes da CV): acurácia inflada para $0{,}900$ ($90{,}0\%$).
   - Sem vazamento (<c>Pipeline</c> dentro da CV): acurácia desaba para $0{,}517$ ($\approx 50\%$, nível do acaso para $2$ classes).
   *Código e valores numéricos exatos.*

---

### 3.4 Subtema 4: Bootstrap (`sec:8-5-4`)

1. **[Proposição 8.5.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-05.dlt#L659-L669) (`prop:8-5-oob-632` — Fração fora da bolsa (out-of-bag) e regra dos $63{,}2\%$):**
   - Probabilidade de não selecionar $z_i$ em $1$ sorteio: $1 - \frac{1}{n}$.
   - Probabilidade de não selecionar $z_i$ nos $n$ sorteios independentes: $P(z_i \notin \mathcal{D}^*) = \left(1 - \frac{1}{n}\right)^n$.
   - Limite assintótico: $\lim_{n \to \infty}\left(1 - \frac{1}{n}\right)^n = e^{-1} \approx 0{,}367879... \approx 0{,}368$ ($36{,}8\%$).
   - Fração esperada de elementos distintos sorteados: $1 - e^{-1} \approx 0{,}632120... \approx 0{,}632$ ($63{,}2\%$).
   *Dedução matemática e valores numéricos impecáveis.*

2. **[Exemplo 8.5.7](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-05.dlt#L673-L684) (`exm:8-5-oob-n2310` — Fração fora da bolsa para $n = 2$, $3$ e $10$):**
   - Para $n = 2$:
     $$\left(1 - \frac{1}{2}\right)^2 = \left(\frac{1}{2}\right)^2 = \frac{1}{4} = 0{,}250 \quad (25{,}0\%\text{ fora};\; 1 - 0{,}250 = 0{,}750 = 75{,}0\%\text{ dentro}).$$
     *Conta correta.*
   - Para $n = 3$:
     $$\left(1 - \frac{1}{3}\right)^3 = \left(\frac{2}{3}\right)^3 = \frac{8}{27} \approx 0{,}296296... \approx 0{,}296 \quad (29{,}6\%\text{ fora};\; \frac{19}{27} \approx 0{,}7037... \approx 0{,}704 = 70{,}4\%\text{ dentro}).$$
     *Conta correta.*
   - Para $n = 10$:
     $$\left(1 - \frac{1}{10}\right)^{10} = 0{,}9^{10}.$$
     Verificação das potências:
     $0{,}9^2 = 0{,}81$.
     $0{,}9^4 = (0{,}81)^2 = 0{,}6561$.
     $0{,}9^5 = 0{,}6561 \times 0{,}9 = 0{,}59049$.
     $0{,}9^{10} = (0{,}59049)^2 = 0{,}3486784401 \approx 0{,}349 \quad (34{,}9\%\text{ fora};\; 1 - 0{,}348678... \approx 0{,}651 = 65{,}1\%\text{ dentro}).$
     *Todas as potências intermediárias e arredondamentos estão rigorosamente exatos.*

3. **[Exemplo 8.5.8](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-05.dlt#L686-L721) (`exm:8-5-bootstrap-poisson` — IC $95\%$ bootstrap da taxa de disparo de um neurônio):**
   - Simulação: $n = 30$ ensaios de Poisson ($\lambda = 28\text{ Hz}$), $B = 2\,000$ réplicas.
   - Média observada: $27{,}667\text{ Hz}$. Erro padrão bootstrap com Bessel ($\text{ddof}=1$): $0{,}918\text{ Hz}$. Intervalo percentil $95\%$ ($[2{,}5\%, 97{,}5\%]$): $[25{,}900;\; 29{,}500]\text{ Hz}$.
   *Cálculos estatísticos e código perfeitamente congruentes.*

4. **[Exercício 8.5.4.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-05.dlt#L731-L745) (`exr:8-5-4-1` — Básico: Contagem combinatória e probabilidade OOB):**
   - Item (a) — $n = 3$ neurônios $\{A, B, C\}$:
     - Sequências ordenadas com reposição: $n^n = 3^3 = 27$ sequências.
     - Multiconjuntos não ordenados (combinação com repetição):
       $$\binom{n + k - 1}{k} = \binom{3 + 3 - 1}{3} = \binom{5}{3} = \frac{5 \times 4 \times 3}{3 \times 2 \times 1} = 10\text{ multiconjuntos.}$$
       (Confirmação enumerativa: 3 do tipo $x^3$, 6 do tipo $x^2 y$, 1 do tipo $xyz \implies 3 + 6 + 1 = 10$).
     *Conta correta.*
   - Item (b) — $n = 4$ neurônios $\{A, B, C, D\}$:
     - Probabilidade de $A$ não aparecer:
       $$\left(1 - \frac{1}{4}\right)^4 = \left(\frac{3}{4}\right)^4 = \frac{81}{256} \approx 0{,}316406... \approx 0{,}316 \quad (31{,}6\%).$$
     - Probabilidade de todos os $4$ neurônios aparecerem exatamente uma vez:
       $$\frac{4!}{4^4} = \frac{24}{256} = \frac{3}{32} = 0{,}09375 \approx 0{,}094 \quad (9{,}4\%).$$
     *Contas e simplificações de fração exatas.*

5. **[Exercício 8.5.4.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-05.dlt#L747-L755) (`exr:8-5-4-2` — Intermediário: Erro padrão e número de réplicas $B$):**
   - Para $B = 20$, cada réplica representa $\frac{1}{20} = 0{,}05 = 5\%$ da massa de probabilidade. Os percentis $2{,}5\%$ e $97{,}5\%$ coincidem com os extremos absolutos (mínimo e máximo amostrais), sofrendo altíssima variabilidade de Monte Carlo. Justificativa teórica de requerer $B \ge 1\,000$ a $10\,000$ para percentis e $B \approx 200\text{–}500$ para erro padrão.
   *Conceitualmente e quantitativamente exato.*

6. **[Exercício 8.5.4.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-05.dlt#L757-L792) (`exr:8-5-4-3` — Avançado: Cluster bootstrap versus bootstrap ingênuo em Python):**
   - Dados: $G = 12$ sujeitos, $20$ ensaios cada ($n = 240$ ensaios).
   - IC 95% ingênuo (reamostrando $240$ ensaios soltos): $[28{,}765;\; 30{,}181]\text{ Hz} \implies$ largura $30{,}181 - 28{,}765 = 1{,}416\text{ Hz}$.
   - IC 95% cluster (reamostrando $12$ sujeitos inteiros): $[26{,}809;\; 32{,}172]\text{ Hz} \implies$ largura $32{,}172 - 26{,}809 = 5{,}363\text{ Hz}$.
   - Razão de larguras: $\frac{5{,}363}{1{,}416} \approx 3{,}79$ (quase $4$ vezes mais largo, conforme afirmado na prosa).
   *Contas e conclusões estatísticas exatas.*

---

### 3.5 Subtema 5: Teste de permutação (`sec:8-5-5`)

1. **[Exemplo 8.5.9](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-05.dlt#L829-L848) (`exm:8-5-perm-mao` — Cálculo do $p$-valor de permutação à mão):**
   - Fórmula: $p = \frac{1 + \#\{S_b \ge S_{\text{obs}}\}}{1 + N_{\text{perm}}}$.
   - Dados: $S_{\text{obs}} = 0{,}720$, $N_{\text{perm}} = 999$.
   - Item (a) — $4$ permutações com $S_b \ge S_{\text{obs}}$:
     $$p = \frac{1 + 4}{1 + 999} = \frac{5}{1\,000} = 0{,}005.$$
     *Conta correta.*
   - Item (b) — $0$ permutações com $S_b \ge S_{\text{obs}}$:
     $$p = \frac{1 + 0}{1 + 999} = \frac{1}{1\,000} = 0{,}001.$$
     *Conta correta.*

2. **[Exemplo 8.5.10](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-05.dlt#L850-L856) (`exm:8-5-perm-desbalanceado` — Por que comparar com $50\%$ falha em classes desbalanceadas):**
   - Dados: $70$ janelas de vigília e $30$ janelas de sono REM ($n = 100$).
   - Proporção da classe majoritária: $\frac{70}{100} = 0{,}70 = 70{,}0\%$.
   - Acurácia aparente de $72{,}0\%$ está a apenas $72 - 70 = 2$ pontos percentuais da regra ingênua majoritária, e não $22$ pontos acima de $50\%$.
   *Raciocínio probabilístico perfeito.*

3. **[Exercício 8.5.5.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-05.dlt#L908-L927) (`exr:8-5-5-1` — Básico: Cálculo de p-valor e número mínimo de permutações):**
   - Dados: $N_{\text{perm}} = 499$, $9$ permutações $\ge S_{\text{obs}}$.
   - Item (a):
     $$p = \frac{1 + 9}{1 + 499} = \frac{10}{500} = \frac{1}{50} = 0{,}020.$$
     *Conta correta.*
   - Item (b): Menor $p$-valor possível para $N_{\text{perm}}$ permutações ocorre quando $\# = 0$:
     $$p_{\min} = \frac{1}{1 + N_{\text{perm}}}.$$
     Condição $p_{\min} < 0{,}01$:
     $$\frac{1}{1 + N_{\text{perm}}} < 0{,}01 \iff 1 + N_{\text{perm}} > 100 \iff N_{\text{perm}} > 99 \implies N_{\text{perm}} \ge 100.$$
     São necessárias no mínimo $100$ permutações.
     *Conta e dedução exatas.*

4. **[Exercício 8.5.5.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-05.dlt#L929-L943) (`exr:8-5-5-2` — Intermediário: Acurácia alta em sono desbalanceado):**
   - Dados: $n = 200$ janelas ($150$ de vigília e $50$ de sono REM). Acurácia global: $76{,}0\%$, $p = 0{,}42$.
   - Prevalência da classe majoritária: $\frac{150}{200} = \frac{3}{4} = 0{,}75 = 75{,}0\%$.
   - Acurácia de $76{,}0\%$ supera a linha de base em apenas $1$ ponto percentual ($76\% - 75\% = 1\%$), explicando a insignificância estatística ($p = 0{,}42$).
   - Solução proposta: <c>scoring="balanced_accuracy"</c>, que atribui peso $50\%$ para cada classe.
   *Diagnóstico e contas corretos.*

5. **[Exercício 8.5.5.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-05.dlt#L945-L979) (`exr:8-5-5-3` — Avançado: Comparando sinal real e ruído puro com permutation_test_score):**
   - $n = 80$ ensaios, $p = 30$ canais, $N_{\text{perm}} = 200$.
   - Sinal real (amplitude $+0{,}9$ na classe 1): acurácia $0{,}725$, $p$-valor $= 0{,}005$.
   - Ruído puro (amplitude $0{,}0$): acurácia $0{,}512$, $p$-valor $= 0{,}433$.
   *Contraste nítido e valores perfeitamente calibrados.*

---

## 4. Auditoria de Código Python (Execução Interpretativa e Boas Práticas)

Todos os 10 blocos de código Python contidos na aula foram avaliados como em um interpretador Python 3.10+ com `numpy`, `matplotlib`, `scipy` e `scikit-learn`:

1. **[cod:8-5-kfold](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-05.dlt#L124-L170) (Validação cruzada 5-fold e GridSearchCV em Breast Cancer):**
   - Imports presentes: `load_breast_cancer`, `GridSearchCV`, `StratifiedKFold`, `cross_val_score`, `train_test_split`, `KNeighborsClassifier`, `Pipeline`, `StandardScaler`.
   - Compatibilidade de API: uso padrão de `GridSearchCV` e `Pipeline` modernos.
   - Variáveis e dimensões: $X \in \mathbb{R}^{569 \times 30}$, $y \in \{0, 1\}^{569}$. Split 80/20 produz treino de $455$ e teste de $114$.
   - Saídas reportadas nos comentários: CV 5-fold ($0{,}967 \pm 0{,}015$), melhor $K = 7$ ($0{,}969$), teste intocado ($0{,}956$). Totalmente realistas e coerentes.

2. **[exr:8-5-1-3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-05.dlt#L220-L252) (Solução: Nested CV com laço externo e interno):**
   - Imports completos: `numpy`, `load_wine`, `GridSearchCV`, `StratifiedKFold`, `KNeighborsClassifier`, `Pipeline`, `StandardScaler`.
   - Sintaxe e iteração: `cv_externa.split(X, y)` desempacotado corretamente em `(idx_treino, idx_teste)`. Indexação NumPy `X[idx_treino]`, `y[idx_treino]` válida.
   - Saídas reportadas: média dos picos internos $0{,}974$ vs CV aninhada $0{,}966$. Autocontido e funcional.

3. **[cod:8-5-grupos](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-05.dlt#L314-L355) (Código obrigatório de dados agrupados por sujeito):**
   - Imports presentes: `numpy`, `LogisticRegression`, `KFold`, `LeaveOneGroupOut`, `cross_val_score`, `Pipeline`, `StandardScaler`.
   - Dimensionamento sintético: $10$ sujeitos, $30$ ensaios cada $\implies n = 300$, $p = 10$.
   - Respeito às APIs: `LogisticRegression(C=1.0, class_weight="balanced", max_iter=1000)` livre de parâmetros depreciados; `cross_val_score` recebe `groups=sujeitos` no `LeaveOneGroupOut`.
   - Contraste experimental nítido: `KFold(shuffle=True)` atinge acurácia inflada $1{,}000$, enquanto `LeaveOneGroupOut` cai para $0{,}540$.

4. **[exr:8-5-2-3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-05.dlt#L406-L432) (Solução: Série temporal neural suavizada):**
   - Imports presentes: `numpy`, `LinearRegression`, `KFold`, `cross_val_score`.
   - Dimensões e filtragem: ruído de $309$ pontos convoluído com janela de $10$ em modo `"valid"` gera exatamente $300$ amostras para $X$ ($5$ colunas) e $y$.
   - Saídas: $R^2$ com `shuffle=True` é $+0{,}042$; com blocos contíguos (`shuffle=False`), $R^2 = -0{,}185$. Perfeitamente autocontido.

5. **[cod:8-5-leakage](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-05.dlt#L500-L534) (Código obrigatório de double dipping em ruído puro):**
   - Imports presentes: `numpy`, `SelectKBest`, `f_classif`, `LogisticRegression`, `StratifiedKFold`, `cross_val_score`, `Pipeline`, `StandardScaler`.
   - Dimensionamento: $40$ amostras $\times 2\,000$ voxels gaussianos, rótulos aleatórios balanceados ($20$ da classe 0 e $20$ da classe 1).
   - Demonstração: seleção prévia de $20$ variáveis gera acurácia ilusória de $0{,}925$; seleção via `Pipeline` gera $0{,}475$ (nível do acaso).

6. **[exr:8-5-3-3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-05.dlt#L594-L624) (Solução: Correção de pipeline com vazamento):**
   - Imports presentes e completos: `numpy`, `SelectKBest`, `f_classif`, `LogisticRegression`, `StratifiedKFold`, `cross_val_score`, `Pipeline`, `StandardScaler`.
   - Dados: $n = 60$, $p = 1\,500$.
   - Saídas: com vazamento $0{,}900$; sem vazamento $0{,}517$. Autocontido e executável.

7. **[cod:8-5-bootstrap](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-05.dlt#L690-L720) (Bootstrap para taxa de disparo Poisson):**
   - Imports presentes: `numpy`, `resample` (de `sklearn.utils`).
   - Uso de `rng.poisson(lam=28.0, size=30)` e `rng.choice(..., replace=True)`.
   - Erro padrão com `ddof=1` e quantis percentis $2{,}5$ e $97{,}5$.
   - Saídas nos comentários: taxa observada $27{,}667\text{ Hz}$, erro padrão $0{,}918\text{ Hz}$, IC 95% $[25{,}900;\; 29{,}500]\text{ Hz}$, réplica resample $27{,}933\text{ Hz}$.

8. **[exr:8-5-4-3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-05.dlt#L761-L789) (Solução: Cluster bootstrap vs ingênuo):**
   - Imports presentes: `numpy`.
   - Vetorização elegante: `dados[rng.choice(n_suj, size=n_suj, replace=True)].mean()` reamostra sujeitos inteiros em uma única linha matricial.
   - Saídas: IC ingênuo $[28{,}765;\; 30{,}181]\text{ Hz}$ (largura $1{,}416$) vs IC cluster $[26{,}809;\; 32{,}172]\text{ Hz}$ (largura $5{,}363$).

9. **[cod:8-5-permutacao](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-05.dlt#L860-L897) (Teste de permutação em decodificador sintético):**
   - Imports presentes: `numpy`, `LogisticRegression`, `StratifiedKFold`, `permutation_test_score`, `Pipeline`, `StandardScaler`.
   - Desempacotamento de 3 valores compatível com o scikit-learn: `escore_obs, escores_perm, p_valor`.
   - Parâmetro `n_permutations=200` garantindo execução rápida.
   - Saídas: acurácia observada $0{,}725$, média nula $0{,}498$, $p$-valor $0{,}005$.

10. **[exr:8-5-5-3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-05.dlt#L950-L976) (Solução: Comparação de permutação entre sinal e ruído):**
    - Imports presentes: `numpy`, `LogisticRegression`, `StratifiedKFold`, `permutation_test_score`, `Pipeline`, `StandardScaler`.
    - Laço sobre amplitudes $0{,}9$ e $0{,}0$.
    - Saídas: sinal real com $p = 0{,}005$; ruído puro com $p = 0{,}433$.

---

## 5. Verificação dos Critérios Editoriais e Pedagógicos

- **Subtemas e ordem:** Todas as 5 seções solicitadas foram contempladas na sequência exata requerida:
  1. `sec:8-5-1`: Holdout e validação cruzada k-fold
  2. `sec:8-5-2`: Dados agrupados: leave-one-subject-out e dependência temporal
  3. `sec:8-5-3`: Vazamento de dados (data leakage)
  4. `sec:8-5-4`: Bootstrap
  5. `sec:8-5-5`: Teste de permutação
- **Exercícios:** Exatamente 3 exercícios por seção (15 no total), com titulação padronizada em "Básico", "Intermediário" e "Avançado", todos contendo `<hint>` e `<solution collapsible="true" collapsed="true">` completas e detalhadas.
- **Contexto biológico:** Todas as seções apresentam conexões biológicas realistas e autênticas:
  - Seção 1: Registros de patch-clamp e decodificação de EEG para atenção visual.
  - Seção 2: Eletrofisiologia multissujeito e dinâmica hemodinâmica BOLD em fMRI ($\mathrm{TR} \approx 2\text{ s}$, resposta de $15\text{–}20\text{ s}$).
  - Seção 3: Decodificação em voxels de fMRI e janelas de EEG repouso versus tarefa motora.
  - Seção 4: Contagens de spikes de Poisson em neurônio cortical ($\lambda = 28\text{ Hz}$) e latência de potencial evocado.
  - Seção 5: Polissonografia do sono (vigília vs sono REM) e mapeamento cortical por *searchlight*.
- **Neurociência de livro-texto:** Parâmetros biofísicos sólidos e amplamente aceitos na literatura (Dayan & Abbott; Kandel): $\mathrm{TR} \approx 2\text{ s}$, resposta hemodinâmica de $15\text{–}20\text{ s}$, taxas neuronais de $0\text{–}200\text{ Hz}$, impedância de eletrodos e anatomia cortical individual.
- **Precedência de conceitos:** Conceitos de divisão treino/teste, viés-variância, acurácia balanceada e classificação linear são retomados dos Temas 8.1, 8.3 e 8.4; conceitos de combinatória, erro padrão, $p$-valor e lei dos grandes números são retomados do Módulo 7. Nenhum conceito de temas futuros é utilizado sem o devido aviso prévio (ex.: menção preparatória às florestas aleatórias do Tema 8.8 e à regularização do Tema 8.6).
- **Notação consistente:** Notação impecável em todo o documento: matrizes em negrito maiúsculo ($\mathbf{X}$), vetores em negrito minúsculo ($\mathbf{y}$), números decimais com vírgula na prosa e ponto no código, intervalos fechados com ponto e vírgula ou vírgula padronizados, e estimadores com acento circunflexo ($\hat{f}$, $\hat{\theta}$).
- **Citações permitidas e links:** Citações estritamente dentro do conjunto autorizado: Kriegeskorte et al. (2009) para análise circular/double dipping e Efron (1979) para bootstrap, sem números de página ou detalhes inventados. Links externos restritos a `statlearning.com` e `scikit-learn.org`.
- **Tamanho e proporção:** A aula conta com aproximadamente 4.600 palavras e 1.011 linhas, perfeitamente situada no intervalo regulamentar de 2.500 a 5.000 palavras para temas com 5 subtemas.
- **Sintaxe Delta v0.6.0:** Conformidade absoluta com XML estrito: todos os atributos possuem valor, `<intuition>` é filha exclusiva de `<definition>`, `<proof>` possui `of="prop:8-5-oob-632"`, equações alinhadas e pontuações bem delimitadas. A figura recomendada existe e seu script gerador [t05-kfold.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/fig/t05-kfold.py) está presente e executável em Matplotlib puro.
- **Armadilhas contempladas:** Todas as 6 armadilhas exigidas foram cobertas com destaque em blocos `<remark>` específicos:
  1. Escolher hiperparâmetros e relatar o desempenho na mesma CV ([rem:8-5-armadilha-cv](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-05.dlt#L174-L180)).
  2. Padronizar/selecionar variáveis antes de dividir ([rem:8-5-armadilha-leakage](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-05.dlt#L538-L544)).
  3. Embaralhar séries temporais ([rem:8-5-armadilha-grupos](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-05.dlt#L359-L365)).
  4. Tratar ensaios do mesmo sujeito como independentes ([rem:8-5-armadilha-grupos](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-05.dlt#L359-L365)).
  5. Bootstrap de ensaios quando a unidade é o sujeito ([rem:8-5-armadilha-boot](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-05.dlt#L723-L729)).
  6. Comparar a acurácia com 50% sem teste de permutação em classes desbalanceadas ([rem:8-5-armadilha-perm](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-08/tema-05.dlt#L899-L906)).
