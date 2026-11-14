# Relatório de Revisão Técnica — Módulo 07 · Tema 01 (Combinatória)

- **Arquivo revisado:** [tema-01.dlt](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt)
- **Documentos de referência:** [PADRAO-AULAS.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/PADRAO-AULAS.md) e [DELTA-COLA.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/DELTA-COLA.md)
- **Data da revisão:** 14 de novembro de 2026
- **Perfil do revisor:** Matemático, Neurocientista Computacional, Programador Python e Professor de Alunos de Ciências Biológicas

---

## 1. Veredito

**CORRIGIR**

A aula possui méritos didáticos e estruturais excepcionais: contextualização biológica realista e rigorosa em todas as seções (genética mendeliana, código genético, arranjo de eletrodos em EEG de 64 canais, padrões binários de disparos de populações neurais corticais), demonstrações completas e elegantes (relação de Stifel via argumento combinatório e Binômio de Newton), progressão intuitiva antes da formalização e 16 exercícios graduados com dicas e soluções passo a passo.

Contudo, a emissão do parecer **CORRIGIR** decorre de **1 erro objetivo no código Python e na representação biológica do sítio de restrição EcoRI** na solução do [Exercício 7.1.4.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L812-L844) (`exr:7-1-4-4`), somado à **ausência da chamada explícita de `itertools.combinations`** no bloco de código [cod:7-1-comb-stifel](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L548-L564) (requisito expresso do subtema), além de pequenos apontamentos de precisão terminológica e formatação.

Ajustando os pontos detalhados na tabela e nas seções seguintes, a aula estará pronta para aprovação e compilação definitiva.

---

## 2. Tabela de Problemas e Observações

| Severidade | Local | Trecho | Correção sugerida |
|---|---|---|---|
| **Erro factual / Código Python** | Seção 4 (`sec:7-1-4`), [exr:7-1-4-4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L823-L833), linhas ~823 e ~832 | `# Codificamos A=0, T=1, G=2, C=3; logo GAATTC = [2, 0, 0, 1, 1, 2]` e `& (fita[5:] == 2)` | Na codificação adotada no comentário ($A=0, T=1, G=2, C=3$), a base citosina ($C$) corresponde ao inteiro $3$. O sítio de restrição canônico da EcoRI é $5'\text{-GAATTC-}3'$. Logo, o último nucleotídeo deve ser $3$, e não $2$ (que é guanina). O código atual está buscando a sequência $\text{GAATTG}$.<br/>**Correção:** Alterar o comentário para `logo GAATTC = [2, 0, 0, 1, 1, 3]` e a linha 832 para `& (fita[5:] == 3)`. |
| **Pedagógico** | Seção 3 (`sec:7-1-3`), [cod:7-1-comb-stifel](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L546-L564), linhas ~546–564 | Prose: `e <c>itertools.combinations</c> enumera todos os subconjuntos.` Código: apenas `itertools.combinations_with_replacement` | O subtema exigia expressamente o uso de `itertools.combinations`. A prosa menciona a função, mas o bloco exemplifica apenas a versão com reposição (`combinations_with_replacement`). Para um aluno de Biologia, é essencial ver o código da combinação simples para não confundir com o caso com reposição.<br/>**Correção:** Incluir no bloco a linha:<br/>`trios_enum = list(itertools.combinations(range(10), 3))`<br/>`print(f"Trios de neurônios enumerados: {len(trios_enum)}")  # Trios de neurônios enumerados: 120` |
| **Formato / Pedagógico** | Seção 1 (`sec:7-1-1`), [rem:7-1-mult-vs-soma](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L119), linha ~119 | `porque os $1 \cdot 4 \cdot 1 = 4$ códons da forma $\text{A}\_\text{A}$ pertencem aos dois grupos.` | O uso de sublinhado escapado `\text{A}\_\text{A}` dentro de fórmula KaTeX pode ser confundido visualmente por alunos com índice inferior faltante ou caractere especial truncado. Em biologia molecular, posições arbitrárias usam o código IUPAC $\text{N}$ ou hífen explícito.<br/>**Correção:** Escrever `$\text{ANA}$ (isto é, $\text{A}$ na primeira posição, qualquer uma das $4$ bases na segunda e $\text{A}$ na terceira)`. |
| **Pedagógico** | Seção 4 (`sec:7-1-4`), [exm:7-1-sitio-restricao](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L721-L727), linhas ~721–727 | `ao longo de uma fita de DNA ... em média cerca de uma vez a cada $4\,096$ pares de bases!` | Uma fita simples é medida em nucleotídeos ou bases ($\text{nt}$ / $\text{b}$), enquanto o sítio duplex da enzima forma pares de bases ($\text{pb}$). Como a conta considera uma fita simples de $6$ posições independentes, vale afinar a linguagem para alunos rigorosos de biologia.<br/>**Correção:** Esclarecer: `em uma fita simples lida em $5' \to 3'$, o motivo de $6$ bases surge a cada $4\,096$ nucleotídeos, correspondendo no duplex ao sítio de restrição palindrômico de $6\text{ pb}$ da EcoRI.` |

---

## 3. Cobertura dos Subtemas Pedidos pelo Gestor

Todos os subtemas definidos pelo gestor foram integralmente abordados na estrutura da aula:

1. **Subtema 1 (`sec:7-1-1`): Princípio multiplicativo e princípio aditivo**
   - *Conteúdo coberto:* Árvore de possibilidades (*possibility tree*), princípio multiplicativo ($n_1 \cdot n_2 \cdots n_k$), princípio aditivo para casos disjuntos e inclusão-exclusão para uniões não disjuntas; sequências de comprimento $k$ com $n$ símbolos repetíveis ($n^k$).
   - *Exemplos biológicos obrigatórios:*
     - Códons de RNA: $4^3 = 64$ trincas possíveis, insuficiência de duplas ($4^2 = 16 < 20$ aminoácidos), 61 códons codificantes e 3 de parada ([exm:7-1-codons](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L71-L90)).
     - Sequências de DNA de 10 bases: $4^{10} = 1\,048\,576$ ([exm:7-1-codons](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L86-L88)).
     - Padrões binários de atividade de 10 neurônios corticais ($2^{10} = 1\,024$ configurações e 11 esparsas com $\le 1$ ativo) ([exm:7-1-padroes-neurais](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L92-L113)).
   - *Código:* `itertools.product` conferindo $4^3 = 64$ e simulação vetorizada em NumPy ([cod:7-1-codons](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L125-L136) e [cod:7-1-sim-principios](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L140-L156)).

2. **Subtema 2 (`sec:7-1-2`): Permutações e arranjos**
   - *Conteúdo coberto:* Fatorial e justificativa combinatória e analítica de $0! = 1$; permutações simples $P_n = n!$; arranjos simples $A(n, k) = \frac{n!}{(n-k)!}$ quando a ordem importa; permutações com repetição $\frac{n!}{n_1! \cdots n_r!}$.
   - *Exemplos obrigatórios:*
     - Contrabalanceamento de 4 condições em neuroimagem: $4! = 24$ ordens ([exm:7-1-contrabalanceamento](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L301-L312)).
     - Escolha ordenada de 3 dentre 8 estímulos visuais: $A(8, 3) = 8 \cdot 7 \cdot 6 = 336$ ([exm:7-1-contrabalanceamento](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L313-L316)).
     - Sequências de DNA de 6 bases com 2 A, 2 T, 1 G e 1 C: $\frac{6!}{2!\,2!\,1!\,1!} = 180$ ([exm:7-1-dna-composicao](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L319-L325)).
   - *Código:* `math.factorial`, `math.perm` e `itertools.permutations` ([cod:7-1-perm-arr](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L337-L346) e [cod:7-1-sim-perm](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L350-L363)).

3. **Subtema 3 (`sec:7-1-3`): Combinações e o triângulo de Pascal**
   - *Conteúdo coberto:* Combinação simples $C(n, k) = \binom{n}{k} = \frac{n!}{k!(n-k)!}$ quando a ordem não importa; relação com arranjos ($A(n, k) = k! \cdot C(n, k)$); simetria $\binom{n}{k} = \binom{n}{n-k}$; relação de Stifel $\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$ com demonstração curta recolhível via argumento de partição combinatória; triângulo de Pascal associado à figura [fig:7-1-pascal](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/fig/triangulo-pascal.svg); combinação com repetição $CR(n, k) = \binom{n+k-1}{k}$ via estrelas e barras (*stars and bars*).
   - *Exemplos biológicos obrigatórios:*
     - Pares de eletrodos em EEG de 64 canais para conectividade: $\binom{64}{2} = 2\,016$ pares ([exm:7-1-eeg-neuronios](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L497-L508)).
     - Seleção de 3 dentre 10 neurônios registrados: $\binom{10}{3} = 120$ trios ([exm:7-1-eeg-neuronios](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L509-L512)).
     - Genótipos de gene com $n$ alelos em organismo diploide: $\binom{n}{2} + n = \frac{n(n+1)}{2}$. Aplicação ao sistema ABO ($n=3$): 6 genótipos ($\text{AA}, \text{BB}, \text{OO}, \text{AO}, \text{BO}, \text{AB}$) gerando 4 fenótipos ($\text{A}, \text{B}, \text{AB}, \text{O}$) ([exm:7-1-genotipos-abo](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L515-L539)).
   - *Armadilha comum:* Diferenciar arranjo de combinação e evitar a contagem dupla de pares ([rem:7-1-ordem-importa](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L541-L545)).
   - *Código:* `math.comb` e `itertools.combinations_with_replacement` (sugerida adição de `itertools.combinations`).

4. **Subtema 4 (`sec:7-1-4`): Da contagem à probabilidade**
   - *Conteúdo coberto:* Definição clássica de probabilidade em espaços equiprováveis $P(A) = \frac{|A|}{|\Omega|}$ com aviso explícito de limitação a eventos equiprováveis; Binômio de Newton $(a+b)^n = \sum \binom{n}{k} a^k b^{n-k}$ com prova distributiva combinatória; consequência $\sum \binom{n}{k} = 2^n$; antecipação da fórmula binomial $\binom{n}{k} p^k (1-p)^{n-k}$ para o tema seguinte.
   - *Exemplos biológicos obrigatórios:*
     - Cruzamento $Aa \times Aa$: quadro de Punnett com 4 gametas equiprováveis, proporção genotípica $1:2:1$ ([exm:7-1-punnett](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L698-L712)).
     - Probabilidade de exatamente 2 filhos heterozigotos em 4 filhos: $\binom{4}{2} (1/2)^2 (1/2)^2 = 6/16 = 3/8 = 0{,}375$ ([exm:7-1-punnett](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L713-L716)).
     - Ocorrência do sítio de restrição EcoRI ($\text{GAATTC}$) de 6 pb ao acaso: $(1/4)^6 = 1/4\,096 \approx 0{,}000244$ ([exm:7-1-sitio-restricao](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L719-L728)).
   - *Código:* Simulação de 100 mil famílias em NumPy e conferência com `scipy.stats.binom.pmf` conferindo $3/8 = 0{,}375$ ([cod:7-1-sim-punnett](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L737-L761)).

---

## 4. Auditoria de Contas e Recálculo Passo a Passo

Todas as contas dos exemplos e dos exercícios foram refeitas e auditadas analiticamente:

### 4.1 Subtema 1: Princípio multiplicativo e princípio aditivo (`sec:7-1-1`)

1. **[Exemplo 7.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L71-L90) (`exm:7-1-codons`):**
   - Item (a): Duplas de $4$ bases: $4^2 = 16$. Como $16 < 20$, insuficiente. **Correto.**
   - Item (b): Trincas: $4^3 = 64$. Códons de parada $= 3$. Códons codificantes: $64 - 3 = 61$. **Correto.**
   - Item (c): Sequências de DNA de 10 bases: $4^{10} = (2^2)^{10} = 2^{20} = 1\,024 \times 1\,024 = 1\,048\,576$. **Correto.**

2. **[Exemplo 7.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L92-L113) (`exm:7-1-padroes-neurais`):**
   - Item (a): $10$ neurônios binários: $2^{10} = 1\,024$. **Correto.**
   - Item (b): Padrões esparsos com $\le 1$ neurônio ativo: $0$ ativos ($1$ padrão: todos $0$) $+ 1$ ativo ($10$ padrões com um único $1$). Total: $1 + 10 = 11$. **Correto.**

3. **[Exercício 7.1.1.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L158-L176) (`exr:7-1-1-1`):**
   - Item (a): $2$ letras com repetição ($26^2 = 676$) e $3$ dígitos com repetição ($10^3 = 1\,000$). Total: $676 \times 1\,000 = 676\,000$. **Correto.**
   - Item (b): Dígitos distintos: $10 \times 9 \times 8 = 720$. Total: $676 \times 720 = 486\,720$. **Correto.**

4. **[Exercício 7.1.1.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L178-L196) (`exr:7-1-1-2`):**
   - Item (a): Começam com $\text{A}$: $1 \times 4 \times 4 = 16$. **Correto.**
   - Item (b): Pelo menos um $\text{A}$: Total ($64$) $-$ sem nenhum $\text{A}$ ($3^3 = 27$): $64 - 27 = 37$. **Correto.**

5. **[Exercício 7.1.1.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L198-L216) (`exr:7-1-1-3`):**
   - Item (a): Tripeptídeos com $20$ aminoácidos: $20^3 = 8\,000$. **Correto.**
   - Item (b): Primeiro e último idênticos: $20 \times 20 \times 1 = 400$. **Correto.**

6. **[Exercício 7.1.1.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L218-L246) (`exr:7-1-1-4`):**
   - Frequência teórica: $\frac{11}{1\,024} \approx 0{,}010742 \approx 0{,}0107$. Código de simulação e contagem exata conferidos. **Correto.**

---

### 4.2 Subtema 2: Permutações e arranjos (`sec:7-1-2`)

1. **[Exemplo 7.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L301-L317) (`exm:7-1-contrabalanceamento`):**
   - Item (a): Contrabalanceamento de $4$ condições: $P_4 = 4! = 24$. **Correto.**
   - Item (b): $3$ de $8$ estímulos em ordem: $A(8, 3) = \frac{8!}{5!} = 8 \times 7 \times 6 = 336$. **Correto.**

2. **[Exemplo 7.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L319-L325) (`exm:7-1-dna-composicao`):**
   - $6$ bases ($2\text{A}, 2\text{T}, 1\text{G}, 1\text{C}$): $\frac{6!}{2!\,2!\,1!\,1!} = \frac{720}{4} = 180$. **Correto.**

3. **[Exercício 7.1.2.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L365-L383) (`exr:7-1-2-1`):**
   - Item (a): $5$ estímulos distintos: $P_5 = 5! = 120$. **Correto.**
   - Item (b): Referência fixa na primeira posição: $1 \times 4! = 24$. **Correto.**

4. **[Exercício 7.1.2.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L385-L393) (`exr:7-1-2-2`):**
   - $3$ fármacos em $3$ dias distintos dentre $10$: $A(10, 3) = 10 \times 9 \times 8 = 720$. **Correto.**

5. **[Exercício 7.1.2.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L395-L403) (`exr:7-1-2-3`):**
   - Pentapeptídeos ($2\text{Ala}, 2\text{Gly}, 1\text{Ser}$): $\frac{5!}{2!\,2!\,1!} = \frac{120}{4} = 30$. **Correto.**

6. **[Exercício 7.1.2.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L405-L435) (`exr:7-1-2-4`):**
   - $A(6, 4) = 360$. Começam com $0$: $A(5, 3) = 60$. Proporção: $\frac{60}{360} = \frac{1}{6} \approx 0{,}1667$. Código exato e simulação conferidos. **Correto.**

---

### 4.3 Subtema 3: Combinações e o triângulo de Pascal (`sec:7-1-3`)

1. **[Exemplo 7.5](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L497-L513) (`exm:7-1-eeg-neuronios`):**
   - Item (a): Pares de eletrodos em EEG de 64 canais: $\binom{64}{2} = \frac{64 \times 63}{2} = 32 \times 63 = 2\,016$. **Correto.**
   - Item (b): Trios dentre $10$ neurônios: $\binom{10}{3} = \frac{10 \times 9 \times 8}{6} = 120$. **Correto.**

2. **[Exemplo 7.6](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L515-L539) (`exm:7-1-genotipos-abo`):**
   - Item (a): Homozigotos $= n$; heterozigotos $= \binom{n}{2} = \frac{n(n-1)}{2}$. Total: $\frac{n(n-1) + 2n}{2} = \frac{n(n+1)}{2}$. Equivalência com $CR(n, 2) = \binom{n+1}{2}$. **Correto.**
   - Item (b): Para $n = 3$ (ABO): $\frac{3 \times 4}{2} = 6$ genótipos ($\text{AA}, \text{BB}, \text{OO}, \text{AO}, \text{BO}, \text{AB}$) e $4$ fenótipos ($\text{A}, \text{B}, \text{AB}, \text{O}$). **Correto.**

3. **[Exercício 7.1.3.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L584-L592) (`exr:7-1-3-1`):**
   - Pares não ordenados entre $100$ neurônios: $\binom{100}{2} = \frac{100 \times 99}{2} = 4\,950$. **Correto.**

4. **[Exercício 7.1.3.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L594-L603) (`exr:7-1-3-2`):**
   - Gene com $4$ alelos: $\frac{4 \times 5}{2} = 10$ genótipos ($4$ homozigotos $+ 6$ heterozigotos). **Correto.**

5. **[Exercício 7.1.3.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L605-L617) (`exr:7-1-3-3`):**
   - Subconjuntos de $5$ eletrodos em $32$:
     $$\binom{32}{5} = \frac{32 \times 31 \times 30 \times 29 \times 28}{120} = 8 \times 31 \times 29 \times 28 = 248 \times 812 = 201\,376.$$
     Contas passo a passo auditadas e exatas. **Correto.**

6. **[Exercício 7.1.3.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L619-L652) (`exr:7-1-3-4`):**
   - Item (a): $CR(3, 4) = \binom{3+4-1}{4} = \binom{6}{4} = \binom{6}{2} = 15$. **Correto.**
   - Item (b): Eletrodo $0$ na ROI: $\frac{\binom{31}{4}}{\binom{32}{5}} = \frac{5}{32} = 0{,}15625$. Simulação e código em Python conferidos. **Correto.**

---

### 4.4 Subtema 4: Da contagem à probabilidade (`sec:7-1-4`)

1. **[Exemplo 7.7](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L698-L717) (`exm:7-1-punnett`):**
   - Item (a): Cruzamento $Aa \times Aa$: $\Omega = \{AA, Aa, aA, aa\}$. $P(AA) = 1/4$, $P(Aa) = 2/4 = 1/2$, $P(aa) = 1/4$. **Correto.**
   - Item (b): $4$ filhos, exatamente $2$ heterozigotos: $\binom{4}{2} (1/2)^2 (1/2)^2 = 6 \times \frac{1}{16} = \frac{3}{8} = 0{,}375$. **Correto.**

2. **[Exemplo 7.8](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L719-L728) (`exm:7-1-sitio-restricao`):**
   - Sítio EcoRI de $6$ bases equiprováveis: $(1/4)^6 = \frac{1}{4\,096} \approx 0{,}00024414 \approx 2{,}44 \times 10^{-4}$. **Correto.**

3. **[Exercício 7.1.4.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L763-L781) (`exr:7-1-4-1`):**
   - Item (a): Códon de parada: $3/64 \approx 0{,}046875 \approx 0{,}0469$ ($4{,}69\%$). **Correto.**
   - Item (b): Sem uracila: $3^3 / 64 = 27/64 \approx 0{,}421875 \approx 0{,}4219$ ($42{,}19\%$). **Correto.**

4. **[Exercício 7.1.4.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L783-L795) (`exr:7-1-4-2`):**
   - Pelo menos um $aa$ em $3$ filhos: $1 - (3/4)^3 = 1 - 27/64 = 37/64 \approx 0{,}578125 \approx 0{,}5781$ ($57{,}81\%$). **Correto.**

5. **[Exercício 7.1.4.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L797-L810) (`exr:7-1-4-3`):**
   - Padrões com número par de ativos em $8$ neurônios:
     $$(1 + 1)^8 + (1 - 1)^8 = 256 + 0 = 2 \sum_{k \text{ par}} \binom{8}{k} \implies \sum_{k \text{ par}} \binom{8}{k} = 128.$$
     Probabilidade: $128 / 256 = 1/2 = 0{,}5$. Conferência pela linha 8 do Triângulo de Pascal: $1 + 28 + 70 + 28 + 1 = 128$. **Correto.**

6. **[Exercício 7.1.4.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L812-L844) (`exr:7-1-4-4`):**
   - Janelas deslizantes em $100\,000$ bases: $100\,000 - 6 + 1 = 99\,995$ janelas. Ocorrências esperadas: $99\,995 / 4\,096 \approx 24{,}41$. Frequência teórica: $1 / 4\,096 \approx 0{,}000244$.
   - **Atenção:** Como demonstrado na Tabela de Problemas, a implementação em código possui um bug na codificação da base final ($C=3$ vs. teste de $2$). **Requer correção.**

---

## 5. Auditoria Linha a Linha dos Blocos de Código Python

Todos os blocos de código foram inspecionados quanto a sintaxe, dependências, formas de vetores (*shapes*) e saídas comentadas:

1. **[cod:7-1-codons](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L125-L136):**
   - Imports: `import itertools`.
   - Lógica: `itertools.product(bases, repeat=3)` gera 64 trincas; filtro por `c[0] == "A"` resulta em 16.
   - Comentários de saída: `Total de códons: 64`, `Códons que começam com A: 16`, `DNA de 10 bases: 1048576`, `Padrões de 10 neurônios: 1024`. **Batem exatamente.**

2. **[cod:7-1-sim-principios](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L140-L156):**
   - Imports: `import numpy as np`. Semente fixa: `np.random.default_rng(42)`.
   - Vetorização: matriz de inteiros $(100\,000, 3)$ com valores em $\{0, 1, 2, 3\}$.
   - Condições booleanas para códons de parada (UAA: 1,0,0; UAG: 1,0,2; UGA: 1,2,0) perfeitamente definidas.
   - Saída: `Frequência simulada de parada: 0.0469` contra teórico $3/64 = 0{,}046875$. **Bate com a simulação.**

3. **Solução de [exr:7-1-1-4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L227-L245):**
   - Imports: `itertools`, `numpy`.
   - Contagem exata via list comprehension com `sum(p) <= 1` devolve 11.
   - Simulação com matriz $(100\,000, 10)$ e soma em `axis=1`.
   - Saídas comentadas: 1024, 11 e `aprox. 0.0107`. **Batem perfeitamente.**

4. **[cod:7-1-perm-arr](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L337-L346):**
   - Imports: `itertools`, `math`.
   - `math.factorial(4) == 24`, `math.perm(8, 3) == 336`, `len(set(itertools.permutations("AATTGC"))) == 180`. **Batem perfeitamente.**

5. **[cod:7-1-sim-perm](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L350-L363):**
   - Geração engenhosa de permutações uniformes em lote via `rng.random((n_sim, 4)).argsort(axis=1)`.
   - Verificação de adjacência `(perms[:, :-1] == 0) & (perms[:, 1:] == 1)`.
   - Saída comentada: `aprox. 0.25 (teórico: 6/24 = 0.25)`. **Bate com a teoria.**

6. **Solução de [exr:7-1-2-4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L414-L434):**
   - `math.perm(6, 4) == 360`, `len(arranjos) == 360`, filtragem por `a[0] == 0` dá 60.
   - Simulação `[:, :4]` com conferência empírica de `0.1667`. **Bate perfeitamente.**

7. **[cod:7-1-comb-stifel](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L548-L564):**
   - `math.comb(64, 2) == 2016`, `math.comb(10, 3) == 120`.
   - Stifel: $56 == 56$. Genótipos ABO: lista de 6 elementos gerada por `combinations_with_replacement`.
   - *Ressalva pedagógica:* Falta ilustrar `itertools.combinations` simples.

8. **[cod:7-1-sim-comb](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L568-L582):**
   - Simulação de subconjuntos de 3 neurônios a partir de 10. `(sorteios >= 3).all(axis=1)` verifica neurônios inibitórios.
   - Saídas comentadas: `0.2917` e `0.2917`. **Batem com exatidão.**

9. **Solução de [exr:7-1-3-4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L631-L651):**
   - `math.comb(3 + 4 - 1, 4) == 15`. Simulação de inclusão do canal 0 em ROI de 5 dentre 32.
   - Saídas comentadas: `0.15625` e `0.15625`. **Batem com exatidão.**

10. **[cod:7-1-sim-punnett](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L737-L761):**
    - `scipy.stats.binom.pmf(2, n=4, p=0.5)` e contagem manual `math.comb(4, 2) * (0.5**2) * (0.5**2)`.
    - Simulação com arrays booleanos `gameta_pai != gameta_mae`.
    - Saídas: `0.3750` e `0.3750`. **Batem com exatidão.**

11. **Solução de [exr:7-1-4-4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L817-L843):**
    - Vetor de $100\,000$ inteiros em $\{0, 1, 2, 3\}$.
    - Fatiamento com 6 janelas deslocadas de $99\,995$ posições.
    - **Erro encontrado:** O fatiamento `fita[5:] == 2` compara a 6ª base com o valor $2$ ($\text{G}$), em vez de $3$ ($\text{C}$), descompassado com a definição da enzima EcoRI e com a própria legenda no comentário.

---

## 6. Auditoria de Neurociência e Biologia

1. **Afirmações de Neurociência:**
   - O uso de blocos de repouso, faces, casas e palavras para fMRI reflete tarefas clássicas de mapeamento visual ventral (área de faces fusiforme - FFA, área de lugares para-hipocampal - PPA) descritas em manuais (Kandel et al., *Principles of Neural Science*).
   - O modelo de conectividade funcional em matrizes triangulares a partir de pares de eletrodos em EEG ($2\,016$ pares para 64 canais) é a prática padrão de campo em neurofisiologia e neuroimagem.
   - A discretização de estados binários (disparo/silêncio em janelas de 10 ms) é a abordagem clássica de modelos de máxima entropia (*Ising models*) aplicados a redes corticais (Dayan & Abbott, *Theoretical Neuroscience*, Cap. 1–2).
   - Todas as afirmações de neurociência são rigorosas e de livro-texto.

2. **Afirmações de Biologia Molecular e Genética:**
   - Código genético: 64 códons, 61 codificantes e 3 de parada ($\text{UAA}, \text{UAG}, \text{UGA}$); redundância/degenerescência do código genético. Impossibilidade de duplas ($4^2 = 16 < 20$). Fatos padrão de bioquímica e biologia molecular (Alberts et al., *Molecular Biology of the Cell*).
   - Sistema sanguíneo ABO: 3 alelos autossômicos ($\text{A}, \text{B}, \text{O}$), codominância entre $\text{A}$ e $\text{B}$, recessividade de $\text{O}$, resultando em 6 genótipos e 4 fenótipos.
   - Enzima de restrição EcoRI: endonuclease de restrição tipo II que reconhece o sítio palindrômico $5'\text{-GAATTC-}3'$.
   - Todas as afirmações biológicas são autênticas e precisas.

---

## 7. Estrutura Editorial, Formato e Sintaxe Delta

1. **Estrutura Geral:**
   - Documento no formato `<document>` com único `<chapter id="tema-7-1">`.
   - Metadados completos com link de retorno ao guia (`../../index.html#tema-7-1`).
   - Abertura com "Por que isso importa", Objetivos com verbos de ação e Pré-requisitos claros.
   - Seção de "Resumo" com 8 itens objetivos e fórmulas-chave.
   - Seção "Para ir além" apontando diretamente para os materiais do `index.html` (livro do Tertuliano, canal StatQuest e documentação oficial de `scipy.stats`).

2. **Exercícios, Dicas e Demonstrações:**
   - 16 exercícios graduados (4 por seção: Básico, Básico/Intermediário, Intermediário, Avançado).
   - **100% dos exercícios possuem `<hint>` e `<solution>` completa**, com justificativa matemática e contextualização biológica/computacional.
   - Todas as soluções e demonstrações utilizam `collapsible="true" collapsed="true"`.
   - Demonstrações de proposições e teoremas (Stifel e Binômio de Newton) estão devidamente associadas via atributo `of="..."`.

3. **Figuras:**
   - Referência a [fig:7-1-pascal](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/fig/triangulo-pascal.svg) com arquivo SVG existente, gerado pelo script [triangulo-pascal.py](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/fig/triangulo-pascal.py).
   - Atributos `alt` e `caption` informativos e precisos.

4. **Sintaxe XML e Delta:**
   - Não há tags proibidas (`<interactive>`, `<cite>`, `<bibliography>`, `<youtube>`).
   - Todos os atributos possuem valor explícito (`numbered="false"`, `collapsible="true"`, `collapsed="true"`).
   - Matemática KaTeX delimitada corretamente por `$...$` e `$$...$$` sem quebras de linha em branco.
   - Entidades HTML na prosa devidamente tratadas.

5. **Extensão e Notação:**
   - Contagem aproximada de palavras: ~4.600 palavras (perfeitamente dentro da faixa de 2.500 a 5.000 palavras para 4 subtemas).
   - Notação consistente em todo o documento: $\binom{n}{k}$, $A(n, k)$, $P_n$, $CR(n, k)$, vírgula decimal na prosa e ponto no código.

---

## 8. Conclusão e Próximos Passos

A aula está primorosamente escrita e estruturada. Para que receba o parecer de **APROVAR**, o autor deve executar as seguintes correções pontuais em [conteudo/modulo-07/tema-01.dlt](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt):

1. **No [exr:7-1-4-4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L823-L833):** Corrigir a codificação da base citosina ($\text{C}$) para $3$ tanto no comentário quanto na comparação booleana (`fita[5:] == 3`).
2. **No bloco [cod:7-1-comb-stifel](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L548-L564):** Inserir um exemplo explícito de enumeração de combinações simples com `itertools.combinations`.
3. **No [rem:7-1-mult-vs-soma](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L119):** Substituir a notação `\text{A}\_\text{A}` por `\text{ANA}` com explicação verbal.
4. **No [exm:7-1-sitio-restricao](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-07/tema-01.dlt#L721-L727):** Ajustar o texto para distinguir com precisão nucleotídeos em fita simples e pares de bases no duplex.

Após a aplicação dessas correções, a aula atingirá nota máxima de exatidão técnica, didática e computacional.
