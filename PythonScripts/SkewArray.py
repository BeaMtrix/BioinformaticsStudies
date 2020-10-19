def SkewArray(Genome):
    # your code here
    n=0
    s=[0]
    for i in range(len(Genome)):
        if Genome[i]=="C":
            n-=1
            s.append(n)
        elif Genome[i]=="G":
            n+=1
            s.append(n)
        else:
            n=n
            s.append(n)
    return s