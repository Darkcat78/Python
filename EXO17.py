etr1 = input("Entrer un mot\n")
r_etr1= etr1[::-1]

def palindrome(etr1,r_etr1):

    return etr1 == r_etr1
   
if palindrome(etr1,r_etr1) is True:
    print("Le mot",etr1,"est un palindrome !")
    
else:
    print("Dommage ce n'est pas un palindrome")


