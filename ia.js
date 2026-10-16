/* ============================================================
   EXERCÍCIOS COM IA
   Painel "Exercícios com IA" na visão de cada tema. O aluno escolhe a
   quantidade, escreve orientações se quiser, e a função gerar-exercicios
   (supabase/functions/gerar-exercicios) pede os exercícios à IA (Groq ou
   Gemini, conforme a chave configurada no Supabase).

   Só funciona com login: é o login que permite o limite diário por aluno
   e guardar o histórico. Sem login, o painel convida a entrar.

   Os textos da IA entram na página sempre escapados (esc), nunca como HTML.
   As fórmulas vêm em LaTeX ($...$ e $$...$$) e são desenhadas pelo KaTeX.
   Cada geração pode ser baixada como PDF (pela janela de impressão do
   navegador) ou como .tex, para editar e compilar no Overleaf.

   Este arquivo usa do conta.js: sb, usuario, usuarioId e abrirAuth; e do
   script principal: esc.
   ============================================================ */
const IA_MAX_ORIENTACOES = 300;
const IA_MAX_QUANTIDADE = 5;

let iaTema = null;        // tema aberto na tela, ex.: "3-2"
let iaDono = null;        // de quem são os dados em memória (id do usuário)
let iaGeracoes = {};      // tema → lista de gerações já carregadas do banco
let iaRascunho = {};      // tema → {quantidade, orientacoes} digitados
let iaGerando = null;     // tema com um pedido em andamento
let iaRestantes = null;   // gerações que o aluno ainda tem hoje
let iaMensagem = {};      // tema → {texto, erro}
let iaRecolhidas = new Set();  // ids das gerações minimizadas

/* Chamado pelo script principal toda vez que a visão de um tema é desenhada. */
function montarIA(tema){
  iaTema = tema;
  if(usuarioId !== iaDono) esquecerIA();
  renderIA();
  if(usuario) carregarIA(tema);
}

/* Chamado pelo conta.js quando a pessoa entra ou sai. */
function atualizarIA(){
  if(iaTema && document.getElementById("iaBox")) montarIA(iaTema);
}

// trocou de conta (ou saiu): nada do usuário anterior fica na tela
function esquecerIA(){
  iaDono = usuarioId;
  iaGeracoes = {}; iaRascunho = {}; iaMensagem = {};
  iaRecolhidas = new Set();
  iaRestantes = null;
}

async function carregarIA(tema){
  const dono = usuarioId;
  if(iaRestantes === null){
    const {data, error} = await sb.rpc("geracoes_restantes_hoje");
    if(error) console.error(error);
    else if(dono === usuarioId){ iaRestantes = data; renderSaldoIA(); }
  }
  if(iaGeracoes[tema]) return;
  const {data, error} = await sb.from("exercicios")
    .select("id, orientacoes, itens, criado_em")
    .eq("tema", tema)
    .order("criado_em", {ascending:false})
    .limit(10);
  if(error){ console.error(error); return; }
  if(dono !== usuarioId) return;   // a pessoa saiu enquanto carregava
  iaGeracoes[tema] = data.map(repararGeracao);
  if(tema === iaTema) renderListaIA();
}

/* ---------------- desenho ---------------- */

function renderIA(){
  const box = document.getElementById("iaBox");
  if(!box) return;
  if(!sb){
    box.innerHTML = `<p class="note">Os exercícios com IA estão indisponíveis agora.</p>`;
    return;
  }
  if(!usuario){
    box.innerHTML = `
      <p class="note">Entre na sua conta para gerar exercícios deste tema com IA — do jeito que você pedir.</p>
      <button class="btn" onclick="abrirAuth()">Entrar para gerar exercícios</button>`;
    return;
  }
  const r = iaRascunho[iaTema] || {quantidade:3, orientacoes:""};
  const gerando = iaGerando === iaTema;
  box.innerHTML = `
    <div class="ia-form">
      <label class="ia-qtd">Quantidade
        <select id="iaQtd" onchange="guardarRascunhoIA()">
          ${Array.from({length:IA_MAX_QUANTIDADE}, (_, i) =>
            `<option${i + 1 === r.quantidade ? " selected" : ""}>${i + 1}</option>`).join("")}
        </select>
      </label>
      <label class="ia-ori">Orientações (opcional)
        <textarea id="iaOri" rows="2" maxlength="${IA_MAX_ORIENTACOES}" oninput="guardarRascunhoIA()"
          placeholder="Ex.: quero exercícios que usem mais desigualdades com frações">${esc(r.orientacoes)}</textarea>
        <span class="ia-cont" id="iaCont">${r.orientacoes.length}/${IA_MAX_ORIENTACOES}</span>
      </label>
      <div class="ia-acoes">
        <button class="btn-primary" id="iaBtn" onclick="gerarIA()"${gerando ? " disabled" : ""}>${gerando ? "Gerando…" : "Gerar exercícios"}</button>
        <span class="ia-saldo" id="iaSaldo"></span>
      </div>
      <p class="ia-msg" id="iaMsg" aria-live="polite"></p>
      <p class="ia-aviso">Exercícios gerados por IA podem conter erros: confira as resoluções. As orientações são enviadas a um serviço de IA externo, então não escreva dados pessoais nelas.</p>
    </div>
    <div id="iaLista"></div>`;
  renderSaldoIA();
  renderMensagemIA();
  renderListaIA();
}

function renderSaldoIA(){
  const el = document.getElementById("iaSaldo");
  if(!el) return;
  el.textContent = iaRestantes === null ? ""
    : iaRestantes === 1 ? "resta 1 geração hoje"
    : `restam ${iaRestantes} gerações hoje`;
}

function renderMensagemIA(){
  const el = document.getElementById("iaMsg");
  if(!el) return;
  const m = iaGerando === iaTema
    ? {texto:"Gerando os exercícios… isso costuma levar alguns segundos.", erro:false}
    : iaMensagem[iaTema];
  el.textContent = m ? m.texto : "";
  el.classList.toggle("erro", !!(m && m.erro));
}

function renderListaIA(){
  const el = document.getElementById("iaLista");
  if(!el) return;
  const lista = iaGeracoes[iaTema];
  if(!lista){ el.innerHTML = ""; return; }
  if(!lista.length){
    el.innerHTML = `<p class="note">Você ainda não gerou exercícios deste tema.</p>`;
    return;
  }
  const todasRecolhidas = lista.every(g => iaRecolhidas.has(g.id));
  el.innerHTML = (lista.length > 1 ? `
    <p style="text-align:right;font-size:.78rem">
      <button class="linkbtn" onclick="recolherTodasIA(${!todasRecolhidas})">${todasRecolhidas ? "expandir todas" : "minimizar todas"}</button>
    </p>` : "") + lista.map(g => {
    const recolhida = iaRecolhidas.has(g.id);
    const n = g.itens.length;
    return `
    <article class="ia-ger">
      <header class="ia-ger-h">
        <span>${esc(new Date(g.criado_em).toLocaleString("pt-BR", {dateStyle:"short", timeStyle:"short"}))}${g.orientacoes ? ` · “${esc(g.orientacoes)}”` : ""}${recolhida ? ` · ${n} exercício${n > 1 ? "s" : ""}` : ""}</span>
        <span class="ia-ger-acoes">
          <button class="linkbtn" onclick="recolherGeracaoIA(${Number(g.id)})" aria-expanded="${!recolhida}">${recolhida ? "expandir" : "minimizar"}</button>
          <button class="linkbtn" onclick="baixarPdfIA(${Number(g.id)})" title="Abre a janela de impressão: escolha &quot;Salvar como PDF&quot;">baixar PDF</button>
          <button class="linkbtn" onclick="baixarTexIA(${Number(g.id)})" title="Código LaTeX, para editar ou compilar no Overleaf">baixar .tex</button>
          <button class="linkbtn" onclick="apagarGeracaoIA(${Number(g.id)})">apagar</button>
        </span>
      </header>
      <ol class="ia-exs"${recolhida ? ' style="display:none"' : ""}>
        ${g.itens.map(e => `
          <li>
            <p class="ia-enun">${esc(e.enunciado)}</p>
            ${e.dica ? `<details><summary>Ver dica</summary><p>${esc(e.dica)}</p></details>` : ""}
            <details><summary>Ver resolução</summary><p>${esc(e.resolucao)}</p></details>
          </li>`).join("")}
      </ol>
    </article>`;
  }).join("");
  desenharFormulas(el);
}

function recolherGeracaoIA(id){
  iaRecolhidas.has(id) ? iaRecolhidas.delete(id) : iaRecolhidas.add(id);
  renderListaIA();
}

function recolherTodasIA(recolher){
  for(const g of iaGeracoes[iaTema] || []) recolher ? iaRecolhidas.add(g.id) : iaRecolhidas.delete(g.id);
  renderListaIA();
}

/* ---------------- fórmulas (KaTeX) ---------------- */

// A IA às vezes escreve "\times" com a barra simples dentro do JSON, e o JSON
// lê "\t" como tabulação: a fórmula vira "imes". Dentro das fórmulas esses
// caracteres nunca são de verdade, então dá para desfazer. A função do servidor
// já faz isso nas gerações novas; aqui vale também para as guardadas antes.
const LATEX_QUEBRADO = {"\t":"\\t", "\b":"\\b", "\f":"\\f", "\r":"\\r"};
const COMANDOS_COM_N = /\n(?=(?:eq|abla|u|ot|eg|i|leq|geq|mid|exists|subseteq|ewline)(?![a-zA-Z]))/g;
function repararLatex(texto){
  return (texto || "").replace(/\$\$[\s\S]+?\$\$|\$[^$]+?\$/g, f => f
    .replace(/[\t\b\f\r](?=[a-zA-Z])/g, c => LATEX_QUEBRADO[c])
    .replace(COMANDOS_COM_N, "\\n"));
}
function repararGeracao(g){
  return {...g, itens:g.itens.map(e => ({
    enunciado:repararLatex(e.enunciado), dica:repararLatex(e.dica), resolucao:repararLatex(e.resolucao),
  }))};
}

const KATEX_CSS = "https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.11/katex.min.css";

// troca os trechos $...$ e $$...$$ por fórmulas desenhadas. Se o KaTeX não
// carregou (sem internet), as fórmulas ficam como texto, mas nada quebra.
function desenharFormulas(el){
  if(!window.renderMathInElement) return;
  renderMathInElement(el, {
    delimiters:[{left:"$$", right:"$$", display:true}, {left:"$", right:"$", display:false}],
    throwOnError:false,
  });
}

/* ---------------- ações ---------------- */

// guarda o que a pessoa digitou: a visão do tema é redesenhada ao marcar
// "estudado", e o texto não pode sumir por isso
function guardarRascunhoIA(){
  const orientacoes = document.getElementById("iaOri").value;
  iaRascunho[iaTema] = {quantidade:+document.getElementById("iaQtd").value, orientacoes};
  document.getElementById("iaCont").textContent = `${orientacoes.length}/${IA_MAX_ORIENTACOES}`;
}

const IA_ERROS = {
  limite: "Você já usou todas as gerações de hoje. Amanhã tem mais!",
  ia_ocupada: "A IA está com muitos pedidos agora. Tente de novo em alguns minutos — esta tentativa não contou no seu limite.",
  ia_falhou: "A IA não conseguiu gerar os exercícios desta vez. Tente de novo — esta tentativa não contou no seu limite.",
  login: "Sua sessão expirou. Entre de novo para continuar.",
  pedido_invalido: "Pedido inválido. Confira a quantidade e o tamanho das orientações.",
};

async function gerarIA(){
  const tema = iaTema, dono = usuarioId;
  if(iaGerando) return;
  guardarRascunhoIA();
  const {quantidade, orientacoes} = iaRascunho[tema];
  iaGerando = tema;
  delete iaMensagem[tema];
  renderIA();

  const {data, error} = await sb.functions.invoke("gerar-exercicios", {
    body:{tema, quantidade, orientacoes:orientacoes.trim()},
  });
  iaGerando = null;
  if(dono !== usuarioId) return;   // a pessoa saiu no meio do caminho

  if(error){
    // a função responde {erro, restantes}; sem resposta, foi a conexão
    const corpo = await (error.context && error.context.json ? error.context.json().catch(() => ({})) : {});
    if(typeof corpo.restantes === "number") iaRestantes = corpo.restantes;
    iaMensagem[tema] = {
      texto: IA_ERROS[corpo.erro] || "Não foi possível falar com o servidor. Confira sua conexão e tente de novo.",
      erro: true,
    };
    console.error(error);
  } else {
    iaRestantes = data.restantes;
    iaGeracoes[tema] = [repararGeracao(data.geracao), ...(iaGeracoes[tema] || [])];
    iaRascunho[tema] = {...iaRascunho[tema], orientacoes:""};
  }
  if(tema === iaTema) renderIA();
}

/* ---------------- baixar ---------------- */

function acharGeracaoIA(id){
  for(const tema in iaGeracoes){
    const g = iaGeracoes[tema].find(x => x.id === id);
    if(g) return {tema, g};
  }
  return null;
}

function infoTemaIA(tema){
  const [mi, ti] = tema.split("-").map(Number);
  const m = MODS.find(x => x.id === mi);
  return {m, t:m.themes[ti - 1]};
}

// "exercicios-algebra-2026-10-16"
function nomeArquivoIA(tema, g){
  const {t} = infoTemaIA(tema);
  const dia = new Date(g.criado_em).toLocaleDateString("sv-SE");
  return `exercicios ${t.n} ${dia}`.normalize("NFD").replace(/[\u0300-\u036f]/g, "")
    .toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");
}

function baixarArquivo(nome, conteudo, tipo){
  const url = URL.createObjectURL(new Blob([conteudo], {type:tipo}));
  const a = Object.assign(document.createElement("a"), {href:url, download:nome});
  document.body.append(a);
  a.click();
  a.remove();
  setTimeout(() => URL.revokeObjectURL(url), 10000);
}

/* PDF: monta uma folha de exercícios com cara de LaTeX (texto em STIX Two,
   fórmulas com as fontes do KaTeX) e abre a janela de impressão, onde se escolhe "Salvar
   como PDF". Dicas e resoluções vão para outra página, para o aluno tentar
   resolver antes de olhar. */
function documentoPdfIA(tema, g){
  const {m, t} = infoTemaIA(tema);
  const lista = campo => `<ol>${g.itens.map(e =>
    `<li><div class="txt">${esc(e[campo] || "(sem dica)")}</div></li>`).join("")}</ol>`;
  const corpo = document.createElement("div");
  corpo.innerHTML = `
    <header>
      <p class="serie">Trilha · Neuro Computacional — Módulo ${pad2(m.id)} · ${esc(m.title)}</p>
      <h1>Exercícios: ${esc(t.n)}</h1>
      <p class="meta">Gerado em ${esc(new Date(g.criado_em).toLocaleDateString("pt-BR"))}${g.orientacoes ? ` · Orientações: “${esc(g.orientacoes)}”` : ""}</p>
    </header>
    <h2>Exercícios</h2>${lista("enunciado")}
    <section class="gabarito">
      <h2>Dicas</h2>${lista("dica")}
      <h2>Resoluções</h2>${lista("resolucao")}
    </section>
    <footer>Exercícios gerados por IA: podem conter erros, confira as resoluções. ${esc(location.origin + location.pathname)}</footer>`;
  desenharFormulas(corpo);
  return `<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<title>${esc(nomeArquivoIA(tema, g))}</title>
<link rel="stylesheet" href="${KATEX_CSS}">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=STIX+Two+Text:ital,wght@0,400;0,700;1,400&display=swap">
<style>
@page{size:A4;margin:2.2cm 2cm}
body{margin:0;font-family:"STIX Two Text","Latin Modern Roman","Times New Roman",serif;font-size:12pt;line-height:1.45;color:#000;background:#fff}
header{border-bottom:.6pt solid #000;padding-bottom:8pt;margin-bottom:6pt}
.serie{font-size:9pt;letter-spacing:.06em;text-transform:uppercase;margin:0}
h1{font-size:20pt;font-weight:normal;margin:6pt 0 4pt}
.meta{font-size:10pt;margin:0}
h2{font-size:13pt;font-weight:bold;margin:18pt 0 8pt}
ol{padding-left:1.6em;margin:0}
li{margin-bottom:12pt;break-inside:avoid}
.txt{white-space:pre-wrap}
.katex{font-size:1.05em}
.katex-display{margin:6pt 0}
.gabarito{break-before:page}
footer{margin-top:28pt;padding-top:6pt;border-top:.4pt solid #888;font-size:9pt;color:#444}
</style></head><body>${corpo.innerHTML}</body></html>`;
}

function imprimirDocumento(html, titulo){
  const quadro = document.createElement("iframe");
  quadro.style.cssText = "position:fixed;right:0;bottom:0;width:0;height:0;border:0";
  quadro.srcdoc = html;
  quadro.onload = async () => {
    const w = quadro.contentWindow;
    w.document.body.offsetHeight;          // força o layout, para as fontes começarem a carregar
    try { await w.document.fonts.ready; } catch(e){}
    // o navegador sugere o nome do PDF a partir do título da página
    const tituloAntes = document.title;
    document.title = titulo;
    w.focus();
    w.print();
    document.title = tituloAntes;
    setTimeout(() => quadro.remove(), 60000);
  };
  document.body.append(quadro);
}

function baixarPdfIA(id){
  const achado = acharGeracaoIA(id);
  if(!achado) return;
  imprimirDocumento(documentoPdfIA(achado.tema, achado.g), nomeArquivoIA(achado.tema, achado.g));
}

/* .tex: o texto comum é escapado para o LaTeX; as fórmulas passam como estão.
   Compila no Overleaf com pdfLaTeX, XeLaTeX ou LuaLaTeX. */
const TEX_ESPECIAIS = {"\\":"\\textbackslash{}", "{":"\\{", "}":"\\}", "&":"\\&", "%":"\\%",
  "#":"\\#", "_":"\\_", "^":"\\textasciicircum{}", "~":"\\textasciitilde{}", "$":"\\$"};
// símbolos que podem aparecer fora das fórmulas e que o pdfLaTeX não conhece
const TEX_UNICODE = {"≥":"\\geq", "≤":"\\leq", "≠":"\\neq", "≈":"\\approx", "×":"\\times", "−":"-",
  "→":"\\to", "←":"\\leftarrow", "↔":"\\leftrightarrow", "⇒":"\\Rightarrow", "±":"\\pm", "∞":"\\infty",
  "√":"\\surd", "∑":"\\sum", "∫":"\\int", "∂":"\\partial", "∈":"\\in", "∉":"\\notin", "⊂":"\\subset",
  "∪":"\\cup", "∩":"\\cap", "∀":"\\forall", "∃":"\\exists", "α":"\\alpha", "β":"\\beta", "γ":"\\gamma",
  "δ":"\\delta", "ε":"\\varepsilon", "η":"\\eta", "θ":"\\theta", "κ":"\\kappa", "λ":"\\lambda", "μ":"\\mu",
  "ν":"\\nu", "ξ":"\\xi", "π":"\\pi", "ρ":"\\rho", "σ":"\\sigma", "τ":"\\tau", "φ":"\\varphi", "χ":"\\chi",
  "ψ":"\\psi", "ω":"\\omega", "Δ":"\\Delta", "Θ":"\\Theta", "Λ":"\\Lambda", "Π":"\\Pi", "Σ":"\\Sigma",
  "Φ":"\\Phi", "Ψ":"\\Psi", "Ω":"\\Omega", "✓":"\\checkmark", "✔":"\\checkmark", "✗":"\\times"};

function textoParaTex(texto){
  return (texto || "").trim()
    // separa fórmulas ($$...$$ e $...$) do texto comum
    .split(/(\$\$[\s\S]+?\$\$|\$[^$\n]+?\$)/)
    .map((parte, i) => {
      if(i % 2) return parte.startsWith("$$") ? `\\[${parte.slice(2, -2)}\\]` : parte;
      return parte.replace(/[\\{}&%#_^~$]/g, c => TEX_ESPECIAIS[c]);
    })
    .join("")
    // cada quebra de linha vira um parágrafo (linhas vazias se juntam)
    .replace(/\n\s*\n/g, "\n").replace(/\n/g, "\\par\n");
}

function documentoTexIA(tema, g){
  const {m, t} = infoTemaIA(tema);
  const lista = campo => [
    "\\begin{enumerate}",
    ...g.itens.map(e => `\\item ${textoParaTex(e[campo] || "(sem dica)")}\n`),
    "\\end{enumerate}",
  ].join("\n");
  return [
    "% Exercícios gerados por IA — Trilha Neuro Computacional",
    "% Compila no Overleaf com pdfLaTeX, XeLaTeX ou LuaLaTeX.",
    "\\documentclass[11pt,a4paper]{article}",
    "\\usepackage{iftex}",
    "\\ifPDFTeX",
    "  \\usepackage[utf8]{inputenc}",
    "  \\usepackage[T1]{fontenc}",
    "  \\usepackage{lmodern}",
    "\\fi",
    "\\usepackage[brazil]{babel}",
    "\\usepackage{amsmath,amssymb}",
    "\\usepackage[margin=2.2cm]{geometry}",
    "\\usepackage{newunicodechar}",
    ...Object.entries(TEX_UNICODE).map(([c, cmd]) => `\\newunicodechar{${c}}{\\ensuremath{${cmd}}}`),
    "\\setlength{\\parindent}{0pt}",
    "\\setlength{\\parskip}{4pt}",
    "",
    `\\title{Exercícios: ${textoParaTex(t.n)}}`,
    `\\author{Trilha Neuro Computacional --- Módulo ${pad2(m.id)}: ${textoParaTex(m.title)}}`,
    `\\date{${new Date(g.criado_em).toLocaleDateString("pt-BR")}}`,
    "",
    "\\begin{document}",
    "\\maketitle",
    g.orientacoes ? `\\noindent\\textit{Orientações: ${textoParaTex(g.orientacoes)}}\n` : "",
    "\\section*{Exercícios}",
    lista("enunciado"),
    "",
    "\\newpage",
    "\\section*{Dicas}",
    lista("dica"),
    "",
    "\\section*{Resoluções}",
    lista("resolucao"),
    "",
    "\\vfill",
    "{\\footnotesize Exercícios gerados por IA: podem conter erros, confira as resoluções.\\par}",
    "\\end{document}",
    "",
  ].join("\n");
}

function baixarTexIA(id){
  const achado = acharGeracaoIA(id);
  if(!achado) return;
  baixarArquivo(nomeArquivoIA(achado.tema, achado.g) + ".tex", documentoTexIA(achado.tema, achado.g), "application/x-tex");
}

async function apagarGeracaoIA(id){
  if(!confirm("Apagar estes exercícios do seu histórico?")) return;
  const {error} = await sb.from("exercicios").delete().eq("id", id);
  if(error){
    iaMensagem[iaTema] = {texto:"Não foi possível apagar agora. Tente de novo.", erro:true};
    renderMensagemIA();
    console.error(error);
    return;
  }
  for(const tema in iaGeracoes) iaGeracoes[tema] = iaGeracoes[tema].filter(g => g.id !== id);
  renderListaIA();
}
