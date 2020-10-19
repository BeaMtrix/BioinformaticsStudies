def SkewArray(Genome):
    array = [0]
    Skew = 0
    for i in Genome:
        if i == 'A' or i == 'T':
            Skew += 0
            array.append(Skew)
        if i == 'C':
            Skew -= 1
            array.append(Skew)
        if i == 'G':
            Skew += 1
            array.append(Skew)
    return array

def MinimumSkew(Genome):
    array = SkewArray(Genome)
    positions = []
    count = 0
    minarray = min(array)
    for i in array:
        if i == minarray:
            positions.append(count)
        count +=1
    return positions