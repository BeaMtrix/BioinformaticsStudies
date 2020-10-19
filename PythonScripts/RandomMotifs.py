import random

def RandomMotifs(Dna, k, t):
    t = len(Dna)
    l = len(Dna[0])
    RandomMotif =[]
    for i in range(t):
        r = random.randint(1,l-k) 
        RandomMotif.append(Dna[i][r:r+k])
    return RandomMotif