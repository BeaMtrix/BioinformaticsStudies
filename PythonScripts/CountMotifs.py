#Input: A set of k-mers Motifs
#Output: Count(Motifs)
def Count(Motifs):
	count = {"A":[],
		 "C":[],
		 "T":[],
		 "G":[]}
	k = len(Motifs[0])
    	for symbol in "ACGT":
        	count[symbol] = []
        for j in range(k):
             count[symbol].append(0)
	t = len(Motifs)
    	for i in range(t):
        	for j in range(k):
            		symbol = Motifs[i][j]
           		count[symbol][j] += 1

returns count