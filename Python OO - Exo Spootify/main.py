"""
- Créer une énumération de Genre avec au moins 3 genres

- Créer une première class "jouable" avec méthode abstraite "jouer() pour jouer les "piste"

- plusieur class contrètes qui héritent de Jouable :
    Chanson
    Podcast
    Publicite
Chaque class doit re-définir jouer() pour adapté

- Faut faire l'encapsulation, gérer les trucs __privé mettre les getters et setters

Méthodes à implémenter

- ajouter_piste(piste)
- lire_playlist()
- filtrer_par_genre(genre)
- duree_totale()
"""
from Models import Jouable, Chanson, Genre, Podcast, Publicite, Playlist

def main():
    chanson1 = Chanson("Chicago","MJ",3,Genre.POP.value)
    chanson2 = Chanson("Alter Ego","Doechi",2,Genre.RAP.value)
    playlist1 = Playlist("Ma Playlist")

    chanson1.jouer()

    playlist1.ajouter_piste(chanson1)
    playlist1.ajouter_piste(chanson2)
    print(playlist1.nom)
    print(playlist1.pistes)
    #print(playlist1.lire_playlist)
    

if __name__ == "__main__":
    main()