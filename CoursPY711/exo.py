class Voiture:
    def __init__(self,marque,immat="XX 000 XX",misecircuit="01-01-1970"):
        self.immat= immat
        self.misecircuit= misecircuit
        self.marque = marque

    def __str__(self):
        return "Voiture"+self.marque

    def get_immat(self):
        return self.immat

    def get_misecircuit(self):
        return self.misecircuit

    def get_marque(self):
        return self.marque

    def set_immat(self,new_immat):
        self.immat= new_immat

    def set_misecircuit(self,new_circuit):
        self.misecircuit= new_circuit
    
    def set_marque(self,new_marque):
        self.marque= new_marque

    def IsCollection(self,misecircuit):
        date= misecircuit.split("-")
        if date[2] < 1999:
            return("C'est une voiture de collection")
        else:
            return("Ce n'est pas une voiture de collection")

v1=Voiture("Renault","BQ 950 HT","13-05-1997")
v2=Voiture("BMW")

print(v1.get_marque() ,v1.get_misecircuit() ,v1.get_immat(),v1.IsCollection)
print(v2.get_marque(),v2.get_misecircuit() ,v2.get_immat(),v2.IsCollection )

v2.set_immat(input("Entrer l'immat:"))
v2.set_misecircuit(input("Entrer la mise en circu:"))     

print(v2.get_marque(),v2.get_misecircuit() ,v2.get_immat(),v2.IsCollection )

print(v1)
