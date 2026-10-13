/* ============================================================
   CONTA E SINCRONIZAÇÃO (Supabase)
   A página funciona de dois jeitos:
   - sem conta: progresso só no localStorage deste navegador
   - com conta: progresso guardado na tabela `progresso` do Supabase

   Login por link mágico: a pessoa digita o e-mail, recebe um link e, ao
   clicar, volta para a página já identificada. Não existe senha.

   A chave abaixo é a "publishable": foi feita para ficar no navegador.
   Quem protege os dados é o Row Level Security do banco (supabase/esquema.sql),
   que só deixa cada usuário ler e alterar as próprias linhas.

   Este arquivo usa do script principal da página: done, saveProg,
   atualizarMarcacoes e esc.
   ============================================================ */
const SUPABASE_URL = "https://aqhrxxjuvdwghctamtfl.supabase.co";
const SUPABASE_CHAVE = "sb_publishable_oKs7aMt62GnAqhINZk1EKQ_KAn2htuJ";

// se a biblioteca não carregar (sem internet, CDN fora do ar), a página
// continua funcionando só com o localStorage
const sb = window.supabase ? window.supabase.createClient(SUPABASE_URL, SUPABASE_CHAVE) : null;
let usuario = null;      // e-mail identificado, ou null

function iniciarConta(){
  renderAuth();
  if(!sb) return;
  sb.auth.onAuthStateChange((_evento, sessao)=>{
    const antes = usuario;
    usuario = sessao ? sessao.user.email : null;
    renderAuth();
    // o setTimeout tira a chamada de dentro do callback: o supabase-js
    // trava se a gente consultar o banco enquanto ele avisa da sessão
    if(usuario && usuario !== antes) setTimeout(()=> sincronizar().catch(console.error), 0);
  });
}

/* União do progresso local com o da conta — ninguém perde nada. */
async function sincronizar(){
  const locais = [...done].map(tema => ({tema}));
  if(locais.length){
    const {error} = await sb.from("progresso").upsert(locais, {onConflict:"user_id,tema", ignoreDuplicates:true});
    if(error) throw error;
  }
  const {data, error} = await sb.from("progresso").select("tema");
  if(error) throw error;
  done = new Set(data.map(linha => linha.tema));
  saveProg();
  atualizarMarcacoes();
}

function enviarMarcacao(key, marcado){
  if(!sb || !usuario) return;
  const pedido = marcado
    ? sb.from("progresso").upsert({tema:key}, {onConflict:"user_id,tema", ignoreDuplicates:true})
    : sb.from("progresso").delete().eq("tema", key);
  pedido.then(({error})=>{ if(error) console.error(error); });
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
  // o link do e-mail traz a pessoa de volta para esta mesma página
  const {error} = await sb.auth.signInWithOtp({
    email,
    options:{emailRedirectTo: location.origin + location.pathname},
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

async function sair(){
  // scope "local": sai só deste navegador, sem derrubar os outros aparelhos
  await sb.auth.signOut({scope:"local"}).catch(console.error);
}
