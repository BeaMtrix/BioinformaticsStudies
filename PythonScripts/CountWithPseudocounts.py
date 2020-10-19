def CountWithPseudocounts(Motifs):
    t = len(Motifs)#quantidade de strings na lista 
    k = len(Motifs[0])#Tamanho das strings(motivos)
    count = {} #Inicia o dicionário da lista
    for symbol in "ACGT":
    count[symbol] = []#Coloca cada letra no dicionário
        for j in range(k):
            count[symbol].append(1)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count