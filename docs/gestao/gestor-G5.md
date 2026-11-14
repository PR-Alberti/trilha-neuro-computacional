# Relatório do gestor G5: Módulo 9 (Deep Learning)

Data: 14/11/2026. Branch `aulas-delta`. O trabalho parou porque a cota das duas famílias Gemini acabou: as respostas foram `RESOURCE_EXHAUSTED`, com "Resets in ~4h38m" às 18h25, tanto no Hydrogen quanto no Flash. As ordens que faltam rodar já estão escritas na pasta de rascunho do G5 (veja "Como retomar").

## Situação geral

- **Arquivos.** As 9 aulas estão em `conteudo/modulo-09/tema-01.dlt` … `tema-09.dlt`, e há 9 scripts de figura em `conteudo/modulo-09/fig/tTT-*.py`, cada um com o seu `.svg` gerado.
- **Projeto.** O `project.toml` lista os 9 temas. `delta build project.toml` termina **sem erro e sem aviso**, e `delta lint` sai com **0**. A saída está em `aulas/modulo-09/`. Não rodei `scripts/compilar-aulas.mjs`.
- **Tamanho.** Todas as aulas têm entre 3800 e 4840 palavras de prosa: o código não entra na conta e cada fórmula conta como 1 palavra. As versões originais de 9.2, 9.3, 9.5 e 9.6 tinham de 6600 a 8000 palavras e foram enxugadas por ordem minha. A partir do 9.7, a ordem de escrita já trazia o limite de 5000 palavras como regra obrigatória.
- **Código.** Executei cada bloco Python isoladamente com `~/.local/share/venv-aulas/bin/python`, limitado a 2 threads para imitar o Colab. Todos rodam em CPU entre 0,2 e 16 s.
  - Os comentários de saída esperada que tinham sido inventados foram trocados pelas saídas reais.
  - **Exceção: o GAN do 9.7.** Esse comentário continua sem corresponder à saída real; veja a pendência na tabela.
- **Revisor.**
  - Os temas 9.1, 9.2, 9.3, 9.4 e 9.7 receberam parecer do Flash em `docs/revisao/modulo-09/`, todos com veredito **APROVAR**, só com observações pedagógicas.
  - Os temas 9.5, 9.6, 9.8 e 9.9 **ficaram sem parecer** por causa da cota.

## Tabela por tema

| Tema | Estado | Seções definidas pelo gestor | Principais correções | Pendências |
|---|---|---|---|---|
| 9.1 Fundamentos | **Aprovado** | (1) Do neurônio biológico ao artificial; (2) Redes multicamadas e funções de perda; (3) Backpropagation pela regra da cadeia; (4) Treinando de verdade: SGD, Adam e um MLP em PyTorch | Saídas reais nos comentários do MLP em `load_digits` (acurácia ≈ 0,967) e do *weight decay*; enunciado do exr:9-1-3-4 corrigido (6 camadas, 5 fatores φ′); 3 ajustes pedagógicos do parecer. Conferi todas as contas das seções 1, 3 e 4, o backprop numérico, Adam e momento, e o Resumo. | — |
| 9.2 CNN | **Aprovado** | (1) Convolução em 1D e 2D; (2) Filtros como campos receptivos; (3) Uma CNN pequena em PyTorch; (4) CNNs como modelos do córtex visual | Enxugada de 8011 para 4388 palavras; `-&gt;` dentro do código (dava SyntaxError); 3 erros KaTeX (`&gt;`/`&lt;` e "ª" dentro da matemática); saídas reais (R² do ridge 0,49 e não "0,70–0,85"; curva de sintonia de Gabor); comparação CNN × MLP corrigida (acurácia equivalente, ≈ 96 %, com menos parâmetros). Conferi os exercícios da seção 1 e todo o código. | Ajustes pedagógicos do parecer: separador de milhar na tabela, `.detach()`, frase "modelo sem intercepto" no ridge 1D. A ordem está pronta (lote C) e não foi executada por falta de cota. |
| 9.3 RNN | **Aprovado** | (1) Estado oculto e recorrência; (2) Retropropagação no tempo e o gradiente que some; (3) LSTM e GRU; (4) RNNs como modelos de dinâmica cortical | Enxugada de 7843 para 4297 palavras; 10 erros KaTeX (`&lt;`/`&gt;` dentro da matemática); saídas reais do integrador GRU (0,930 contra teto teórico Φ(1,398) ≈ 0,919, explicado como flutuação amostral) e da tarefa com atraso. Conferi a LSTM à mão (c₁ = 1,1119, h₁ = 0,5883), o exemplo de Mante (autovalor 1 ao longo de v₁), 0,5²⁰ e 1,5²⁰, e a contagem de parâmetros da LSTM e da GRU. | Ajustes pedagógicos do parecer (índice Euler × RNN, variante do `nn.GRU`, decimais intermediários). Lote C. |
| 9.4 Representações | **Aprovado** | (1) Embeddings: de símbolos a vetores; (2) Espaço latente e autoencoders; (3) Medindo semelhança: cosseno, distância e correlação; (4) RSA: comparando modelos e cérebros | Erro KaTeX; o Spearman da RSA dizia "0,55–0,75" e o valor real é 0,86 (0,78 sem a diagonal e 0,84 com ela); a acurácia do MLP foi rotulada como **de treino**. Conferi os exercícios da seção 3 e o código. | Três frases pedagógicas do parecer. Lote C. |
| 9.5 Transformers | Compila; **falta o revisor** | (1) Atenção: consultas, chaves e valores; (2) Autoatenção, várias cabeças e máscara causal; (3) Posição e o bloco Transformer; (4) Transformers na ciência: LLMs, AlphaFold e o cérebro | Enxugada de 6606 para 4379 palavras; saídas reais (acurácia 0,985). Conferi a atenção à mão (3 tokens, d_k = 2, que bate com o NumPy e com o PyTorch), a fórmula 4d² + 4d = 16 640 e o Resumo. | Parecer do revisor e correções que vierem dele. |
| 9.6 GNN | Compila; **falta o revisor** | (1) Grafos e a matriz de adjacência; (2) Troca de mensagens entre vizinhos; (3) Uma camada GCN em PyTorch; (4) GNNs na biologia e na neurociência | Enxugada de 7553 para 4370 palavras; o comentário sobre *oversmoothing* estava inventado (0,34 → 0,04) e o real é 0,354 → 0,155; GCN ≈ 97 % contra MLP ≈ 71 %. Conferi a figura (A, graus), A², a equivariância e o Resumo. | Parecer do revisor e correções. |
| 9.7 Generativos | Revisor APROVAR; **com pendência** | Seções do guia: VAE, GAN, Diffusion (com a subseção "Do cérebro à imagem") | Saídas reais do VAE e da difusão; legenda da figura (o `\mathcal{N}` não aparecia). Conferi o Resumo, a KL (μ = 1, σ = 0,5 → 0,8181), D* = 0,75 e os valores de ᾱ_t. | **GAN**: com ruído de 1 dimensão, o desvio gerado varia de 0,65 a 1,26 conforme a semente e o número de threads, e o comentário atual ("entre 1,0 e 1,6") não confere. Testei e passei ao autor uma configuração estável: z ∈ ℝ⁸, lr = 1e-3, 4000 passos, o que dá desvio de 1,19 a 1,22 em 3 sementes e ~15 s. Lote C, junto com 2 ajustes do parecer (letra z reaproveitada no DDPM, arredondamento da KL). |
| 9.8 LLM | Compila; **falta o revisor** | (1) Tokenização: do texto aos números; (2) Pré-treino: prever o próximo token; (3) Ajuste fino e alinhamento; (4) Embeddings semânticos e o cérebro | Saídas reais (perplexidade de 18 para ≈ 4,05; acurácia da cabeça congelada 0,88; correlações do modelo de codificação). Conferi o BPE à mão contra o código (desempate alfabético), o LoRA (16 777 216 contra 65 536) e o Resumo (Huth et al., 2016, com embedding de coocorrência e não LLM). | Parecer do revisor e correções. |
| 9.9 Reinforcement Learning | Compila; **falta o revisor** | (1) Agente, ambiente e recompensa; (2) Valor e a equação de Bellman; (3) Aprendizado por diferença temporal e dopamina; (4) Q-learning e um mundo em grade | 8 erros KaTeX corrigidos. Conferi Rescorla–Wagner (0,3; 0,51; 0,657), Bellman na cadeia (V(A) = 0,9), o TD com a dopamina (δ migra para o estímulo e vale −1 na omissão) e o Q-learning (Q* = γ⁵ ≈ 0,590, caminho de 6 passos). Todo o código confere. | Parecer do revisor e correções. |

## Decisões técnicas e desvios

- **Limite de tamanho.** Apliquei o limite de 5000 palavras do contrato. As aulas cortadas passaram a ter 2 exemplos e 3 exercícios por seção (Básico, Intermediário e Avançado).
- **Threads da CPU.** Rodei o código com 2 threads (`OMP_NUM_THREADS=2`). Com as 32 threads da máquina, o GAN levou 188 s e deu resultados diferentes. Num Colab com 2 núcleos o tempo cai para cerca de 15 s.
- **Modelos usados.** Os temas 9.7 a 9.9 e os lotes de correção foram feitos pelo Hydrogen depois que a cota voltou. Os pareceres foram escritos pelo Flash. Quando o Flash esgotou, tentei o Hydrogen como revisor, mas ele também estava sem cota.
- **Correções manuais.** Não fiz nenhuma. Os erros recorrentes de `&lt;`/`&gt;` dentro de `$...$` foram todos corrigidos pelo autor, em lote.

## Como retomar (depois que a cota voltar)

As ordens estão em `/tmp/claude-336166952/-home-al-pedro-alberti/50153656-da93-42f3-9736-b244dac32ddb/scratchpad/trilha/gestores/G5/`.

1. `ordem-lote-c.txt` (Hydrogen): conserta o GAN do 9.7 e aplica os ajustes pedagógicos dos temas 9.2, 9.3, 9.4 e 9.7.
2. `ordem-revisor-05.txt`, `-06`, `-08` e `-09` (Flash): os quatro pareceres que faltam.
3. Uma ordem de correção em lote com os erros apontados nesses pareceres, seguida de `delta build project.toml && delta lint` em `conteudo/modulo-09/`.
4. Rodar de novo `tools/rodar_codigo.py tema-07.dlt <saida>` para confirmar a saída do GAN.
