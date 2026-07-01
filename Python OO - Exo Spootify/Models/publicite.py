from .jouable import Jouable

class Publicite(Jouable):
    def __init__(self, marque, duree):
        self.marque = marque
        self.duree = duree

    def jouer(self):
        print(f"\n La publicité de {self.marque} est lancée. \n Durée : {self.duree}")
        return 