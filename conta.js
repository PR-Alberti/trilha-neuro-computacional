/* ============================================================
   CONTA E SINCRONIZAÇÃO (Supabase)
   A página funciona de dois jeitos:
   - sem conta: progresso só no localStorage deste navegador
   - com conta: progresso guardado na tabela `progresso` do Supabase

   Dois jeitos de entrar, nenhum com senha guardada por nós:
   - link mágico: a pessoa digita o e-mail, recebe um link e, ao clicar,
     volta para a página já identificada
   - conta Google: aparece só se o provedor estiver ligado no Supabase

   A chave abaixo é a "publishable": foi feita para ficar no navegador.
   Quem protege os dados é o Row Level Security do banco (supabase/esquema.sql),
   que só deixa cada usuário ler e alterar as próprias linhas.

   Este arquivo usa do script principal da página: done, saveProg,
   atualizarMarcacoes e esc.
   ============================================================ */
const SUPABASE_URL = "https://aqhrxxjuvdwghctamtfl.supabase.co";
const SUPABASE_CHAVE = "sb_publishable_oKs7aMt62GnAqhINZk1EKQ_KAn2htuJ";

// Quando o link do e-mail não vale mais (expirou, ou já foi usado), o Supabase
// devolve a pessoa para cá com o erro na URL. Guardamos o motivo e limpamos a
// URL, para o erro não ficar no endereço nem confundir a navegação por hash.
const erroDoLink = new URLSearchParams(location.hash.slice(1)).get("error_code")
  || new URLSearchParams(location.search).get("error_code");
if(erroDoLink) history.replaceState(null, "", location.pathname);

// se a biblioteca não carregar (sem internet, CDN fora do ar), a página
// continua funcionando só com o localStorage
const sb = window.supabase ? window.supabase.createClient(SUPABASE_URL, SUPABASE_CHAVE) : null;
// para onde o link do e-mail e o Google trazem a pessoa de volta: esta página
const VOLTA = location.origin + location.pathname;
let usuario = null;      // e-mail identificado, ou null
let usuarioId = null;    // id dessa pessoa no Supabase

// id da conta à qual o progresso deste navegador já foi unido
const CONTA_KEY = "guia-neuro-conta";
// marcações que ainda não chegaram ao banco: {"3-2": true, "1-4": false}
const PEND_KEY = "guia-neuro-pendentes";

function lerLocal(chave, padrao){
  try { return JSON.parse(localStorage.getItem(chave)) ?? padrao; } catch(e){ return padrao; }
}
function gravarLocal(chave, valor){
  try {
    valor === null ? localStorage.removeItem(chave) : localStorage.setItem(chave, JSON.stringify(valor));
  } catch(e){}
}

function iniciarConta(){
  renderAuth();
  if(!sb) return;
  if(erroDoLink){
    abrirAuth();
    avisoAuth(erroDoLink === "otp_expired"
      ? "Esse link expirou ou já foi usado. Peça um novo abaixo."
      : "Não foi possível entrar com esse link. Peça um novo abaixo.", true);
  }
  mostrarGoogleSeAtivo();
  sb.auth.onAuthStateChange((_evento, sessao)=>{
    const antes = usuarioId;
    usuario = sessao ? sessao.user.email : null;
    usuarioId = sessao ? sessao.user.id : null;
    renderAuth();
    // o setTimeout tira a chamada de dentro do callback: o supabase-js
    // trava se a gente consultar o banco enquanto ele avisa da sessão
    if(usuarioId && usuarioId !== antes) setTimeout(()=> sincronizar().catch(console.error), 0);
  });
}

/* Depois do login, a conta é a fonte da verdade: o que vale é o que está
   no banco. A exceção é a primeira vez de uma conta neste navegador — aí o
   que já estava marcado aqui é unido à conta, para ninguém perder nada. */
async function sincronizar(){
  if(lerLocal(CONTA_KEY, null) !== usuarioId){
    const locais = [...done].map(tema => ({tema}));
    if(locais.length){
      const {error} = await sb.from("progresso").upsert(locais, {onConflict:"user_id,tema", ignoreDuplicates:true});
      if(error) throw error;
    }
    gravarLocal(CONTA_KEY, usuarioId);
  }
  await enviarPendentes();
  const {data, error} = await sb.from("progresso").select("tema");
  if(error) throw error;
  done = new Set(data.map(linha => linha.tema));
  // o que ainda não conseguiu subir continua valendo na tela
  for(const [tema, marcado] of Object.entries(lerLocal(PEND_KEY, {}))){
    marcado ? done.add(tema) : done.delete(tema);
  }
  saveProg();
  atualizarMarcacoes();
}

function pedidoMarcacao(tema, marcado){
  return marcado
    ? sb.from("progresso").upsert({tema}, {onConflict:"user_id,tema", ignoreDuplicates:true})
    : sb.from("progresso").delete().eq("tema", tema);
}

/* Cada marcação entra na lista de pendentes antes de ir para o banco e só
   sai de lá quando o banco confirma. Se a internet cair ou a aba fechar no
   meio do caminho, a próxima sincronização tenta de novo. */
function enviarMarcacao(key, marcado){
  if(!sb || !usuario) return;
  gravarLocal(PEND_KEY, {...lerLocal(PEND_KEY, {}), [key]: marcado});
  pedidoMarcacao(key, marcado).then(({error})=>{
    if(error) return console.error(error);
    confirmarEnvio(key, marcado);
  });
}

function confirmarEnvio(tema, marcado){
  const pend = lerLocal(PEND_KEY, {});
  // se a pessoa mudou de ideia enquanto o pedido viajava, o novo valor fica
  if(pend[tema] !== marcado) return;
  delete pend[tema];
  gravarLocal(PEND_KEY, Object.keys(pend).length ? pend : null);
}

async function enviarPendentes(){
  for(const [tema, marcado] of Object.entries(lerLocal(PEND_KEY, {}))){
    const {error} = await pedidoMarcacao(tema, marcado);
    if(error) return console.error(error);
    confirmarEnvio(tema, marcado);
  }
}

function renderAuth(){
  const el = document.getElementById("authArea");
  if(!sb){ el.innerHTML = ""; return; }
  el.innerHTML = usuario
    ? `<span class="auth-mail" title="${esc(usuario)}">${esc(usuario)}</span><button class="btn" onclick="sair()">Sair</button>`
    : `<button class="btn" onclick="abrirAuth()">Salvar progresso</button>`;
}

function avisoAuth(texto, erro){
  const el = document.getElementById("authErr");
  el.textContent = texto;
  el.style.color = erro ? "" : "inherit";
}

function abrirAuth(){ avisoAuth("", true); document.getElementById("authDlg").showModal(); }
function fecharAuth(){ document.getElementById("authDlg").close(); }

document.getElementById("authForm").addEventListener("submit", async ev=>{
  ev.preventDefault();
  const email = document.getElementById("authEmail").value.trim();
  const botao = document.getElementById("authSubmit");
  botao.disabled = true;
  avisoAuth("Enviando…", false);
  const {error} = await sb.auth.signInWithOtp({
    email,
    options:{emailRedirectTo: VOLTA},
  });
  botao.disabled = false;
  if(error){
    avisoAuth(error.status === 429
      ? "Muitos pedidos de link em pouco tempo. Tente de novo daqui a alguns minutos."
      : "Não foi possível enviar o link. Confira o e-mail e tente de novo.", true);
    console.error(error);
    return;
  }
  avisoAuth(`Enviamos um link para ${email}. Abra o e-mail e clique nele para entrar (confira também o spam).`, false);
});

/* Pergunta ao Supabase quais formas de login estão ligadas no painel
   (Authentication → Sign In / Providers) e só então mostra o botão do Google.
   Assim o botão nunca aparece sem funcionar. */
async function mostrarGoogleSeAtivo(){
  try {
    const r = await fetch(SUPABASE_URL + "/auth/v1/settings", {headers:{apikey: SUPABASE_CHAVE}});
    const cfg = await r.json();
    document.getElementById("authGoogle").hidden = !(cfg.external && cfg.external.google);
  } catch(e){}
}

async function entrarComGoogle(){
  // leva a pessoa à tela do Google; na volta, o supabase-js completa o login
  const {error} = await sb.auth.signInWithOAuth({provider:"google", options:{redirectTo: VOLTA}});
  if(error){
    avisoAuth("Não foi possível abrir o login do Google. Tente de novo.", true);
    console.error(error);
  }
}

async function sair(){
  await enviarPendentes().catch(console.error);
  // scope "local": sai só deste navegador, sem derrubar os outros aparelhos
  await sb.auth.signOut({scope:"local"}).catch(console.error);
  esquecerProgressoLocal();
}

/* Ao sair, o progresso some deste navegador (ele continua guardado na conta).
   Sem isso, num computador compartilhado, a próxima pessoa a entrar herdaria
   as marcações de quem usou antes. */
function esquecerProgressoLocal(){
  gravarLocal(CONTA_KEY, null);
  gravarLocal(PEND_KEY, null);
  done = new Set();
  saveProg();
  atualizarMarcacoes();
}
