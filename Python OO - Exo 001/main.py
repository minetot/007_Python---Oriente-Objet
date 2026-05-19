from Models import Elephant, Soigneur, Enclos
import random

def main():
    elephant1 = Elephant()
    soigneur1 = Soigneur()
    enclos1 = Enclos()

    soigneur1.caracteristique_soigneur("Juju", 2000, 3 , 42)
    elephant1.caracteristique_elepant("Jumbo", random.randint(0, 100), random.randint(0, 100), True, "Juju")
    enclos1.caracteristique_enclos("La Ferme en Folie", 40, 20, elephant1.caracteristique_elepant)
    

    soigneur1.nourir_animal(elephant1)
    soigneur1.entretenir(elephant1)

if __name__ == "__main__":
    main()