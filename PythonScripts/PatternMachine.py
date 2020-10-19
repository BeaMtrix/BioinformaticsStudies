#--Obtendo a sequência reversa ao seguimento--#
def reverse(pattern):
    reverse = (" ") #string vazia
    a=len(pattern)
    for i in range(a):
        base = pattern[i]
        reverse = str(base)+reverse
        i-=1
    return reverse
    
#--Obtendo a fita complementar ao seguimento--# 
def Complement(pattern):
    complement = ("")
    a = len(pattern)
    for i in range(a):
        base = pattern[i]
        if base == "A":
            complement = complement + "U"
            i+=1
        if base == "U":
            complement = complement + "A"
            i+=1
        if base == "C":
            complement = complement + "G"
            i+=1
        if base == "G":
            complement = complement + "C"
            i+=1
        
    return complement
    
#--Mostra todas as posições iniciais da região procurada no seguimento--# 
def PatternMatching(pattern,gen):
    posicoes = []
    for i in range(len(gen)-len(pattern)+1):
        if pattern == gen[i:i+len(pattern)]:
            posicoes.append(i)
    return posicoes
    
#--Obtem a fitacomplementar reversa do seguimento proposto--#    
def ReverseComplement(pattern):
    pattern = reverse(pattern)
    pattern = Complement(pattern)
    return pattern
    
bace1_local= "AAAUCCAUCAAGGCAGCCUCC"#região de interação entre bace1 e bace1-as

#--Sequencia do lncRNA--#
bace1_as="GGCUCACCGCAACCUCCACCGUCCUGAGUUAAAGUGAUUCUCCUGUCUCAGCCCCCUGAGUAGCUAGGAUUACAGGCGUGCGCCACCACACCCAGCUAAUUUUUGUACUUUUAGUAGAGAUGGGAUUUCACCCUGUUGGUCAGGCUGGUCUUGAACUCCUGACCUAGUGAUCUGCCCACCUUGGCCUCCCAAAGUGCUGGGAUUACAGGCGUGAGCCACCACGCCUGGCUAGGGGAAGAGUGUUUUAAGAGCUCUGAGUAGAAGGGUCUAAGUGCAGACAUCUUGGCUGUUGCUGAAGAAUGUGACUCUCACCGCCUCCCUCUGACACUGUACCAUCUCUUUUACCCCCAUCCUUAGUCCACUCACGGAGGAGGCUGCCUUGAUGGAUUUGACUGCAGCUUCAAACACUUUCUUGGGCAAACGAAGGUUGGUGGUGCCACUGUCCACAAUGCUCUUGUCAUAGUUGUACUAAGAGGGAAAAGAGAGAGUUAAAAGAGUCAAAAGGUUUUUGAUGCUGGGCUCUGGGCAGUAGGGGGUUACUGCUGGGGCCCCAGCUGGGUUGGCAUCUUGGCUUUGGCACCUCCUAAGUGUACCUGCUUGGACAAGUUAACCUCUGUGCCUCAGUUCCUUCAUCUCUAAAGUGAGGAUAAAAAUAGCACCUACCUCAAAGGGUUAUUGUAAGGAUUAAAUAAAUCAGCAAUGUAAAGCACUUAGAAUCGUGCCCAGCAGAGAGAAGGCACUUGGUAAAUGUUUAUUCUUGUUAAUCUUGGGUGGGCAGGUAGUCUCCAAACUUGAAAAUAAAAAUACCUUGUUUAGUGCUUUUAAAAAAAAAAAAAAAAA"
print ("BACE1-AS possui: " + len(bace1_as)+ " nucleotídeos")

bace1_as_local = ReverseComplement(bace1_local)

#--Ponto inicial onde o seguimento buscado inicia--#
print (PatternMatching(bace1_as_local,bace1_as))