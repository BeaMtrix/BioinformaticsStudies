# Insert your Count(Motifs) function here.
def Count(Motifs):
    k = len(Motifs[0])
    count = {'A': [0]*k, 'T' : [0]*k, 'G' : [0]*k, 'C' : [0]*k}
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] +=1
    return count

# Input: A set of kmers Motifs
# Output: A consensus string of Motifs.
def Consensus(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    consensus = ''
    freq_letter = ''
    count = Count(Motifs)
    for j in range(k):
        list = [count['A'][j], count['T'][j], count['C'][j], count['G'][j]]
        list.sort()
        m = list[-1]
        for symbol in 'ACTG':
            if count[symbol][j] == m:
                freq_letter = ''.join(symbol)
        consensus+= freq_letter[0]
    return consensus