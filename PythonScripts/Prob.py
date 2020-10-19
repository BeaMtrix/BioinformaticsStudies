def Pr(Text, Profile):
    prob=1.0
    len_text=len(Text)
    for i in range (len_text):
        prob *= Profile[Text[i]][i]
    return prob