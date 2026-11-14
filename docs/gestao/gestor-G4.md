# Relatório do gestor G4: Módulo 8 (Machine Learning)

**Estado em 14/11/2026, 18h15.** O trabalho parou porque a cota de todos os modelos Gemini acabou: Hydrogen, Flash e Argon devolvem `RESOURCE_EXHAUSTED`, com reinício previsto para daqui a cerca de 4h38. Este relatório segue a regra "se tudo esgotar, pare e relate". A cota já tinha acabado uma vez, entre 15h20 e 17h50. Ao todo, 6 das 12 aulas estão aprovadas, 2 estão escritas com pendência e 4 ainda não foram escritas.

`conteudo/modulo-08/project.toml` lista os temas 01 a 07. Com essa lista, `delta build` não mostra erros nem avisos e `delta lint` retorna 0 ("no problems found"). Deixei o tema 08 fora do `inputs` de propósito, porque ele ainda tem erros do KaTeX (veja abaixo). O arquivo `tema-08.dlt` continua na pasta.

## Tabela por tema

| Tema | Estado | Seções definidas pelo gestor | Principais correções | Pendências |
|---|---|---|---|---|
| 8.1 Introdução | **Aprovado** | 1 O que é aprender a partir de dados · 2 Dados, notação e a interface do scikit-learn · 3 Treino × teste: o erro que importa · 4 Viés, variância e sobreajuste | 26 avisos do KaTeX resolvidos (`\operatorname{Viés}` → `\operatorname{\text{Viés}}`). Saídas de 5 blocos de código trocadas pelas reais, e a prosa refeita para combinar: a curva em U de teste ficou 102 → 35 → 67 (antes dizia "centenas"), e o Monte Carlo deu viés² 60/4/0,04 e variância 4,7/6,6/16,5. Três ajustes pedagógicos sugeridos pelo revisor. | — |
| 8.2 Regressão (polinomial) | **Aprovado** | 1 Regressão linear simples · 2 Regressão linear múltipla e mínimos quadrados em forma matricial · 3 Regressão polinomial · 4 Encoding model de um voxel | **Erro factual:** o exemplo da lei de Ohm se dizia "abaixo do limiar", mas tinha potenciais de −42 e −26 mV. Refiz com dados sublimiares (R = 39 MΩ, V_rep = −69,85 mV). Saídas de 6 blocos de código corrigidas. `svg.fonttype` adicionado ao script da figura. Notas sobre Φ e sobre a HRF. | — |
| 8.3 Classificação | **Aprovado** | 1 Regressão logística · 2 KNN · 3 LDA · 4 Decodificação neural (MVPA) | Os 2 blocos de código do exercício de vazamento não rodavam (NameError) e ficaram autocontidos. O MVPA dava 1,000 nos 3 classificadores; agora usa orientações a 10° e janela de 0,1 s (logística 0,82, KNN 0,67, LDA 0,82). A frase "100 % no treino com C grande" era falsa (o real é 0,989). Saídas de 7 blocos corrigidas. Aula enxugada de 5 600 para 4 700 palavras. | — |
| 8.4 Métricas estatísticas | **Aprovado** | 1 Matriz de confusão e acurácia · 2 Precisão, recall, especificidade e F1 · 3 Limiar, curva ROC e AUC · 4 MSE, RMSE, MAE e R² · 5 Classes desbalanceadas | 35 avisos do KaTeX resolvidos (`\mathrm{Acurácia}` etc.). `&amp;` trocado por `&` dentro das matrizes. A simulação de classes desbalanceadas era difícil demais (a logística padrão tinha recall 0); recebeu `class_sep=2.0`. A frase sobre a acurácia "caindo" com τ estava errada. Saídas de 9 blocos corrigidas. Três notas do revisor. Aula enxugada para 4 300 palavras. | — |
| 8.5 Reamostragem | **Aprovado** | 1 Holdout e k-fold · 2 Dados agrupados: LOSO e dependência temporal · 3 Vazamento de dados · 4 Bootstrap · 5 Teste de permutação | O exercício de série temporal com `LinearRegression` não mostrava o efeito (R² de 0,006). Passou a usar `KNeighborsRegressor`: 0,23 com embaralhamento contra −1,17 em blocos. Saídas de 11 blocos corrigidas, com p-valores 0,045 e 0,905. Três notas do revisor. Aula cortada de 6 700 para 4 200 palavras. | — |
| 8.6 Regularização | **Aprovado** | 1 Por que regularizar · 2 Ridge (L2) · 3 Lasso e elastic net · 4 Escolha de λ por CV · 5 Ridge nos encoding models | Saídas de 9 blocos corrigidas, por exemplo a correlação de teste OLS 0,68 contra ridge 0,78 (o texto dizia 0,55 e 0,77). A prosa agora diz que o elastic net deixa entrar 6 variáveis de ruído e que o ridge global empata com o ridge por voxel nesta simulação. Notas do revisor sobre a SVD e a normalização do lasso. | Tamanho no limite (≈ 5 100 palavras na minha contagem, que superestima). |
| 8.7 Estudo de variáveis | **Pendente** | 1 Padronização e escala · 2 Multicolinearidade · 3 Seleção forward, backward e melhor subconjunto · 4 Importância por permutação | Compila sem erro; revisor consultado (veredito APROVAR, 5 sugestões); códigos executados (todos rodam). | Falta rodar a ordem pronta `corr1-tema-07.txt`: as saídas de 8 blocos estão desatualizadas (por exemplo, a prosa diz 80 % de acurácia com vazamento e o real é 65 %), mais as 5 notas do revisor. |
| 8.8 Árvores | **Pendente** | 1 Árvores de decisão · 2 Gini e entropia · 3 Profundidade, poda e sobreajuste · 4 Bagging e random forest | Os códigos rodam e as 2 figuras foram geradas. | **22 erros do KaTeX** (`&gt;` e `&lt;` dentro de `$...$`), por isso a aula está fora do `inputs`. A ordem `corr0-tema-08.txt` (KaTeX e saídas reais de 6 blocos) parou por falta de cota. Depois dela, falta o revisor. |
| 8.9 Aprendizado não supervisionado | **Não escrito** | 1 PCA revisitada · 2 K-means · 3 Agrupamento hierárquico · 4 Como escolher K e validar · 5 Tipos celulares e spike sorting | — | A ordem `ordem-tema-09.txt` está pronta. Sobrou `fig/t09-dendrograma.py` e `.svg` de uma execução interrompida; o próximo autor pode sobrescrever. |
| 8.10 GAMs | **Não escrito** | 1 Funções de base e splines · 2 Suavização · 3 Modelos aditivos generalizados (SplineTransformer + Ridge) · 4 Interpretabilidade: funções parciais | — | Ordem pronta. |
| 8.11 SVM | **Não escrito** | 1 Hiperplanos e margem máxima · 2 Margem suave e C · 3 Kernels · 4 SVM na prática em neurociência | — | Ordem pronta. |
| 8.12 Métodos adicionais | **Não escrito** | 1 Ensembles · 2 Boosting · 3 Stacking · 4 A caixa de ferramentas completa | — | Ordem pronta. |

## Minha conferência pessoal

- **Código:** executei todos os blocos Python das aulas 01 a 08 com `~/.local/share/venv-aulas/bin/python`. Depois das correções, as saídas comentadas das aulas 01 a 06 batem exatamente com a execução. Nenhum bloco usa API obsoleta, e nenhum baixa arquivos.
- **Contas refeitas por mim:**
  - 8.1: seção 3 inteira.
  - 8.2: seções 1 e 2 inteiras.
  - 8.3: LDA (seção 3).
  - 8.4: ROC/AUC, as contas de prevalência e Bayes e os exemplos de desbalanceamento.
  - 8.6: regra de um erro padrão e *soft thresholding*.
  - Resumos de 01, 02, 05 e 06.
  Não encontrei erro de conta. Os erros que achei foram factuais (a lei de Ohm) e saídas de código inventadas pelos autores, já que o Gemini não executa código.
- **Revisores:** todos deram APROVAR e deixaram passar o erro da lei de Ohm, as saídas falsas e os avisos do KaTeX. Por isso a execução do código e a compilação feitas por mim foram indispensáveis.

## Decisões técnicas

- Notação comum do módulo, fixada em todas as ordens: X (n×p), y, β, λ, e a escala exata das funções objetivo de `Ridge`, `Lasso`, `ElasticNet`, `LogisticRegression` e `SVC`.
- Proibi `penalty=` e `multi_class=` em `LogisticRegression`, porque estão obsoletos no sklearn 1.8 ou mais novo.
- Dentro da matemática, palavra com acento só aparece em `\text{}`.
- Blocos de código de exercício também precisam ser autocontidos.
- Em três aulas mudei parâmetros de simulação, testados por mim antes, para que o exemplo didático funcionasse de verdade (MVPA, desbalanceamento, série temporal).

## Para retomar (quando a cota voltar)

As ordens estão em `/tmp/claude-336166952/-home-al-pedro-alberti/50153656-da93-42f3-9736-b244dac32ddb/scratchpad/trilha/gestores/G4/`. Rode-as na ordem abaixo:

1. `corr1-tema-07.txt`
2. `corr0-tema-08.txt`
3. `revisor-tema-08.txt`
4. `ordem-tema-09.txt` a `ordem-tema-12.txt`, cada uma seguida de `revisor-tema-TT.txt`

Em cada tema: compilar, conferir com `ferramentas/conferir.sh TT`, que compila, procura acentos na matemática, conta palavras e compara as saídas do código. Depois, mandar a ordem de correção. Ao final, voltar `tema-08.dlt` (e os seguintes) para o `inputs`.
