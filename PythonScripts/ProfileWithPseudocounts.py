def ProfileWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    cont=CountWithPseudocounts(Motifs)#numero de aparições de cada letra(A,C,T e G)
    for i in range(k):
        su=0
        for symbol in "ACGT":
            su=su+cont[symbol][i]
        for symbol in "ACGT":
            cont[symbol][i] = cont[symbol][i]/su #porcentagem de cada letra(total de aparições/todas)
    profile=cont
    return profile