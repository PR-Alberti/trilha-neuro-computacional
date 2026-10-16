// Copia o catálogo de temas (PHASES e MODS do index.html) para dentro da
// função gerar-exercicios. A função precisa saber de que trata cada tema para
// montar o pedido à IA, e não pode confiar no que a página manda.
//
// Rode sempre que mudar os temas no index.html:
//   node scripts/exportar-temas.mjs
import { readFileSync, writeFileSync } from "node:fs";

const raiz = new URL("..", import.meta.url);
const html = readFileSync(new URL("index.html", raiz), "utf8");
const FUNCAO = new URL("supabase/functions/gerar-exercicios/index.ts", raiz);

function extrair(nome){
  const m = html.match(new RegExp(`const ${nome} = (\\[[\\s\\S]*?\\n\\]);`));
  if(!m) throw new Error(`não achei "const ${nome} = [...]" no index.html`);
  return new Function(`return ${m[1]}`)();
}

const PHASES = extrair("PHASES"), MODS = extrair("MODS");
const NIVEIS = ["Básico", "Intermediário", "Avançado"];

const temas = {};
for(const m of MODS){
  m.themes.forEach((t, i) => {
    temas[`${m.id}-${i + 1}`] = {
      fase: PHASES[m.ph].name,
      modulo: `${m.title} — ${m.sub}`,
      ponte: m.bio,
      tema: t.n,
      nivel: NIVEIS[t.lv],
      descricao: t.d,
      subtemas: t.t,
    };
  });
}

const bloco = "// <temas> gerado por scripts/exportar-temas.mjs — não edite à mão\n"
  + `const TEMAS: Record<string, Tema> = ${JSON.stringify(temas, null, 1)};\n`
  + "// </temas>";
const fonte = readFileSync(FUNCAO, "utf8");
const novo = fonte.replace(/\/\/ <temas>[\s\S]*?\/\/ <\/temas>/, bloco);
if(novo === fonte && !fonte.includes(bloco)) throw new Error("marcadores <temas> não encontrados na função");
writeFileSync(FUNCAO, novo);
console.log(`${Object.keys(temas).length} temas copiados para ${FUNCAO.pathname}`);
