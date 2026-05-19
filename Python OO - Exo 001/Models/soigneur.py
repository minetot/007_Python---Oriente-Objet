from Models import Elephant

class Soigneur: 
    def caracteristique_soigneur(self, nom, date_naissance, experience, nb_animaux_responsable):
        self.nom = nom
        self.date_naissance = date_naissance
        self.experience = experience
        self.nb_animaux_responsable = nb_animaux_responsable

    def nourir_animal(self, elephant : Elephant):
        if elephant.appetit < 60 :
            elephant.manger()
            print (f"{self.nom} à nouri l'animale")

        else : 
            print (f"L'éléphant {elephant.nom} n'a pas encore faim")


    def entretenir(self, elephant : Elephant):
        if elephant.satisfaction < 50 :
            elephant.entretenu()
            print (f"{self.nom} à entretenu {elephant.nom}")
        else :
            print ("sybau")