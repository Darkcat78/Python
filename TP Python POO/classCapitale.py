from classVille import *

class Capitale(Ville):
    def __init__(self,nom,nomPays,nbHabitants=0):       #On remet les valeurs de la classe Ville
        super().__init__(nom,nbHabitants)               #On appelle la classe Ville et on remet les valeurs
        self.nomPays= nomPays.upper()

    def __str__(self):
        return self.nom +", Nombre d'habitants :" +str(self.nbHabitants) +", Capitale de :"+self.nomPays +" "+ self.categorie()

    def get_nomPays(self):
        return self.nomPays

    def set_nomPays(self,new_nomPays):
        self.nomPays= new_nomPays

    def categorie(self):
            return "Catégorie C"

    


