class Ville:

    def __init__(self,nom,nbHabitants=0):
        self.nom= nom.upper()
        self.nbHabitants= nbHabitants
        

    def __str__(self):
        return self.nom + ", Nombre d'habitants :" +str(self.nbHabitants)+ " "+self.categorie()

    def get_nom(self):
        return self.nom

    def get_nbHabitants(self):
        return self.nbHabitants

    def set_nbHabitants(self,new_nbHabitants):
        if int(new_nbHabitants)>0:
            self.nbHabitants= new_nbHabitants
        else:
            self.nbHabitants= 0

    def nbHabitantsConnu(self):         #Savoir si le nb Habitants est connu
        if self.nbHabitants>0:
            return True
        else:
            return False

    
    def categorie(self):
        if self.nbHabitantsConnu() == True:

            if self.nbHabitants < 500000:
                return "Catégorie A"
            elif self.nbHabitants >= 500000:
                return "Catégorie B"
        else:
            return "Catégorie ?"