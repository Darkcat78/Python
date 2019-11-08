class Film:
    def __init__(self,titre,sorite,numero,cout,recette,Liste=[]):
        self.titre = titre
        self.sortie = sorite
        self.numero = numero
        self.cout = cout
        self.recette = recette
        self.Liste = Liste

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

    


class Acteur:
    def __init__(self,nom,prenom,ListeP=[]):
        self.nom= nom
        self.prenom=prenom
        self.ListeP=ListeP

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
        nbPersonnage=len(ListeP).__str__()
        return "Nombre de personnage :"+ nbPersonnage


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
ListeP = [Personnage1.get_nom()+Personnage1.get_prenom(),Personnage2.get_prenom()+Personnage2.get_nom()] 

#Données de la liste Acteur
A1= Acteur("Mayhew","Peter ",ListeP)
A2= Acteur("Ford","Harrison ")
A3= Acteur("Hamil","Mark ")

Liste = [A1.get_prenom() + A1.get_nom(),",",A2.get_prenom() + A2.get_nom(),",",A3.get_prenom() + A3.get_nom()]




#Run de la classe Film
Film1= Film("Le reveil de la force","2015","Episode VII","100millions €","200millions €",Liste)
print(Film1)
print(A1)
print(A1.nbPersonnage())

"""Film2 = Film(input("Titre "),input("Annee de sortie "),input("Numero "),input("cout "),input("recette "))
print("Star Wars",Film2.get_titre(),Film2.get_numero(),Film2.get_sortie(),"A couté :",Film2.get_cout(),"et a rapporté : ",Film2.get_recette())"""



