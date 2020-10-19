def Motifs(Profile, Dna):
    lst=[]
    k=4
    for elements in Dna:
        lst.append(ProfileMostProbableKmer(elements, k , Profile))
    return lst

def Pr(Text, Profile):
    prob=1.0
    len_text=len(Text)
    for i in range (len_text):
        prob *= Profile[Text[i]][i]
    return prob

def ProfileMostProbableKmer(text, k, profile):
    len_text=len(text)
    k_mer=text[0:k]
    prob=0.0
    for i in range (len_text - k + 1):
        prob1=Pr(text[i:i+k],profile)
        if prob1>prob:
            prob=prob1
            k_mer=text[i:i+k]
    return k_mer