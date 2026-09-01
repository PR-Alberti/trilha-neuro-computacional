# Guia de Estudos: ML para Neurociência Computacional

Página web com uma trilha de estudos de Machine Learning voltada a estudantes de
Ciências Biológicas rumo à neurociência computacional — do pré-cálculo ao deep learning.

## Estrutura

| Arquivo | O que é |
|---|---|
| `index.html` | A página do guia (versão em construção) |
| `Guia.pdf` | O roteiro de conteúdo original que a página segue |
| `testes/modulo-NN.pdf` | Teste de cada módulo — PDFs genéricos; substitua pelo teste autêntico mantendo o nome |
| `modelos/index_modelo.html` | Modelo de estilo original (Tailwind), base visual da página |
| `modelos/guia_brain_encode_decode.html` | Segundo modelo, com outra abordagem (CSS próprio + JS) |

## Como a página funciona

A página é orientada a dados: o conteúdo do guia vive em dois arrays JavaScript
(`PHASES` e `MODS`) e o HTML dos módulos é gerado a partir deles. Para editar o
conteúdo, edite os arrays — não o HTML.

- Cada módulo é um `<details>` nativo: dá para **minimizar ou expandir** (botões
  "Expandir/Recolher tudo" no topo).
- Cada tema do conteúdo programático abre **isoladamente** numa visão própria,
  com subtemas, prompt de exercícios para IA e materiais do módulo.
- A navegação usa **roteamento por hash**: `#modulo-3` expande e rola até o
  módulo 3; `#tema-3-2` abre o 2º tema do módulo 3. Links são compartilháveis e
  o botão "voltar" do navegador funciona.
- **Layout desktop**: sidebar fixa com os módulos e progresso; corpo do módulo em
  2 colunas (temas | materiais + teste) em telas largas.
- Cada tema tem um **nível** (`lv`: 0 Básico · 1 Intermediário · 2 Avançado), com
  filtro por nível na página — a atribuição é editável no array `MODS`.
- **Modo escuro**: toggle no header, salvo em `localStorage` (`guia-tema`) e
  respeitando `prefers-color-scheme` por padrão.
- **Progresso**: "Marcar como estudado" em cada tema, salvo em `localStorage`
  (`guia-neuro-progresso`) e refletido nos cartões, módulos e sidebar.
- **Teste da seção**: cada módulo aponta para `testes/modulo-NN.pdf`.

## Como visualizar

Basta abrir o `index.html` no navegador. Para um servidor local (evita problemas de
cache e simula melhor um site de verdade):

```bash
python3 -m http.server 8000
# abra http://localhost:8000
```

## Fluxo de trabalho (git)

- `main` — versão estável.
- `pagina-base` — branch de desenvolvimento da primeira versão da página.

Quando a página estiver pronta, a branch é mesclada na `main` (via Pull Request no
GitHub ou `git merge`).

## Publicação futura

O plano é tornar o repositório público e servir a página pelo **GitHub Pages**
(Settings → Pages → branch `main`), já que o `index.html` está na raiz.
