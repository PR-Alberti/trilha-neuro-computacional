/* ============================================================
   EXERCÍCIOS COM IA
   Painel "Exercícios com IA" na visão de cada tema. O aluno escolhe a
   quantidade, escreve orientações se quiser, e a função gerar-exercicios
   (supabase/functions/gerar-exercicios) pede os exercícios ao Gemini.

   Só funciona com login: é o login que permite o limite diário por aluno
   e guardar o histórico. Sem login, o painel convida a entrar.

   Os textos da IA entram na página sempre escapados (esc), nunca como HTML.

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
  iaGeracoes[tema] = data;
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
      <p class="ia-aviso">Exercícios gerados por IA podem conter erros: confira as resoluções. As orientações são enviadas ao Google Gemini, então não escreva dados pessoais nelas.</p>
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
  el.innerHTML = lista.map(g => `
    <article class="ia-ger">
      <header class="ia-ger-h">
        <span>${esc(new Date(g.criado_em).toLocaleString("pt-BR", {dateStyle:"short", timeStyle:"short"}))}${g.orientacoes ? ` · “${esc(g.orientacoes)}”` : ""}</span>
        <button class="linkbtn" onclick="apagarGeracaoIA(${Number(g.id)})">apagar</button>
      </header>
      <ol class="ia-exs">
        ${g.itens.map(e => `
          <li>
            <p class="ia-enun">${esc(e.enunciado)}</p>
            ${e.dica ? `<details><summary>Ver dica</summary><p>${esc(e.dica)}</p></details>` : ""}
            <details><summary>Ver resolução</summary><p>${esc(e.resolucao)}</p></details>
          </li>`).join("")}
      </ol>
    </article>`).join("");
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
    iaGeracoes[tema] = [data.geracao, ...(iaGeracoes[tema] || [])];
    iaRascunho[tema] = {...iaRascunho[tema], orientacoes:""};
  }
  if(tema === iaTema) renderIA();
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
