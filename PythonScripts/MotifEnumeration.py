def MotifEnumeration(dna, k, d):
    patterns=[]
    for i in range (0,len(dna[0])-k+1):
        neighbors=Neighbors(dna[0][i:i+k],d)
        for j in neighbors:
            count=0
            for l in dna:
                for i in range(0,len(l)-k+1):
                    if HammingDistance(j, l[i:i+k])<=d:
                        count+=1
                        break
            if count==len(dna):
                patterns.append(j)
    Patterns = [] 
    [Patterns.append(x) for x in patterns if x not in Patterns] 
    Result = ""
    for item in Patterns:
        Result = Result + " " + str(item)
    return Result