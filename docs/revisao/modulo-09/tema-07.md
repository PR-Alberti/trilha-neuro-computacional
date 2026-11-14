# Relatório de Revisão Técnica — Módulo 09 · Tema 07 (Generativos)

- **Arquivo revisado:** [tema-07.dlt](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-07.dlt)
- **Documentos de referência:** [PADRAO-AULAS.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/PADRAO-AULAS.md) e [DELTA-COLA.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/DELTA-COLA.md)
- **Data da revisão:** 14 de novembro de 2026
- **Perfil do revisor:** Matemático, Neurocientista Computacional, Especialista em Deep Learning/PyTorch e Professor de Alunos de Ciências Biológicas

---

## 1. Veredito

**APROVAR**

A aula [conteudo/modulo-09/tema-07.dlt](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-07.dlt) cumpre integralmente os requisitos de rigor conceitual, didática matemática, relevância neurocientífica e conformidade editorial. O tema apresenta os modelos generativos modernos (VAE, GAN e Difusão) desmistificando a passagem de modelos discriminativos para probabilísticos e culminando na fronteira da neurociência computacional: a reconstrução de estímulos perceptuais a partir de registros hemodinâmicos de fMRI.

Principais conclusões da auditoria técnica:
1. **Exatidão matemática rigorosa:** Todas as demonstrações (derivação da ELBO por Jensen, divergência KL gaussiana fechada, discriminador ótimo de GAN no equilíbrio minimax e forma fechada do processo direto de difusão por soma de variâncias) e todas as contas dos exemplos e das soluções dos 9 exercícios foram refeitas e auditadas analiticamente; não há erro aritmético ou algébrico em nenhuma das resoluções.
2. **Código Python auditado linha a linha:** Os três blocos executáveis (<c>cod:9-7-vae</c>, <c>cod:9-7-gan</c> e <c>cod:9-7-difusao</c>) são 100% autocontidos, utilizam tensores Float32 de dimensões estritamente compatíveis, implementam corretamente as funções de perda do PyTorch 2.x (<c>binary_cross_entropy</c>, <c>BCEWithLogitsLoss</c> e <c>mse_loss</c>), gerenciam gradientes de forma segura com <c>detach()</c> e <c>torch.no_grad()</c>, executam em poucos segundos em CPU e trazem comentários de saída compatíveis com simulações reais.
3. **Neurociência de livro-texto e citações bibliográficas reais:** As aplicações biológicas articulam conceitos canônicos (dinâmica de baixa dimensão em populações corticais com citação de Dayan & Abbott; estágios de sono em EEG; limites espaciais e temporais do fMRI com TR $\approx 2\text{ s}$). As citações de papers fundamentais de machine learning e neuroimagem funcional são autênticas e completas: Kingma & Welling (2014); Goodfellow et al. (2014); Sohl-Dickstein et al. (2015); Ho, Jain & Abbeel (2020); Rombach et al. (2022); Shen, Horikawa, Majima & Kamitani (2019, *PLOS Computational Biology*); e Takagi & Nishimoto (2023, *CVPR*).
4. **Conformidade de escopo e extensão:** A aula cobre com profundidade todas as seções obrigatórias ("VAE", "GAN" e "Diffusion", com a subseção dedicada "Do cérebro à imagem: reconstrução de estímulos"), seguidas do Resumo com fórmulas-chave e "Para ir além". Todos os 9 exercícios dispõem de `<hint>` e `<solution>` completa recolhida por padrão. O volume de prosa totaliza aproximadamente 3.950 palavras, dentro da faixa contratual estipulada de 3.500 a 5.000 palavras.

Abaixo registram-se 4 apontamentos de polimento pedagógico e de configuração de compilação.

---

## 2. Tabela de Problemas e Sugestões

| Severidade | Local | Trecho | Correção sugerida |
|---|---|---|---|
| Formato | [project.toml](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/project.toml#L2), linha 2 | `inputs = ["tema-01.dlt", "tema-02.dlt", "tema-03.dlt", "tema-04.dlt", "tema-05.dlt", "tema-06.dlt"]` | O arquivo de configuração do módulo não inclui o `tema-07.dlt` na lista de entradas (`inputs`). Para que a aula seja compilada no livro unificado do Módulo 9 ao executar o compilador Delta, adicione `"tema-07.dlt"` ao array: `inputs = [..., "tema-06.dlt", "tema-07.dlt"]`. |
| Pedagógico | Seção 1 (`sec:9-7-1`), [exm:9-7-kl-mao](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-07.dlt#L102-L104), linha ~103 | `$$D_{\mathrm{KL}} = \frac{1}{2}\left(1 + 0{,}25 - (-1{,}3863) - 1\right) = \frac{1{,}6363}{2} \approx 0{,}8181.$$` | O resultado analítico exato com $\ln 4 = 1{,}386294\dots$ fornece $\frac{1{,}636294\dots}{2} \approx 0{,}818147\dots \approx 0{,}8181$. No entanto, se o estudante de biologia utilizar estritamente os valores intermediários arredondados apresentados na linha anterior ($\frac{1{,}6363}{2}$), o quociente direto resulta em $0{,}81815$, que por arredondamento para 4 casas decimais seria $0{,}8182$. Recomenda-se adicionar uma curta advertência: *(calculado retendo a precisão interna da máquina no logaritmo)* ou explicitar $\frac{1{,}63629}{2} \approx 0{,}8181$. |
| Pedagógico | Seção 3 (`sec:9-7-3`), [eq:9-7-ddpm-sample](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-07.dlt#L418) e [exr:9-7-3-3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-07.dlt#L589), linhas ~418 e ~589 | `$\mathbf{x}_{t-1} = \dots + \sigma_t \mathbf{z}, \qquad \mathbf{z} \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$` e `sorteamos $z = -0{,}5$` | Nas Seções 1 (VAE) e 2 (GAN), a letra $\mathbf{z}$ denota o *código latente* de baixa dimensão da representação. Na equação clássica de amostragem reversa do DDPM (Ho et al., 2020), a mesma letra $\mathbf{z}$ é adotada pela literatura para representar o *ruído branco gaussiano* adicionado em cada passo de Langevin. Para evitar que alunos iniciantes confundam esse ruído com um espaço latente de autoencoder, sugere-se incluir uma breve observação logo abaixo da equação: *(atenção: aqui $\mathbf{z}$ denota o ruído aleatório injetado no passo estocástico da difusão, e não uma variável latente compactada como no VAE)*. |
| Pedagógico | Seções 1 e 2 (`sec:9-7-1` e `sec:9-7-2`), [exm:9-7-vae-neuro](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-07.dlt#L107-L110) e [exm:9-7-gan-neuro](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-07.dlt#L284-L287), linhas ~108 e ~285 | Exemplos conceituais de VAE em dinâmicas populacionais e GAN em aumento de dados de EEG | Ambos os exemplos biológicos cumprem com elegância a contextualização qualitativa, enquanto os exercícios subsequentes (`exr:9-7-1-2` e `exr:9-7-2-2`) fornecem a aplicação quantitativa. Contudo, para estrito alinhamento à diretriz de PADRAO-AULAS.md ("Pelo menos 2 `<example>` resolvidos passo a passo, e pelo menos 1 com contexto biológico realista"), sugere-se enriquecer esses dois exemplos no corpo do texto com números típicos da fisiologia (ex.: matriz de disparos de $N = 128$ canais corticais reduzida a $d = 3$ trajetórias latentes; segmentos de EEG de $256\text{ Hz}$ com janelas de $2\text{ s}$). |

---

## 3. Recálculo e Auditoria de Todas as Contas

Todas as fórmulas teóricas, deduções e resoluções quantitativas foram recalculadas passo a passo. Abaixo apresenta-se o registro detalhado da auditoria analítica.

### 3.1 Subtema 1: VAE (`sec:9-7-1`)

1. **[Teorema 9.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-07.dlt#L67-L79) (`thm:9-7-elbo` — Limite Inferior da Evidência / ELBO):**
   - Relação fundamental de verossimilhança marginal com distribuição variacional $q_{\boldsymbol{\phi}}(\mathbf{z} \mid \mathbf{x})$:
     $$\log p_{\boldsymbol{\theta}}(\mathbf{x}) = \log \int q_{\boldsymbol{\phi}}(\mathbf{z} \mid \mathbf{x}) \frac{p_{\boldsymbol{\theta}}(\mathbf{x}, \mathbf{z})}{q_{\boldsymbol{\phi}}(\mathbf{z} \mid \mathbf{x})}\,d\mathbf{z} = \log \mathbb{E}_{q_{\boldsymbol{\phi}}(\mathbf{z} \mid \mathbf{x})}\!\left[\frac{p_{\boldsymbol{\theta}}(\mathbf{x}, \mathbf{z})}{q_{\boldsymbol{\phi}}(\mathbf{z} \mid \mathbf{x})}\right].$$
   - Aplicação da desigualdade de Jensen para a função côncava $\log$:
     $$\log \mathbb{E}[Y] \ge \mathbb{E}[\log Y] \implies \log p_{\boldsymbol{\theta}}(\mathbf{x}) \ge \mathbb{E}_{q}\!\left[\log \frac{p_{\boldsymbol{\theta}}(\mathbf{x} \mid \mathbf{z}) p(\mathbf{z})}{q_{\boldsymbol{\phi}}(\mathbf{z} \mid \mathbf{x})}\right] = \mathbb{E}_q[\log p_{\boldsymbol{\theta}}(\mathbf{x} \mid \mathbf{z})] - D_{\mathrm{KL}}\!\left(q_{\boldsymbol{\phi}}(\mathbf{z} \mid \mathbf{x}) \,\|\, p(\mathbf{z})\right).$$
   *Dedução analítica irrepreensível.*

2. **[Proposição 9.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-07.dlt#L83-L94) (`prop:9-7-kl-gauss` — Divergência KL Fechada e Reparametrização):**
   - Para densidades gaussianas univariadas $q(z) = \mathcal{N}(\mu, \sigma^2)$ e $p(z) = \mathcal{N}(0, 1)$:
     $$D_{\mathrm{KL}}(q \,\|\, p) = \int q(z) \ln \frac{q(z)}{p(z)}\,dz = \mathbb{E}_q\!\left[-\frac{1}{2}\ln(2\pi\sigma^2) - \frac{(z-\mu)^2}{2\sigma^2} + \frac{1}{2}\ln(2\pi) + \frac{z^2}{2}\right]$$
     $$= -\frac{1}{2}\ln \sigma^2 - \frac{1}{2} + \frac{1}{2}\mathbb{E}_q[z^2] = -\frac{1}{2}\ln \sigma^2 - \frac{1}{2} + \frac{1}{2}(\sigma^2 + \mu^2) = \frac{1}{2}\left(\mu^2 + \sigma^2 - \ln \sigma^2 - 1\right).$$
   - Soma sobre $d$ dimensões independentes da gaussiana diagonal: $\frac{1}{2}\sum_{j=1}^d (\mu_j^2 + \sigma_j^2 - \ln \sigma_j^2 - 1)$.
   - Reparametrização: com $\boldsymbol{\varepsilon} \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$, $\mathbf{z} = \boldsymbol{\mu} + \boldsymbol{\sigma} \odot \boldsymbol{\varepsilon}$ possui esperança $\mathbb{E}[\mathbf{z}] = \boldsymbol{\mu}$ e matriz de covariância $\operatorname{Cov}(\mathbf{z}) = \operatorname{diag}(\boldsymbol{\sigma}^2)$, permitindo a diferenciação direta em relação a $\boldsymbol{\mu}$ e $\boldsymbol{\sigma}$.
   *Fórmulas exatas e corretas.*

3. **[Exemplo 9.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-07.dlt#L98-L105) (`exm:9-7-kl-mao` — Cálculo à mão da KL e reparametrização):**
   - Parâmetros: $d = 1$, $\mu = 1$, $\sigma = 0{,}5 \implies \mu^2 = 1$, $\sigma^2 = 0{,}25$.
   - Logaritmo: $\ln(0{,}25) = -\ln 4 \approx -1{,}386294$.
   - Divergência KL:
     $$D_{\mathrm{KL}} = \frac{1}{2}\left(1 + 0{,}25 - (-1{,}386294) - 1\right) = \frac{1{,}636294}{2} \approx 0{,}818147 \approx 0{,}8181.$$
   - Amostra reparametrizada com $\varepsilon = -0{,}4$:
     $$z = 1 + 0{,}5 \cdot (-0{,}4) = 1 - 0{,}2 = 0{,}8.$$
   *Valores conferidos e exatos.*

4. **[Exercício 9.7.1.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-07.dlt#L195-L206) (`exr:9-7-1-1` — KL gaussiana bidimensional à mão):**
   - Entrada: $\boldsymbol{\mu} = (1,\, 0)^\top$, $\boldsymbol{\sigma} = (1,\, 2)^\top$, com $\ln 2 \approx 0{,}6931$.
   - Dimensão 1 ($\mu_1 = 1$, $\sigma_1 = 1$):
     $$D_1 = \frac{1}{2}\left(1^2 + 1^2 - \ln(1) - 1\right) = \frac{1}{2}(1 + 1 - 0 - 1) = \frac{1}{2}(1) = 0{,}5.$$
   - Dimensão 2 ($\mu_2 = 0$, $\sigma_2 = 2 \implies \sigma_2^2 = 4$, $\ln 4 = 2\ln 2 \approx 2 \cdot 0{,}6931 = 1{,}3862$):
     $$D_2 = \frac{1}{2}\left(0 + 4 - 1{,}3862 - 1\right) = \frac{1}{2}(3 - 1{,}3862) = \frac{1{,}6138}{2} = 0{,}8069.$$
   - Soma total: $D_{\mathrm{KL}} = D_1 + D_2 = 0{,}5 + 0{,}8069 = 1{,}3069$.
   *Contas rigorosamente corretas.*

5. **[Exercício 9.7.1.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-07.dlt#L208-L220) (`exr:9-7-1-2` — Fator latente neural e log-variância):**
   - Entrada: $\boldsymbol{\mu} = (1{,}5;\, -0{,}8)^\top$, $\log \boldsymbol{\sigma}^2 = (0;\, -2\ln 2)^\top$, ruído $\boldsymbol{\varepsilon} = (0{,}4;\, -1{,}0)^\top$.
   - Desvios-padrão:
     $$\sigma_1 = \exp\!\left(\frac{1}{2} \cdot 0\right) = e^0 = 1, \qquad \sigma_2 = \exp\!\left(\frac{1}{2} \cdot (-2\ln 2)\right) = e^{-\ln 2} = \frac{1}{2} = 0{,}5.$$
   - Coordenadas latentes reparametrizadas:
     $$z_1 = \mu_1 + \sigma_1 \varepsilon_1 = 1{,}5 + 1 \cdot 0{,}4 = 1{,}9.$$
     $$z_2 = \mu_2 + \sigma_2 \varepsilon_2 = -0{,}8 + 0{,}5 \cdot (-1{,}0) = -0{,}8 - 0{,}5 = -1{,}3.$$
     $$\mathbf{z} = (1{,}9;\, -1{,}3)^\top.$$
   *Contas exatas.*

6. **[Exercício 9.7.1.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-07.dlt#L222-L231) (`exr:9-7-1-3` — Análise assintótica dos regimes de $\beta$-VAE):**
   - Caso $\beta = 0$: a perda se resume a $-\mathbb{E}[\log p_{\boldsymbol{\theta}}(\mathbf{x} \mid \mathbf{z})]$. O codificador não é coagido para $\mathcal{N}(\mathbf{0}, \mathbf{I})$, dispersando os dados em variedades descontínuas. Sortear $\mathbf{z} \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$ cai em vazios intermodais, produzindo ruído visual.
   - Caso $\beta = 100$: a regularização domina absolutamente, forçando $q_{\boldsymbol{\phi}}(\mathbf{z} \mid \mathbf{x}) \to \mathcal{N}(\mathbf{0}, \mathbf{I})$ independentemente de $\mathbf{x}$ (*posterior collapse*). A informação de $\mathbf{x}$ na representação latente decai a zero, e a melhor previsão quadrática do decodificador degenera na média marginal do conjunto de treino.
   *Demonstração qualitativa e teórica impecável.*

---

### 3.2 Subtema 2: GAN (`sec:9-7-2`)

1. **[Proposição 9.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-07.dlt#L256-L269) (`prop:9-7-d-otimo` — Discriminador Ótimo e Equilíbrio Minimax):**
   - Função objetivo contínua para $D$ sob gerador $G$ fixo:
     $$V(D, G) = \int \left[p_{\text{dados}}(\mathbf{x}) \ln D(\mathbf{x}) + p_g(\mathbf{x}) \ln(1 - D(\mathbf{x}))\right] d\mathbf{x}.$$
   - Otimização pontual para $y = D(\mathbf{x}) \in (0, 1)$ com $a = p_{\text{dados}}(\mathbf{x}) > 0$ e $b = p_g(\mathbf{x}) > 0$:
     $$f(y) = a \ln y + b \ln(1 - y) \implies f'(y) = \frac{a}{y} - \frac{b}{1 - y} = 0 \iff a(1 - y) = by \iff y^* = \frac{a}{a + b}.$$
     $$f''(y) = -\frac{a}{y^2} - \frac{b}{(1 - y)^2} < 0 \quad (\text{máximo estrito global}).$$
     Portanto, $D^*(\mathbf{x}) = \frac{p_{\text{dados}}(\mathbf{x})}{p_{\text{dados}}(\mathbf{x}) + p_g(\mathbf{x})}$.
   - Ponto de sela / equilíbrio ideal ($p_g = p_{\text{dados}}$):
     $$D^*(\mathbf{x}) = \frac{p_{\text{dados}}}{2p_{\text{dados}}} = \frac{1}{2}.$$
     $$V(D^*, G^*) = \int p_{\text{dados}}(\mathbf{x}) \ln \frac{1}{2}\,d\mathbf{x} + \int p_{\text{dados}}(\mathbf{x}) \ln \frac{1}{2}\,d\mathbf{x} = 2 \ln \frac{1}{2} = -2\ln 2 = -\ln 4 \approx -1{,}386294 \approx -1{,}386.$$
   *Dedução analítica clássica confirmada.*

2. **[Exemplo 9.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-07.dlt#L275-L283) (`exm:9-7-gan-mao` — Discriminador ótimo numérico):**
   - Densidades: $p_{\text{dados}}(x) = 0{,}6$ e $p_g(x) = 0{,}2$.
   - Substituição:
     $$D^*(x) = \frac{0{,}6}{0{,}6 + 0{,}2} = \frac{0{,}6}{0{,}8} = \frac{3}{4} = 0{,}75.$$
   *Valor e interpretação de densidade corretos.*

3. **[Exercício 9.7.2.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-07.dlt#L347-L358) (`exr:9-7-2-1` — Discriminador ótimo em dois pontos):**
   - Ponto $x_1$: $p_{\text{dados}}(x_1) = 0{,}1$, $p_g(x_1) = 0{,}4$:
     $$D^*(x_1) = \frac{0{,}1}{0{,}1 + 0{,}4} = \frac{0{,}1}{0{,}5} = 0{,}20.$$
   - Ponto $x_2$: $p_{\text{dados}}(x_2) = 0{,}5$, $p_g(x_2) = 0{,}1$:
     $$D^*(x_2) = \frac{0{,}5}{0{,}5 + 0{,}1} = \frac{0{,}5}{0{,}6} = \frac{5}{6} \approx 0{,}8333 \approx 0{,}833.$$
   - Interpretação: como $D^*(x_1) = 0{,}20 < 0{,}5$, $p_g(x_1) > p_{\text{dados}}(x_1)$, caracterizando excesso de massa sintética em $x_1$.
   *Resolução analítica exata.*

4. **[Exercício 9.7.2.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-07.dlt#L360-L367) (`exr:9-7-2-2` — Colapso de modos em sono EEG):**
   - Identifica corretamente a patologia de *mode collapse* (colapso de modos), na qual o gerador mapeia o ruído $\mathbf{z}$ apenas para o modo de menor resistência do discriminador (estágio N2), eliminando N1 e REM e induzindo viés severo no treinamento subsequente de decodificadores.
   *Diagnóstico conceitual exato.*

5. **[Exercício 9.7.2.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-07.dlt#L369-L380) (`exr:9-7-2-3` — Gradientes da perda minimax vs não saturante):**
   - Se $D(G(\mathbf{z})) = \sigma(s)$ com $\sigma'(s) = \sigma(s)(1 - \sigma(s))$:
   - Derivada da perda minimax ($\ln(1 - \sigma(s))$):
     $$\frac{d}{ds}\ln(1 - \sigma(s)) = \frac{-\sigma'(s)}{1 - \sigma(s)} = \frac{-\sigma(s)(1 - \sigma(s))}{1 - \sigma(s)} = -\sigma(s).$$
   - Derivada da perda não saturante ($-\ln \sigma(s)$):
     $$\frac{d}{ds}(-\ln \sigma(s)) = \frac{-\sigma'(s)}{\sigma(s)} = \frac{-\sigma(s)(1 - \sigma(s))}{\sigma(s)} = -(1 - \sigma(s)).$$
   - Avaliação numérica para $s = -5$:
     $$\sigma(-5) = \frac{1}{1 + e^5} \approx \frac{1}{1 + 148{,}413159} = \frac{1}{149{,}413159} \approx 0{,}00669285 \approx 0{,}0067.$$
     - Gradiente minimax: $-\sigma(-5) \approx -0{,}0067$.
     - Gradiente não saturante: $-(1 - \sigma(-5)) = -(1 - 0{,}006693) \approx -0{,}9933$.
   - Razão das magnitudes: $\frac{0{,}993307}{0{,}006693} \approx 148{,}4 \approx 150\times$.
   *Dedução por regra da cadeia e aritmética perfeitas.*

---

### 3.3 Subtema 3: Diffusion (`sec:9-7-3`)

1. **[Proposição 9.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-07.dlt#L400-L413) (`prop:9-7-difusao-fechada` — Forma Fechada do Processo Direto):**
   - Processo elementar markoviano: $\mathbf{x}_t = \sqrt{\alpha_t}\,\mathbf{x}_{t-1} + \sqrt{1 - \alpha_t}\,\boldsymbol{\varepsilon}_t$, com $\boldsymbol{\varepsilon}_t \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$ independentes.
   - Para $t = 2$:
     $$\mathbf{x}_2 = \sqrt{\alpha_2}\left(\sqrt{\alpha_1}\,\mathbf{x}_0 + \sqrt{1 - \alpha_1}\,\boldsymbol{\varepsilon}_1\right) + \sqrt{1 - \alpha_2}\,\boldsymbol{\varepsilon}_2 = \sqrt{\alpha_1 \alpha_2}\,\mathbf{x}_0 + \sqrt{\alpha_2(1 - \alpha_1)}\,\boldsymbol{\varepsilon}_1 + \sqrt{1 - \alpha_2}\,\boldsymbol{\varepsilon}_2.$$
   - Soma de duas normais independentes $X \sim \mathcal{N}(\mathbf{0}, \sigma_a^2 \mathbf{I})$ e $Y \sim \mathcal{N}(\mathbf{0}, \sigma_b^2 \mathbf{I}) \implies X + Y \sim \mathcal{N}(\mathbf{0}, (\sigma_a^2 + \sigma_b^2)\mathbf{I})$:
     $$\sigma_{\text{total}}^2 = \alpha_2(1 - \alpha_1) + (1 - \alpha_2) = \alpha_2 - \alpha_1\alpha_2 + 1 - \alpha_2 = 1 - \alpha_1\alpha_2 = 1 - \bar{\alpha}_2.$$
   - Logo, $\mathbf{x}_2 = \sqrt{\bar{\alpha}_2}\,\mathbf{x}_0 + \sqrt{1 - \bar{\alpha}_2}\,\boldsymbol{\varepsilon}$. Por indução finita, $\mathbf{x}_t = \sqrt{\bar{\alpha}_t}\,\mathbf{x}_0 + \sqrt{1 - \bar{\alpha}_t}\,\boldsymbol{\varepsilon}$.
   *Prova matemática exata e didática.*

2. **[Exemplo 9.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-07.dlt#L427-L440) (`exm:9-7-difusao-mao` — Cronograma direto, SNR e valor pontual):**
   - Parâmetro: $\beta_t = 0{,}1 \implies \alpha_t = 1 - 0{,}1 = 0{,}9$.
     - $t = 1$: $\bar{\alpha}_1 = 0{,}9$, variância de ruído $1 - \bar{\alpha}_1 = 0{,}1 \implies \mathrm{SNR}_1 = \frac{0{,}9}{0{,}1} = 9{,}00$.
     - $t = 2$: $\bar{\alpha}_2 = 0{,}9^2 = 0{,}81$, variância de ruído $1 - 0{,}81 = 0{,}19 \implies \mathrm{SNR}_2 = \frac{0{,}81}{0{,}19} \approx 4{,}263158 \approx 4{,}263$.
     - $t = 3$: $\bar{\alpha}_3 = 0{,}9^3 = 0{,}729$, variância de ruído $1 - 0{,}729 = 0{,}271 \implies \mathrm{SNR}_3 = \frac{0{,}729}{0{,}271} \approx 2{,}690037 \approx 2{,}690$.
   - Amostra ruidosa em $t = 2$ para $x_0 = 2$ e $\varepsilon = -1$:
     $$\sqrt{\bar{\alpha}_2} = \sqrt{0{,}81} = 0{,}9, \qquad \sqrt{1 - \bar{\alpha}_2} = \sqrt{0{,}19} \approx 0{,}43588989 \approx 0{,}4359.$$
     $$x_2 = 0{,}9 \cdot 2 + 0{,}4359 \cdot (-1) = 1{,}8 - 0{,}4359 = 1{,}3641.$$
   *Valores auditados e corretos.*

3. **[Exercício 9.7.3.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-07.dlt#L566-L576) (`exr:9-7-3-1` — Difusão direta em dois passos):**
   - Entrada: $\beta_1 = \beta_2 = 0{,}2 \implies \alpha_1 = \alpha_2 = 0{,}8$.
   - Coeficientes acumulados: $\bar{\alpha}_2 = 0{,}8 \cdot 0{,}8 = 0{,}64$, variância de ruído $1 - \bar{\alpha}_2 = 1 - 0{,}64 = 0{,}36$.
   - Razão sinal-ruído:
     $$\mathrm{SNR}_2 = \frac{0{,}64}{0{,}36} = \frac{16}{9} \approx 1{,}777778 \approx 1{,}778.$$
   - Ponto ruidoso para $x_0 = -2$ e $\varepsilon = 0{,}5$:
     $$\sqrt{0{,}64} = 0{,}8, \qquad \sqrt{0{,}36} = 0{,}6.$$
     $$x_2 = 0{,}8 \cdot (-2) + 0{,}6 \cdot 0{,}5 = -1{,}6 + 0{,}3 = -1{,}3.$$
   *Resolução sem qualquer erro aritmético.*

4. **[Exercício 9.7.3.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-07.dlt#L578-L586) (`exr:9-7-3-2` — Limites da decodificação fMRI e viés do prior):**
   - Explicação neurocomputacional correta: a regressão *ridge* sobre voxels de fMRI possui baixa resolução e ruído hemodinâmico, recuperando apenas a categoria macro ("relógio de parede") e a geometria aproximada (silhueta circular). Ao decodificar com difusão latente, o modelo completa os detalhes finos (ponteiros em 10h10) usando a distribuição marginal aprendida em seu conjunto massivo de imagens naturais, e não por leitura direta do córtex visual.
   *Raciocínio biológico e computacional perfeito.*

5. **[Exercício 9.7.3.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-07.dlt#L587-L596) (`exr:9-7-3-3` — Passo reverso DDPM numérico à mão):**
   - Entrada: $t = 2$, $\beta_2 = 0{,}36$, $\alpha_2 = 0{,}64$, $\bar{\alpha}_2 = 0{,}36$, $x_2 = 1{,}4$, $\varepsilon_{\boldsymbol{\theta}}(x_2, 2) = 0{,}8$, $z = -0{,}5$, $\sigma_2 = \sqrt{\beta_2} = \sqrt{0{,}36} = 0{,}6$.
   - Raízes quadradas: $\sqrt{\alpha_2} = \sqrt{0{,}64} = 0{,}8$; $\sqrt{1 - \bar{\alpha}_2} = \sqrt{1 - 0{,}36} = \sqrt{0{,}64} = 0{,}8$.
   - Equação reversa:
     $$x_1 = \frac{1}{\sqrt{\alpha_2}}\left(x_2 - \frac{\beta_2}{\sqrt{1 - \bar{\alpha}_2}}\,\varepsilon_{\boldsymbol{\theta}}(x_2, 2)\right) + \sigma_2 z.$$
   - Cálculo do termo determinístico (média):
     $$\frac{\beta_2}{\sqrt{1 - \bar{\alpha}_2}}\,\varepsilon_{\boldsymbol{\theta}} = \frac{0{,}36}{0{,}8} \cdot 0{,}8 = 0{,}36.$$
     $$x_2 - 0{,}36 = 1{,}4 - 0{,}36 = 1{,}04.$$
     $$\mu_1 = \frac{1{,}04}{0{,}8} = \frac{104}{80} = 1{,}3.$$
   - Termo estocástico: $\sigma_2 z = 0{,}6 \cdot (-0{,}5) = -0{,}3$.
   - Resultado final: $x_1 = 1{,}3 - 0{,}3 = 1{,}0$.
   - Justificativa do último passo: em $t = 1 \to 0$, $z$ é anulado para que a amostra gerada atinja diretamente a média limpa $\mathbf{x}_0$, sem contaminação estocástica desnecessária.
   *Todas as etapas são analiticamente exatas.*

---

## 4. Auditoria de Código Python (linha a linha)

Todos os scripts foram analisados sob a ótica de execução em PyTorch 2.x e scikit-learn 1.x:

1. **Script <c>cod:9-7-vae</c> ([linhas 114–185](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-07.dlt#L114-L185)):**
   - **Imports e reprodutibilidade:** Importa `torch`, `torch.nn as nn`, `torch.nn.functional as F`, `load_digits` e `DataLoader`/`TensorDataset`. Fixa sementes com `torch.manual_seed(0)` e `np.random.seed(0)`.
   - **Dados e dtypes:** `load_digits().data / 16.0` normaliza pixels de $[0, 16]$ para $[0, 1]$ e converte com `dtype=torch.float32`. Forma $(1797, 64)$ plenamente compatível com `nn.Linear(64, 32)`. O `DataLoader` com `batch_size=64` é desempacotado via `for (lote,) in loader:`.
   - **Grafo e reparametrização:** A classe `VAE` implementa `self.fc_mu` e `self.fc_logvar` separadamente. A função `reparameterize` calcula `std = torch.exp(0.5 * logvar)` e sorteia `eps = torch.randn_like(std)`. A retropropagação flui livremente através de `mu + std * eps`.
   - **Função de perda:** Implementa `rec = F.binary_cross_entropy(x_hat, lote, reduction="sum")` e `kl = -0.5 * torch.sum(1.0 + logvar - mu.pow(2) - logvar.exp())`. Ambas as perdas estão em escala de soma por lote, equilibrando perfeitamente a reconstrução dos 64 pixels com as 2 dimensões latentes.
   - **Geração e saídas:** `modelo.dec(torch.randn(5, 2))` sob `torch.no_grad()` gera tensores $(5, 64)$ em $[0, 1]$ devido à sigmoide final. As saídas comentadas (`Reconstrucao media ≈ 24.23 | KL medio ≈ 1.49`) são matematicamente consistentes com o platô de 40 épocas.

2. **Script <c>cod:9-7-gan</c> ([linhas 291–338](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-07.dlt#L291-L338)):**
   - **Arquitetura 1D:** Gerador $G$ e Discriminador $D$ utilizam `nn.Linear(1, 32)`, ativações `nn.LeakyReLU(0.2)` e projeção linear de saída para 1 dimensão contínua.
   - **Estabilidade e critério:** Utiliza `nn.BCEWithLogitsLoss()`, operando diretamente sobre os logits de $D$ com proteção contra subfluxo numérico.
   - **Isolamento de gradientes:** Na atualização de $D$, as amostras falsas recebem `.detach()` (`x_falso = G(torch.randn(256, 1)).detach()`), impedindo que o gradiente da perda de $D$ vaze para os parâmetros de $G$.
   - **Perda não saturante:** $G$ é treinado minimizando `bce(D(G(z)), torch.ones(256, 1))`, o que implementa com exatidão a maximização de $\log D(G(\mathbf{z}))$.
   - **Otimizadores:** `Adam` com `betas=(0.5, 0.999)` segue rigorosamente as boas práticas consolidadas da arquitetura DCGAN (Radford et al., 2015). A nota final comentada esclarece de forma transparente a variabilidade inerente da dispersão gerada.

3. **Script <c>cod:9-7-difusao</c> ([linhas 443–500](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/tema-07.dlt#L443-L500)):**
   - **Cronograma analítico:** Constrói $\beta_t \in [10^{-3}, 0{,}2]$ para $T = 50$, $\alpha_t = 1 - \beta_t$ e $\bar{\alpha}_t$ com `torch.cumprod`.
   - **Condicionamento temporal:** A rede recebe a concatenação `torch.cat([x_t, t_norm], dim=1)` com dimensão de entrada 2, intermediada por camadas lineares com `nn.SiLU()` (ativação padrão de DDPMs).
   - **Treino de ruído:** Amostra $t \sim \mathcal{U}\{0, T-1\}$, calcula $x_t$ em forma fechada (`torch.sqrt(ab) * x0 + torch.sqrt(1.0 - ab) * eps`) e minimiza `F.mse_loss(pred_eps, eps)`.
   - **Amostragem reversa iterativa:** Itera de $t = 49$ até $0$, calcula a média conforme a fórmula teórica de Ho et al. (2020) e adiciona ruído estocástico apenas quando `t_idx > 0`, anulando-o em `t_idx == 0`.
   - **Separação bimodal:** Amostra $2.000$ pontos e divide em $x < 0$ e $x \ge 0$, recuperando frações de $\approx 0{,}49$ e $0{,}51$, com médias próximas de $-2$ e $+2$ e desvios de $\approx 0{,}3$.

---

## 5. Neurociência e Citações Bibliográficas

Todas as referências bibliográficas inseridas no texto foram checadas contra as bases de dados acadêmicas (PubMed, IEEE Xplore, Google Scholar e arXiv):

1. **Kingma & Welling (2014):** *Auto-Encoding Variational Bayes*, ICLR 2014. Artigo seminal do VAE, introduzindo a ELBO e o truque da reparametrização. Citação canônica correta.
2. **Dayan & Abbott (2001):** *Theoretical Neuroscience: Computational and Mathematical Modeling of Neural Systems*, MIT Press. Referência máxima de livro-texto para dinâmica de populações neurais e variedades de baixa dimensão.
3. **Goodfellow et al. (2014):** *Generative Adversarial Nets*, NeurIPS 2014. Artigo fundador das GANs, formulando o jogo minimax e a prova do discriminador ótimo $D^*(\mathbf{x})$.
4. **Sohl-Dickstein et al. (2015):** *Deep Unsupervised Learning using Nonequilibrium Thermodynamics*, ICML 2015. Artigo pioneiro que estabeleceu a conexão entre difusão física e aprendizado generativo.
5. **Ho, Jain & Abbeel (2020):** *Denoising Diffusion Probabilistic Models (DDPM)*, NeurIPS 2020. Artigo clássico que estabeleceu a perda simplificada no ruído e a equação de amostragem discreta.
6. **Rombach et al. (2022):** *High-Resolution Image Synthesis with Latent Diffusion Models*, CVPR 2022. Artigo que criou o *Stable Diffusion*, demonstrando o ganho de eficiência ao difundir no espaço latente de um autoencoder pré-treinado.
7. **Shen, Horikawa, Majima & Kamitani (2019):** *Deep image reconstruction from human brain activity*, *PLOS Computational Biology* 15(1): e1006634. Artigo marco na reconstrução de imagens vistas e imaginadas a partir de fMRI usando redes profundas e geradores. Autor, ano e revista 100% corretos.
8. **Takagi & Nishimoto (2023):** *High-resolution image reconstruction with latent diffusion models from human brain activity*, *IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*, 2023. Artigo que utilizou o *Natural Scenes Dataset* (NSD) para ligar o sinal BOLD cortical ao espaço latente do *Stable Diffusion* via regressão *ridge*. Autor, ano e conferência 100% corretos.

As discussões neurocientíficas são equilibradas e de livro-texto: explicita-se a baixa resolução hemodinâmica do sinal BOLD (TR $\approx 2\text{ s}$), alerta-se para o risco de atribuir ao cérebro detalhes gerados pelo *prior* do modelo generativo e discutem-se os limites éticos de privacidade neural.

---

## 6. Conformidade Estrutural, Editorial e Notacional

- **Estrutura de Seções:** A aula possui exatamente as 3 seções do programa ("VAE", "GAN", "Diffusion"), incluindo a subseção pedida sobre reconstrução cerebral a partir de fMRI, além das seções obrigatórias "Resumo" e "Para ir além".
- **Identificadores (IDs):** Todos os ambientes seguem a convenção com prefixo `9-7` em letras minúsculas sem acento (`sec:9-7-1`, `def:9-7-vae`, `thm:9-7-elbo`, `prop:9-7-kl-gauss`, `exm:9-7-kl-mao`, `exr:9-7-1-1`, `eq:9-7-elbo`, `fig:9-7-difusao`, `tbl:9-7-comparacao`).
- **Exercícios:** Exatamente 3 exercícios por seção (totalizando 9), graduados em Básico, Intermediário e Avançado. Todos possuem `<hint>` e `<solution collapsible="true" collapsed="true">` com raciocínio analítico completo. Pelo menos um exercício por seção é contextualizado na neurociência (`exr:9-7-1-2`, `exr:9-7-2-2`, `exr:9-7-3-2`).
- **Figuras:** A aula referencia `<figure src="fig/t07-difusao.svg" id="fig:9-7-difusao">`. O arquivo SVG existe na pasta `conteudo/modulo-09/fig/` e foi gerado pelo script [fig/t07-difusao.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-09/fig/t07-difusao.py), configurado com `plt.rcParams['svg.fonttype'] = 'none'` e legendas em português.
- **Notação Matemática:** Consistente com o Módulo 9. Vetores em negrito minúsculo ($\mathbf{x}$, $\mathbf{z}$, $\boldsymbol{\mu}$, $\boldsymbol{\sigma}$, $\boldsymbol{\varepsilon}$), matriz identidade $\mathbf{I}$, parâmetros $\boldsymbol{\theta}$ e $\boldsymbol{\phi}$, e perda $\mathcal{L}$. Na Seção 1, a aula faz a distinção explícita de que $\sigma$ representa desvio-padrão (não a sigmoide), e na Seção 2 utiliza $\sigma_{\text{log}}$ para a função logística.
- **Tamanho:** A contagem total de palavras de prosa é de cerca de 3.950 palavras, dentro da faixa contratual de 3.500 a 5.000 palavras.

---

## 7. Conclusão

A aula cumpre rigorosamente todos os padrões de qualidade didática, formalismo matemático e reprodutibilidade computacional exigidos pelo projeto. O parecer é de **APROVAÇÃO**, com a recomendação operacional de registrar o arquivo no `project.toml` e implementar os pequenos esclarecimentos pedagógicos listados na Tabela de Problemas.
