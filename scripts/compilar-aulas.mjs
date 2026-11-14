// Compila as aulas em Delta (conteudo/modulo-NN/*.dlt) para HTML em aulas/
// e gera o índice aulas/indice.js consumido pelo index.html.
//
// Uso:
//   node scripts/compilar-aulas.mjs
//   node scripts/compilar-aulas.mjs --modulo 1
import { existsSync, mkdirSync, readdirSync, readFileSync, writeFileSync } from "node:fs";
import { basename, join } from "node:path";
import { spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";

const raiz = fileURLToPath(new URL("..", import.meta.url));
const dirConteudo = join(raiz, "conteudo");
const dirAulas = join(raiz, "aulas");
const arqIndice = join(dirAulas, "indice.js");
const DELTA_BIN = process.env.DELTA_BIN || "delta";

function parseArgs(argv) {
  let moduloAlvo = null;
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === "--modulo") {
      const val = argv[++i];
      if (!val || !/^\d+$/.test(val)) {
        throw new Error("Uso: node scripts/compilar-aulas.mjs [--modulo N]");
      }
      moduloAlvo = Number(val);
    } else if (a.startsWith("--modulo=")) {
      const val = a.slice("--modulo=".length);
      if (!val || !/^\d+$/.test(val)) {
        throw new Error("Uso: node scripts/compilar-aulas.mjs [--modulo N]");
      }
      moduloAlvo = Number(val);
    } else {
      throw new Error(`Argumento desconhecido: ${a}`);
    }
  }
  return { moduloAlvo };
}

function descobrirModulos() {
  if (!existsSync(dirConteudo)) return [];
  const modulos = [];
  for (const ent of readdirSync(dirConteudo, { withFileTypes: true })) {
    if (!ent.isDirectory() || ent.name.startsWith("_")) continue;
    const match = ent.name.match(/^modulo-(\d+)$/);
    if (!match) continue;
    const dir = join(dirConteudo, ent.name);
    if (!existsSync(join(dir, "project.toml"))) continue;
    const num = Number(match[1]);
    modulos.push({
      nome: ent.name,
      num,
      nn: String(num).padStart(2, "0"),
      dir,
    });
  }
  return modulos.sort((a, b) => a.num - b.num);
}

function rodarDelta(argsCmd, cwd) {
  const res = spawnSync(DELTA_BIN, argsCmd, {
    cwd,
    encoding: "utf8",
    maxBuffer: 20 * 1024 * 1024,
  });
  if (res.error) {
    throw new Error(`Não foi possível executar "${DELTA_BIN} ${argsCmd.join(" ")}": ${res.error.message}`);
  }
  return res;
}

function parseJsonSeguro(texto) {
  const limpo = (texto || "").trim();
  if (!limpo) return null;
  try {
    return JSON.parse(limpo);
  } catch {
    const inicioObj = limpo.indexOf("{");
    const inicioArr = limpo.indexOf("[");
    let inicio = -1;
    let fim = -1;
    if (inicioObj !== -1 && (inicioArr === -1 || inicioObj < inicioArr)) {
      inicio = inicioObj;
      fim = limpo.lastIndexOf("}");
    } else if (inicioArr !== -1) {
      inicio = inicioArr;
      fim = limpo.lastIndexOf("]");
    }
    if (inicio !== -1 && fim > inicio) {
      try {
        return JSON.parse(limpo.slice(inicio, fim + 1));
      } catch {
        return null;
      }
    }
    return null;
  }
}

function contarLint(stdout, status) {
  const data = parseJsonSeguro(stdout);
  let avisos = 0;
  let erros = 0;

  const contarLista = (lista) => {
    for (const item of lista) {
      if (!item || typeof item !== "object") continue;
      const sev = String(item.severity ?? item.level ?? item.type ?? item.kind ?? "").toLowerCase();
      if (sev.includes("err")) erros++;
      else if (sev.includes("warn") || sev.includes("aviso")) avisos++;
    }
  };

  if (Array.isArray(data)) {
    contarLista(data);
  } else if (data && typeof data === "object") {
    const errNum = data.errors ?? data.errorCount ?? data.summary?.errors;
    const warnNum = data.warnings ?? data.warningCount ?? data.summary?.warnings;
    if (typeof errNum === "number" || typeof warnNum === "number") {
      erros = typeof errNum === "number" ? errNum : 0;
      avisos = typeof warnNum === "number" ? warnNum : 0;
    } else {
      for (const chave of ["diagnostics", "issues", "messages", "results"]) {
        if (Array.isArray(data[chave])) contarLista(data[chave]);
      }
      if (Array.isArray(data.errors)) erros += data.errors.length;
      if (Array.isArray(data.warnings)) avisos += data.warnings.length;
      if (Array.isArray(data.files)) {
        for (const f of data.files) {
          if (!f || typeof f !== "object") continue;
          for (const chave of ["diagnostics", "issues", "messages"]) {
            if (Array.isArray(f[chave])) contarLista(f[chave]);
          }
          if (Array.isArray(f.errors)) erros += f.errors.length;
          if (Array.isArray(f.warnings)) avisos += f.warnings.length;
        }
      }
    }
  }

  if (status !== 0 && erros === 0) {
    erros = 1;
  }
  return { avisos, erros };
}

function extrairTemasDoOutline(mod, outlineData) {
  const temas = {};
  const files = Array.isArray(outlineData?.files) ? outlineData.files : [];
  for (const f of files) {
    const nomeArq = basename(String(f?.file || ""));
    const matchTema = nomeArq.match(/^tema-(\d+)\.dlt$/);
    if (!matchTema) continue;
    const tNum = Number(matchTema[1]);
    const tt = String(tNum).padStart(2, "0");
    const key = `${mod.num}-${tNum}`;
    const entries = Array.isArray(f.entries) ? f.entries : [];
    const chapter = entries.find((e) => e && e.tag === "chapter");
    if (!chapter) continue;
    const secoes = (Array.isArray(chapter.children) ? chapter.children : [])
      .filter((c) => c && c.tag === "section")
      .map((s) => ({
        id: s.id ?? "",
        num: s.num ?? "",
        titulo: s.title ?? "",
      }));
    temas[key] = {
      url: `aulas/modulo-${mod.nn}/tema-${tt}.html`,
      titulo: chapter.title ?? "",
      secoes,
    };
  }
  return temas;
}

function lerIndiceExistente() {
  if (!existsSync(arqIndice)) return {};
  try {
    const txt = readFileSync(arqIndice, "utf8");
    const m = txt.match(/window\.AULAS\s*=\s*(\{[\s\S]*\})\s*;?\s*$/);
    if (!m) return {};
    const obj = JSON.parse(m[1]);
    return obj && typeof obj === "object" ? obj : {};
  } catch {
    return {};
  }
}

function removerModuloDoIndice(indice, modNum) {
  const prefixo = `${modNum}-`;
  for (const k of Object.keys(indice)) {
    if (k.startsWith(prefixo)) delete indice[k];
  }
}

function ordenarAulas(obj) {
  const ordenado = {};
  const chaves = Object.keys(obj).sort((a, b) => {
    const [ma, ta] = a.split("-").map(Number);
    const [mb, tb] = b.split("-").map(Number);
    if (ma !== mb) return ma - mb;
    if (ta !== tb) return ta - tb;
    return a.localeCompare(b);
  });
  for (const k of chaves) ordenado[k] = obj[k];
  return ordenado;
}

function main() {
  let moduloAlvo;
  try {
    ({ moduloAlvo } = parseArgs(process.argv.slice(2)));
  } catch (err) {
    console.error(err.message);
    process.exit(1);
  }

  const modulos = descobrirModulos();
  if (moduloAlvo !== null && !modulos.some((m) => m.num === moduloAlvo)) {
    console.error(`Módulo ${moduloAlvo} não encontrado (com project.toml) em conteudo/.`);
    process.exit(1);
  }

  const indice = moduloAlvo !== null ? lerIndiceExistente() : {};
  const resumos = [];
  let houveFalha = false;

  for (const mod of modulos) {
    if (moduloAlvo !== null && mod.num !== moduloAlvo) {
      // Releia o outline dos demais sem recompilar; se falhar, mantém o que já estava em indice.js
      try {
        const resOut = rodarDelta(["outline", "--json"], mod.dir);
        const outlineData = resOut.status === 0 ? parseJsonSeguro(resOut.stdout) : null;
        if (outlineData) {
          removerModuloDoIndice(indice, mod.num);
          Object.assign(indice, extrairTemasDoOutline(mod, outlineData));
        }
      } catch {
        // Mantém entradas existentes desse módulo em aulas/indice.js
      }
      continue;
    }

    const resBuild = rodarDelta(["build", "project.toml"], mod.dir);
    const buildOk = resBuild.status === 0;
    if (!buildOk) {
      houveFalha = true;
      if (resBuild.stdout) console.error(resBuild.stdout.trim());
      if (resBuild.stderr) console.error(resBuild.stderr.trim());
    }

    const resLint = rodarDelta(["lint", "--json"], mod.dir);
    const { avisos, erros } = contarLint(resLint.stdout, resLint.status);
    if (erros > 0) {
      houveFalha = true;
      if (resLint.stderr) console.error(resLint.stderr.trim());
    }

    const resOutline = rodarDelta(["outline", "--json"], mod.dir);
    const outlineData = resOutline.status === 0 ? parseJsonSeguro(resOutline.stdout) : null;
    let temasCompilados = 0;
    if (outlineData) {
      removerModuloDoIndice(indice, mod.num);
      const temas = extrairTemasDoOutline(mod, outlineData);
      temasCompilados = Object.keys(temas).length;
      Object.assign(indice, temas);
    } else if (resOutline.status !== 0) {
      houveFalha = true;
      if (resOutline.stderr) console.error(resOutline.stderr.trim());
    }

    resumos.push({
      modulo: mod.nn,
      temas: temasCompilados,
      avisos,
      erros,
      buildOk,
    });
  }

  mkdirSync(dirAulas, { recursive: true });
  const ordenado = ordenarAulas(indice);
  const saida =
    "// Arquivo gerado automaticamente por scripts/compilar-aulas.mjs — não edite à mão.\n" +
    `window.AULAS = ${JSON.stringify(ordenado, null, 2)};\n`;
  writeFileSync(arqIndice, saida, "utf8");

  console.log("=== Resumo da compilação das aulas ===");
  if (resumos.length === 0) {
    console.log("Nenhum módulo encontrado para compilar.");
  } else {
    let totTemas = 0;
    let totAvisos = 0;
    let totErros = 0;
    for (const r of resumos) {
      totTemas += r.temas;
      totAvisos += r.avisos;
      totErros += r.erros;
      const status = !r.buildOk ? "FALHA (build)" : r.erros > 0 ? "FALHA (lint)" : "OK";
      console.log(`Módulo ${r.modulo}: ${r.temas} tema(s), ${r.avisos} aviso(s), ${r.erros} erro(s) [${status}]`);
    }
    console.log(`Total: ${resumos.length} módulo(s), ${totTemas} tema(s) compilado(s), ${totAvisos} aviso(s), ${totErros} erro(s).`);
  }
  console.log(`Índice atualizado: aulas/indice.js (${Object.keys(ordenado).length} aula(s) no total).`);

  if (houveFalha) {
    process.exitCode = 1;
  }
}

main();
