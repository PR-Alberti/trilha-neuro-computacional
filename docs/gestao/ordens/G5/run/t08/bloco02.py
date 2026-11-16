
def codificar(palavra, fusoes):
    tokens = list(palavra)
    for a, b in fusoes:
        novos, i = [], 0
        while i < len(tokens):
            if i < len(tokens) - 1 and tokens[i] == a and tokens[i + 1] == b:
                novos.append(a + b)
                i += 2
            else:
                novos.append(tokens[i])
                i += 1
        tokens = novos
    return tokens

fusoes = [("e", "u"), ("eu", "r"), ("n", "eur"), ("neur", "o")]
print(codificar("neurose", fusoes))  # ['neuro', 's', 'e']
          