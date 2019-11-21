from classVille import *
from classCapitale import *

Toulouse=Ville("Toulouse")
Strasbourg=Ville("Strasbourg",272975)
Paris=Capitale("Paris","France")
Rome=Capitale("Rome","Italie",2700000)

Paris.set_nbHabitants(input("nombre d'habitant de paris? "))

print("Ville de "+Toulouse.get_nom())
print(Strasbourg)
print(Paris)
print(Rome)
print("Ville de "+ Toulouse.get_nom() +" "+Toulouse.categorie())
print("Ville de "+ Strasbourg.get_nom() +" "+ Strasbourg.categorie())
print("Ville de "+ Paris.get_nom() +" "+ Paris.categorie())