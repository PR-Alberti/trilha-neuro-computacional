# Relatório do Gestor G1: Fundamentos de Cálculo

Escopo: Módulo 1 (Pré-Cálculo), temas 2 a 5, e Módulo 2 (Cálculo Real), temas 1 a 3. São 7 aulas.

**Situação em 14/11/2026, 18h15.** As 7 aulas existem, compilam com `delta build` e passam no `delta lint` (código de saída 0) nos dois módulos. Todas as figuras foram geradas pelos scripts e conferidas visualmente. Os 7 pareceres estão em `docs/revisao/`.

- **Aprovadas:** 4 aulas (1.2, 1.3, 2.1 e 2.2).
- **Com pendência:** 3 aulas (1.4, 1.5 e 2.3). As ordens de correção já estão escritas, mas não rodaram porque a cota do Gemini acabou: Hydrogen e Flash voltam em cerca de 4h40 (por volta das 22h50) e Argon em 162 h.

## Tabela por tema

| Tema | Estado | Seções | Principais correções feitas | Pendências |
|---|---|---|---|---|
| **1.2 Geometria** (`modulo-01/tema-02.dlt`) | **Aprovado** | Os 3 subtemas do guia. Conteúdo que eu defini para cada um: Introdução (unidades, semelhança e escala em microscopia); Áreas (corte de tecido, soma de áreas celulares em hexágonos, Pitágoras); Relações de ângulos (orientação em V1, Hubel e Wiesel) | Passagem de potências na conversão cm→nm; significado de µm⁻¹ na razão superfície/volume; `alt` da figura encurtado | Nenhuma de conteúdo |
| **1.3 Funções** (`modulo-01/tema-03.dlt`) | **Aprovado** | Os 4 subtemas do guia. Introdução com curva de sintonia gaussiana, sigmoide f-I e equação de Hill; composição estímulo→potencial→taxa; inversa como decodificação; transformações de gráfico. Duas figuras | Pré-requisitos atribuíam "plano cartesiano e distância" à Geometria 1.2 (corrigido); separador `;` nos pares com decimal; unidades em pares e em r₀ | Cosmética: o texto chama o Módulo 9 de "Redes Neurais e Deep Learning", e o nome no guia é "Deep Learning" (ordem `correcao-1-3b.txt` pronta) |
| **1.4 Trigonometria** (`modulo-01/tema-04.dlt`) | **Pendência** (parecer: CORRIGIR) | Os 4 subtemas do guia. Radianos, A·sen(2πft + φ), bandas do EEG, modelo circadiano (cosinor), ângulo visual, arctan da orientação, sintonia de cosseno (Georgopoulos, 1982), soma de senoides. Uma figura | Nenhuma ainda: as duas ordens (Hydrogen e depois Flash) bateram na cota | **Erro factual achado por mim** no `exr:1-4-2-4`: o enunciado diz "voo para o oeste" com o pico passando para as 23 h locais. O correto é **leste**. **Erro factual do parecer:** cita "Álgebra Linear (Módulo 3)", que é o Módulo 5. Pedagógico: `sec` usada sem definição; frase "0 < α, β" ambígua. Ordem: `correcao-1-4.txt` |
| **1.5 Geometria Analítica** (`modulo-01/tema-05.dlt`) | **Pendência leve** (parecer: APROVAR) | Os 3 subtemas do guia. Distância como distância entre padrões de atividade (2 e 3 neurônios); reta I = g(V − E) com o repouso como média ponderada das condutâncias; círculo e campo receptivo centro-periferia. Uma figura (curva I-V) | Nenhuma ainda | Só pedagógicas: lembrar a bomba Na⁺/K⁺ ao falar das correntes de repouso; unidades em I(V) = 4V + 120; distinção entre circunferência e círculo; espaço antes de `</item>`. Ordem: `correcao-1-5.txt` |
| **2.1 Limite** (`modulo-02/tema-01.dlt`) | **Aprovado** | Os 6 subtemas do guia. Limites no infinito e Michaelis–Menten ficaram em Propriedades; continuidade no fim de Limites laterais (degrau do disparo); sen x/x pelo sanduíche. Três figuras (ε-δ, Michaelis–Menten, degrau) | A seção ε-δ não tinha exemplo biológico: virou o controle da taxa de disparo pela corrente, com os mesmos números da figura; legenda explicando a bolinha vazia; Resumo dizia lim 1/x^r = 0 para x→−∞ com r real (restrito a n inteiro); continuidade de quocientes e de tan | Nenhuma |
| **2.2 Derivada** (`modulo-02/tema-02.dlt`) | **Aprovado** | Os 6 subtemas do guia. Abertura com leitura do LIF; ReLU e degrau em derivabilidade; cadeia com sigmoide, gaussiana (melhor discriminação nos flancos) e um quadro "Ponte para o backpropagation"; implícita com Michaelis–Menten e Boyle; exercício-miniatura do projeto final (V(t) polinomial). Duas figuras e um bloco Python | Passagem rK/4 explicitada; marcas dos eixos com vírgula decimal; rótulos das figuras padronizados | Nenhuma |
| **2.3 Integral de Riemann** (`modulo-02/tema-03.dlt`) | **Pendência** (parecer: CORRIGIR) | Os 6 subtemas do guia. Somas de Riemann (figura), carga Q = ∫I dt, BOLD com TR = 2 s, TFC com a carga sináptica, AUC farmacocinética (figura), resposta hemodinâmica simplificada, softplus como primitiva da sigmoide, senoide do EEG. Um bloco Python | Autor havia escrito `&lt;`/`&gt;` dentro da matemática (29 erros de KaTeX). Corrigido por ordem, e o diff confirmou que só os escapes mudaram | **Formato:** `<eqref>` na prosa (linha ~255; o certo é `<ref to=.../>`). Falta "Armadilha comum" na sec 5; termos em inglês; passagem de sinais no TFC; vírgula no rótulo da figura AUC. Ordem: `correcao-2-3.txt` |

## Minha conferência por amostragem

- **Exercícios refeitos (uma seção inteira por aula, ou mais):** 1.2 sec 3; 1.3 sec 3 e exemplos da sec 1; 1.4 sec 2; 1.5 sec 3; 2.1 sec 2; 2.2 sec 4. Todas as contas estão certas, exceto o fato do jet lag na 1.4.
- **Aula 2.3:** conferi as contas-chave AUC = 50 e 43,23; resposta hemodinâmica = 8 e 70/9; Q(τ) = 316 fC.
- **Resumos:** conferi os 7. O único problema foi o lim 1/x^r da 2.1, já corrigido.
- **Código Python:** rodei os blocos da 2.2 (razão incremental) e da 2.3 (somas de Riemann). A saída é idêntica aos comentários.
- **Figuras:** as 11 foram geradas e conferidas em PNG. Os parâmetros batem com o texto (por exemplo, as condutâncias da curva I-V dão repouso de −70,0 mV).

## Decisões técnicas

- **Seções:** todos os temas têm subtemas no guia, e as seções seguem exatamente esses subtemas. Defini o conteúdo de cada "Introdução" e onde entram os tópicos pedidos pelo maestro (ver tabela).
- **Notação:** mantive `\tan` em todo o bloco e recusei a sugestão de trocar por `\operatorname{tg}`, porque o seno usa `\operatorname{sen}` e as funções inversas usam `\arctan`.
- **Sugestões de revisor recusadas:** trocar `<` e `>` por `\lt` e `\gt` dentro da matemática, que já está correto.
- **Módulo 2:** criei `conteudo/modulo-02/project.toml` a partir do modelo.
- **Revisores:** como o autor e o revisor são modelos diferentes (Hydrogen e Flash), os pareceres foram independentes. As correções foram conferidas por mim via diff, sem nova rodada de revisão.
- **Tamanho (pendência para o maestro):** as aulas têm entre 6 500 e 8 000 palavras de prosa, sem contar a matemática. O padrão pede de 2 500 a 5 000, e a piloto tem cerca de 4 550 pela mesma contagem; em bytes, as aulas têm de 1,4 a 2 vezes a piloto. No Módulo 2 (6 subtemas, com 2 exemplos e 3 exercícios por seção) o excesso é quase inevitável. **Não mandei cortar**, para não arriscar regressões em contas já conferidas. Se o maestro quiser, a 1.3 e a 1.4 são as candidatas.

## Como retomar

Quando a cota voltar, rode o script abaixo. Ele aplica `correcao-1-4.txt`, `correcao-2-3.txt`, `correcao-1-5.txt` e `correcao-1-3b.txt`, regera as figuras e compila os dois módulos:

`/tmp/claude-336166952/-home-al-pedro-alberti/50153656-da93-42f3-9736-b244dac32ddb/scratchpad/trilha/gestores/G1/pendentes.sh`

Depois, confira:

- na 1.4, se a palavra "oeste" saiu e o Módulo 5 foi corrigido;
- na 2.3, com `grep -c "<eqref"`, se o resultado é 0.

Ordens, logs e versões anteriores (`versoes/`) estão em `/tmp/claude-336166952/-home-al-pedro-alberti/50153656-da93-42f3-9736-b244dac32ddb/scratchpad/trilha/gestores/G1/`.
