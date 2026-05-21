from Models import Elephant, Soigneur, Enclos

def main():
    
    enclos1 = Enclos()
    soigneur1 = Soigneur()
    elephant1 = Elephant()
    elephant2 = Elephant()

    enclos1.enclos_data("Jardin", 10, "Moyen", set())
    soigneur1.soigneur_data("Jack", 1975, 10, set())
    elephant1.elephant_data("Jumbo", 50, 50, True, soigneur1)
    elephant2.elephant_data("Tiérry", 100, 80, True, soigneur1)

    print (elephant2.elephant_data_display)
    print (soigneur1.liste_animaux_responsable_ajout(elephant1))
    print (soigneur1.liste_animaux_responsable_ajout(elephant2))
    print (soigneur1.nourir(elephant1))
    
if __name__ == "__main__":
    main()