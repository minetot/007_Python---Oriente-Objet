from enum import Enum
from .jouable import Jouable
class Genre(Enum):
    POP = "Pop"
    RAP = "Rap"
    ROCK = "Rock"
    JAZZ = "Jazz"

class Chanson(Jouable):
    def __init__(self, titre, artiste, duree, genre : Genre):
        self.titre = titre
        self.artiste = artiste
        self.duree = duree
        self.genre = genre

    def jouer(self):
        print(f"\n La musique {self.titre} est lancée. \n Titre : {self.titre} \n Artiste : {self.artiste} \n Durée : {self.duree}")
        