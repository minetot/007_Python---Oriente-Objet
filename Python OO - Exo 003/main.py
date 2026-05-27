from Models import Elephant, Soigneur, Enclos, Animal, Tools

def main():
    Tools.Clear_console()
    enclos1 = Enclos("Jardin", 10, "Moyen", set())
    soigneur1 = Soigneur("Jack", 1975, 10, set())
    elephant1 = Elephant("Jumbo", 50, 50, True, soigneur1,10)
    elephant2 = Elephant("Tiérry", 100, 80, True, soigneur1,10)

    # enclos1.definir("Jardin", 10, "Moyen", set())
    # soigneur1.definir("Jack", 1975, 10, set())
    # elephant1.definir("Jumbo", 50, 50, True, soigneur1)
    # elephant2.definir("Tiérry", 100, 80, True, soigneur1)

    #print(elephant2.elephant_data_display)
    print(soigneur1.liste_animaux_responsable_ajout(elephant1))
    print(soigneur1.liste_animaux_responsable_ajout(elephant2))
    print(soigneur1.nourir(elephant1))
    print(soigneur1.entretenir(elephant2))
    print(elephant1.soigneur)

    print(enclos1.capacite_max)
    
    # def afficher_bruit(animal):
    #     print(animal.faire_bruit())
    # afficher_bruit(elephant1)
if __name__ == "__main__":
    main()