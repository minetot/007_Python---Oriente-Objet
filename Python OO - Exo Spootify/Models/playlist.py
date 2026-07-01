
class Playlist():
    def __init__(self, nom):
        self.nom = nom
        self.__pistes = []

    @property
    def pistes(self):
        nom_piste = []
        
        return nom_piste
    
    def ajouter_piste(self, chanson):
        self.pistes.append(chanson)
        print(f"\nLa piste {chanson.titre} est ajouter à la playliste. \n")

    def lire_playlist(self, chanson):
        if self.pistes.len() != 0 :
            for i, self.pistes in enumerate(self.pistes):
                print(f" {i} : {chanson.titre}")
        else :
            print("La playlist est vide")

    def filtrer_par_genre(self, chanson):
        # playlist_order_by_genre = sorted(self.pistes, jouable.)
        # return 
        pass