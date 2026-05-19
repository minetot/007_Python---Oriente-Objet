from Models import Elephant

class Enclos : 
    def caracteristique_enclos(self, nom, capacite_max, taille, liste_animaux):
        self.nom = nom
        self.capacite_max = capacite_max
        self.taille = taille
        self.liste_animaux = liste_animaux
    
    def ajouter_animal(self, elephant : Elephant):
        self.liste_animaux.append(elephant)
        print (f"L'animal {elephant.nom} à été ajouté")

    def enleve_animal(self, elephant : Elephant):
        self.liste_animaux.remove(elephant)
        print (f"L'animal {Elephant.nom} a été retiré")

    def aficher_animaux(self):
        print (self.liste_animaux)