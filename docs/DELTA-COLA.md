# Cola de Sintaxe do Delta (v0.6.0)

Referência objetiva para autores das aulas, baseada estritamente na documentação
em `referencias/delta/*.dlt`, `referencias/delta/README.md` e nos exemplos em
`referencias/delta/exemplos/`. Veja também o contrato editorial em
[PADRAO-AULAS.md](PADRAO-AULAS.md).

> ## Regras deste projeto (prevalecem sobre o resto da cola)
>
> - **ERRO Nº 1 DOS AUTORES**: dentro de `$...$`, `$$...$$`, `<equation>` e `<code>`, escreva `<`, `>` e `&` **puros**. `&lt;` e `&gt;` na matemática quebram o KaTeX. O escape só vale na prosa.
> - **Saídas de código**: nunca invente a saída esperada. Escreva `# saída: (o gestor confere)`; o gestor roda o código e põe o valor real.
> - **Título do documento**: `Módulo N · <título do módulo>`. O capítulo é o tema:
>   `<chapter id="tema-M-T">`.
> - **Link de volta ao guia**: só no `<meta-item key="Guia">`. Não o repita abaixo
>   do título do capítulo.
> - **Proibido** nas aulas:
>   - `<interactive>`, que exige um pacote e sai vazio;
>   - `<cite>`, `<bibliography>` e arquivos `.ref`: cite clássicos por nome e ano,
>     na prosa;
>   - `<youtube>`, exceto vídeos que já estão nos materiais do módulo, no `index.html`.
> - **Figuras**: o `<figure src>` precisa de um arquivo que exista.
>   - Gere a figura com um script Python em `conteudo/modulo-NN/fig/<nome>.py`
>     (matplotlib, rótulos em português, com `plt.rcParams['svg.fonttype'] = 'none'` para o SVG ficar leve), que salva
>     `conteudo/modulo-NN/fig/<nome>.svg`.
>   - Na aula, use `src="fig/<nome>.svg"`.
>   - O autor escreve o script e o gestor o executa com
>     `~/.local/share/venv-aulas/bin/python fig/<nome>.py` (a partir de
>     `conteudo/modulo-NN`).
>   - Use no máximo 3 figuras por aula, e só quando ajudarem de verdade:
>     gráficos de funções, curvas de sintonia, paisagens de custo.
> - **Dicas e soluções**: `<hint>` dentro do `<exercise>`, e
>   `<solution collapsible="true" collapsed="true">`. Demonstrações em
>   `<proof collapsible="true" collapsed="true">`.

---

## 1. Projeto (`project.toml`) e esqueleto de capítulo (`book`)

Cada módulo é um projeto Delta com um `project.toml` e um arquivo `.dlt` por tema:

```toml
inputs = ["tema-01.dlt", "tema-02.dlt"]
out = "../../aulas/modulo-01"

[document]
type = "book"
lang = "pt-BR"
theme-accent = "indigo"
```

- `inputs`: lista obrigatória dos arquivos na ordem do livro (define a numeração contínua e a ordem das citações).
- `out`: pasta de saída para os HTMLs (padrão: pasta atual). Os arquivos são achatados (`tema-01.dlt` → `tema-01.html`).
- `packages`: lista opcional de pacotes aplicados a todos os arquivos.
- `[document]`: atributos padrão aplicados ao `<document>` de cada arquivo (`type`, `lang`, `theme`, `theme-accent`, `theme-mode`, `proofs`). Um atributo declarado no próprio `.dlt` sobrescreve o padrão do `project.toml`.

### Esqueleto de um arquivo de capítulo

```xml
<document>
  <title>Módulo 1 · Pré-cálculo</title>

  <meta>
    <meta-item key="Guia"><link to="../../index.html#tema-1-1">Voltar ao guia (Tema 1.1)</link></meta-item>
  </meta>

  <floating>
    <title>Sumário</title>
    <toc scope="project" depth="1"/>
  </floating>

  <chapter id="tema-1-1">
    <title>Nome do Tema</title>

    <link to="../../index.html#tema-1-1">Voltar ao guia de estudos</link>

    <toc/>

    <section id="sec:1-1-1">
      <eyebrow>Subtema 1</eyebrow>
      <title>Nome do Subtema</title>
      <intro>
        Parágrafo de abertura em destaque antes do corpo da seção.
      </intro>

      <subsection id="sub:1-1-1-a">
        <title>Subseção</title>
        Texto da subseção.
      </subsection>
    </section>
  </chapter>

  <footer>
    Guia de Estudos: ML para Neurociência Computacional.
  </footer>
</document>
```

Notas sobre tags estruturais:
- `<document>` aceita `id`, `lang` (`pt-BR`, `en`, ...), `type` (`article`, `book`, `presentation`), `theme` (`impatech` ou caminho `.css`), `theme-accent` (`red`, `orange`, `yellow`, `lime`, `green`, `teal`, `sky`, `blue`, `indigo`, `purple`, `pink`, `slate`), `theme-mode` (`dark`, `auto`) e `proofs` (`open`). Em projetos com `[document]` no `project.toml`, pode ir sem atributos.
- Divisões: `<chapter>`, `<section>`, `<subsection>`, `<subsubsection>`. Atributos comuns: `id` (sempre ASCII sem acento), `numbered="false"` (não numera nem consome contador), `num="texto"`, `collapsible="true"`, `collapsed="true"`.
- `<toc/>`: sumário local (padrão `depth="2"`). Com `scope="project"`, lista títulos de todos os arquivos do projeto. Um `<title>` filho troca o rótulo "Sumário".
- `<meta>` / `<meta-item key="...">`: exibidos abaixo do título; funcionam no `<document>`, em seções e dentro de ambientes numerados.
- `<eyebrow>` e `<intro>`: abertura de seção (`<section>`).
- **Sobre `<header>`**: na documentação lida (`referencias/delta/layout.dlt`), `<header>` só aparece documentado como cabeçalho de `<table>`, não como cabeçalho de `<document>` ou `<chapter>`. Para o link de volta ao guia (`../../index.html#tema-M-T`) no topo da aula usando apenas tags documentadas, use `<meta>`/`<meta-item>` e/ou um `<link>` logo abaixo de `<chapter><title>...</title>`.

---

## 2. Prosa, listas, links e notas

Parágrafos são separados por uma linha em branco (não use tag `<p>`).

### Formatação inline

```xml
Texto em <strong>negrito</strong> (ou <b>negrito</b>),
<em>itálico</em> (ou <i>itálico</i>), <u>sublinhado</u>,
<s>riscado</s>, <mark>destacado</mark> e <c>código inline</c>.
```

### Listas (`<list>` e `<item>`)

Atributos de `<list>`: `marker` (`number`, `a`, `A`, `i`, `I`, `dash`; sem atributo usa marcador redondo), `start="número"`, `animated="true"` (em apresentações). Listas podem ser aninhadas dentro de `<item>`.

```xml
<list marker="number">
  <item>Primeiro passo.</item>
  <item>
    Segundo passo, com sublista:
    <list marker="dash">
      <item>Detalhe A;</item>
      <item>Detalhe B.</item>
    </list>
  </item>
</list>
```

### Links externos, relativos e referências cruzadas (`<ref>`)

```xml
Veja a <link to="https://numpy.org">documentação do NumPy</link> ou
volte para <link to="../../index.html#tema-1-1">o índice do guia</link>.

Pelo <ref to="thm:1-1-media"/>, o valor esperado converge.
Confira <ref to="eq:1-1-soma">a fórmula da soma</ref>.
```

- `<ref to="id"/>` monta o rótulo automático no idioma do documento ("Teorema 1.1", "Equação 1.2") com prévia ao passar o mouse ou clicar. Funciona entre arquivos do mesmo `project.toml`.
- `<ref to="id">texto próprio</ref>` substitui o rótulo automático mantendo o link e a prévia.

### Notas (`<sidenote>` e `<hint>`)

```xml
O potencial de repouso fica perto de $-70\text{ mV}$.<sidenote>Valor típico em neurônios corticais de mamíferos.</sidenote>

Um espaço <hint><title>de Banach</title>Espaço vetorial normado e completo.</hint> aparece na análise.
```

- `<sidenote>`: nota de margem.
- `<hint>`: texto escondido atrás de um gatilho clicável inline; `<title>` define o texto do gatilho. Aceita `show-icon="false"`.

### Citações e bibliografia (`<cite>`, `<bibliography>`, `<paper>`)

```xml
Conforme descrito em <cite paper="kandel"/> e <cite papers="dayan,gerstner"/>.

<bibliography>
  <paper id="kandel">
    <author>Kandel, E. R. et al.</author>
    <title>Principles of Neural Science</title>
    <journal>McGraw-Hill</journal>
    <year>2021</year>
    <link>https://example.org</link>
  </paper>
</bibliography>
```

Também é possível carregar de arquivo separado: `<bibliography src="refs.ref"/>`. Campos de `<paper>`: `author`, `title`, `journal`, `year`, `link` (ou `url`). Atenção: `<cite>` usa `paper` ou `papers`, nunca `to`.

---

## 3. Matemática

O Delta renderiza LaTeX na compilação via KaTeX.

### Formas de escrita

- **Na linha**: `$e^{i\pi} + 1 = 0$` ou `<m>f(x) = x^2</m>`. Matemática com `$...$` não atravessa linha em branco nem fechamento de tag.
- **Em destaque, sem número**: `$$a^2 + b^2 = c^2$$` ou `<equation numbered="false">a^2 + b^2 = c^2</equation>`.
- **Em destaque, numerada**: `<equation id="eq:1-1-nernst">...</equation>`.
- **Alinhada em várias linhas, numerada**: `<equations id="eq:1-1-sistema">...</equations>` (embrulhada em `aligned` do LaTeX; use `&` para alinhar e `\\` para quebrar linha).

```xml
A derivada de $f(x) = x^2$ é <m>f'(x) = 2x</m>.

<equation id="eq:1-1-euler">e^{i\pi} + 1 = 0</equation>

<equations id="eq:1-1-serie">
  S &= 1 + \frac{1}{2} + \frac{1}{4} + \cdots \\
    &= 2
</equations>

Por \eqref{eq:1-1-euler} dentro da fórmula:
$A \stackrel{\ref{eq:1-1-euler}}{=} 0$.
```

- Dentro de fórmulas, `\ref{id}` e `\eqref{id}` produzem números clicáveis com prévia.

### O que escapar e o que não escapar

| Contexto | `<`, `>` e `&` | `$` literal |
|---|---|---|
| Prosa comum | Escapar: `&lt;`, `&gt;`, `&amp;` | Escapar: `\$` |
| Dentro de `$...$`, `$$...$$`, `<m>`, `<equation>`, `<equations>` | **Não escapar** (`$a < b$`, `&=`) | `\$` se precisar de cifrão no LaTeX |
| Dentro de `<code>` | **Não escapar** | Livre |

### Macros

A documentação em `referencias/delta/*.dlt` **não documenta** definição de macros LaTeX customizadas (não há tag `<macro>` nem preâmbulo documentado). Escreva as expressões usando os comandos padrão do LaTeX/KaTeX.

---

## 4. Ambientes

### Ambientes numerados

Cada tag tem contagem própria (reiniciada a cada `<section>`).

- **Família do teorema**: `<theorem>` (Teorema), `<proposition>` (Proposição), `<lemma>` (Lema), `<corollary>` (Corolário), `<conjecture>` (Conjectura), `<claim>` (Afirmação), `<observation>` (Observação).
- **Outros ambientes**: `<definition>` (Definição), `<example>` (Exemplo), `<remark>` (Comentário), `<exercise>` (Exercício), `<problem>` (Problema).

Atributos comuns: `id`, `numbered="false"`, `num="texto"`, `collapsible="true"`, `collapsed="true"`. Um `<title>` filho é opcional.

```xml
<definition id="def:1-1-media">
  <title>Média amostral</title>
  Para $n$ observações $x_1, \dots, x_n$, definimos $\bar{x} = \frac{1}{n}\sum_{i=1}^n x_i$.
</definition>

<theorem id="thm:1-1-desigualdade">
  <title>Desigualdade triangular</title>
  Para quaisquer $x, y \in \mathbb{R}$, vale $|x + y| \le |x| + |y|$.
</theorem>

<proposition id="prop:1-1-linear">
  A média é um operador linear.
</proposition>

<lemma id="lem:1-1-aux">
  Se $a \le b$, então $a + c \le b + c$.
</lemma>

<corollary id="cor:1-1-conseq">
  Para todo $x \in \mathbb{R}$, $|x - y| \ge \bigl||x| - |y|\bigr|$.
</corollary>

<observation id="obs:1-1-escala">
  A unidade do potencial de membrana é o milivolt ($\text{mV}$).
</observation>

<example id="exm:1-1-disparo">
  <title>Taxa de disparo</title>
  Se um neurônio dispara $15$ vezes em $0{,}5\text{ s}$, sua taxa é $30\text{ Hz}$.
</example>

<remark id="rem:1-1-armadilha">
  <title>Armadilha comum</title>
  Não confunda média com mediana em distribuições assimétricas.
</remark>
```

### Demonstrações (`<proof>`) e soluções (`<solution>`)

Não recebem número. O atributo `of="id"` liga a prova ao resultado; quando `<proof>` ou `<solution>` vem **dentro** ou **logo depois** do resultado/exercício (sem parágrafo ou figura no meio), ela se junta à caixa dele como barra de rodapé e **já começa fechada** (`collapsed="false"` a abre inicialmente). Nos exemplos oficiais também se usa `collapsible="true" collapsed="true"` de forma explícita.

```xml
<proof of="thm:1-1-desigualdade" collapsible="true" collapsed="true">
  Como $-|x| \le x \le |x|$ e $-|y| \le y \le |y|$, somando as desigualdades
  obtemos $-(|x|+|y|) \le x+y \le |x|+|y|$.
</proof>
```

Exercício e problema com `<hint>` e `<solution>` recolhida:

```xml
<exercise id="exr:1-1-1-1">
  <title>Básico — Taxa de disparo</title>
  Um neurônio emitiu $40$ potenciais de ação em $2\text{ s}$. Qual a taxa média em Hz?
  <hint><title>Ver dica</title>Divida o número de disparos pela duração em segundos.</hint>
  <solution collapsible="true" collapsed="true">
    Dividindo $40$ disparos por $2\text{ s}$, obtemos $20\text{ Hz}$.
  </solution>
</exercise>

<problem id="prob:1-1-1-1">
  <title>Avançado — Variação relativa</title>
  Mostre que $\bar{x}$ minimiza $\sum_{i=1}^n (x_i - c)^2$.
  <solution collapsible="true" collapsed="true">
    Derive $f(c) = \sum_{i=1}^n (x_i - c)^2$ em relação a $c$ e iguale a zero:
    $f'(c) = -2\sum_{i=1}^n (x_i - c) = 0 \implies c = \bar{x}$.
  </solution>
</problem>
```

### `<intuition>`, `<strategy>` e `<obstacle>`

**Importante:** na sintaxe do Delta, `<intuition>`, `<strategy>` e `<obstacle>` **NÃO existem fora de resultados ou passos de prova**. Elas só podem ser filhas diretas de um resultado (`theorem`, `proposition`, `lemma`, `corollary`, `conjecture`, `claim`, `definition`) ou de um `<step>` dentro de `<proof>`/`<solution>`. Colocá-las fora desses blocos ou atribuir-lhes `id` gera **erro de compilação**. Todas começam recolhidas (`collapsed="false"` deixa aberta).

```xml
<theorem id="thm:1-1-bolzano">
  <title>Bolzano–Weierstrass</title>
  Toda sequência limitada em $\mathbb{R}$ possui subsequência convergente.
  <intuition>
    Infinitos pontos em um intervalo finito precisam se acumular em algum lugar.
  </intuition>
</theorem>
```

### Caixas de destaque (`<box>`)

Bloco não numerado com barra lateral colorida. `type` aceita `"note"` (azul), `"tip"` (verde), `"warning"` (laranja) e `"danger"` (vermelho). `color` aceita nome da paleta, hex ou cor CSS (sobrescreve `type`).

```xml
<box type="warning">
  <title>Atenção às unidades</title>
  Sempre converta milissegundos para segundos antes de calcular frequências em Hz.
</box>
```

---

## 5. Código (`<code>` e `<c>`)

- `<c>trecho</c>`: código inline sem destaque de sintaxe.
- `<code lang="python">...</code>`: bloco com destaque de sintaxe na compilação e botão de copiar.
  - Linguagens aceitas em `lang`: `python` (`py`), `xml` (`dlt`, `html`), `bash` (`sh`), `javascript` (`js`), `typescript` (`ts`), `css`, `toml`, `text`.
  - `numbered="false"`: omite a numeração do bloco como ambiente (sem isso, `<code>` é numerado por seção como ambiente).
  - `lines="false"`: esconde os números das linhas.
  - `collapsible="true"` e `collapsed="true"`: permitem recolher o bloco.
  - O conteúdo é literal (não escape `<`, `>`, `&`), mas termina no primeiro `</code>` literal que aparecer.

```xml
<code lang="python" id="cod:1-1-media">
import numpy as np

potenciais = np.array([-70.0, -68.5, -71.2])
print(f"Média: {potenciais.mean():.2f} mV")  # Média: -69.90 mV
</code>

<code lang="python" numbered="false" lines="false">
x = [1, 2, 3]
print(sum(x) / len(x))  # 2.0
</code>
```

---

## 6. Tabelas, figuras, colunas, YouTube e `<interactive>`

### Tabelas (`<table>`)

Aceita `id`, `numbered="false"` e `max-height="250px"` (rolagem com cabeçalho fixo). Em `<column>`: `align="right"` e `mono="true"`. O alinhamento no `<header>` vale para a coluna inteira.

```xml
<table id="tbl:1-1-ions" max-height="250px">
  <title>Concentrações iônicas típicas</title>
  <header>
    <column>Íon</column>
    <column align="right">Interno (mM)</column>
    <column align="right">Externo (mM)</column>
  </header>
  <row><column mono="true">K+</column><column align="right">140</column><column align="right">5</column></row>
  <row><column mono="true">Na+</column><column align="right">15</column><column align="right">145</column></row>
  <caption>Valores aproximados em neurônios de mamíferos.</caption>
</table>
```

### Figuras (`<figure>`)

Imagens locais são lidas na compilação e embutidas no HTML. Um `src` ausente gera aviso (não erro).

```xml
<figure src="diagrama.png" alt="Esquema da membrana celular" id="fig:1-1-membrana">
  <caption>Representação dos canais de sódio e potássio na membrana.</caption>
</figure>
```

### Colunas de layout (`<columns>` e `<column>`)

`width` com número puro indica peso proporcional; com unidade CSS indica largura fixa. Sem `width`, as colunas dividem o espaço igualmente. Em telas estreitas, empilham automaticamente.

```xml
<columns>
  <column width="2">Coluna principal, com o dobro da largura da coluna ao lado.</column>
  <column>Coluna lateral mais estreita.</column>
</columns>
```

### Vídeo do YouTube (`<youtube>`)

Aceita URL completa, link curto (`youtu.be/...`), `/embed`, `/shorts` ou ID de 11 caracteres. É o único elemento que depende de internet.

```xml
<youtube src="https://youtu.be/dQw4w9WgXcQ" id="vid:1-1-palestra">
  <caption>Apresentação introdutória sobre o tema.</caption>
</youtube>
```

### Bloco interativo (`<interactive>`)

Bloco numerado para exibir um componente interativo (geralmente vindo de um pacote importado via `<import>` ou `packages` no `project.toml`).

```xml
<interactive id="int:1-1-grafico">
  <caption>Componente interativo acoplado a um pacote Delta.</caption>
</interactive>
```

---

## 7. Regras de XML estrito e erros mais comuns

1. **Atributo sem valor é erro fatal**: nunca escreva `numbered` ou `collapsible` sozinho; escreva sempre `numbered="false"`, `collapsible="true"`, `collapsed="true"`.
2. **`<`, `>` e `&` na prosa**: fora da matemática e de `<code>`/`<c>`, escreva `&lt;`, `&gt;` e `&amp;`. Dentro de `$...$`, `$$...$$`, `<m>`, `<equation>`, `<equations>` e `<code>`, escreva `<`, `>` e `&` diretamente.
3. **`$` sozinho na prosa**: um cifrão desemparelhado é erro de compilação. Escreva `\$` para cifrão literal.
4. **Tags não fechadas ou cruzadas**: toda tag aberta deve fechar na ordem inversa, ou usar `/>` quando vazia (`<ref to="id"/>`, `<toc/>`).
5. **`id` em português com acento ou duplicado**: use sempre `id` ASCII sem acento nem espaço (ex.: `sec:1-1-1`, `thm:1-1-nome`). `id` repetido gera aviso; `<ref to="..."/>` para `id` inexistente gera aviso e vira `??`.
6. **`<cite>` com `to`**: `<cite>` usa `paper="..."` ou `papers="..."`, nunca `to="..."`.
7. **`<intuition>` fora do lugar ou com `id`**: só pode ficar dentro de resultados ou `<step>`, e nunca pode ter `id` (ambos geram erro de compilação).
8. **`</code>` dentro de `<code>`**: fecha o bloco de código prematuramente; na prosa, use `<c></code></c>`.

---

## 8. Como recolher por padrão

Para recolher qualquer ambiente, seção ou bloco de código por padrão, use:

```xml
collapsible="true" collapsed="true"
```

Exemplos:
- Demonstração recolhida: `<proof of="thm:1-1-nome" collapsible="true" collapsed="true">...</proof>`
- Solução recolhida: `<solution collapsible="true" collapsed="true">...</solution>`
- Seção ou exercício recolhido: `<section id="sec:extra" collapsible="true" collapsed="true">`
- Bloco de código recolhido: `<code lang="python" collapsible="true" collapsed="true">`
- `<intuition>`, `<strategy>` e `<obstacle>` já começam recolhidas por padrão (use `collapsed="false"` apenas se quiser abri-las).
