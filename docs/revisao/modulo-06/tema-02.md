# Relatório de Revisão Técnica — Módulo 06 · Tema 02 (Comandos iniciais e lógica básica)

- **Arquivo revisado:** [tema-02.dlt](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-06/tema-02.dlt)
- **Documentos de referência:** [PADRAO-AULAS.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/PADRAO-AULAS.md) e [DELTA-COLA.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/DELTA-COLA.md)
- **Data da revisão:** 14 de novembro de 2026
- **Perfil do revisor:** Matemático, Neurocientista Computacional, Programador Python Sênior e Professor de Alunos de Ciências Biológicas

---

## 1. Veredito

**APROVAR**

A aula [tema-02.dlt](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-06/tema-02.dlt) apresenta qualidade técnica, didática e conceitual excepcional. Todos os códigos Python são autocontidos e executam exatamente como apresentado; cada comentário de saída foi auditado e bate de forma estrita com a saída real do interpretador Python 3; todas as contas numéricas de exemplos e exercícios foram integralmente recalculadas e confirmadas; a sintaxe Delta v0.6.0 foi rigorosamente respeitada (sem tags proibidas, com XML estrito bem formatado, IDs limpos e ambientes devidamente fechados); as contextualizações biológicas são autênticas, baseadas em literatura clássica (Dayan & Abbott; Kandel; Hodgkin & Huxley; Luck); e a progressão pedagógica é perfeitamente calibrada para alunos de Biologia em transição para a Neurociência Computacional.

Foram identificadas 4 observações de refinamento pedagógico e formatação na tabela a seguir, nenhuma de natureza impeditiva.

---

## 2. Tabela de Problemas e Observações

| Severidade | Local | Trecho | Correção sugerida |
|---|---|---|---|
| Formato | Seção 2 (`sec:6-2-2`), linha ~305 | `alinhamento à direita em campo de largura fixa (como $5$ caracteres), usando dois-pontos e o sinal de maior seguido da largura, como mostrado no bloco abaixo (útil para manter colunas retas).` | Para consistência com os dois itens anteriores da lista (que usam `<c>f"{taxa:.1f} Hz"</c>` e `<c>f"{fracao:.1%}"</c>`), sugere-se incluir o padrão inline em código: `<item><c>f"{n:>5}"</c>: alinhamento à direita em campo de largura fixa ($5$ caracteres), preenchendo com espaços à esquerda (útil para tabelas e relatórios alinhados).</item>`. |
| Pedagógico | Seção 3 (`sec:6-2-3`), `exr:6-2-3-3`, linha ~553 | `v_ok = (-80.0 <= v_rep) and (v_rep <= -58.0)` | A formulação com `and` é pedagogicamente correta para exercitar operadores lógicos compostos. Como enriquecimento de repertório da linguagem Python, recomenda-se adicionar uma nota comentada na solução informando que o Python também aceita comparações encadeadas: `v_ok = -80.0 <= v_rep <= -58.0`, idêntica à notação algébrica usual. |
| Pedagógico | Seção 4 (`sec:6-2-4`), `exr:6-2-4-2`, linha ~757 | `else:`<br>`    comp = "C"` | O laço assume implicitamente que qualquer base diferente de `'A'`, `'T'` e `'C'` é `'G'`. Em pipelines reais de bioinformática, leituras podem conter bases ambíguas (como `'N'`) ou ruídos. Sugere-se explicitar no enunciado que a fita é composta estritamente pelas 4 bases canônicas maiúsculas, ou estruturar o condicional com `elif base == "G": comp = "C"` e um `else:` preventivo (como `comp = "N"`). |
| Pedagógico | Seção 4 (`sec:6-2-4`), `exr:6-2-4-3`, linha ~785 | `duracao_s = (len(traco) * dt_ms) / 1000` | Para $N = 20$ amostras com espaçamento $\Delta t = 1{,}0\text{ ms}$, o intervalo entre o primeiro e o último ponto cobre $(N - 1) \cdot \Delta t = 19\text{ ms} = 0{,}019\text{ s}$. Como o enunciado definiu formalmente "janela total de $0{,}02\text{ s}$" (tratando as 20 amostras como 20 caixas temporais de $1\text{ ms}$ cada), a conta da solução está perfeitamente coerente com o texto; sugere-se apenas uma breve frase esclarecendo essa convenção de caixa de amostragem para evitar dúvidas de alunos mais formalistas. |

---

## 3. Recálculo e Auditoria de Contas

Todas as contas dos exemplos e das soluções dos exercícios foram refeitas passo a passo:

### 3.1 Subtema 1: Variáveis, tipos e operadores (`sec:6-2-1`)

1. **[Exemplo 6.2.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-06/tema-02.dlt#L127-L144) (`exm:6-2-mv-taxa`):**
   - Conversão de potencial: $V = \frac{-70\text{ mV}}{1\,000} = -0{,}07\text{ V}$.
   - Taxa média de disparo: $\text{taxa} = \frac{36\text{ spikes}}{1{,}5\text{ s}} = 24{,}0\text{ Hz}$.
   - Tipo retornado por `/`: `float` em ambas as operações. **Correto.**
2. **[Exemplo 6.2.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-06/tema-02.dlt#L146-L166) (`exm:6-2-duracao-registro`):**
   - Divisão inteira: $125 // 60 = 2$ horas.
   - Resto: $125 \% 60 = 5$ minutos ($2 \times 60 + 5 = 125$).
   - Condição booleana: $(2 \ge 2) \land (120 \ge 100) \equiv \text{True} \land \text{True} \equiv \text{True}$.
   - Atribuição composta: $120 + 15 = 135$. **Correto.**
3. **[Armadilha de ponto flutuante](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-06/tema-02.dlt#L168-L182) (`rem:6-2-ponto-flutuante`):**
   - Em ponto flutuante IEEE 754 de 64 bits, $0{,}1 + 0{,}2 = 0{,}300000000000000044408920985006\dots$
   - Comparação exata $0{,}1 + 0{,}2 == 0{,}3$ resulta em `False`.
   - $|(0{,}1 + 0{,}2) - 0{,}3| \approx 5{,}55 \times 10^{-17} < 10^{-9}$ resulta em `True`.
   - `math.isclose(0.1 + 0.2, 0.3)` avalia com tolerância relativa padrão $10^{-9}$ e retorna `True`. **Correto.**
4. **[Exercício 6.2.1.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-06/tema-02.dlt#L184-L202) (`exr:6-2-1-1`):**
   - Temperatura: $T_K = 37{,}5 + 273{,}15 = 310{,}65\text{ K}$.
   - Duração: $\text{janela\_s} = \frac{250\text{ ms}}{1\,000} = 0{,}25\text{ s}$.
   - Tipos inspecionados: `temp_c` é `<class 'float'>` e `janela_ms` é `<class 'int'>`. **Correto.**
5. **[Exercício 6.2.1.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-06/tema-02.dlt#L204-L222) (`exr:6-2-1-2`):**
   - Horas: $7\,520 // 3\,600 = 2$.
   - Resto após horas: $7\,520 \% 3\,600 = 320\text{ s}$.
   - Minutos: $320 // 60 = 5$.
   - Segundos finais: $320 \% 60 = 20$.
   - Prova real: $2 \times 3\,600 + 5 \times 60 + 20 = 7\,200 + 300 + 20 = 7\,520\text{ s}$. **Correto.**
6. **[Exercício 6.2.1.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-06/tema-02.dlt#L224-L244) (`exr:6-2-1-3`):**
   - Análise dimensional: $1\text{ M}\Omega \cdot 1\text{ nA} = 10^6\,\Omega \cdot 10^{-9}\text{ A} = 10^{-3}\text{ V} = 1\text{ mV}$.
   - Potencial inicial: $V_m = -70{,}0 + (50{,}0 \times 0{,}2) = -70{,}0 + 10{,}0 = -60{,}0\text{ mV}$.
   - Após incremento com `+=`: $V_m = -60{,}0 + 6{,}0 = -54{,}0\text{ mV}$.
   - Teste lógico: $(-54{,}0 \ge -55{,}0) \land (-54{,}0 < 40{,}0) \equiv \text{True} \land \text{True} \equiv \text{True}$. **Correto.**
7. **[Exercício 6.2.1.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-06/tema-02.dlt#L246-L263) (`exr:6-2-1-4`):**
   - Três passos: $0{,}1 + 0{,}1 + 0{,}1 = 0{,}30000000000000004$.
   - `t_acumulado == 0.3` dá `False`.
   - `abs(t_acumulado - 0.3) < 1e-9` dá `True`.
   - `math.isclose(t_acumulado, 0.3)` dá `True`. **Correto.**

---

### 3.2 Subtema 2: Texto e saída: strings e f-strings (`sec:6-2-2`)

1. **[Exemplo 6.2.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-06/tema-02.dlt#L320-L338) (`exm:6-2-conteudo-gc`):**
   - String normalizada: `"atgGCcGt".upper()` $\to$ `"ATGGCCGT"`, tamanho $N = 8$.
   - Contagens: `'G'` aparece nas posições 2, 3 e 6 ($3$ vezes); `'C'` nas posições 4 e 5 ($2$ vezes).
   - Total GC: $3 + 2 = 5$.
   - Fração GC: $5 / 8 = 0{,}625$.
   - Formatação `:.1%`: $0{,}625 \times 100\% = 62{,}5\%$. **Correto.**
2. **[Exemplo 6.2.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-06/tema-02.dlt#L340-L358) (`exm:6-2-tabela-fstring`):**
   - Taxas de disparo: $45 / 2{,}0 = 22{,}5\text{ Hz}$; $128 / 2{,}0 = 64{,}0\text{ Hz}$.
   - Alinhamento de campos: `45:>5` produz três espaços e "45" (`"   45"`, 5 caracteres); `128:>5` produz dois espaços e "128" (`"  128"`, 5 caracteres).
   - Saídas formatadas: `"N01 |    45 spikes | 22.5 Hz"` e `"N02 |   128 spikes | 64.0 Hz"`. Perfeito alinhamento de colunas. **Correto.**
3. **[Exercício 6.2.2.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-06/tema-02.dlt#L368-L383) (`exr:6-2-2-1`):**
   - `sujeito.upper()` gera `"CAMUNDONGO_04"`.
   - `amostras = 500` com `:>5` preenche dois espaços à esquerda (`"  500"`).
   - `18.46` formatado com `:.1f` arredonda para `18.5`.
   - Saída gerada: `"CAMUNDONGO_04 |   500 amostras | 18.5 Hz"`. **Correto.**
4. **[Exercício 6.2.2.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-06/tema-02.dlt#L385-L401) (`exr:6-2-2-2`):**
   - DNA inicial: `"atgCgtTacA"`.
   - Maiúsculas: `"ATGCGTTACA"`.
   - Substituição de `'T'` por `'U'`: `"AUGCGUUACA"` ($N = 10$).
   - Primeira base: `rna[0] == "A"`.
   - Ocorrências de `'U'`: índices 1, 5 e 6 ($3$ uracilas).
   - Fração: $3 / 10 = 0{,}300 \to 30{,}0\%$. **Correto.**
5. **[Exercício 6.2.2.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-06/tema-02.dlt#L403-L418) (`exr:6-2-2-3`):**
   - String original: `"sujeito_a;v1;2000hz"`.
   - Processamento: `.upper()` $\to$ `"SUJEITO_A;V1;2000HZ"`, `.replace(";", " | ")` $\to$ `"SUJEITO_A | V1 | 2000HZ"`, `.replace("_", "-")` $\to$ `"SUJEITO-A | V1 | 2000HZ"`.
   - Contagem de caracteres: `len("SUJEITO-A")` ($9$) + `len(" | ")` ($3$) + `len("V1")` ($2$) + `len(" | ")` ($3$) + `len("2000HZ")` ($6$) = $9 + 3 + 2 + 3 + 6 = 23$.
   - Contagem do caractere `'0'`: em `"2000HZ"` aparecem exatamente $3$ dígitos zero. **Correto.**

---

### 3.3 Subtema 3: Decisões com if, elif e else (`sec:6-2-3`)

1. **[Exemplo 6.2.5](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-06/tema-02.dlt#L439-L465) (`exm:6-2-estado-membrana`):**
   - Partição de $\mathbb{R}$:
     - $[-55{,}0;\, +\infty) \to$ "acima do limiar"
     - $(-69{,}5;\, -55{,}0) \to$ "despolarizado"
     - $[-70{,}5;\, -69{,}5] \to$ "em repouso"
     - $(-\infty;\, -70{,}5) \to$ "hiperpolarizado"
   - Avaliação para $V_m = -62{,}0\text{ mV}$:
     - $-62{,}0 \ge -55{,}0 \implies \text{False}$
     - $-62{,}0 > -69{,}5 \implies \text{True} \to$ estado = `"despolarizado"`. **Correto.**
2. **[Exemplo 6.2.6](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-06/tema-02.dlt#L467-L487) (`exm:6-2-classificar-ph`):**
   - Para $\text{pH} = 7{,}40$:
     - $7{,}40 < 0 \lor 7{,}40 > 14 \implies \text{False}$
     - $7{,}40 < 6{,}95 \implies \text{False}$
     - $7{,}40 \le 7{,}05 \implies \text{False}$
     - `else:` $\to$ classe = `"básica"`.
   - Saída formatada: `"pH 7.40: solução básica"`. **Correto.**
3. **[Exercício 6.2.3.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-06/tema-02.dlt#L497-L521) (`exr:6-2-3-1`):**
   - $f = 10{,}5\text{ Hz}$.
   - $10{,}5 < 4 \implies \text{False}$; $10{,}5 < 8 \implies \text{False}$; $10{,}5 < 13 \implies \text{True} \to$ banda `"alfa"`. **Correto.**
4. **[Exercício 6.2.3.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-06/tema-02.dlt#L523-L540) (`exr:6-2-3-2`):**
   - `codigo_amostra = ""` é falsy $\implies$ `not ""` avalia para `True`.
   - Pela regra do curto-circuito em `or`, a expressão completa é `True`.
   - Imprime `"Registro inválido"`. **Correto.**
5. **[Exercício 6.2.3.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-06/tema-02.dlt#L542-L566) (`exr:6-2-3-3`):**
   - $V_{\text{rep}} = -68{,}0\text{ mV} \in [-80{,}0;\, -58{,}0] \implies v_{\text{ok}} = \text{True}$.
   - $R_{\text{acesso}} = 18{,}5\text{ M}\Omega \le 25{,}0\text{ M}\Omega \implies r_{\text{ok}} = \text{True}$.
   - $v_{\text{ok}} \land r_{\text{ok}} \implies \text{True} \to$ imprime `"Célula aceita"`. **Correto.**
6. **[Exercício 6.2.3.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-06/tema-02.dlt#L568-L588) (`exr:6-2-3-4`):**
   - `codon = "atg".upper()` $\to$ `"ATG"`.
   - `len(codon) != 3` $\implies \text{False}$.
   - `codon == "ATG"` $\implies \text{True} \to$ imprime `"Códon de início (ATG)"`. **Correto.**

---

### 3.4 Subtema 4: Repetição: for e while (`sec:6-2-4`)

1. **[Exemplo 6.2.7](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-06/tema-02.dlt#L613-L630) (`exm:6-2-for-gc`):**
   - Sequência: `"ATGGCCGT"`.
   - Itera base a base: incrementa em $i \in \{2, 3, 4, 5, 6\}$, acumulando $gc = 5$.
   - Conferência com métodos: `.count("G") + .count("C") = 3 + 2 = 5`. **Correto.**
2. **[Exemplo 6.2.8](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-06/tema-02.dlt#L634-L653) (`exm:6-2-cruzamento-limiar`):**
   - Série: `[-70, -68, -54, -40, 20, -60, -72, -65, -55, 10, -68]`, limiar = $-55\text{ mV}$.
   - Cruzamento 1: $i = 2$, transição de $-68$ para $-54$ ($-68 < -55 \land -54 \ge -55$).
   - Transições $i = 3$ ($-54 \to -40$) e $i = 4$ ($-40 \to 20$): amostra anterior $\ge -55$, não conta.
   - Cruzamento 2: $i = 8$, transição de $-65$ para $-55$ ($-65 < -55 \land -55 \ge -55$).
   - Total de disparos detectados: $2$. Amostras individuais $\ge -55$: seriam $5$ (mostrando a relevância biofísica do algoritmo). **Correto.**
3. **[Exemplo 6.2.9](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-06/tema-02.dlt#L669-L685) (`exm:6-2-while-bacterias`):**
   - População inicial: $N_0 = 100$.
   - Equação: $N(g) = 100 \cdot 2^g$.
   - $N(13) = 100 \cdot 8\,192 = 819\,200 \le 1\,000\,000$ (executa mais uma iteração).
   - $N(14) = 100 \cdot 16\,384 = 1\,638\,400 > 1\,000\,000$ (condição torna-se `False`, laço encerra).
   - Resposta do `while`: `Gerações: 14 | População: 1638400`. **Correto.**
4. **[Exemplo 6.2.10](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-06/tema-02.dlt#L689-L705) (`cod:6-2-break-continue`):**
   - Leituras: `[-70, None, -65, -52, 120, -68]`.
   - $-70$: válida, soma = $-70$, $n = 1$.
   - `None`: `continue` salta para a próxima iteração.
   - $-65$: válida, soma = $-135$, $n = 2$.
   - $-52$: válida, soma = $-187$, $n = 3$.
   - $120$: saturação $\ge 100$, `break` encerra o laço (o último valor $-68$ nunca é lido).
   - Média: $\frac{-187}{3} \approx -62{,}333\dots \to -62{,}3\text{ mV}$. **Correto.**
5. **[Exercício 6.2.4.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-06/tema-02.dlt#L716-L737) (`exr:6-2-4-1`):**
   - Taxas: $[12{,}0;\, 45{,}5;\, 8{,}5;\, 30{,}0;\, 24{,}0]\text{ Hz}$.
   - Soma: $12{,}0 + 45{,}5 + 8{,}5 + 30{,}0 + 24{,}0 = 120{,}0\text{ Hz}$.
   - Média: $120{,}0 / 5 = 24{,}0\text{ Hz}$.
   - Maiores que $20{,}0\text{ Hz}$: $45{,}5$, $30{,}0$ e $24{,}0$ ($3$ neurônios). **Correto.**
6. **[Exercício 6.2.4.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-06/tema-02.dlt#L739-L764) (`exr:6-2-4-2`):**
   - Fita: $5'\text{-ATGGCT-}3'$.
   - Complementar direto: $3'\text{-TACCGA-}5'$.
   - Complementar reverso: $5'\text{-AGCCAT-}3'$.
   - Execução do acumulador `comp + rev_comp`:
     - `'A'` $\to$ `'T'`, `rev_comp = "T"`
     - `'T'` $\to$ `'A'`, `rev_comp = "AT"`
     - `'G'` $\to$ `'C'`, `rev_comp = "CAT"`
     - `'G'` $\to$ `'C'`, `rev_comp = "CCAT"`
     - `'C'` $\to$ `'G'`, `rev_comp = "GCCAT"`
     - `'T'` $\to$ `'A'`, `rev_comp = "AGCCAT"`. **Correto.**
7. **[Exercício 6.2.4.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-06/tema-02.dlt#L766-L790) (`exr:6-2-4-3`):**
   - Série de $20$ pontos: `[-70, -68, -60, -52, 20, -45, -66, -72, -70, -69, -68, -65, -55, 15, -50, -64, -71, -70, -69, -70]`.
   - Cruzamentos do limiar $-55\text{ mV}$ ($traco[i - 1] < -55 \land traco[i] \ge -55$):
     - $i = 3$: de $-60$ para $-52$ (Spike 1).
     - $i = 12$: de $-65$ para $-55$ (Spike 2).
   - Duração da janela: $\frac{20 \times 1{,}0\text{ ms}}{1\,000} = 0{,}02\text{ s}$.
   - Taxa média: $\frac{2\text{ spikes}}{0{,}02\text{ s}} = 100{,}0\text{ Hz}$. **Correto.**
8. **[Exercício 6.2.4.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-06/tema-02.dlt#L792-L811) (`exr:6-2-4-4`):**
   - Concentração inicial $C_0 = 100{,}0\text{ mg/L}$, decaimento $C(t) = 100 \cdot (0{,}8)^t$, limite $= 10{,}0\text{ mg/L}$.
   - Resolução analítica: $(0{,}8)^t < 0{,}10 \implies t > \frac{\ln(0{,}10)}{\ln(0{,}8)} \approx \frac{-2{,}302585}{-0{,}223144} \approx 10{,}3188\text{ h}$.
   - Para $t = 10$: $C(10) = 100 \cdot 0{,}8^{10} \approx 10{,}7374\text{ mg/L} \ge 10{,}0$ (continua).
   - Para $t = 11$: $C(11) = 100 \cdot 0{,}8^{11} \approx 8{,}5899\text{ mg/L} < 10{,}0$ (encerra o laço).
   - Formatação `:.2f`: `8.59 mg/L` após `11` horas. **Correto.**

---

## 4. Auditoria Linha a Linha dos Códigos Python

| Bloco de Código | ID | Linhas | Imports e Dependências | Sintaxe e Execução | Comentários vs. Saída Real |
|---|---|:---:|---|---|---|
| Atribuição | `cod:6-2-atribuicao` | 61–65 | Built-in puro | Válido, sem erros | `# -55` confere exatamente |
| Tipos e conversão | `cod:6-2-tipos` | 85–100 | Built-in puro | Válido, sem erros | Todas as 7 impressões conferem |
| Operadores | `cod:6-2-operadores` | 113–123 | Built-in puro | Válido, sem erros | `4.0`, `3 1`, `1024`, `True` conferem |
| Exemplo unidades | `cod:6-2-exm-unidades` | 131–141 | Built-in puro | Válido, sem erros | `-0.07`, `24.0` conferem |
| Exemplo tempo | `cod:6-2-exm-tempo` | 150–163 | Built-in puro | Válido, sem erros | `2 5`, `True`, `135` conferem |
| Ponto flutuante | `cod:6-2-float-isclose` | 174–181 | `import math` no topo | Válido, sem erros | `False`, `True`, `True` conferem |
| Solução Exr 1.1 | `cod:6-2-sol-1-1` | 191–200 | Built-in puro | Válido, sem erros | `310.65 0.25`, classes conferem |
| Solução Exr 1.2 | `cod:6-2-sol-1-2` | 211–220 | Built-in puro | Válido, sem erros | `2 5 20` confere |
| Solução Exr 1.3 | `cod:6-2-sol-1-3` | 231–242 | Built-in puro | Válido, sem erros | `-60.0`, `-54.0 True` conferem |
| Solução Exr 1.4 | `cod:6-2-sol-1-4` | 253–261 | `import math` no topo | Válido, sem erros | `False`, `True`, `True` conferem |
| Métodos de string | `cod:6-2-strings-metodos` | 287–297 | Built-in puro | Válido, sem erros | Todas as 6 impressões conferem |
| F-strings | `cod:6-2-fstrings` | 308–316 | Built-in puro | Válido, sem erros | `24.0 Hz`, `62.5%`, `ID:   42` conferem |
| Exemplo GC | `cod:6-2-exm-gc` | 324–335 | Built-in puro | Válido, sem erros | Ambas as saídas conferem |
| Exemplo tabela | `cod:6-2-exm-tabela` | 344–355 | Built-in puro | Válido, sem erros | Alinhamento e valores conferem |
| Solução Exr 2.1 | `cod:6-2-sol-2-1` | 375–381 | Built-in puro | Válido, sem erros | Formatação e espaços conferem |
| Solução Exr 2.2 | `cod:6-2-sol-2-2` | 392–399 | Built-in puro | Válido, sem erros | RNAm e porcentagem conferem |
| Solução Exr 2.3 | `cod:6-2-sol-2-3` | 410–416 | Built-in puro | Válido, sem erros | String limpa, tamanho 23, zeros 3 |
| Exemplo membrana | `cod:6-2-exm-membrana` | 449–462 | Built-in puro | Válido, sem erros | `-62.0 mV -> despolarizado` confere |
| Exemplo pH | `cod:6-2-exm-ph` | 471–484 | Built-in puro | Válido, sem erros | `pH 7.40: solução básica` confere |
| Solução Exr 3.1 | `cod:6-2-sol-3-1` | 504–519 | Built-in puro | Válido, sem erros | `10.5 Hz -> banda alfa` confere |
| Solução Exr 3.2 | `cod:6-2-sol-3-2` | 530–538 | Built-in puro | Válido, sem erros | `Registro inválido` confere |
| Solução Exr 3.3 | `cod:6-2-sol-3-3` | 549–564 | Built-in puro | Válido, sem erros | `Célula aceita` confere |
| Solução Exr 3.4 | `cod:6-2-sol-3-4` | 575–586 | Built-in puro | Válido, sem erros | `Códon de início (ATG)` confere |
| Exemplo for GC | `cod:6-2-exm-for-gc` | 617–627 | Built-in puro | Válido, sem erros | `5 | 5` confere |
| Exemplo spikes | `cod:6-2-exm-spikes` | 638–650 | Built-in puro | Válido, sem erros | `Spikes detectados: 2` confere |
| Exemplo bactérias | `cod:6-2-exm-bacterias` | 673–682 | Built-in puro | Válido, sem erros | `14 | 1638400` confere |
| Break e continue | `cod:6-2-break-continue` | 689–703 | Built-in puro | Válido, sem erros | `Válidas: 3 | Média: -62.3 mV` confere |
| Solução Exr 4.1 | `cod:6-2-sol-4-1` | 723–735 | Built-in puro | Válido, sem erros | `120.0 Hz | 24.0 Hz | 3` confere |
| Solução Exr 4.2 | `cod:6-2-sol-4-2` | 746–762 | Built-in puro | Válido, sem erros | `"AGCCAT"` confere |
| Solução Exr 4.3 | `cod:6-2-sol-4-3` | 775–788 | Built-in puro | Válido, sem erros | `Spikes: 2 | Taxa: 100.0 Hz` confere |
| Solução Exr 4.4 | `cod:6-2-sol-4-4` | 799–809 | Built-in puro | Válido, sem erros | `Horas: 11 | 8.59 mg/L` confere |

---

## 5. Checklist de Conformidade Editorial e Pedagógica

| Critério avaliado | Status | Análise detalhada |
|---|:---:|---|
| **Dica e solução completa em cada exercício** | **OK** | Todos os 15 exercícios contêm `<hint><title>Ver dica</title>...</hint>` e `<solution collapsible="true" collapsed="true">` com o raciocínio completo passo a passo, conferência explícita e código funcional. |
| **Pelo menos um exemplo biológico por seção** | **OK** | **Seção 1:** Potencial de membrana piramidal ($-70\text{ mV}$), taxa de disparo ($24\text{ Hz}$), registro eletrofisiológico de $125\text{ min}$, homeotermia ($37{,}5\,^\circ\text{C}$), EEG contínuo e modelo passivo linear de membrana.<br>**Seção 2:** Conteúdo GC de fita de DNA, tabela comparativa de disparos neuronais, transcrição gênica para RNAm com uracilas e metadados de laboratório.<br>**Seção 3:** Classificação de estados de membrana (repouso, despolarizado, limiar, hiperpolarizado), pH fisiológico arterial ($7{,}40$), bandas do EEG (delta a gama), controle de qualidade em *patch-clamp* e códon de início de tradução (`ATG`).<br>**Seção 4:** Contagem de GC com acumulador, algoritmo de cruzamento de limiar para detecção de *spikes*, cinética de crescimento bacteriano ($100 \cdot 2^{14} > 10^6$), complementar reverso de DNA, decaimento plasmático de fármaco e tratamento de artefatos/saturação de sinal. |
| **Afirmações de neurociência de livro-texto** | **OK** | Valores de repouso ($-70\text{ mV}$), limiar ($-55\text{ mV}$), faixas de resistência de entrada ($50\text{ M}\Omega$) e de acesso ($18{,}5\text{ M}\Omega \le 25\text{ M}\Omega$), bandas clássicas de EEG (delta $< 4\text{ Hz}$, teta $4\text{--}8\text{ Hz}$, alfa $8\text{--}13\text{ Hz}$, beta $13\text{--}30\text{ Hz}$, gama $\ge 30\text{ Hz}$) e duração de potenciais de ação ($1\text{--}2\text{ ms}$) seguem fielmente Kandel (*Principles of Neural Science*), Dayan & Abbott (*Theoretical Neuroscience*) e Luck (*ERP Technique*). |
| **Sequenciamento pedagógico de conceitos** | **OK** | Nenhuma estrutura avançada é usada sem explicação prévia. Atribuição simples precede tipos e operadores; operadores precedem condicionais; condicionais antecedem laços. Quando listas literais e fatiamento são mencionados, há aviso explícito de que serão aprofundados no tema *Estruturas de dados básicas*. |
| **Executabilidade dos códigos Python** | **OK** | Todos os 31 blocos de código rodam sem dependências não declaradas. Onde necessário (`math`), o import está presente no próprio bloco. Nenhum erro de sintaxe, indentação ou nome de variável indefinido. |
| **Consistência de notação matemática e código** | **OK** | Separação rigorosa entre texto e código: decimais com vírgula na prosa ($0{,}02\text{ s}$, $1{,}5\text{ s}$, $-70{,}0\text{ mV}$) e com ponto dentro de código Python e f-strings (`0.02`, `1.5`, `-70.0`). Notação de grandezas com `\text{mV}`, `\text{Hz}`, `\text{s}` padronizada em KaTeX. |
| **Cobertura de todos os subtemas pedidos** | **OK** | Cobre integralmente os 4 subtemas definidos pelo gestor: `sec:6-2-1 Variáveis, tipos e operadores`, `sec:6-2-2 Texto e saída: strings e f-strings`, `sec:6-2-3 Decisões com if, elif e else` e `sec:6-2-4 Repetição: for e while`. Inclui todos os pontos específicos (pitfall de float, conversão de unidades, GC content, input(), critérios de membrana e pH, cruzamento de limiar e duplicação bacteriana). |
| **Tamanho dentro do padrão** | **OK** | A aula possui aproximadamente 3.850 palavras (844 linhas), situando-se perfeitamente dentro da faixa recomendada de 2.500 a 5.000 palavras. |
| **Conformidade técnica Delta v0.6.0** | **OK** | XML estrito válido: caracteres `<` e `>` devidamente escapados na prosa (`&lt;`, `&gt;`) e puros dentro de matemática KaTeX e código; `<intuition>` empregado estritamente como filho de `<definition>`; atributos booleanos com valor explícito (`collapsible="true" collapsed="true"`); IDs ASCII sem acentos; metadados completos com link de retorno ao guia. |

---

## 6. Conclusão da Revisão

A aula [tema-02.dlt](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-06/tema-02.dlt) está **plenamente aprovada para compilação e publicação**. As pequenas observações apontadas na Tabela de Problemas e Observações são puramente de enriquecimento pedagógico e podem ser incorporadas oportunamente em ciclos rotineiros de polimento editorial, sem qualquer impedimento à publicação imediata.
