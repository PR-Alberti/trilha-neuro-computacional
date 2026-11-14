# Padrão das aulas (escritas em Delta)

Este é o contrato que todos os autores (agentes Gemini) e gestores técnicos
(agentes Claude) seguem. A sintaxe do Delta está em [DELTA-COLA.md](DELTA-COLA.md).
A documentação completa do Delta (em `.dlt`) está em `referencias/delta/`, e o
roteiro original do guia em `referencias/Guia.txt`.

## Público

Estudantes de **Ciências Biológicas**: base matemática de ensino médio (às vezes
enferrujada), em geral sem programação. O destino é a **neurociência
computacional**. Quem lê está estudando sozinho, então a aula precisa se bastar.

## Arquivos

| Caminho | O que é |
|---|---|
| `conteudo/modulo-NN/project.toml` | Projeto Delta do módulo (`type = "book"`, `lang = "pt-BR"`). `inputs` lista os temas na ordem do guia |
| `conteudo/modulo-NN/tema-TT.dlt` | Uma aula por tema. `NN` e `TT` com dois dígitos, na ordem do array `MODS` do `index.html` |
| `aulas/modulo-NN/tema-TT.html` | Saída compilada. **Nunca editar à mão**; gerar com `node scripts/compilar-aulas.mjs` |

Cada `tema-TT.dlt` é um `<document>` com **um único `<chapter id="tema-M-T">`**,
cujo título é o nome do tema (igual ao do `MODS`).

## Identificadores (únicos dentro do módulo)

- Seção de subtema: `sec:M-T-S` (S = número do subtema, a partir de 1)
- Definição, teorema, proposição: `def:M-T-nome`, `thm:M-T-nome`, `prop:M-T-nome`
- Exemplo: `exm:M-T-nome` · Exercício: `exr:M-T-S-k` · Equação: `eq:M-T-nome`
- Use só letras minúsculas sem acento, dígitos e hífen depois do prefixo.

## Estrutura de cada aula

1. **Abertura** (antes da primeira seção):
   - *Por que isso importa*: 1–2 parágrafos que ligam o tema à biologia ou à
     neurociência, com exemplos concretos (curva de sintonia, potencial de
     membrana, bandas de EEG, voxels de fMRI...). Parta do campo `bio`/`d` do módulo.
   - *Objetivos*: 3 a 6 itens no formato "Ao final, você consegue…".
   - *Pré-requisitos*: os temas anteriores de que a aula depende.
2. **Uma `<section>` por subtema**, na ordem do guia. Quando o guia não lista
   subtemas, o gestor define de 3 a 5 seções que cubram a descrição do tema.
   Em cada seção:
   - **Intuição primeiro**, em linguagem simples, com analogia biológica quando
     for natural (não force).
   - **Formalização**: `<definition>`, `<theorem>`/`<proposition>`, com
     `<proof>` recolhível quando a demonstração for curta e instrutiva. Se ela for
     longa, explique a ideia em prosa.
   - **Pelo menos 2 `<example>` resolvidos passo a passo**, e pelo menos 1 com
     contexto biológico realista: potencial de repouso ≈ −70 mV, disparo de
     0–200 Hz, TR do fMRI ≈ 2 s etc.
   - `<remark>` com o título "Armadilha comum" quando houver um erro típico.
   - **3 a 5 `<exercise>` graduados**, com o título começando por "Básico",
     "Intermediário" ou "Avançado". Cada um tem `<hint>` e `<solution>`
     **completa**, com o raciocínio e não só a resposta. Pelo menos 1 é aplicado à
     biologia ou à neurociência.
3. **Programação, ML e DL** (módulos 6, 8 e 9, e trechos dos módulos 4, 5 e 7):
   - Use blocos `<code lang="python">` autocontidos, que rodam no Google Colab
     com numpy, pandas, matplotlib, scikit-learn ou torch.
   - Use dados sintéticos ou conjuntos que já vêm nas bibliotecas
     (`sklearn.datasets` etc.).
   - Mostre a saída esperada em comentários.
   - Os exercícios podem ser de código, com a solução em código.
4. **Fechamento**: uma seção "Resumo", com 5 a 10 itens e as fórmulas-chave, e
   uma seção "Para ir além", que aponta os materiais do módulo (campo `mats`).

## Estilo

- **Idioma**: português do Brasil, em segunda pessoa ("você"), amigável e
  rigoroso, sem enrolação.
- **Termos em inglês**: dê o termo em inglês entre parênteses na primeira vez,
  porque os papers usam inglês: "sobreajuste (*overfitting*)".
- **Decimais**: vírgula na prosa ($0{,}5$ dentro da matemática) e ponto dentro
  de código.
- **Notação**: vetores em negrito ($\mathbf{x}$), matrizes maiúsculas em negrito
  ($\mathbf{A}$), conjuntos com `\mathbb` ($\mathbb{R}$). Mantenha a mesma
  notação nos temas do mesmo módulo.
- **Tamanho**: de 2500 a 5000 palavras por tema, conforme o número de subtemas.
- **Continuidade**: não use um conceito que só aparece em módulos posteriores
  sem avisar ("veremos no Módulo 5"). Retome temas anteriores pelo nome.

## Exatidão (inegociável)

- Toda conta, fórmula, demonstração e solução tem de estar certa. Na dúvida,
  simplifique em vez de arriscar.
- Fatos de neurociência só de livro-texto padrão (Kandel; Dayan & Abbott;
  Gerstner et al.). **Não invente** artigos, autores, números de página nem
  links. Clássicos amplamente conhecidos podem ser citados por nome e ano
  (Hodgkin & Huxley, 1952).
- **Links**: só os que já estão no `index.html` ou documentações oficiais
  estáveis (docs.python.org, numpy.org, scikit-learn.org, pytorch.org).

## Delta (regras duras)

- Use XML estrito: sem atributo sem valor; `&lt;`, `&gt;` e `&amp;` na prosa; `<`
  e `&` puros dentro da matemática e do código.
- A aula precisa compilar com `delta build` **sem erro** e passar no
  `delta lint` (código de saída 0).
- Soluções e demonstrações ficam recolhidas por padrão.
- O cabeçalho de cada aula tem um link de volta ao guia:
  `../../index.html#tema-M-T`.

## Fluxo de trabalho

```
Gestor técnico (Claude) ──ordem──▶ Autor (Gemini) escreve tema-TT.dlt
        │                                   │
        │◀── compila + lint (delta) ────────┘
        │──ordem──▶ Revisor (Gemini, outro modelo) → docs/revisao/modulo-NN/tema-TT.md
        │◀── lê o parecer e confere por amostragem (contas, código, fatos)
        └──ordem de correção──▶ Autor … até aprovar
```

Os agentes Gemini **nunca usam o terminal**. Quem compila e roda o lint é o
gestor. O gestor não escreve o conteúdo: ele dá ordens precisas e confere.
