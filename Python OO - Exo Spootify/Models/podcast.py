from .jouable import Jouable

class Podcast(Jouable):
    def __init__(self,titre,animateur,duree):
        self.titre = titre
        self.animateur = animateur
        self.duree = duree

    def jouer(self):
        print(f"\n Le podcast {self.titre} est lancée. \n Animateur : {self.animateur} \n Durée : {self.duree}")
        return 