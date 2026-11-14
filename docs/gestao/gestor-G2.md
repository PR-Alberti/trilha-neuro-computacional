# Relatório do gestor G2: Matemática dos dados (Módulos 3, 4 e 5)

**Estado em 14/11/2026, 18h20.** O trabalho parou porque a cota de **todos** os modelos
Gemini do `agy` se esgotou. Hydrogen e Flash voltam em cerca de 4h40, por volta das 22h50.
Argon volta só daqui a cerca de 160 h.

- **Prontas:** 7 de 12 aulas, aprovadas e corrigidas: 3.1, 3.2, 3.3, 4.1, 4.3*, 5.1* e 5.2*.
- **Aprovadas sem as correções finais:** 4.2.
- **Escrita mas fora do `project.toml`, por não compilar:** 5.3.
- **Não iniciadas:** 5.4, 5.5 e 5.6. As ordens de escrita já estão prontas.

\* Os itens marcados com asterisco têm pendências indicadas na tabela.

`delta build` e `delta lint` (saída 0) passam nos três módulos, com os `inputs` atuais:

| Módulo | `inputs` |
|---|---|
| 3 | `tema-01.dlt`, `tema-02.dlt`, `tema-03.dlt` |
| 4 | `tema-01.dlt`, `tema-02.dlt`, `tema-03.dlt` |
| 5 | `tema-01.dlt`, `tema-02.dlt` |

Todas as 9 figuras foram geradas pelos scripts em `conteudo/modulo-NN/fig/`. Todos os blocos
Python foram executados com `~/.local/share/venv-aulas/bin/python`, e as saídas batem com os
comentários (com uma exceção na 5.3, listada abaixo).

## Tabela por tema

As contagens de palavras não incluem fórmulas nem código. Por esse critério, a piloto 1.1 tem
cerca de 3 600 palavras.

| Tema | Estado | Seções definidas por mim | Principais correções | Pendências |
|---|---|---|---|---|
| **3.1 Funções vetoriais** | **Aprovado** (revisor: APROVAR) | O guia tem 1 subtema ("Introdução e visualização"). Fiz uma seção com 3 subseções: vetores; funções vetoriais e espaço de estados; limite, derivada, velocidade e comprimento de arco | `f(t)` → `c(t)`, para não confundir com a frequência *f*; unidade (Hz) do comprimento de arco no espaço de estados; velocidade angular na hélice; retirada uma afirmação sobre o conteúdo dos capítulos do livro da Diomara | Nenhuma |
| **3.2 Diferencial em várias variáveis** | **Aprovado** | Os 6 subtemas do guia, na ordem dele. A derivada parcial básica entra na Introdução; a prova de "gradiente = maior subida" fica na seção Derivada direcional, com `<ref>` | Prosa enxugada (de ~5 900 para ~4 200 palavras), sem mexer em contas; 140/13 < √116 explicitado; enunciado do 3-2-4-1 | Nenhuma |
| **3.3 Integrais múltiplas** | **Aprovado** | Os 4 subtemas do guia | Passagem intermediária na integral iterada; alerta contra usar o jacobiano inverso; notação de B e E; raciocínio acrescentado às soluções da seção 4 | Nenhuma. A aula é enxuta (~2 700 palavras), dentro do padrão |
| **4.1 Espaço de variáveis** | **Aprovado** | Configurações como pontos; função custo como paisagem; curvas de nível; ajuste de 2 parâmetros (busca em grade com numpy). Dados: (0,2; 21), (0,4; 27), (0,6; 43), (0,8; 49), com mínimo exato *a* = 50, *b* = 10, *J* = 5 | Cortada de ~6 500 para ~3 900 palavras: saiu 1 exercício por seção e os ids foram renumerados. Também: região viável, Σ1 = *m*, trecho de código autocontido, rótulos da figura | Nenhuma |
| **4.2 Minimização e maximização** | **Aprovado pelo revisor, sem erro matemático. Correções não aplicadas** | Pontos críticos em 1D; pontos críticos em 2D e Hessiana (D = f_xx·f_yy − f_xy², sela); mínimos quadrados (equações normais, mesmos dados da 4.1); Lagrange introdutório | Nenhuma ainda | **Longa demais (~6 800 palavras).** Falta cortar 1 exercício por seção e enxugar a prosa, além de 2 polimentos do parecer. A ordem está pronta em `G2/ordem-correcao-4-2-5-3.txt` |
| **4.3 Métodos computacionais** | **Pronta, mas sem parecer** | Gradiente descendente (numpy); taxa de aprendizado (w_k = (1 − ηc)^k·w₀, 0 < η < 2/c); mínimos locais, global e paisagens de energia (Hopfield 1982, enovelamento, SGD). Responde ao projeto final do módulo | Nenhuma necessária: os 7 blocos de código batem exatamente com as saídas; conferi as duas figuras (curvas de nível com trajetórias de η = 0,10 e η = 0,23; quártica com bacias de atração) e o Resumo | **A revisão Gemini falhou por cota.** Ordem em `G2/ordem-revisao-4-3.txt` |
| **5.1 Vetores, matrizes e operações** | **Aprovado.** Correções aplicadas em parte | Vetores (estado da população); matrizes (X ∈ ℝ^{N×T}, neurônios × tempo); produto matriz-vetor (W_ij = de j para i); produto de matrizes | Nota sobre o princípio de Dale no exemplo da rede linear | Polimentos de `G2/ordem-correcao-m5a.txt` (itens 2 e 3): frase sobre índices da transposta e itens (a)/(b) no exr:5-1-4-3. ~5 300 palavras, aceitável |
| **5.2 Sistemas lineares e transformações** | **Revisor: CORRIGIR**, só por erro de compilação. Nenhum erro matemático | Forma matricial; eliminação de Gauss; matriz como transformação do plano (det 2×2); inversa e mistura de fontes no EEG | **Corrigi à mão** o `$\det &lt; 0$` → `$\det < 0$`. Era a única coisa que impedia o build do módulo; as duas ordens de correção falharam por cota | **Longa demais (~6 600 palavras).** Também faltam a nota de Dale, a nota de unidades do EEG e um espaço sobrando em `</item>`. Itens 4 a 8 de `G2/ordem-correcao-m5a.txt` |
| **5.3 Bases e espaços vetoriais** | **Escrita. Não compila** e está fora do `project.toml` | Espaços e subespaços; span e independência linear; base, dimensão e posto; mudança de base | Nenhuma ainda | 3 erros de KaTeX por `&gt;` dentro da matemática (linhas ~112, 261 e 264); zero negativo na saída de um bloco de código. Faltam a revisão e o acréscimo aos `inputs`. Ordem em `G2/ordem-correcao-4-2-5-3.txt` |
| **5.4 Ortogonalidade** | Não iniciada | Produto interno e ângulo; projeção; bases ortonormais e Gram–Schmidt; mínimos quadrados como projeção (mesmos dados da 4.2) | — | Ordem pronta: `G2/ordem-escrita-5-4.txt` |
| **5.5 Autovalores e autovetores** | Não iniciada | Direções preservadas; cálculo 2×2; estabilidade de x_{t+1} = A·x_t; Markov (convenção por colunas, canal iônico com α/(α+β)) | — | Ordem pronta: `G2/ordem-escrita-5-5.txt` |
| **5.6 Decomposições** | Não iniciada | Diagonalização e teorema espectral; SVD e posto baixo; PCA de população sintética (N = 50, T = 200) com código | — | Ordem pronta: `G2/ordem-escrita-5-6.txt` |

`G2` é a pasta `/tmp/claude-336166952/-home-al-pedro-alberti/50153656-da93-42f3-9736-b244dac32ddb/scratchpad/trilha/gestores/G2`.
Lá estão as ordens, os logs e o `lanca.sh`. O comando é
`lanca.sh <ordem> <nome-do-log> [modelo]`, rodado a partir da raiz do repositório.

## Decisões técnicas

1. **Notação** comum aos Módulos 3 a 5:
   - vetores em `\mathbf` minúsculo;
   - matrizes em `\mathbf` maiúsculo;
   - `\boldsymbol` para gregos;
   - ∇f sem negrito;
   - J(**w**) para o custo e η para a taxa de aprendizado;
   - no Módulo 5, vetores-coluna, X com N neurônios × T instantes, W_ij = sinapse de j para i;
   - cadeia de Markov estocástica por colunas, com p_{t+1} = P·p_t.
2. **Fio condutor dos dados.** O mesmo conjunto de dados atravessa a 4.1 (grade), a 4.2
   (equações normais) e a 4.3 (gradiente descendente). Também está previsto para a 5.4
   (projeção).
3. **Tamanho.** As primeiras aulas do Hydrogen passaram de 6 500 palavras. Por isso:
   - pus um limite rígido na ordem comum;
   - mandei cortar 1 exercício por seção (ficaram 3) e enxugar a prosa, sem tocar nas contas.
4. **Revisor substituto.** Tentei o `gemini-4-argon-high` quando o Flash esgotou, mas ele já
   estava esgotado. Nenhuma aula foi revisada por modelo diferente do Flash.
5. **Correção manual.** Fiz uma só: o `&lt;` na 5.2. O Gemini reincide em pôr `&lt;`/`&gt;`
   dentro de `$…$`, o que quebra o KaTeX. A regra foi reforçada nas ordens pendentes.

## Para retomar (a partir das 22h50)

Mantenha no máximo 3 chamadas ao mesmo tempo.

1. `ordem-correcao-4-2-5-3.txt` e `ordem-correcao-m5a.txt`, no autor Hydrogen.
2. Depois, `ordem-revisao-4-3.txt` e as revisões da 5.3, no Flash.
3. Depois, `ordem-escrita-5-4.txt`, `5-5` e `5-6`, que já incluem a regra de tamanho.
4. Acrescente cada tema aos `inputs` do Módulo 5 só depois de passar no lint.
