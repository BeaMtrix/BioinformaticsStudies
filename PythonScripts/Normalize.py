def Normalize(P):

    d = {}
    for k,v in P.items():
        d[k] = P[k]/sum(P.values())
    return d

d = {'A': 0.1, 'C': 0.1, 'G': 0.1, 'T': 0.1}