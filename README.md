# Guia de Estudos: ML para Neurociência Computacional

Página web com uma trilha de estudos de Machine Learning voltada a estudantes de
Ciências Biológicas rumo à neurociência computacional — do pré-cálculo ao deep learning.

## Estrutura

| Arquivo | O que é |
|---|---|
| `index.html` | A página do guia (versão em construção) |
| `conta.js` | Login e progresso sincronizado, via Supabase |
| `ia.js` | Painel "Exercícios com IA" na visão de cada tema |
| `supabase/esquema.sql` | Tabelas e regras de acesso do banco |
| `supabase/functions/gerar-exercicios/` | Função do servidor que pede os exercícios à IA (Groq ou Gemini) |
| `scripts/exportar-temas.mjs` | Copia o catálogo de temas do `index.html` para a função |
| `servidor/` | Versão anterior do backend (API própria), não usada pela página |
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

## Conta e progresso (Supabase)

Quem quiser pode entrar para o progresso acompanhar a pessoa entre aparelhos.
A página continua estática (GitHub Pages); o login e o banco ficam no
[Supabase](https://supabase.com), e todo o código disso está em
[conta.js](conta.js).

- **Entrar sem senha**: link mágico por e-mail, ou conta Google (o botão só
  aparece se o provedor estiver ligado no painel do Supabase).
- **Progresso por usuário** na tabela `progresso`
  ([supabase/esquema.sql](supabase/esquema.sql)). O **Row Level Security** do
  banco garante que cada pessoa só lê e altera as próprias linhas — por isso a
  chave "publishable" pode ficar à vista no `conta.js`.
- **A conta é a fonte da verdade**: na primeira vez de uma conta num navegador,
  o que já estava marcado ali é unido à conta; depois disso vale o que está no
  banco. Marcações feitas sem internet ficam pendentes e sobem depois.
- **Sair** limpa o progresso daquele navegador (ele continua na conta), para
  computadores compartilhados.
- **Minha conta** (clicando no e-mail): diz o que é guardado — só o e-mail e os
  temas marcados — e permite apagar a conta com tudo.
- Sem login, ou se o Supabase estiver fora do ar, a página funciona como
  antes, com o progresso só no `localStorage`.

> **Nunca vão para o repositório:** a chave `service_role`/secreta do Supabase,
> a senha do banco e a chave da IA. Só a chave "publishable" é pública.

### Configurar um projeto Supabase do zero

1. Criar o projeto com *Enable automatic RLS* marcado.
2. *SQL Editor* → colar [supabase/esquema.sql](supabase/esquema.sql) → *Run*
   (pode rodar de novo a cada mudança no arquivo; ele não apaga dados).
3. *Authentication → URL Configuration*: **Site URL** com o endereço do site
   publicado; em **Redirect URLs**, esse mesmo endereço com `**` no fim e
   `http://localhost:8000/**` para testar localmente.
4. Pôr a *Project URL* e a chave *publishable* no topo do `conta.js`.
5. Opcional: *Authentication → Sign In / Providers → Google*, com uma
   credencial OAuth criada no Google Cloud.

### Limites conhecidos

- O envio de e-mail embutido do Supabase permite poucos links por hora e é
  pensado para testes. Para uma turma, ligar o login com Google ou configurar
  um SMTP próprio.
- No plano gratuito, o projeto Supabase é pausado depois de um tempo sem uso e
  precisa ser reativado no painel.

## Exercícios com IA (Groq ou Gemini)

Na visão de cada tema, quem está logado pode gerar exercícios: escolhe a
quantidade (1 a 5) e, se quiser, escreve orientações ("quero mais exercícios
de desigualdades com frações"). Cada exercício vem com dica e resolução,
escondidas até o aluno abrir, e fica no histórico dele.

```
página (ia.js) → função gerar-exercicios (Supabase) → Groq ou Gemini
                  1. confere o login
                  2. gasta uma geração do limite diário
                  3. monta o pedido: dados do tema + orientações do aluno
                  4. chama a IA com a chave secreta
                  5. guarda os exercícios e devolve para a página
```

- **Dois provedores, ambos com camada gratuita**: a função usa o **Groq** se o
  secret `GROQ_API_KEY` existir; senão, o **Gemini** (`GEMINI_API_KEY`). O
  resto (página, banco, limites) não muda. O Groq entrou porque o Google negou
  acesso ao Gemini à conta usada no projeto ("Your project has been denied
  access").
- **Modelo reserva**: se o modelo principal estiver sobrecarregado ou sem cota
  (comum na camada gratuita), a função tenta automaticamente um mais leve
  (`gemini-3.5-flash-lite` no Gemini, `openai/gpt-oss-20b` no Groq). A coluna
  `modelo` da tabela `exercicios` registra qual respondeu.
- **A chave da IA nunca sai do servidor**: fica nos secrets do Supabase, e a
  página só fala com a função.
- **Limite**: 10 gerações por aluno por dia (horário de Brasília). O número
  mora em `limite_diario_ia()` no [supabase/esquema.sql](supabase/esquema.sql).
  Se a IA falha, a geração é devolvida ao aluno.
- **Formato fixo**: a função exige da IA uma resposta em JSON com
  `enunciado`, `dica` e `resolucao`, e confere o resultado antes de guardar.
  Isso também segura orientações que tentam desviar a IA do tema.
- **Catálogo de temas**: a função monta o pedido com o nome, a descrição e os
  subtemas de cada tema, copiados do `index.html` — não confia no que a página
  manda. Ao mudar os temas, rode `node scripts/exportar-temas.mjs` e publique a
  função de novo.
- **Privacidade**: o nome e o e-mail do aluno nunca vão para a IA; só o tema
  e as orientações. Na camada gratuita do Gemini, o Google pode usar esse
  conteúdo para melhorar os produtos dele — a página avisa para não escrever
  dados pessoais nas orientações.
- **Fórmulas em LaTeX**: a IA escreve a matemática entre `$...$` e `$$...$$`,
  e a página a desenha com o [KaTeX](https://katex.org).
- **Baixar**: cada geração vira um **PDF** — uma folha de exercícios, com dicas
  e resoluções numa página separada, aberta na janela de impressão do navegador
  (*Salvar como PDF*) — ou um **`.tex`**, que compila no Overleaf com pdfLaTeX,
  XeLaTeX ou LuaLaTeX.

### Colocar no ar (uma vez)

1. **Banco**: *SQL Editor* → colar o [supabase/esquema.sql](supabase/esquema.sql)
   inteiro → *Run*.
2. **Chave da IA** (uma das duas). **Não cole a chave em arquivo nenhum do
   repositório.**
   - Groq: em <https://console.groq.com>, *API Keys* → *Create API Key*.
   - Gemini: em <https://aistudio.google.com>, *Get API key* → criar a chave.
3. **Secret**: no Supabase, *Edge Functions* → *Secrets* → nome
   `GROQ_API_KEY` (ou `GEMINI_API_KEY`), valor = a chave → *Save*.
4. **Função**: *Edge Functions* → *Deploy a new function* → *Via Editor* →
   nome `gerar-exercicios` → apagar o código de exemplo, colar todo o
   [index.ts](supabase/functions/gerar-exercicios/index.ts) → *Deploy function*.
   Deixe a verificação de JWT ligada (o padrão): a função só é chamada por
   quem está logado.
5. **Testar**: abrir um tema em `http://localhost:8000`, entrar e clicar em
   *Gerar exercícios*. Se der erro, os detalhes aparecem em *Edge Functions →
   gerar-exercicios → Logs*.

Para trocar o modelo sem mexer no código, crie o secret `IA_MODELO` (padrões:
`openai/gpt-oss-120b` no Groq, `gemini-3.8-flash` no Gemini). Para atualizar a função depois, abra-a no painel,
cole o código novo e clique em *Deploy updates*.

## API própria (versão anterior)

A pasta `servidor/` guarda a primeira versão do backend, escrita à mão como
exercício: FastAPI + SQLite sem ORM, com identificação só por e-mail e sessão
em cookie. **A página não usa mais essa API** — ela foi trocada pelo Supabase
porque um servidor próprio precisaria de uma hospedagem com processo e disco
sempre ligados, o que os planos gratuitos não garantem. O servidor ainda entrega a página localmente
(`uvicorn app:app --reload` dentro de `servidor/`), mas as rotas `/api/...`
ficaram sem uso.

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

## Publicação

O repositório é público e a página é servida pelo **GitHub Pages** a partir da
branch `main` (o `index.html` está na raiz):
<https://pr-alberti.github.io/trilha-neuro-computacional/>. Cada `git push` na
`main` atualiza o site.
