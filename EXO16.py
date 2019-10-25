while True:

    char1 = input("Quel est le premier mot\n")
    char2 = input("Quel est le deuxieme mot\n")

    if len(char1)!=len(char2):
        print("Veuillez entrer deux mots de meme longueur")
        continue
    else:
        break



def distance_hamming(char1,char2):
    comp = zip(char1, char2)
    difference = 0
    for i1,i2 in comp:
        if i1==i2:
         difference=difference+1

    return difference
difference=distance_hamming(char1,char2)
print("la distance de hamming est de :",difference)



