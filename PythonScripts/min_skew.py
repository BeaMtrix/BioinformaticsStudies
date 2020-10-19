def MinSkew(Genome):
    min_skew=[]
    Skew=[0]
    n=0
    m=0
    for i in range(len(Genome)):
        if Genome[i]=="C":
            n-=1
            Skew.append(n)
            
        elif Genome[i]=="G":
            n+=1
            Skew.append(n)

        else:
            n=n
            Skew.append(n)  
    
    m= min(Skew)
    for i in range(len(Skew)):
        if Skew[i]<=m:
            min_skew.append(i)
    print (Skew)
    print (m)
     
    return (min_skew)