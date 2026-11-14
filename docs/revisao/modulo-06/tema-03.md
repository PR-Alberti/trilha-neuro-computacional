# Relatório de Revisão Técnica — Módulo 06 · Tema 03 (Informática básica)

- **Arquivo revisado:** [tema-03.dlt](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-06/tema-03.dlt)
- **Documentos de referência:** [PADRAO-AULAS.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/PADRAO-AULAS.md) e [DELTA-COLA.md](file:///home/al.pedro.alberti/trilha-neuro-computacional/docs/DELTA-COLA.md)
- **Data da revisão:** 14 de novembro de 2026
- **Perfil do revisor:** Matemático, Neurocientista Computacional, Programador Python Sênior e Professor de Alunos de Ciências Biológicas

---

## 1. Veredito

**APROVAR**

A aula [tema-03.dlt](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-06/tema-03.dlt) cumpre com primor todos os requisitos conceituais, matemáticos, pedagógicos, neurocientíficos e sintáticos estabelecidos pela gestão técnica e pelo contrato editorial.

Todos os cálculos numéricos dos exemplos e dos 16 exercícios foram minuciosamente auditados e recalculados passo a passo, estando 100% corretos. Todos os blocos de código Python e comandos Bash foram analisados linha a linha (sintaxe, imports, nomes de variáveis, argumentos de funções e saídas esperadas em comentários), sendo rigorosamente autocontidos, portáteis e reprodutíveis.

A contextualização com a neurociência e a biologia é impecável e fundamentada na literatura de referência (Kandel; Dayan & Abbott; Luck; BIDS/OpenNeuro): aborda organização de árvores de diretórios de experimentos eletrofisiológicos e de neuroimagem, metadados de sessões de EEG ($250\text{--}1\,000\text{ Hz}$, $64$ canais, paradigma *oddball* auditivo), tempos de repetição de fMRI ($\text{TR} \approx 2{,}0\text{ s}$), disparos de células piramidais de CA1, potenciais de repouso ($-70\text{ mV}$ e $-70{,}5\text{ mV}$), limiares de disparo ($-55\text{ mV}$), unidades biofísicas ($\mu\text{V}$, $\text{mV}$, $\text{Hz}$), tabelas de eventos BIDS (`sub-01_events.tsv`) e formatos padrão da área (`.npy`, `.edf`, `.fif`, `.nii`/`.nii.gz`).

A progressão pedagógica é exemplar para estudantes de Ciências Biológicas sem experiência anterior em sistemas operacionais ou manipulação de arquivos em baixo nível: estabelece analogias intuitivas (como caixas e tubos em ultrafreezers de laboratório), alerta antecipadamente sobre estruturas que serão aprofundadas no tema seguinte (listas e dicionários em *Estruturas de dados básicas* e `pandas.read_csv` em *Bibliotecas*) e trata com extrema clareza as armadilhas mais traiçoeiras da rotina científica (perda de caminhos relativos em notebooks, destruição irreversível de dados por `rm -r`, armadilhas de codificação de texto UTF-8 versus Latin-1/*mojibake* e arquivos CSV brasileiros exportados pelo Excel com ponto e vírgula e vírgula decimal).

Foram registradas apenas 4 observações de refinamento pedagógico na tabela a seguir, de caráter estritamente consultivo para polimentos futuros, sem necessidade de retrabalho impeditivo.

---

## 2. Tabela de Problemas e Observações

| Severidade | Local | Trecho | Correção sugerida |
|---|---|---|---|
| Pedagógico | Seção 1 (`sec:6-3-1`), `exm:6-3-caminhos-rel-abs`, linha ~117 | `caminho_abs = Path("/dados/eeg/registro.edf")`<br/>`print("Com / inicial é absoluto?", caminho_abs.is_absolute())  # True` | Em ambientes baseados em Unix/POSIX (Linux, macOS e Google Colab), um caminho iniciado por `/` possui raiz e retorna `True` para `.is_absolute()`. No entanto, se o estudante de Biologia executar esse trecho no interpretador local do Windows, o caminho `/dados/...` é interpretado como relativo à unidade atual (*drive-relative*), e `.is_absolute()` retorna `False`. Embora o enunciado tenha contextualizado com precisão *"começando na raiz do Linux"*, sugere-se incluir uma nota comentada breve na explicação esclarecendo que, no Windows, para um caminho ser verdadeiramente absoluto, ele deve especificar a letra da unidade (por exemplo, `Path("C:/dados/eeg/registro.edf")`). |
| Pedagógico | Seção 1 (`sec:6-3-1`), `prop:6-3-pathlib-uso`, linha ~85 | `<item>Atributos de decomposição de um objeto <c>p</c>: <c>p.name</c> (nome completo com extensão), <c>p.stem</c> (nome sem a última extensão), <c>p.suffix</c> (última extensão, com o ponto) e <c>p.parent</c> (pasta que contém <c>p</c>).</item>` | Em neuroimagem computacional (conforme citado no subtema 2 ao apresentar formatos de fMRI), é extremamente comum encontrar arquivos compactados com extensões duplas, como `.nii.gz`. Nesses casos, `p.suffix` extrai apenas `'.gz'` e `p.stem` preserva `'nome.nii'`. Como enriquecimento pedagógico, sugere-se adicionar uma breve menção ao atributo `p.suffixes` (que retorna a lista `['.nii', '.gz']`), preparando o aluno para descompactações e filtros de arquivos NIfTI. |
| Pedagógico | Seção 4 (`sec:6-3-4`), `exr:6-3-4-3`, linha ~886 | `maior = -1.0` | A inicialização com `-1.0` funciona perfeitamente para frequências de disparo em Hz, visto que taxas de disparo neuronais são grandezas estritamente não-negativas ($\ge 0$). No entanto, para consolidar um hábito algorítmico universal em alunos que em breve manipularão potenciais de membrana ou sinais de EEG (cujos valores em mV e $\mu\text{V}$ são frequentemente negativos), sugere-se comentar na solução que a inicialização padrão para busca de valor máximo em coleções genéricas é `float("-inf")` ou o próprio primeiro valor da série. |
| Pedagógico / Formato | Seção 2 (`sec:6-3-2`), `exr:6-3-2-3`, linha ~534 | `json.dump(meta, arq, indent=2)` | No exemplo conceitual da seção (`exm:6-3-json-metadados`), utilizou-se a boa prática `ensure_ascii=False` para garantir que eventuais caracteres acentuados fossem gravados legíveis. No exercício, o dicionário continha apenas chaves em inglês e inteiros, de modo que o comportamento é idêntico. Ainda assim, para uniformidade estilística entre exemplos e soluções, sugere-se manter `ensure_ascii=False` como padrão profilático em todos os blocos de código que exemplificam gravação de JSON. |

---

## 3. Recálculo e Auditoria de Contas e Código

Todas as operações matemáticas, conversões de grandezas biofísicas, estruturas lógicas e trechos de código em Python e Bash foram integralmente auditados:

### 3.1 Subtema 1: Arquivos, pastas e caminhos (`sec:6-3-1`)

1. **[Código 6.3.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-06/tema-03.dlt#L93-L105) (`cod:6-3-pathlib-basico`):**
   - Caminho composto: `Path("dados") / "sujeito-01" / "sessao-01.csv"`.
   - `.name` $\to$ `'sessao-01.csv'`.
   - `.stem` $\to$ `'sessao-01'`.
   - `.suffix` $\to$ `'.csv'`.
   - `.parent` $\to$ `'dados/sujeito-01'`.
   - Saídas esperadas dos `print` conferem perfeitamente. **Correto.**
2. **[Exemplo 6.3.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-06/tema-03.dlt#L109-L125) (`exm:6-3-caminhos-rel-abs`):**
   - Verificação de caminhos: `caminho_rel = Path("exemplo_inexistente") / "eeg" / "registro.edf"`. Como não possui barra inicial nem unidade, `caminho_rel.is_absolute()` avalia para `False`. `caminho_abs = Path("/dados/eeg/registro.edf")` começa com `/` na raiz Linux $\implies `caminho_abs.is_absolute()` retorna `True`. Consulta ao disco: pasta não criada $\implies `caminho_rel.exists()` retorna `False`. **Correto.**
3. **[Exemplo 6.3.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-06/tema-03.dlt#L127-L152) (`exm:6-3-organizar-experimento`):**
   - Produto cartesiano de pastas: $2$ sujeitos (`sujeito-01`, `sujeito-02`) $\times$ $2$ sessões (`sessao-01`, `sessao-02`) $= 4$ pastas.
   - Chamada idempotente `pasta_sessao.mkdir(parents=True, exist_ok=True)`.
   - Saídas de `print` com `pasta_sessao.exists() == True` e `arquivo.name == "eventos.tsv"`. Comentários de saída batem 100%. **Correto.**
4. **[Exercício 6.3.1.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-06/tema-03.dlt#L162-L188) (`exr:6-3-1-1`):**
   - Classificação: (a) absoluto (`/home/...`); (b) e (c) relativos.
   - Resolução de `..`: `dados/brutos/..` retorna para `dados`; concatenando com `/processados/sujeito-01.csv`, resulta estritamente em `dados/processados/sujeito-01.csv`.
   - Script com `.is_absolute()` e `.resolve()` verificado e correto. **Correto.**
5. **[Exercício 6.3.1.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-06/tema-03.dlt#L190-L208) (`exr:6-3-1-2`):**
   - Decomposição de `registros/eeg/sub-04_sessao-02.edf`:
     - Nome: `sub-04_sessao-02.edf`
     - Stem: `sub-04_sessao-02`
     - Sufixo: `.edf`
     - Pasta: `registros/eeg`
   - Comentários de saída batem exatamente. **Correto.**
6. **[Exercício 6.3.1.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-06/tema-03.dlt#L210-L237) (`exr:6-3-1-3`):**
   - Aninhamento de laços: $3$ sujeitos $\times$ $2$ sessões $= 6$ caminhos no formato `dados/sujeito/sessao/spikes.csv`.
   - Uso cirúrgico de `caminho.parent.mkdir(parents=True, exist_ok=True)` evitando criar diretório com nome de arquivo. Saídas em comentários idênticas à ordem dos laços. **Correto.**
7. **[Exercício 6.3.1.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-06/tema-03.dlt#L239-L267) (`exr:6-3-1-4`):**
   - Estrutura multimodal: criação de `estudo_multimodal/README.txt` via `readme.parent.mkdir` e `readme.touch()`.
   - Laço de $2$ sujeitos $\times$ $2$ modalidades (`eeg`, `func`) gerando $4$ diretórios.
   - Saídas de `.exists()` confirmadas como `True` em todas as instâncias. **Correto.**

---

### 3.2 Subtema 2: Extensões e formatos de dados (`sec:6-3-2`)

1. **[Código 6.3.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-06/tema-03.dlt#L329-L346) (`cod:6-3-open-txt`):**
   - Gerenciador de contexto `with open(..., "w", encoding="utf-8")` e leitura com `"r"`.
   - `conteudo.strip()` remove quebras terminais e exibe o bloco de texto esperado. **Correto.**
2. **[Exemplo 6.3.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-06/tema-03.dlt#L352-L400) (`exm:6-3-csv-experimentos`):**
   - Dados gravados via `csv.writer`:
     - Controle: $12{,}0$, $15{,}0$, $18{,}0\text{ Hz}$.
     - Estímulo: $48{,}0$, $54{,}0$, $60{,}0\text{ Hz}$.
   - Contas das médias:
     - $\text{Média}_{\text{controle}} = \frac{12{,}0 + 15{,}0 + 18{,}0}{3} = \frac{45{,}0}{3} = 15{,}0\text{ Hz}$.
     - $\text{Média}_{\text{estímulo}} = \frac{48{,}0 + 54{,}0 + 60{,}0}{3} = \frac{162{,}0}{3} = 54{,}0\text{ Hz}$.
   - Saídas formatadas com `:.1f`: `Média controle: 15.0 Hz` e `Média estímulo: 54.0 Hz`. **Correto.**
3. **[Exemplo 6.3.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-06/tema-03.dlt#L401-L434) (`exm:6-3-json-metadados`):**
   - Gravação com `json.dump(..., indent=2, ensure_ascii=False)`.
   - Leitura com `json.load`: verificação de tipo de dado `type(lido["frequencia_amostragem_hz"])` devolve estritamente `<class 'int'>`. Comentários de saída batem linha a linha. **Correto.**
4. **[Exercício 6.3.2.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-06/tema-03.dlt#L444-L472) (`exr:6-3-2-1`):**
   - Gravação de arquivo `neuronio.txt` com quebras `\n` explícitas; iteração direta `for linha in arq:` com `linha.strip()`. **Correto.**
5. **[Exercício 6.3.2.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-06/tema-03.dlt#L474-L510) (`exr:6-3-2-2`):**
   - Dados de CA1: $12{,}0$, $18{,}0$, $24{,}0$, $26{,}0\text{ Hz}$.
   - Soma: $12{,}0 + 18{,}0 + 24{,}0 + 26{,}0 = 80{,}0\text{ Hz}$.
   - Média: $\frac{80{,}0}{4} = 20{,}0\text{ Hz}$.
   - Saída formatada `:.1f`: `Taxa média: 20.0 Hz`. **Correto.**
6. **[Exercício 6.3.2.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-06/tema-03.dlt#L512-L543) (`exr:6-3-2-3`):**
   - Registro eletrofisiológico: $150\,000$ amostras a $1\,000\text{ Hz}$.
   - Duração: $\frac{150\,000\text{ amostras}}{1\,000\text{ amostras/s}} = 150{,}0\text{ s}$ ($2{,}5\text{ min}$).
   - Saída formatada: `Duração do registro: 150.0 s`. **Correto.**
7. **[Exercício 6.3.2.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-06/tema-03.dlt#L545-L583) (`exr:6-3-2-4`):**
   - Eventos BIDS em TSV: 4 eventos registrados, sendo 3 do tipo `"alvo"` e 1 `"distrator"`.
   - Cada evento alvo dura $0{,}5\text{ s} \implies \text{Duração total dos alvos} = 0{,}5 + 0{,}5 + 0{,}5 = 1{,}5\text{ s}$.
   - Leitura com `csv.DictReader(arq, delimiter="\t")`. Saída: `Alvos: 3 | Duração total: 1.5 s`. **Correto.**

---

### 3.3 Subtema 3: O terminal na prática (`sec:6-3-3`)

1. **[Exemplo 6.3.5](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-06/tema-03.dlt#L622-L639) (`exm:6-3-terminal-experimento`):**
   - Sintaxe Bash testada: `pwd`, `mkdir -p`, `cd`, `touch`, `ls -l`, `ls *.csv`, `cp notas.txt ../processados/`, `mv suj01.csv sub-01.csv`, `ls`.
   - Sequência lógica impecável e explicada passo a passo no texto. **Correto.**
2. **[Exemplo 6.3.6](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-06/tema-03.dlt#L643-L655) (`exm:6-3-terminal-inspecao`):**
   - Comandos no Colab: comando mágico `%cd` para persistência no kernel e comandos com ponto de exclamação (`!pwd`, `!head -n 5 eventos.tsv`, `!wc -l eventos.tsv`). Explicação da diferença de subprocesso precisa. **Correto.**
3. **[Exercício 6.3.3.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-06/tema-03.dlt#L665-L680) (`exr:6-3-3-1`):**
   - Sequência Bash: `pwd`, `cd ~`, `ls -la`, `cd projetos`, `cd -`. Todos os comandos atendem à especificação sem ruídos. **Correto.**
4. **[Exercício 6.3.3.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-06/tema-03.dlt#L682-L697) (`exr:6-3-3-2`):**
   - Criação múltipla com `mkdir -p lab_eeg/brutos lab_eeg/limpos`, arquivos vazios com `touch`, filtro com `ls *.csv`, movimentação com `mv *.csv lab_eeg/brutos/` e cópia com `cp protocolo.txt lab_eeg/limpos/`. **Correto.**
5. **[Exercício 6.3.3.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-06/tema-03.dlt#L699-L711) (`exr:6-3-3-3`):**
   - Pré-visualização com `head -n 10` e contagem com `wc -l`.
   - Dedução lógica: o contador retorna $241$ linhas no total. Como a linha $1$ é o cabeçalho descritivo das colunas, o número exato de eventos experimentais é $241 - 1 = 240$ eventos. **Correto.**
6. **[Exercício 6.3.3.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-06/tema-03.dlt#L713-L726) (`exr:6-3-3-4`):**
   - Diagnóstico do subshell temporário criado pelo `!` e correção através de `%cd dados_experimento` acompanhado de `!pwd` e `!ls -l`. **Correto.**

---

### 3.4 Subtema 4: Codificação de texto (`sec:6-3-4`)

1. **Aritmética de bits, bytes e Unicode:**
   - 1 byte $= 8$ bits $\implies 2^8 = 256$ combinações ($0$ a $255$).
   - ASCII $= 7$ bits $\implies 2^7 = 128$ símbolos ($0$ a $127$).
   - Representação da palavra `"ação"`:
     - `'a'`: U+0061 $\to$ 1 byte ASCII (`0x61`).
     - `'ç'`: U+00E7 $\to$ 2 bytes em UTF-8 (`0xC3 0xA7`).
     - `'ã'`: U+00E3 $\to$ 2 bytes em UTF-8 (`0xC3 0xA3`).
     - `'o'`: U+006F $\to$ 1 byte ASCII (`0x6F`).
     - Contagem de caracteres: $\text{len}(\text{"ação"}) = 4$.
     - Contagem de bytes UTF-8: $1 + 2 + 2 + 1 = 6$ bytes.
   - Gênese do *mojibake* ao decodificar os 6 bytes `b'a\xc3\xa7\xc3\xa3o'` como Latin-1 (onde cada byte é tratado isoladamente):
     - `0x61` $\to$ `'a'`
     - `0xC3` $\to$ `'Ã'`
     - `0xA7` $\to$ `'§'`
     - `0xC3` $\to$ `'Ã'`
     - `0xA3` $\to$ `'£'`
     - `0x6F` $\to$ `'o'`
     - Resultado exato: `"aÃ§Ã£o"`.
   - Demonstração em código no **[Exemplo 6.3.7](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-06/tema-03.dlt#L756-L773) (`exm:6-3-bytes-mojibake`)** conferida com precisão de nível de byte. **Correto.**
2. **[Exemplo 6.3.8](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-06/tema-03.dlt#L782-L819) (`exm:6-3-csv-brasileiro`):**
   - Dados de potencial de repouso: $-70{,}5\text{ mV}$, $-68{,}2\text{ mV}$, $-71{,}3\text{ mV}$.
   - Soma: $-70{,}5 + (-68{,}2) + (-71{,}3) = -210{,}0\text{ mV}$.
   - Média: $\frac{-210{,}0}{3} = -70{,}00\text{ mV}$.
   - Código usa `csv.reader(arq, delimiter=";")`, descarta o cabeçalho com `next(leitor)`, converte com `.replace(",", ".")` e `float(...)`. Saídas nos comentários batem 100%. **Correto.**
3. **[Exercício 6.3.4.1](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-06/tema-03.dlt#L826-L844) (`exr:6-3-4-1`):**
   - `"sinapse"`: 7 caracteres, 7 bytes ASCII/UTF-8.
   - `"mV"`: 2 caracteres, 2 bytes ASCII/UTF-8.
   - `"μV"`: o símbolo grego micro $\mu$ (U+03BC) ocupa 2 bytes em UTF-8 (`0xCE 0xBC`), e `'V'` ocupa 1 byte. Logo: 2 caracteres, 3 bytes. Comentários de saída batem perfeitamente. **Correto.**
4. **[Exercício 6.3.4.2](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-06/tema-03.dlt#L846-L864) (`exr:6-3-4-2`):**
   - Reversão de *mojibake*: `.encode("latin-1")` reconstrói a sequência original de bytes UTF-8 em bruto, e `.decode("utf-8")` os interpreta na tabela correta. Recupera com perfeição `"ação"` e `"estimulação"`. **Correto.**
5. **[Exercício 6.3.4.3](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-06/tema-03.dlt#L866-L902) (`exr:6-3-4-3`):**
   - Registros: $10{,}5$, $22{,}5$, $30{,}0$, $17{,}0\text{ Hz}$.
   - Soma: $10{,}5 + 22{,}5 + 30{,}0 + 17{,}0 = 80{,}0\text{ Hz}$.
   - Média: $\frac{80{,}0}{4} = 20{,}0\text{ Hz}$.
   - Máximo: $\max(10{,}5, 22{,}5, 30{,}0, 17{,}0) = 30{,}0\text{ Hz}$.
   - Saída formatada `:.1f`: `Máxima: 30.0 Hz | Média: 20.0 Hz`. **Correto.**
6. **[Exercício 6.3.4.4](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-06/tema-03.dlt#L904-L932) (`exr:6-3-4-4`):**
   - Normalização de quebras de linha: `replace("\r\n", "\n")` gravado com `newline="\n"`.
   - Inspeção em modo binário (`"rb"`): `b"\r" in bruto` retorna estritamente `False`.
   - Inspeção dos bytes gravados exibe `b'canal,unidade\nCz,\xce\xbcV\nPz,\xce\xbcV\n'`, comprovando a integridade dos bytes `\xce\xbc` do caractere $\mu$ e a ausência de `\r`. **Correto.**

---

## 4. Conferência dos Subtemas Solicitados pelo Gestor

A aula aborda integralmente todos os tópicos e requisitos didáticos especificados pela gestão técnica:

| Seção e Subtema | Tópicos solicitados pelo gestor | Status na aula |
|---|---|:---:|
| **Subtema 1 (`sec:6-3-1`)**<br>*Arquivos, pastas e caminhos* | Sistema de arquivos como árvore; raiz (`/` no Linux/macOS, `C:\` no Windows); pasta pessoal (`~`); caminho absoluto $\times$ relativo; pasta de trabalho atual (*working directory*); `.` e `..`; separador `/` $\times$ `\` e problemas de escape com strings puras; uso do `pathlib.Path` (`Path.cwd()`, concatenação com `/`, `.name`, `.stem`, `.suffix`, `.parent`, `.exists()`, `.mkdir(parents=True, exist_ok=True)`). Exemplo biológico: organização de experimento em pastas de sujeitos e sessões em laços. Armadilhas: caminhos relativos que "somem" no notebook e caracteres especiais/espaços em nomes de arquivos. | **100% Coberto**<br>(linhas 39–268) |
| **Subtema 2 (`sec:6-3-2`)**<br>*Extensões e formatos de dados* | Extensão como mera convenção versus estrutura real dos bytes; distinção entre arquivos de texto e arquivos binários; detalhamento com blocos de texto cru de CSV, TSV e JSON; manipulação em Python com `with open(..., encoding="utf-8")`, módulo `csv` (`csv.writer`, `csv.DictReader`, `newline=""`) e módulo `json` (`json.dump`, `json.load`); citação sem código de formatos da neurociência (`.npy`, `.edf`, `.fif`, `.nii`/`.nii.gz`, padrão BIDS com `participants.tsv` e `*_events.tsv`, OpenNeuro); aviso sobre `pandas.read_csv` no tema *Bibliotecas*. Exemplos biológicos: tabela de disparos em CSV calculando médias por condição e metadados JSON de EEG. | **100% Coberto**<br>(linhas 270–584) |
| **Subtema 3 (`sec:6-3-3`)**<br>*O terminal na prática* | `pwd`, `ls` (`ls -l`, `ls -a`, `ls -la`), `cd` (`cd ..`, `cd ~`, `cd -`), `mkdir` (`-p`), `touch`, `cp` (`cp -r`), `mv`, `rm` e o perigo irreversível de `rm -r` sem lixeira, `cat`, `head -n`, `wc -l`, curinga `*` (`ls *.csv`), atalhos `Tab` e histórico com setas; menção ao PowerShell do Windows (`dir`, `cd`, `mkdir`, apelido `ls`); comandos no Colab com `!` e explicação da não persistência de `!cd` frente ao comando mágico `%cd`. Todos os blocos em `<code lang="bash">`. Exemplos biológicos: estruturação de pastas do experimento e contagem de eventos com `wc -l`. | **100% Coberto**<br>(linhas 586–727) |
| **Subtema 4 (`sec:6-3-4`)**<br>*Codificação de texto* | Bits e bytes ($2^8 = 256$); ASCII (7 bits, 128 caracteres); Unicode e UTF-8 com tamanho variável de bytes (confirmação empírica de `len("ação") == 4` e `len("ação".encode("utf-8")) == 6`); explicação minuciosa da gênese do *mojibake* (`aÃ§Ã£o`) pela leitura indevida em Latin-1/`cp1252`; obrigatoriedade profilática de `encoding="utf-8"`; finais de linha `\n` $\times$ `\r\n`; CSV "brasileiro" do Excel com delimitador `;` e vírgula decimal (leitura via `csv.reader(..., delimiter=";")` e `.replace(",", ".")`). Armadilha do Excel alterando codificação e separador ao salvar. | **100% Coberto**<br>(linhas 729–933) |

---

## 5. Checklist Rigoroso dos Critérios Editoriais e Pedagógicos

| Critério avaliado | Status | Análise detalhada |
|---|:---:|---|
| **Dica e solução completa em cada exercício** | **OK** | Todos os 16 exercícios contêm `<hint><title>Ver dica</title>...</hint>` e `<solution collapsible="true" collapsed="true">` completas, apresentando o raciocínio dedutivo detalhado, o código correspondente e as saídas esperadas. |
| **Pelo menos um exemplo biológico por seção** | **OK** | **Seção 1:** Organização de pastas de neurofisiologia (`exp_neuro/dados/brutos/sujeito-XX/sessao-YY`), arquivos de EEG (`sub-04_sessao-02.edf`), e estudo multimodal (EEG e fMRI).<br/>**Seção 2:** Disparos neuronais em camundongos sob controle e estímulo, metadados de sessão de EEG (amostragem a $500\text{ Hz}$, $64$ canais, paradigma *oddball* auditivo), disparos em CA1 e eventos BIDS.<br/>**Seção 3:** Manipulação de pastas de córtex (`exp_cortex`), inspeção de eventos de fMRI (`sessao_events.tsv`) e contagem de eventos experimentais.<br/>**Seção 4:** Termos biofísicos ("sinapse", "mV", "μV"), eletrodos de EEG (`Cz`, `Pz`), potenciais de repouso de neurônios corticais ($-70{,}5\text{ mV}$) e taxas de disparo celulares. |
| **Afirmações de neurociência de livro-texto** | **OK** | Todos os parâmetros e descrições técnicas seguem rigorosamente a literatura padrão (Kandel; Dayan & Abbott; Luck): amostragem de EEG entre $250$ e $1\,000\text{ Hz}$, TR de fMRI $\approx 2{,}0\text{ s}$, potenciais de membrana basais entre $-70$ e $-55\text{ mV}$, taxas de disparo fisiológicas até $200\text{ Hz}$, montagem de canais 10-20 e formato padrão BIDS do consórcio internacional. |
| **Sequenciamento pedagógico de conceitos** | **OK** | Nenhum conceito técnico é exigido sem apresentação prévia. O autor teve o cuidado de sinalizar quando utilizou estruturas que serão consolidadas nos temas seguintes (como listas e dicionários em *Estruturas de dados básicas* e leitura avançada via `pandas.read_csv` em *Bibliotecas*). |
| **Código Python executável e saídas consistentes** | **OK** | Todos os 20 blocos de código Python rodam perfeitamente de ponta a ponta sem qualquer dependência externa não instalada (utilizam estritamente a biblioteca padrão: `pathlib`, `csv`, `json`). Todos os comentários de saída batem com precisão absoluta com o stdout do interpretador Python 3. |
| **Consistência de notação e estilo** | **OK** | Uso rigoroso de vírgula decimal na prosa e fórmulas KaTeX ($15{,}0\text{ Hz}$, $-70{,}00\text{ mV}$, $1{,}5\text{ s}$) e ponto decimal dentro dos blocos de código Python (`15.0`, `-70.00`, `1.5`). Unidades de medida KaTeX formatadas com `\text{...}` ($\text{Hz}$, $\text{mV}$, $\mu\text{V}$, $\text{s}$). |
| **Estrutura e seções requeridas** | **OK** | Estrutura completa: contextualização biológica inicial ("Por que isso importa"), 4 objetivos com verbos de ação, pré-requisitos listados, 4 seções de subtemas numeradas, seção de "Resumo" estruturada em 6 tópicos e seção "Para ir além" apontando links oficiais estáveis. |
| **Tamanho do texto dentro do padrão** | **OK** | O arquivo totaliza 962 linhas e aproximadamente 4.300 palavras, enquadrando-se perfeitamente na faixa exigida pelo padrão editorial (2.500 a 5.000 palavras). |
| **Conformidade com a sintaxe Delta v0.6.0** | **OK** | XML estrito em toda a sua extensão; ausência total de tags proibidas (`<interactive>`, `<cite>`, `<youtube>`); atributos sempre com valor (`numbered="false"`, `lines="false"`, `collapsible="true"`, `collapsed="true"`); blocos de `<intuition>` utilizados exclusivamente dentro de `<definition>`; identificadores únicos e em formato ASCII sem acentuação; entidades de texto devidamente protegidas (`&lt;`, `&gt;`, `&amp;` na prosa). |

---

## 6. Conclusão da Revisão

A aula [tema-03.dlt](file:///home/al.pedro.alberti/trilha-neuro-computacional/conteudo/modulo-06/tema-03.dlt) está **plenamente aprovada para compilação**. 

O texto equilibra com excelência o rigor formal da informática com a empatia pedagógica necessária para acolher estudantes de Biologia, desmistificando o terminal, o sistema de arquivos e os meandros de codificação de texto por meio de práticas concretas e aplicadas à Neurociência Computacional. As observações registradas na Seção 2 são recomendações construtivas de refinamento pedagógico que poderão ser incorporadas em rodadas futuras de manutenção editorial sem qualquer prejuízo à publicação imediata da obra.
