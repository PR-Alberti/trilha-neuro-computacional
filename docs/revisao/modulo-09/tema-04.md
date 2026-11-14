# Relatório de Revisão Técnica — Módulo 09 · Tema 04 (Representações)

- **Arquivo revisado:** [tema-04.dlt](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-04.dlt)
- **Documentos de referência:** [PADRAO-AULAS.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/PADRAO-AULAS.md) e [DELTA-COLA.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/DELTA-COLA.md)
- **Data da revisão:** 14 de novembro de 2026
- **Perfil do revisor:** Matemático, Neurocientista Computacional, Especialista em Deep Learning/PyTorch e Professor de Alunos de Ciências Biológicas

---

## 1. Veredito

**APROVAR**

A aula [conteudo/modulo-09/tema-04.dlt](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-04.dlt) cumpre com rigor e excelência todos os requisitos pedagógicos, matemáticos, neurobiológicos e computacionais estabelecidos nas diretrizes editoriais do curso. Apresenta o tema complexo de representações densas, aprendizado não supervisionado por variedades e comparação de modelos profundos com dados cerebrais (RSA) de forma clara, gradual e matematicamente exata para estudantes de Ciências Biológicas.

Principais conclusões da auditoria:
1. **Exatidão matemática estrita:** Todas as contas de todos os exemplos e das resoluções dos 16 exercícios foram integralmente refeitas à mão; 100% das operações matriciais, distâncias euclidianas, similaridades de cosseno, correlações de Pearson e Spearman conferem rigorosamente sem qualquer inconsistência numérica.
2. **Código Python auditado linha a linha:** Todos os blocos executáveis (<c>cod:9-4-embedding-pytorch</c>, <c>cod:9-4-ae-digits</c>, <c>cod:9-4-matriz-similaridade</c>, <c>cod:9-4-rsa-digits</c> e os scripts das soluções dos exercícios 9.4.3.4 e 9.4.4.4) são autocontidos, utilizam tensores, matrizes e dtypes apropriados (<c>float32</c>/<c>long</c>), respeitam as APIs atuais do PyTorch 2.x e do scikit-learn 1.x, e trazem saídas comentadas fiéis e reprodutíveis em CPU. O teste de permutação implementado para RSA (<c>np.ix_(perm, perm)</c>) segue o padrão estatístico correto da literatura.
3. **Neurociência de livro-texto e citações canônicas:** O texto contextualiza adequadamente o código populacional em taxas de disparo (Dayan &amp; Abbott; Kandel), o funil anatômico da retina aos axônios do nervo óptico (~100:1), as variedades neurais de baixa dimensão no córtex motor e a geometria representacional no córtex inferotemporal (IT). Todas as citações bibliográficas são autênticas e históricas: Baldi &amp; Hornik (1989), Mikolov et al. (2013), Kriegeskorte, Mur &amp; Bandettini (2008, *Frontiers in Systems Neuroscience*) e Kriegeskorte et al. (2008, *Neuron*).
4. **Estrutura e conformidade editorial:** Cobre integralmente as 4 seções temáticas solicitadas ("Embeddings: de símbolos a vetores", "Espaço latente e autoencoders", "Medindo semelhança: cosseno, distância e correlação", "RSA: comparando modelos e cérebros"), complementadas por "Resumo" e "Para ir além". Todos os 16 exercícios possuem dica (<c>&lt;hint&gt;</c>) e solução passo a passo completa e recolhida por padrão (<c>&lt;solution collapsible="true" collapsed="true"&gt;</c>). A figura vetorial [fig/t04-rdm.svg](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/fig/t04-rdm.svg) existe, está associada ao script gerador [fig/t04-rdm.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/fig/t04-rdm.py) e cumpre todas as normas de estilo (sem texto embutido em curvas, rótulos legíveis em português e fundo transparente). O texto totaliza aproximadamente 4.100 palavras de prosa, perfeitamente calibrado dentro da faixa exigida de 3.500 a 5.000 palavras.

A tabela a seguir registra 3 observações pontuais de natureza estritamente pedagógica para enriquecer ainda mais o material em iterações futuras, sem necessidade de bloqueio ou reformulação.

---

## 2. Tabela de Problemas e Sugestões

| Severidade | Local | Trecho | Correção sugerida |
|---|---|---|---|
| Pedagógico | Seção 2 (`sec:9-4-2`), `cod:9-4-ae-digits`, linha ~253–277 | `pca.fit_transform(X_np)` e `autoencoder(X_t)` | No script comparativo, tanto a PCA quanto o autoencoder são ajustados sobre a totalidade de `load_digits` sem divisão em conjunto de treino/teste. Embora esse procedimento seja metodologicamente padrão para comparar a capacidade intrínseca de reconstrução e compressão não supervisionada de um espaço fixo (variedade curva vs. hiperplano), alunos de Biologia acostumados com a divisão obrigatória de treino/teste (estudada nos Módulos 8 e 9.1) podem estranhar a ausência de validação cruzada. Sugere-se inserir um breve comentário no código ou na prosa esclarecendo: *“Aqui avaliamos a capacidade geométrica de compressão sobre o conjunto completo; em aplicações preditivas ou gerativas, emprega-se divisão de treino/validação para evitar sobreajuste (*overfitting*).”* |
| Pedagógico | Seção 3 (`sec:9-4-3`), `tbl:9-4-invariancias`, linha ~357–388 | Coluna `Invariante a \alpha\mathbf{u} (\alpha > 0)?` | A tabela e o texto especificam corretamente a invariância a ganhos estritamente positivos ($\alpha > 0$). Para consolidar a intuição matemática de discentes, convém registrar em nota de rodapé ou na legenda da tabela o que ocorre sob reflexão de sinal ($\alpha < 0$): tanto o cosseno quanto Pearson invertem o sinal ($\cos(-\mathbf{u}, \mathbf{v}) = -\cos(\mathbf{u}, \mathbf{v})$ e $r(-\mathbf{u}, \mathbf{v}) = -r(\mathbf{u}, \mathbf{v})$), indicando perfis perfeitamente anti-alinhados, enquanto a distância euclidiana cresce monotonicamente. |
| Pedagógico | Seção 4 (`sec:9-4-4`), `def:9-4-rdm`, linha ~523 | `$D_{ij} = 1 - r(\mathbf{r}_i, \mathbf{r}_j) \in [0, 2]$` | A definição adota $1 - r$ de Pearson como a métrica canônica de dissimilaridade da RSA clássica (Kriegeskorte et al., 2008), o que é ideal por cancelar variações basais e ganhos globais de excitabilidade. Para conectar a aula a *toolboxes* modernas de neuroimagem computacional (como o `rsatoolbox`), sugere-se incluir uma frase indicando que, embora $1 - r$ seja a formulação mais difundida, certas aplicações utilizam distância euclidiana, distância de cosseno ou distância de Mahalanobis cruzada (*crossnobis*), conforme a pergunta fisiológica em estudo. |

---

## 3. Recálculo e Auditoria de Todas as Contas

Todas as deduções, multiplicações matriciais, normas, distâncias e correlações da aula foram recalculadas à mão passo a passo. Abaixo registra-se a conferência pormenorizada de cada elemento matemático.

### 3.1 Subtema 1: Embeddings: de símbolos a vetores (`sec:9-4-1`)

1. **[Proposição 9.4.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-04.dlt#L67-L74) (`prop:9-4-lookup` — Propriedades da Consulta One-Hot):**
   - Dada $\mathbf{E} \in \mathbb{R}^{V \times d}$ com linhas $\mathbf{e}_k^\top$, as colunas de $\mathbf{E}^\top$ são $\mathbf{e}_1, \dots, \mathbf{e}_V$.
   - O produto $\mathbf{E}^\top \mathbf{o}_i = \sum_{k=1}^V o_{i,k} \mathbf{e}_k = 1 \cdot \mathbf{e}_i = \mathbf{e}_i$.
   - Para $i \ne j$, os índices unitários não se sobrepõem: $\mathbf{o}_i^\top \mathbf{o}_j = 0$.
   - A diferença $\mathbf{o}_i - \mathbf{o}_j$ possui uma coordenada $+1$ no índice $i$, uma coordenada $-1$ no índice $j$ e zero nas demais:
     $$\|\mathbf{o}_i - \mathbf{o}_j\|_2 = \sqrt{1^2 + (-1)^2 + 0} = \sqrt{2} \approx 1{,}4142.$$
     *Deduções e propriedades exatas.*

2. **[Exemplo 9.4.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-04.dlt#L86-L98) (`exm:9-4-lookup-mao` — Multiplicação one-hot e distâncias à mão):**
   - Matriz $\mathbf{E} \in \mathbb{R}^{4 \times 3}$:
     $$\mathbf{E} = \begin{pmatrix} 0{,}8 & 0{,}6 & 0{,}1 \\ 0{,}7 & 0{,}7 & 0{,}2 \\ -0{,}5 & 0{,}2 & 0{,}9 \\ -0{,}4 & 0{,}1 & 0{,}8 \end{pmatrix}.$$
   - Com $\mathbf{o}_2 = (0, 1, 0, 0)^\top$, $\mathbf{e}_2 = \mathbf{E}^\top \mathbf{o}_2 = (0{,}7;\; 0{,}7;\; 0{,}2)^\top$, idêntico à 2ª linha de $\mathbf{E}$.
   - Distância $\|\mathbf{e}_1 - \mathbf{e}_2\|_2$:
     $$\|\mathbf{e}_1 - \mathbf{e}_2\|_2 = \sqrt{(0{,}8 - 0{,}7)^2 + (0{,}6 - 0{,}7)^2 + (0{,}1 - 0{,}2)^2} = \sqrt{0{,}01 + 0{,}01 + 0{,}01} = \sqrt{0{,}03} \approx 0{,}173205 \approx 0{,}173.$$
   - Distância $\|\mathbf{e}_1 - \mathbf{e}_3\|_2$:
     $$\|\mathbf{e}_1 - \mathbf{e}_3\|_2 = \sqrt{(0{,}8 - (-0{,}5))^2 + (0{,}6 - 0{,}2)^2 + (0{,}1 - 0{,}9)^2} = \sqrt{1{,}3^2 + 0{,}4^2 + (-0{,}8)^2} = \sqrt{1{,}69 + 0{,}16 + 0{,}64} = \sqrt{2{,}49} \approx 1{,}57797 \approx 1{,}578.$$
   - Razão de distâncias: $1{,}57797 / 0{,}173205 \approx 9{,}11$ (aproximadamente 9 vezes mais próximos).
     *Todas as contas fechadas com exatidão.*

3. **[Exemplo 9.4.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-04.dlt#L100-L108) (`exm:9-4-codigo-populacional` — Código populacional olfatório em 4 neurônios):**
   - Padrões: $\mathbf{r}(s_1) = (45, 38, 5, 2)^\top$, $\mathbf{r}(s_2) = (40, 42, 8, 3)^\top$, $\mathbf{r}(s_3) = (4, 6, 52, 48)^\top$.
   - $\|\mathbf{r}(s_1) - \mathbf{r}(s_2)\|_2$:
     $$\sqrt{(45-40)^2 + (38-42)^2 + (5-8)^2 + (2-3)^2} = \sqrt{5^2 + (-4)^2 + (-3)^2 + (-1)^2} = \sqrt{25 + 16 + 9 + 1} = \sqrt{51} \approx 7{,}1414 \approx 7{,}14\text{ Hz}.$$
   - $\|\mathbf{r}(s_1) - \mathbf{r}(s_3)\|_2$:
     $$\sqrt{(45-4)^2 + (38-6)^2 + (5-52)^2 + (2-48)^2} = \sqrt{41^2 + 32^2 + (-47)^2 + (-46)^2} = \sqrt{1\,681 + 1\,024 + 2\,209 + 2\,116} = \sqrt{7\,030} \approx 83{,}845 \approx 83{,}85\text{ Hz}.$$
     *Contas e unidades corretas.*

4. **[Exercício 9.4.1.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-04.dlt#L144-L153) (`exr:9-4-1-1` — Consulta e distâncias em nucleotídeos à mão):**
   - $\mathbf{E} = \begin{pmatrix} 1{,}0 & 0{,}2 \\ 0{,}8 & 0{,}4 \\ -0{,}6 & 0{,}9 \end{pmatrix}$, $\mathbf{o}_3 = (0, 0, 1)^\top \implies \mathbf{e}_3 = (-0{,}6;\; 0{,}9)^\top$.
   - $\|\mathbf{e}_1 - \mathbf{e}_2\|_2 = \sqrt{(1{,}0 - 0{,}8)^2 + (0{,}2 - 0{,}4)^2} = \sqrt{0{,}04 + 0{,}04} = \sqrt{0{,}08} \approx 0{,}28284 \approx 0{,}283$.
   - $\|\mathbf{e}_1 - \mathbf{e}_3\|_2 = \sqrt{(1{,}0 - (-0{,}6))^2 + (0{,}2 - 0{,}9)^2} = \sqrt{1{,}6^2 + (-0{,}7)^2} = \sqrt{2{,}56 + 0{,}49} = \sqrt{3{,}05} \approx 1{,}7464 \approx 1{,}746$.
     *Contas exatas.*

5. **[Exercício 9.4.1.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-04.dlt#L155-L162) (`exr:9-4-1-2` — Parâmetros de nn.Embedding em genômica):**
   - $V = 20\,000$ genes, dimensão latente $d = 32$.
   - Total de parâmetros: $20\,000 \times 32 = 640\,000$ pesos (camada sem viés).
   - Fator de redução dimensional: $\frac{20\,000}{32} = 625$ vezes.
     *Contas exatas.*

6. **[Exercício 9.4.1.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-04.dlt#L164-L176) (`exr:9-4-1-3` — Código populacional em V1):**
   - $\mathbf{r}(0^\circ) = (60, 20, 4)^\top$, $\mathbf{r}(15^\circ) = (54, 28, 4)^\top$, $\mathbf{r}(90^\circ) = (4, 16, 64)^\top$.
   - $d(0^\circ, 15^\circ) = \sqrt{(60-54)^2 + (20-28)^2 + 0^2} = \sqrt{36 + 64} = \sqrt{100} = 10{,}0\text{ Hz}$.
   - $d(0^\circ, 90^\circ) = \sqrt{(60-4)^2 + (20-16)^2 + (4-64)^2} = \sqrt{56^2 + 4^2 + (-60)^2} = \sqrt{3\,136 + 16 + 3\,600} = \sqrt{6\,752} \approx 82{,}1705 \approx 82{,}17\text{ Hz}$.
   - $d(15^\circ, 90^\circ) = \sqrt{(54-4)^2 + (28-16)^2 + (4-64)^2} = \sqrt{50^2 + 12^2 + (-60)^2} = \sqrt{2\,500 + 144 + 3\,600} = \sqrt{6\,244} \approx 79{,}0189 \approx 79{,}02\text{ Hz}$.
     *Contas exatas.*

7. **[Exercício 9.4.1.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-04.dlt#L178-L185) (`exr:9-4-1-4` — Invariância ortogonal de embeddings):**
   - Matriz ortogonal $\mathbf{Q} \in \mathbb{R}^{d \times d}$ com $\mathbf{Q}^\top \mathbf{Q} = \mathbf{I}_d$.
   - Produto interno: $\tilde{\mathbf{e}}_i^\top \tilde{\mathbf{e}}_j = (\mathbf{Q}\mathbf{e}_i)^\top (\mathbf{Q}\mathbf{e}_j) = \mathbf{e}_i^\top \mathbf{Q}^\top \mathbf{Q} \mathbf{e}_j = \mathbf{e}_i^\top \mathbf{I}_d \mathbf{e}_j = \mathbf{e}_i^\top \mathbf{e}_j$.
   - Norma euclidiana da diferença com $\mathbf{u} = \mathbf{e}_i - \mathbf{e}_j$:
     $$\|\tilde{\mathbf{e}}_i - \tilde{\mathbf{e}}_j\|_2^2 = \|\mathbf{Q}\mathbf{u}\|_2^2 = (\mathbf{Q}\mathbf{u})^\top (\mathbf{Q}\mathbf{u}) = \mathbf{u}^\top \mathbf{Q}^\top \mathbf{Q} \mathbf{u} = \mathbf{u}^\top \mathbf{u} = \|\mathbf{e}_i - \mathbf{e}_j\|_2^2.$$
     *Demonstração formal perfeita.*

---

### 3.2 Subtema 2: Espaço latente e autoencoders (`sec:9-4-2`)

1. **[Exemplo 9.4.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-04.dlt#L223-L233) (`exm:9-4-ae-linear-mao` — Autoencoder linear à mão):**
   - Entrada: $\mathbf{x} = (2,\; 4,\; -2)^\top$.
   - Codificador: $\mathbf{W}_1 = \begin{pmatrix} 0{,}5 & 0{,}5 & -0{,}5 \end{pmatrix}$.
     $$h = 0{,}5(2) + 0{,}5(4) - 0{,}5(-2) = 1{,}0 + 2{,}0 + 1{,}0 = 4{,}0.$$
   - Decodificador: $\mathbf{W}_2 = (0{,}6;\; 1{,}2;\; -0{,}6)^\top$.
     $$\hat{\mathbf{x}} = 4{,}0 \begin{pmatrix} 0{,}6 \\ 1{,}2 \\ -0{,}6 \end{pmatrix} = \begin{pmatrix} 2{,}4 \\ 4{,}8 \\ -2{,}4 \end{pmatrix}.$$
   - Vetor de erro: $\mathbf{x} - \hat{\mathbf{x}} = (2 - 2{,}4;\; 4 - 4{,}8;\; -2 - (-2{,}4))^\top = (-0{,}4;\; -0{,}8;\; 0{,}4)^\top$.
   - Perda quadrática total:
     $$\|\mathbf{x} - \hat{\mathbf{x}}\|_2^2 = (-0{,}4)^2 + (-0{,}8)^2 + 0{,}4^2 = 0{,}16 + 0{,}64 + 0{,}16 = 0{,}96.$$
   - MSE por coordenada: $\frac{0{,}96}{3} = 0{,}32$.
     *Contas exatas.*

2. **[Exemplo 9.4.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-04.dlt#L235-L238) (`exm:9-4-manifold-neural` — Variedades de baixa dimensão):**
   - Razão de compressão para imagens $8 \times 8$ ($D = 64$) comprimidas para $d = 2$:
     $$\text{Fator} = \frac{64}{2} = 32\times; \qquad \text{Fração} = \frac{2}{64} = 0{,}03125 = 3{,}125\%.$$
     *Aritmética correta.*

3. **[Exercício 9.4.2.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-04.dlt#L291-L298) (`exr:9-4-2-1` — Parâmetros do autoencoder 64 → 16 → 2 → 16 → 64):**
   - Codificador:
     - `Linear(64, 16)`: $64 \times 16 + 16 = 1\,024 + 16 = 1\,040$ parâmetros.
     - `Linear(16, 2)`: $16 \times 2 + 2 = 32 + 2 = 34$ parâmetros.
     - Subtotal codificador: $1\,040 + 34 = 1\,074$.
   - Decodificador:
     - `Linear(2, 16)`: $2 \times 16 + 16 = 32 + 16 = 48$ parâmetros.
     - `Linear(16, 64)`: $16 \times 64 + 64 = 1\,024 + 64 = 1\,088$ parâmetros.
     - Subtotal decodificador: $48 + 1\,088 = 1\,136$.
   - Total geral: $1\,074 + 1\,136 = 2\,210$ parâmetros.
     *Contagens exatas.*

4. **[Exercício 9.4.2.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-04.dlt#L300-L307) (`exr:9-4-2-2` — Autoencoder com ReLU à mão):**
   - Modelo: $h = \mathrm{ReLU}(\mathbf{w}_1^\top \mathbf{x} + b_1)$, $\hat{\mathbf{x}} = \mathbf{w}_2 h$, com $\mathbf{w}_1 = (1, 2, -1)^\top$, $b_1 = -1$ e $\mathbf{w}_2 = (0{,}5;\; 0;\; -0{,}5)^\top$.
   - Para $\mathbf{x} = (1, 1, 0)^\top$:
     $$z_1 = 1(1) + 2(1) - 1(0) - 1 = 2 \implies h = \max(0, 2) = 2.$$
     $$\hat{\mathbf{x}} = 2 \begin{pmatrix} 0{,}5 \\ 0 \\ -0{,}5 \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix}; \qquad \mathbf{x} - \hat{\mathbf{x}} = \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix} \implies \text{erro} = 0^2 + 1^2 + 1^2 = 2.$$
   - Para $\mathbf{x}' = (0, 0, 2)^\top$:
     $$z_1' = 1(0) + 2(0) - 1(2) - 1 = -3 \implies h' = \max(0, -3) = 0.$$
     $$\hat{\mathbf{x}}' = 0 \mathbf{w}_2 = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}; \qquad \mathbf{x}' - \hat{\mathbf{x}}' = \begin{pmatrix} 0 \\ 0 \\ 2 \end{pmatrix} \implies \text{erro} = 0^2 + 0^2 + 2^2 = 4.$$
     *Contas exatas.*

5. **[Exercício 9.4.2.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-04.dlt#L309-L316) (`exr:9-4-2-3` — Erro mínimo em LFP e vantagem não linear):**
   - Variância média por eletrodo: $20\;\mu\text{V}^2$.
   - Fração explicada por $d=3$ componentes: $85\%$ ($0{,}85$).
   - Fração residual não explicada: $100\% - 85\% = 15\%$ ($0{,}15$).
   - Menor MSE linear: $0{,}15 \times 20\;\mu\text{V}^2 = 3{,}0\;\mu\text{V}^2$.
     *Contas e raciocínio corretos.*

---

### 3.3 Subtema 3: Medindo semelhança: cosseno, distância e correlação (`sec:9-4-3`)

1. **[Proposição 9.4.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-04.dlt#L392-L399) (`prop:9-4-norma-cosseno` — Relação entre distância euclidiana e cosseno em vetores unitários):**
   - Dados $\|\mathbf{u}\|_2 = 1$ e $\|\mathbf{v}\|_2 = 1$:
     $$\|\mathbf{u} - \mathbf{v}\|_2^2 = \mathbf{u}^\top \mathbf{u} - 2\mathbf{u}^\top \mathbf{v} + \mathbf{v}^\top \mathbf{v} = 1 - 2\cos(\mathbf{u}, \mathbf{v}) + 1 = 2 - 2\cos(\mathbf{u}, \mathbf{v}).$$
     *Dedução exata.*

2. **[Exemplo 9.4.5](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-04.dlt#L401-L410) (`exm:9-4-cosseno-pearson-mao` — Contas à mão em três dimensões):**
   - Vetores: $\mathbf{u} = (1, 2, 3)^\top$, $\mathbf{v} = (2, 4, 6)^\top$, $\mathbf{w} = (3, 4, 5)^\top$.
   - Entre $\mathbf{u}$ e $\mathbf{v}$:
     $$\mathbf{v} - \mathbf{u} = (1, 2, 3)^\top \implies d_2(\mathbf{u}, \mathbf{v}) = \sqrt{1^2 + 2^2 + 3^2} = \sqrt{14} \approx 3{,}741657 \approx 3{,}742.$$
     $$\mathbf{u}^\top \mathbf{v} = 1(2) + 2(4) + 3(6) = 28; \quad \|\mathbf{u}\|_2 = \sqrt{14}; \quad \|\mathbf{v}\|_2 = \sqrt{4 + 16 + 36} = \sqrt{56} = 2\sqrt{14}.$$
     $$\cos(\mathbf{u}, \mathbf{v}) = \frac{28}{\sqrt{14} \cdot 2\sqrt{14}} = \frac{28}{28} = 1{,}000.$$
   - Entre $\mathbf{u}$ e $\mathbf{w} = \mathbf{u} + 2\mathbf{1}$:
     $$\mathbf{u}^\top \mathbf{w} = 1(3) + 2(4) + 3(5) = 3 + 8 + 15 = 26; \quad \|\mathbf{w}\|_2 = \sqrt{9 + 16 + 25} = \sqrt{50} = 5\sqrt{2}.$$
     $$\cos(\mathbf{u}, \mathbf{w}) = \frac{26}{\sqrt{14}\sqrt{50}} = \frac{26}{\sqrt{700}} = \frac{26}{10\sqrt{7}} \approx \frac{26}{26{,}457513} \approx 0{,}982708 \approx 0{,}9827.$$
   - Centrando pelas médias $\bar{u} = 2$ e $\bar{w} = 4$:
     $$\tilde{\mathbf{u}} = (1-2;\; 2-2;\; 3-2)^\top = (-1, 0, 1)^\top; \qquad \tilde{\mathbf{w}} = (3-4;\; 4-4;\; 5-4)^\top = (-1, 0, 1)^\top.$$
     Como $\tilde{\mathbf{u}} = \tilde{\mathbf{w}}$, $r(\mathbf{u}, \mathbf{w}) = \cos(\tilde{\mathbf{u}}, \tilde{\mathbf{w}}) = 1{,}000$.
     *Contas exatas.*

3. **[Exemplo 9.4.6](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-04.dlt#L412-L419) (`exm:9-4-excitabilidade` — Excitabilidade global e disparo basal em 4 neurônios):**
   - $\mathbf{r}_A = (10, 30, 20, 0)^\top$, $\mathbf{r}_B = (20, 60, 40, 0)^\top$, $\mathbf{r}_C = (20, 40, 30, 10)^\top$.
   - Entre $\mathbf{r}_A$ e $\mathbf{r}_B = 2\mathbf{r}_A$:
     $$\|\mathbf{r}_A\|_2^2 = 100 + 900 + 400 + 0 = 1\,400 \implies d_2 = \sqrt{1\,400} \approx 37{,}4166 \approx 37{,}42\text{ Hz}.$$
     $$\mathbf{r}_A^\top \mathbf{r}_B = 2\,800; \quad \|\mathbf{r}_B\|_2 = \sqrt{400 + 3\,600 + 1\,600} = \sqrt{5\,600} \implies \cos = \frac{2\,800}{\sqrt{1\,400}\sqrt{5\,600}} = 1{,}000; \quad r = 1{,}000.$$
   - Entre $\mathbf{r}_A$ e $\mathbf{r}_C = \mathbf{r}_A + 10\mathbf{1}$:
     $$\mathbf{r}_A^\top \mathbf{r}_C = 10(20) + 30(40) + 20(30) + 0(10) = 200 + 1\,200 + 600 + 0 = 2\,000.$$
     $$\|\mathbf{r}_C\|_2^2 = 400 + 1\,600 + 900 + 100 = 3\,000 \implies \|\mathbf{r}_A\|_2 \|\mathbf{r}_C\|_2 = \sqrt{4\,200\,000} = 100\sqrt{420}.$$
     $$\cos(\mathbf{r}_A, \mathbf{r}_C) = \frac{2\,000}{100\sqrt{420}} = \frac{20}{\sqrt{420}} \approx \frac{20}{20{,}49390} \approx 0{,}97590 \approx 0{,}9759.$$
   - Centrando ($\bar{r}_A = 60/4 = 15$; $\bar{r}_C = 100/4 = 25$):
     $$\tilde{\mathbf{r}}_A = (-5, 15, 5, -15)^\top; \qquad \tilde{\mathbf{r}}_C = (-5, 15, 5, -15)^\top \implies r(\mathbf{r}_A, \mathbf{r}_C) = 1{,}000.$$
     *Contas exatas.*

4. **[Código 9.4.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-04.dlt#L423-L448) (`cod:9-4-matriz-similaridade` — Cosseno e Pearson com perfil oposto $\mathbf{r}_D$):**
   - $\mathbf{r}_D = (0, 10, 20, 30)^\top$, com $\|\mathbf{r}_D\|_2^2 = 0 + 100 + 400 + 900 = 1\,400$.
   - $\mathbf{r}_A^\top \mathbf{r}_D = 0 + 300 + 400 + 0 = 700 \implies \cos(A, D) = \frac{700}{1\,400} = 0{,}5000$.
   - $\mathbf{r}_C^\top \mathbf{r}_D = 0 + 400 + 600 + 300 = 1\,300 \implies \cos(C, D) = \frac{1\,300}{\sqrt{4\,200\,000}} = \frac{13}{\sqrt{420}} \approx 0{,}634335 \approx 0{,}6343$.
   - Para Pearson: $\bar{r}_D = 15 \implies \tilde{\mathbf{r}}_D = (-15, -5, 5, 15)^\top$, $\|\tilde{\mathbf{r}}_D\|_2^2 = 225 + 25 + 25 + 225 = 500$.
     $$\tilde{\mathbf{r}}_A^\top \tilde{\mathbf{r}}_D = (-5)(-15) + 15(-5) + 5(5) + (-15)(15) = 75 - 75 + 25 - 225 = -200.$$
     $$r(A, D) = \frac{-200}{\sqrt{500}\sqrt{500}} = \frac{-200}{500} = -0{,}4000 = -0{,}4.$$
     *Saídas comentadas conferidas matematicamente até a 4ª casa decimal.*

5. **[Exercício 9.4.3.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-04.dlt#L459-L466) (`exr:9-4-3-1` — Métricas à mão):**
   - $\mathbf{u} = (1, 2, 3)^\top$, $\mathbf{v} = (3, 2, 1)^\top$.
   - $d_2(\mathbf{u}, \mathbf{v}) = \sqrt{(-2)^2 + 0^2 + 2^2} = \sqrt{8} \approx 2{,}8284 \approx 2{,}828$.
   - $\mathbf{u}^\top \mathbf{v} = 3 + 4 + 3 = 10$; $\|\mathbf{u}\|_2 = \|\mathbf{v}\|_2 = \sqrt{14} \implies \cos = \frac{10}{14} = \frac{5}{7} \approx 0{,}714285 \approx 0{,}7143$.
   - $\tilde{\mathbf{u}} = (-1, 0, 1)^\top$, $\tilde{\mathbf{v}} = (1, 0, -1)^\top = -\tilde{\mathbf{u}} \implies r = \frac{-2}{2} = -1{,}000$.
     *Contas exatas.*

6. **[Exercício 9.4.3.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-04.dlt#L468-L475) (`exr:9-4-3-2` — Distância pela identidade unitária):**
   - Com $\cos = 0{,}60$: $d_2^2 = 2 - 2(0{,}60) = 0{,}80 \implies d_2 = \sqrt{0{,}80} \approx 0{,}894427 \approx 0{,}8944$.
   - Com $\cos = 0$: $d_2^2 = 2 - 0 = 2 \implies d_2 = \sqrt{2} \approx 1{,}4142 \approx 1{,}414$.
     *Contas exatas.*

7. **[Exercício 9.4.3.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-04.dlt#L477-L484) (`exr:9-4-3-3` — Prova da invariância a deslocamento basal):**
   - $\bar{r}' = \frac{1}{n}\sum_{i=1}^n (r_i + c) = \bar{r} + c$.
   - $\tilde{\mathbf{r}}' = (\mathbf{r} + c\mathbf{1}) - (\bar{r} + c)\mathbf{1} = \mathbf{r} - \bar{r}\mathbf{1} = \tilde{\mathbf{r}}$.
   - Logo $\cos(\tilde{\mathbf{r}}', \tilde{\mathbf{s}}) = \cos(\tilde{\mathbf{r}}, \tilde{\mathbf{s}}) = r(\mathbf{r}, \mathbf{s})$.
     *Demonstração exata.*

8. **[Exercício 9.4.3.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-04.dlt#L486-L509) (`exr:9-4-3-4` — Vizinho mais próximo em NumPy):**
   - Matriz $\mathbf{E}$: linhas normalizadas produzem $\mathbf{e}_0 = (1/\sqrt{5}, 2/\sqrt{5}, 0)$, $\mathbf{e}_1 = (-1/\sqrt{5}, -2/\sqrt{5}, 0)$, $\mathbf{e}_2 = (1/\sqrt{5}, 2/\sqrt{5}, 0)$ e $\mathbf{e}_3 = (0, 0, 1)$.
   - Distâncias de cosseno do item 0:
     - $D_{\cos}(0, 0) = 1 - 1 = 0$;
     - $D_{\cos}(0, 1) = 1 - (-1) = 2$;
     - $D_{\cos}(0, 2) = 1 - 1 = 0$;
     - $D_{\cos}(0, 3) = 1 - 0 = 1$.
   - Linha 0 de $D_{\cos}$: $[0{,}0;\; 2{,}0;\; 0{,}0;\; 1{,}0]$.
   - Ao preencher a diagonal com $+\infty$, o menor valor fora de si mesmo é $0{,}0$ no índice 2.
     *Saídas comentadas e código auditados e corretos.*

---

### 3.4 Subtema 4: RSA: comparando modelos e cérebros (`sec:9-4-4`)

1. **[Exemplo 9.4.7](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-04.dlt#L546-L558) (`exm:9-4-rdm-mao` — Construção da RDM 3 × 3 à mão):**
   - Respostas: $\mathbf{r}_1 = (5, 35, 25, 15)^\top$, $\mathbf{r}_2 = (15, 35, 25, 5)^\top$, $\mathbf{r}_3 = (35, 15, 5, 25)^\top$.
   - Médias: $\bar{r}_1 = \bar{r}_2 = \bar{r}_3 = 20$.
   - Centrados: $\tilde{\mathbf{r}}_1 = (-15, 15, 5, -5)^\top$, $\tilde{\mathbf{r}}_2 = (-5, 15, 5, -15)^\top$, $\tilde{\mathbf{r}}_3 = (15, -5, -15, 5)^\top$.
   - Normas ao quadrado:
     $$\|\tilde{\mathbf{r}}_1\|_2^2 = \|\tilde{\mathbf{r}}_2\|_2^2 = \|\tilde{\mathbf{r}}_3\|_2^2 = 225 + 225 + 25 + 25 = 500.$$
   - Correlações de Pearson e dissimilaridades:
     $$r_{12} = \frac{(-15)(-5) + 15^2 + 5^2 + (-5)(-15)}{500} = \frac{75 + 225 + 25 + 75}{500} = \frac{400}{500} = 0{,}80 \implies D_{12} = 1 - 0{,}80 = 0{,}20.$$
     $$r_{13} = \frac{(-15)(15) + 15(-5) + 5(-15) + (-5)(5)}{500} = \frac{-225 - 75 - 75 - 25}{500} = \frac{-400}{500} = -0{,}80 \implies D_{13} = 1 - (-0{,}80) = 1{,}80.$$
     $$r_{23} = \frac{(-5)(15) + 15(-5) + 5(-15) + (-15)(5)}{500} = \frac{-75 - 75 - 75 - 75}{500} = \frac{-300}{500} = -0{,}60 \implies D_{23} = 1 - (-0{,}60) = 1{,}60.$$
   - RDM resultante:
     $$\mathbf{D} = \begin{pmatrix} 0 & 0{,}20 & 1{,}80 \\ 0{,}20 & 0 & 1{,}60 \\ 1{,}80 & 1{,}60 & 0 \end{pmatrix}; \qquad \mathbf{d}_{\text{tri}} = (0{,}20;\; 1{,}80;\; 1{,}60)^\top.$$
     *Contas exatas.*

2. **[Exemplo 9.4.8](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-04.dlt#L560-L565) (`exm:9-4-rsa-modelo-cerebro` — Spearman entre RDMs):**
   - $\mathbf{d}_{\text{cérebro}} = (0{,}20;\; 1{,}80;\; 1{,}60)^\top \implies$ postos $(1, 3, 2)$.
   - Modelo A: $\mathbf{d}_A = (0{,}10;\; 0{,}90;\; 0{,}70)^\top \implies$ postos $(1, 3, 2) \implies \rho_A = +1{,}00$.
   - Modelo B: $\mathbf{d}_B = (0{,}10;\; 0{,}50;\; 0{,}90)^\top \implies$ postos $(1, 2, 3)$.
   - Diferenças de postos para B: $d_1 = 1 - 1 = 0$, $d_2 = 3 - 2 = 1$, $d_3 = 2 - 3 = -1$.
     $$\sum_{i=1}^3 d_i^2 = 0 + 1 + 1 = 2; \qquad \rho_B = 1 - \frac{6 \sum d_i^2}{m(m^2 - 1)} = 1 - \frac{6 \cdot 2}{3(9 - 1)} = 1 - \frac{12}{24} = 1 - 0{,}50 = +0{,}50.$$
     *Contas exatas.*

3. **[Exercício 9.4.4.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-04.dlt#L633-L640) (`exr:9-4-4-1` — Pares únicos e peso da diagonal):**
   - Para $K = 10$: total de células $K^2 = 100$; pares únicos $\frac{10 \times 9}{2} = 45$.
   - Para $K = 92$: total de células $K^2 = 8\,464$; pares únicos $\frac{92 \times 91}{2} = 46 \times 91 = 4\,186$.
   - Para $K = 4$: total de células $4^2 = 16$; células nulas da diagonal $K = 4$, correspondendo a $\frac{4}{16} = 25\%$ da matriz inteira.
     *Contas exatas.*

4. **[Exercício 9.4.4.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-04.dlt#L642-L650) (`exr:9-4-4-2` — RDM 3 × 3 à mão):**
   - $\mathbf{r}_1 = (10, 20, 30, 20)^\top$, $\mathbf{r}_2 = (14, 28, 26, 12)^\top$, $\mathbf{r}_3 = (30, 20, 10, 20)^\top$.
   - Médias iguais a $20$; centrados: $\tilde{\mathbf{r}}_1 = (-10, 0, 10, 0)^\top$, $\tilde{\mathbf{r}}_2 = (-6, 8, 6, -8)^\top$, $\tilde{\mathbf{r}}_3 = (10, 0, -10, 0)^\top$.
   - Normas ao quadrado: $\|\tilde{\mathbf{r}}_1\|_2^2 = 100 + 100 = 200$; $\|\tilde{\mathbf{r}}_2\|_2^2 = 36 + 64 + 36 + 64 = 200$; $\|\tilde{\mathbf{r}}_3\|_2^2 = 100 + 100 = 200$.
   - Produtos e dissimilaridades:
     $$r_{12} = \frac{60 + 60}{200} = \frac{120}{200} = 0{,}60 \implies D_{12} = 1 - 0{,}60 = 0{,}40.$$
     $$r_{13} = \frac{-100 - 100}{200} = \frac{-200}{200} = -1{,}00 \implies D_{13} = 1 - (-1{,}00) = 2{,}00.$$
     $$r_{23} = \frac{-60 - 60}{200} = \frac{-120}{200} = -0{,}60 \implies D_{23} = 1 - (-0{,}60) = 1{,}60.$$
   - RDM:
     $$\mathbf{D} = \begin{pmatrix} 0 & 0{,}40 & 2{,}00 \\ 0{,}40 & 0 & 1{,}60 \\ 2{,}00 & 1{,}60 & 0 \end{pmatrix}.$$
     *Contas exatas.*

5. **[Exercício 9.4.4.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-04.dlt#L652-L659) (`exr:9-4-4-3` — Spearman versus Pearson em RDM não linear):**
   - Vetores: $\mathbf{d}_{\text{mod}} = (0{,}10;\; 0{,}20;\; 0{,}30;\; 0{,}40;\; 0{,}50;\; 0{,}60)^\top$ e $\mathbf{d}_{\text{cer}} = (0{,}05;\; 0{,}10;\; 0{,}15;\; 0{,}20;\; 0{,}25;\; 1{,}05)^\top$.
   - Ambos são estritamente crescentes $\implies$ postos $(1, 2, 3, 4, 5, 6)$ $\implies \rho_{\text{Spearman}} = 1{,}000$.
   - Médias: $\bar{d}_{\text{mod}} = 2{,}10 / 6 = 0{,}35$; $\bar{d}_{\text{cer}} = 1{,}80 / 6 = 0{,}30$.
   - Centrados:
     $$\tilde{\mathbf{d}}_{\text{mod}} = (-0{,}25;\; -0{,}15;\; -0{,}05;\; 0{,}05;\; 0{,}15;\; 0{,}25)^\top \implies \|\tilde{\mathbf{d}}_{\text{mod}}\|_2^2 = 2(0{,}0625 + 0{,}0225 + 0{,}0025) = 0{,}175.$$
     $$\tilde{\mathbf{d}}_{\text{cer}} = (-0{,}25;\; -0{,}20;\; -0{,}15;\; -0{,}10;\; -0{,}05;\; 0{,}75)^\top \implies \|\tilde{\mathbf{d}}_{\text{cer}}\|_2^2 = 0{,}0625 + 0{,}0400 + 0{,}0225 + 0{,}0100 + 0{,}0025 + 0{,}5625 = 0{,}700.$$
   - Produto interno centrado:
     $$0{,}0625 + 0{,}0300 + 0{,}0075 - 0{,}0050 - 0{,}0075 + 0{,}1875 = 0{,}275.$$
   - Denominador: $\sqrt{0{,}175 \times 0{,}700} = \sqrt{0{,}1225} = 0{,}35$.
   - Correlação linear:
     $$r_{\text{Pearson}} = \frac{0{,}275}{0{,}35} = \frac{275}{350} = \frac{11}{14} \approx 0{,}785714 \approx 0{,}786 < 1.$$
     *Dedução elegante e contas impecáveis.*

---

## 4. Auditoria dos Blocos de Código Python

Todos os blocos de código presentes na aula foram auditados minuciosamente para conformidade com Python 3.11, PyTorch 2.x e scikit-learn 1.x:

1. **[Bloco 1: cod:9-4-embedding-pytorch](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-04.dlt#L112-L134) (Equivalência nn.Embedding versus One-Hot):**
   - *Imports:* <c>import torch</c>, <c>import torch.nn as nn</c>.
   - *Tensores e formas:* <c>emb.weight</c> possui formato `(4, 3)`; <c>E</c> possui formato `(4, 3)`; <c>one_hot</c> possui formato `(1, 4)`; a multiplicação <c>one_hot @ emb.weight</c> gera tensor `(1, 3)` idêntico ao lookup <c>emb(idx)</c>.
   - *Autocontido:* sim, roda sem dependências externas.
   - *Saídas comentadas:* idênticas ao resultado numérico (`[[0.7, 0.7, 0.2]]` e diferença máxima `0.0`).

2. **[Bloco 2: cod:9-4-ae-digits](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-04.dlt#L242-L280) (Autoencoder não linear 64 → 16 → 2 → 16 → 64 vs. PCA):**
   - *Imports:* <c>numpy</c>, <c>torch</c>, <c>torch.nn</c>, <c>load_digits</c>, <c>PCA</c>.
   - *Normalização e dtypes:* divide dados por $16{,}0$ para fixar em $[0, 1]$ e converte explicitamente para <c>np.float32</c>, prevenindo incompatibilidades de tipo entre `Double` e `Float` no PyTorch.
   - *Arquitetura:* garrafa central 2D e camada de reconstrução final lineares; ativações intermediárias <c>nn.ReLU()</c>; total de 2.210 parâmetros treináveis.
   - *Treinamento:* 400 iterações em lote completo com Adam (<c>lr=0.01</c>) executam em menos de 1 segundo em CPU.
   - *Saídas comentadas:* MSE PCA $\approx 0{,}052$ e MSE Autoencoder $\approx 0{,}040$ refletem o comportamento empírico esperado da variedade não linear.

3. **[Bloco 3: cod:9-4-matriz-similaridade](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-04.dlt#L423-L448) (Matrizes de Cosseno e Pearson com NumPy):**
   - *Operações:* normalização $L_2$ por linha com <c>keepdims=True</c>; produto matricial transposto <c>X_norm @ X_norm.T</c>; correlação por linhas via <c>np.corrcoef(X)</c>.
   - *Saídas comentadas:* batem perfeitamente com os cálculos analíticos deduzidos na Seção 3 deste parecer.

4. **[Bloco 4: exr:9-4-3-4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-04.dlt#L491-L507) (Busca de vizinho mais próximo com np.fill_diagonal):**
   - *Lógica:* preenche a diagonal da matriz de distâncias com <c>np.inf</c> antes de chamar <c>np.argmin</c>, impedindo que o ponto selecione a si mesmo (distância zero trivial).
   - *Autocontido e executável.*

5. **[Bloco 5: cod:9-4-rsa-digits](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-04.dlt#L569-L621) (RSA Completa: Protótipos de Dígitos, RDM e Teste de Permutação):**
   - *Sementes:* fixa semente no PyTorch (<c>torch.manual_seed(0)</c>) e no NumPy via gerador moderno (<c>np.random.default_rng(0)</c>).
   - *Extração de triângulo superior:* utiliza <c>np.triu_indices(10, k=1)</c>, garantindo exatamente $K(K-1)/2 = 45$ pares sem diagonal e sem duplicação simétrica.
   - *Teste de permutação estatisticamente correto:* a reordenação simultânea de linhas e colunas por <c>rdm_mlp[np.ix_(perm, perm)][idx]</c> preserva a estrutura matricial da RDM e a diagonal nula; o cálculo de $p$-valor adota a correção padrão não nula <c>(contagem + 1) / (n_perm + 1)</c> (Phipson &amp; Smyth, 2010).
   - *Saídas comentadas:* acurácia de treino $\approx 0{,}999$, 45 pares, Spearman $\approx 0{,}86$, $p \approx 0{,}0020$. Totalmente realistas e reprodutíveis em CPU em ~1 segundo.

6. **[Bloco 6: exr:9-4-4-4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-04.dlt#L666-L692) (Demonstração do viés inflacionário da diagonal):**
   - Compara Spearman nos 45 pares legítimos ($\rho \approx 0{,}78$) contra a matriz achatada com 100 entradas ($\rho \approx 0{,}84$), provando na prática como os zeros diagonais inflam artificialmente a correlação.

7. **[Script da Figura: fig/t04-rdm.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/fig/t04-rdm.py):**
   - Define <c>plt.rcParams["svg.fonttype"] = "none"</c>, formata números decimais com vírgula (`f"{valor:.2f}".replace(".", ",")`), gera mapa de calor viridis com barra de cores legível e salva em [fig/t04-rdm.svg](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/fig/t04-rdm.svg). O arquivo vetorial existe, possui 692 linhas limpas e integra-se perfeitamente ao texto.

---

## 5. Verificação dos Critérios Editoriais e de Neurociência

- **Estrutura das seções obrigatórias:** Cobre com exatidão os 4 subtemas previstos no guia:
  1. `sec:9-4-1`: *Embeddings: de símbolos a vetores* (limitações do *one-hot*, ortogonalidade e dimensionalidade $V$, definição de matriz de embedding $\mathbf{E} \in \mathbb{R}^{V \times d}$, consulta por produto interno $\mathbf{e}_i = \mathbf{E}^\top \mathbf{o}_i$, equivalência com <c>torch.nn.Embedding</c>, hipótese distribucional e Word2Vec, aplicações biológicas em sequências proteicas e scRNA-seq, código populacional neural como embedding em $\mathbb{R}^N$, armadilha da rotação ortogonal $\mathbf{Q}$ e eixos arbitrários);
  2. `sec:9-4-2`: *Espaço latente e autoencoders* (funil biológico dos fotorreceptores da retina ao nervo óptico, codificador $f_{\boldsymbol{\theta}}$, decodificador $g_{\boldsymbol{\psi}}$, gargalo $d < D$, perda quadrática de reconstrução, equivalência linear ao subespaço da PCA segundo Baldi &amp; Hornik 1989 e rotação arbitrária por $\mathbf{B}$, vantagem não linear na captura de variedades curvas, córtex motor e cinemática da mão, código PyTorch vs. PCA em <c>load_digits</c>, autoencoders esparsos e de *denoising*);
  3. `sec:9-4-3`: *Medindo semelhança: cosseno, distância e correlação* (ganho de excitabilidade por atenção vs. aumento basal uniforme, formulação de distância euclidiana, cosseno e correlação de Pearson, identidade $\|\mathbf{u} - \mathbf{v}\|_2^2 = 2 - 2\cos(\mathbf{u}, \mathbf{v})$ em vetores unitários com demonstração, tabela de invariâncias a $\alpha > 0$ e $+c\mathbf{1}$, código com perfis invertidos, armadilha de confundir similaridade com dissimilaridade);
  4. `sec:9-4-4`: *RSA: comparando modelos e cérebros* (incompatibilidade dimensional de unidades artificiais vs. voxels/neurônios, proposta seminal de Kriegeskorte, Mur &amp; Bandettini 2008, matriz RDM $D_{ij} = 1 - r$, extração do triângulo superior com $K(K-1)/2$ pares, justificativa do Spearman por monotonicidade não linear, teste de permutação de rótulos dos estímulos, teto de ruído fisiológico, estudo canônico com 92 imagens em humanos e macacos com categorias animadas/inanimadas e faces em IT, figura vetorial da RDM, código completo em PyTorch/SciPy com <c>load_digits</c> e permutação).
- **Exercícios:** Total de 16 exercícios (4 por seção), com graduação pedagógica balanceada (8 Básicos, 4 Intermediários, 4 Avançados). Todos contêm `<hint><title>Ver dica</title>...</hint>` e `<solution collapsible="true" collapsed="true">` com raciocínio completo, fórmulas e códigos executáveis.
- **Contextualização neurobiológica:** Presente em todas as seções:
  - Seção 1: códigos populacionais em neurônios olfatórios e curvas de sintonia de orientação em V1;
  - Seção 2: funil anatômico da retina (100 milhões de fotorreceptores para 1 milhão de axônios no nervo óptico), variedades neurais no córtex motor e dinâmica de LFPs em múltiplos eletrodos;
  - Seção 3: ganho de excitabilidade global por modulação atencional e disparo basal espontâneo;
  - Seção 4: comparação direta entre representações em redes neurais profundas e fMRI/eletrofisiologia no córtex inferotemporal (IT), separação de categorias animadas/inanimadas e faces.
- **Citações bibliográficas:** Todas autênticas, clássicas e referenciadas no corpo do texto por autor e ano sem invenção de URLs ou páginas fictícias:
  - Baldi &amp; Hornik (1989); Mikolov et al. (2013); Kriegeskorte, Mur &amp; Bandettini (2008); Kriegeskorte et al. (2008).
  - Livros-texto de referência citados na abertura e fechamento: Dayan &amp; Abbott (2001); Kandel et al.; Goodfellow et al. (Deep Learning Book).
  - Links externos limitados às documentações oficiais do PyTorch e scikit-learn.
- **Continuidade conceitual e pré-requisitos:** Retoma explicitamente álgebra linear (produtos internos, ortogonalidade, SVD e PCA do Módulo 5), programação em PyTorch (Módulo 6), estatística não paramétrica (correlações e permutações do Módulo 7), redução de dimensionalidade (Módulo 8) e arquiteturas profundas (Temas 9.1 e 9.2). Conecta-se diretamente aos próximos temas da trilha: Tema 9.5 (Transformers e Atenção) e Tema 9.7 (Autoencoders Variacionais — VAEs).
- **Notação matemática:** Perfeita harmonia com o padrão do Módulo 9: vetores em negrito minúsculo ($\mathbf{x}$, $\mathbf{h}$, $\mathbf{e}_i$, $\mathbf{o}_i$, $\mathbf{r}$), matrizes em negrito maiúsculo ($\mathbf{E}$, $\mathbf{W}$, $\mathbf{D}$, $\mathbf{Q}$), escalares em itálico ($d$, $D$, $V$, $K$, $\rho$, $r$), ativação $\mathrm{ReLU}$ e perda $\mathcal{L}_{\text{rec}}$.
- **Extensão:** O arquivo possui 723 linhas XML e aproximadamente 4.100 palavras de prosa limpa, enquadrando-se perfeitamente na faixa estipulada de 3.500 a 5.000 palavras.
- **Validação de Sintaxe Delta v0.6.0:** Atributos booleanos estritamente explícitos (`collapsible="true" collapsed="true"`); tags `<intuition>` unicamente como filhas diretas de `<definition>`, sem identificadores; `<proof>` com `of="..."` associada; ausência total de tags proibidas (`<interactive>`, `<cite>`, `<bibliography>`, `<youtube>`).

---

## 6. Conclusão

A aula [conteudo/modulo-09/tema-04.dlt](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-04.dlt) é uma obra de excelência acadêmica e didática. Combina clareza conceitual para estudantes de Biologia com rigor matemático irrefutável, implementação computacional moderna e aderência impecável aos fatos e metodologias da neurociência computacional contemporânea. As sugestões apresentadas na tabela são apontamentos de polimento pedagógico e não impedem a publicação imediata da lição.

O veredito técnico final é de **APROVAÇÃO**.
