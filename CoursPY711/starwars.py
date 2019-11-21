class Film:
    def __init__(self,titre,sortie,numero,cout,recette,Liste=[],ListeP=[]):
        self.titre = titre
        self.sortie = sortie
        self.numero = numero
        self.cout = cout
        self.recette = recette
        self.Liste = Liste
        self.ListeP=ListeP

    def listetostr(self):
        tmp=""   
        for i in self.Liste:
            tmp=tmp+i.__str__()+" " #Liste -> acteurs donc i -> acteurs, i.__str__ appelle __str__ de la classe acteur
        return "|Acteurs :"+tmp

    def __str__(self):
        return "Star Wars " + self.numero+" "+ self.titre+" "+self.listetostr()

    def get_titre(self):
        return self.titre
    
    def get_sortie(self):
        return self.sortie

    def get_numero(self):
        return self.numero
    
    def get_cout(self):
        return self.cout

    def get_recette(self):
        return self.recette

    def get_Liste(self):
        return self.Liste

    def get_ListeP(self):
        return self.ListeP
    
    def set_titre(self,n_titre):
        self.titre=n_titre

    def set_sortie(self,n_sortie):
        self.sortie=n_sortie

    def set_numero(self,n_numero):
        self.numero=n_numero

    def set_cout(self,n_cout):
        self.cout=n_cout
    
    def set_recette(self,n_recette):
        self.recette=n_recette

    def set_Liste(self, n_liste):
        self.Liste=n_liste
    def set_ListeP(self, n_listeP):
        self.ListeP= n_listeP

    #Question 11

    def nbActeurs(self):
        return len(self.Liste)

    def nbPersonnage(self):
        return len(self.ListeP)

    def calculBenef(self):
        calcul= self.recette - self.cout

        if calcul >= 0:
            return [True,calcul]
        else:
            return [False,calcul]

    def isBefore(self,annee):
        if annee > self.sortie:
            return True
        else:
            return False

    #Question 12

    def triActeur(self):
        self.Liste = sorted(self.Liste, key = lambda Acteur: Acteur.prenom)
    


class Acteur:
    def __init__(self,nom,prenom,ListeP=[]):
        self.nom = nom
        self.prenom = prenom
        self.ListeP = ListeP

    def listePtoSTR(self):
        tmp=""
        for i in self.ListeP:
            tmp=tmp+i.__str__()+""
        return tmp

    
    def __str__(self):
        return self.nom + self.prenom + self.listePtoSTR()

    def get_nom(self):
        return self.nom

    def get_ListeP(self):
        return self.ListeP
    
    def get_prenom(self):
        return self.prenom       

    def set_nom(self,n_nom):
        self.nom=n_nom

    def set_prenom(self,n_prenom):
        self.prenom=n_prenom

    def nbPersonnage(self):
        nbPersonnage=len(self.ListeP)
        return "Nombre de personnage :"+ str(nbPersonnage)


class Personnage:
    def __init__(self,nom,prenom):
        self.nom = nom
        self.prenom = prenom

    def __str__(self):
        return self.nom + self.prenom

    def get_nom(self):
        return self.nom

    def get_prenom(self):
        return self.prenom

    def set_nom(self,n_nom):
        self.nom=n_nom

    def set_prenom(self,n_prenom):
        self.prenom=n_prenom




#Données de la classe Personnage
Personnage1= Personnage("Skywalker","Luke ")
Personnage2= Personnage("Chewbacca","")
Personnage3= Personnage("Vador","Dark")
ListeP = [Personnage1,Personnage2,Personnage3] 

#Données de la liste Acteur
A1= Acteur("Mayhew","Peter ",ListeP)
A2= Acteur("Ford","Harrison ")
A3= Acteur("Hamil","Mark ")

Liste = [A1,A2,A3]




#Run de la classe Film
Film1= Film("Le reveil de la force",2015,"Episode VII",100,200,Liste,ListeP)
print(Film1)
print(A1)
print(A1.nbPersonnage())

#Tri des Acteurs

Film1.triActeur()

#Collection
collectionPerso=[Personnage1,Personnage2,Personnage3]

Film1.set_ListeP(collectionPerso)
Film1.get_ListeP()
test=Film1.calculBenef()


#Test Benefice
if test[0]:
    print("Le film a été un grand succes: "+ str(test[1])+ "Millions")
else:
    print("Le film a été un échec: "+ str(test[1])+ "Millions")

#Test isBefore
annee= int(input("Année? : "))

if Film1.isBefore(annee):
    print("Ce film est sortie avant"+ str(annee))
else:
    print("Ce film est sortie apres " + str(annee))



"""Film2 = Film(input("Titre "),input("Annee de sortie "),input("Numero "),input("cout "),input("recette "))
print("Star Wars",Film2.get_titre(),Film2.get_numero(),Film2.get_sortie(),"A couté :",Film2.get_cout(),"et a rapporté : ",Film2.get_recette())"""

def makeBackUp(dico):
    for objet in dico:
        print("makeBackup\n")
        print("Année : " + str(dico[objet].get_sortie()))
        print("Titre : " + dico[objet].get_titre())
        print("Bénéfice : " + str(dico[objet].calculBenef()))
        print()


dico = {Film1.get_sortie:Film1}

makeBackUp(dico)