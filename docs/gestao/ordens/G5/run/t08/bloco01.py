
from collections import Counter

vocab = {
    tuple("neuronio"): 4,
    tuple("neuronal"): 3,
    tuple("neural"): 2,
}


def contar_pares(v):
    pares = Counter()
    for tokens, freq in v.items():
        for i in range(len(tokens) - 1):
            pares[(tokens[i], tokens[i + 1])] += freq
    return pares


def fundir_par(v, par):
    novo_vocab = {}
    fusao = par[0] + par[1]
    for tokens, freq in v.items():
        novos = []
        i = 0
        while i < len(tokens):
            if i < len(tokens) - 1 and (tokens[i], tokens[i + 1]) == par:
                novos.append(fusao)
                i += 2
            else:
                novos.append(tokens[i])
                i += 1
        novo_vocab[tuple(novos)] = freq
    return novo_vocab


for passo in range(1, 4):
    pares = contar_pares(vocab)
    # Desempate determinístico: maior frequência e menor par em ordem alfabética
    melhor = min(pares, key=lambda p: (-pares[p], p))
    print(f"Passo {passo}: {melhor} -> '{melhor[0] + melhor[1]}' (freq={pares[melhor]})")
    vocab = fundir_par(vocab, melhor)

print("Tokens finais:", [list(t) for t in vocab])
# Saída exata:
# Passo 1: ('e', 'u') -> 'eu' (freq=9)
# Passo 2: ('eu', 'r') -> 'eur' (freq=9)
# Passo 3: ('n', 'eur') -> 'neur' (freq=9)
# Tokens finais: [['neur', 'o', 'n', 'i', 'o'], ['neur', 'o', 'n', 'a', 'l'], ['neur', 'a', 'l']]
      