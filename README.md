# Guia de Estudos: ML para Neurociência Computacional

Página web com uma trilha de estudos de Machine Learning voltada a estudantes de
Ciências Biológicas rumo à neurociência computacional — do pré-cálculo ao deep learning.

## Estrutura

| Arquivo | O que é |
|---|---|
| `index.html` | A página do guia (versão em construção) |
| `servidor/` | API opcional: identificação por e-mail e progresso sincronizado |
| `Guia.pdf` | O roteiro de conteúdo original que a página segue |
| `testes/modulo-NN.pdf` | Teste de cada módulo — PDFs genéricos; substitua pelo teste autêntico mantendo o nome |

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

## Backend

A pasta `servidor/` traz uma API própria — o caminho de aprendizado de backend:

- **FastAPI + SQLite sem ORM**: o SQL aparece de verdade ([servidor/db.py](servidor/db.py)).
- **Identificação só por e-mail, sem senha** — decisão de piloto. Não existe
  "criar conta": o primeiro `POST /api/entrar` com um e-mail já cria o registro.
  A sessão é server-side, em cookie `HttpOnly`/`SameSite=Lax`
  ([servidor/seguranca.py](servidor/seguranca.py)).
- **Progresso por usuário** na tabela `progresso`; ao se identificar, o progresso
  local do navegador é **mesclado** com o da conta (`POST /api/progresso/sincronizar`).
- O mesmo servidor entrega a página estática — um processo só, sem CORS — e a
  documentação interativa da API fica em `/api/docs`.
- O servidor publica **só** `index.html`, `Guia.pdf` e `testes/` (lista explícita
  no fim de [servidor/app.py](servidor/app.py)). O banco vive em `servidor/dados/`,
  fora do que é publicado — se você adicionar um arquivo novo à página, lembre de
  incluí-lo nessa lista.
- A página continua funcionando **sem** o servidor (modo estático/localStorage):
  ela detecta o backend em tempo de execução e só então mostra o botão
  "Salvar progresso".

> **Aviso do piloto:** sem senha, quem digitar o e-mail de outra pessoa vê o
> progresso dela. Isso é aceitável enquanto o dado guardado é só "quais temas
> foram marcados" e o uso é restrito. Antes de abrir para desconhecidos, troque
> por autenticação de verdade (link mágico por e-mail é o passo natural).

### Rodar o servidor

```bash
cd servidor
python3 -m venv .venv            # ambiente isolado (uma vez)
source .venv/bin/activate
pip install -r requirements.txt  # uma vez
uvicorn app:app --reload         # http://localhost:8000
```

### Pendências antes de expor na internet

- Autenticação de verdade no lugar da identificação só por e-mail
- Servir atrás de HTTPS e marcar o cookie de sessão como `Secure`
- Limite de requisições por IP (rate limiting)
- Backup periódico do `servidor/dados/guia.db`

## Como visualizar

Basta abrir o `index.html` no navegador. Para um servidor local (evita problemas de
cache e simula melhor um site de verdade):

```bash
python3 -m http.server 8000
# abra http://localhost:8000
```

## Fluxo de trabalho (git)

- `main` — versão estável, com a página e o servidor.
- branches de tema (`pagina-base`, `backend-login`, ...) — desenvolvimento, mescladas
  na `main` via Pull Request no GitHub ou `git merge` quando prontas.

## Publicação futura

O plano é tornar o repositório público e servir a página pelo **GitHub Pages**
(Settings → Pages → branch `main`), já que o `index.html` está na raiz.
