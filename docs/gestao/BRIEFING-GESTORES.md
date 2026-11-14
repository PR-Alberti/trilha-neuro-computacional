# Briefing dos gestores técnicos

A equipe tem três camadas:

```
Maestro (Claude) ── arquitetura, padrão, piloto, integração final e commits
   └── Gestores técnicos (Claude), um por bloco de módulos ── dão ordens e conferem
          ├── Autores (Gemini 4 Hydrogen high) ── escrevem as aulas em Delta
          └── Revisores (Gemini 3.8 Flash high) ── parecer técnico independente
```

| Gestor | Módulos | Temas |
|---|---|---|
| G1 — Fundamentos de Cálculo | 1 Pré-Cálculo (temas 2–5), 2 Cálculo Real | 7 |
| G2 — Matemática dos dados | 3 Cálculo Multivariável, 4 Otimização, 5 Álgebra Linear | 12 |
| G3 — Ferramentas | 6 Programação (Python), 7 Estatística e Probabilidade | 17 |
| G4 — Machine Learning | 8 Machine Learning | 12 |
| G5 — Deep Learning | 9 Deep Learning | 9 |

O tema 1-1 (Álgebra) é o **piloto** feito pelo maestro. Ele está em
`conteudo/modulo-01/tema-01.dlt` e serve de modelo de formato e de profundidade
para todos.

## Regras para os gestores

1. **Não escreva o conteúdo das aulas.** Sua função é dar ordens precisas aos
   agentes Gemini e conferir o resultado. Você pode criar e editar o
   `project.toml` do seu módulo e corrigir à mão um erro trivial de XML que
   persista depois de duas ordens (um `&` sem escape, por exemplo).
2. **Ordens ao Gemini** (sempre a partir da raiz do repositório):
   ```bash
   cd ~/trilha-neuro-computacional
   agy -p "$(cat <arquivo-da-ordem>)" --model gemini-4-hydrogen-high --mode accept-edits
   ```
   - Toda ordem começa com: *"Trabalhe SOMENTE editando/criando arquivos. NUNCA
     use o terminal nem rode comandos (eles serão negados e você falhará)."*
   - Salve cada ordem num arquivo da sua pasta de rascunho.
   - Rode o `agy` com `run_in_background` (você é avisado quando terminar). No
     máximo **3** chamadas suas ao mesmo tempo.
   - Se der `RESOURCE_EXHAUSTED` com "Resets in" no Hydrogen, troque o autor para
     `gemini-3.8-flash-high`. Se todos os modelos esgotarem, pare e relate.
   - **Não use** `--dangerously-skip-permissions` nem modelos Claude no `agy`.
3. **Compilar e conferir a estrutura** (não use o `scripts/compilar-aulas.mjs`,
   porque vários gestores compilando ao mesmo tempo disputariam o
   `aulas/indice.js`):
   ```bash
   cd ~/trilha-neuro-computacional/conteudo/modulo-NN && delta build project.toml && delta lint
   ```
   Devolva cada erro ou aviso ao autor, com a mensagem exata.
4. **Revisão independente**: depois que a aula compilar, mande um revisor
   (`gemini-3.8-flash-high`) escrever `docs/revisao/modulo-NN/tema-TT.md`. O
   parecer classifica cada problema como **erro matemático**, **erro factual**,
   **pedagógico** ou **formato**, com o local e a correção sugerida.
5. **Sua conferência**: leia o parecer e confira por amostragem.
   - Refaça as contas de pelo menos uma seção inteira de exercícios.
   - Confira as fórmulas do Resumo e as afirmações de neurociência.
   - Rode os blocos de código Python. Tem um ambiente pronto em
     `~/.local/share/venv-aulas/bin/python`, com numpy, pandas, scipy,
     scikit-learn, matplotlib e torch (CPU). Use `MPLBACKEND=Agg`.
   - Depois mande uma ordem de correção ao autor com a lista exata dos
     problemas, e repita até não restar nenhum erro.
6. **Economia**:
   - Não leia os `.html` compilados, que têm cerca de 1 MB cada.
   - Leia os `.dlt` por trechos (`grep -n`, `sed -n`).
   - Confie no lint para a estrutura e gaste sua atenção em contas, soluções,
     código e fatos.
7. **Git**: não faça commit nem mude branch. O maestro integra e versiona.
8. **Relatório final** em `docs/gestao/gestor-GN.md`, com uma tabela por tema:
   - estado (aprovado ou com pendência);
   - seções definidas por você, quando o guia não tinha subtemas;
   - principais correções feitas;
   - pendências.

   Termine respondendo ao maestro com um resumo de, no máximo, 15 linhas.

## O que vai em cada ordem de escrita

- O caminho do arquivo (`conteudo/modulo-NN/tema-TT.dlt`) e o id do capítulo
  (`tema-M-T`).
- Os campos do tema no `MODS` do `index.html`: nome, `d`, `t` (subtemas) e `lv`.
  Também os campos do módulo: `title`, `bio`, `mats`, `drill` e `final`.
- Os temas anterior e seguinte, para dar continuidade.
- As seções a cobrir: os subtemas do guia ou, se o guia não tiver, as que você
  definir (de 3 a 5, com o conteúdo esperado de cada uma).
- Leitura obrigatória: `docs/PADRAO-AULAS.md`, `docs/DELTA-COLA.md` e a aula
  piloto `conteudo/modulo-01/tema-01.dlt`, como modelo.
- Exigências específicas do tema: que exemplos de biologia usar e quais
  armadilhas conceituais cobrir.

## Ordem padrão do revisor (adapte só o caminho)

> Trabalhe SOMENTE editando/criando arquivos. NUNCA use o terminal nem rode comandos
> (eles serão negados e você falhará).
>
> Você é um revisor técnico rigoroso, ao mesmo tempo matemático, neurocientista
> computacional e professor de alunos de Biologia. Leia `docs/PADRAO-AULAS.md`,
> `docs/DELTA-COLA.md` e a aula `conteudo/modulo-NN/tema-TT.dlt`. **Não edite a
> aula.** Escreva `docs/revisao/modulo-NN/tema-TT.md` com:
>
> 1. **Veredito**: APROVAR ou CORRIGIR.
> 2. **Tabela de problemas**, com as colunas:
>    - severidade: erro matemático, erro factual, pedagógico ou formato;
>    - local: seção, id e linha aproximada;
>    - trecho;
>    - correção sugerida.
>
> Refaça **todas** as contas dos exemplos e das soluções dos exercícios. Confira
> também:
> - se cada exercício tem dica e solução completa;
> - se cada seção tem pelo menos um exemplo biológico;
> - se as afirmações de neurociência são de livro-texto;
> - se algum conceito é usado antes de ser apresentado;
> - se o código Python roda como está;
> - se a notação é consistente;
> - se a aula cobre todos os subtemas pedidos;
> - se o tamanho está dentro do padrão.
