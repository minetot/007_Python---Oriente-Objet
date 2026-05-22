from Models import Elephant

class Enclos:
    """
        - nom : Nom de l'enclo
        - capacite_max : Nombre d'animaux
        - taille : Petit | Moyen | Grand 
        - liste_animaux : Obligatoirement un set
    """
    def definir(self, nom , capacite_max = 15, taille = "Moyen", liste_animaux = set()):
        if not isinstance(liste_animaux, set): # Ici on s'assure que la liste est un set
                raise TypeError("La liste des animaux doit être un set")
        self._nom = nom
        self._capacite_max = capacite_max
        self._taille = taille
        self._liste_animaux = liste_animaux

    @property
    def enclo_data_display(self):
        return f"L'enclo s'appele : {self._nom} \n Capacité Totale : {self._capacite_max} \n Taille : {self._taille} \n Nombre d'animaux dans l'enclo {len.self._liste_animaux}\n"
    
    # Ajours Getter + Setter
    @property
    def nom(self):
        return self._nom
    @nom.setter
    def nom(self, value):
        if not isinstance(value,str):
            raise TypeError("Le nom doit être une chaine")

    @property    
    def capacite_max(self):
        return self._capacite_max
    @capacite_max.setter
    def capacite_max(self, value):
        if not isinstance(value,int) or value < 1:
            raise TypeError("la capaciter max doit être un entier positif")
    
    @property    
    def taille(self):
        return self._taille
    
    @property    
    def liste_animaux(self):
        return self._liste_animaux
    
    # On essaye d'ajouter un animal à l'enclo
    def enclo_ajout(self, animal : Elephant):
        self._liste_animaux.add(animal)
        texte = ""
        for animal in self._liste_animaux_responsable:
            texte += f"- {animal}\n"
        return f"L'animal {animal._nom} est bien dans l'enclos \n {texte}\n" 

    # On essaye de retirer un animal
    def liste_animaux_remove(self, animal : Elephant):
        if animal in self._liste_animaux:
            self._liste_animaux.remove(animal)
        texte = ""
        for animal in self._liste_animaux_responsable:
            texte += f"- {animal}\n"
            return f"L'animal n'est plus dans l'enclos {self._nom}.\n {texte}\n"
        texte = ""
        for animal in self._liste_animaux_responsable:
            texte += f"- {animal}\n"
        return f"L'animal n'est pas dans la liste \n {texte}\n"
    
    # On décide d'afficher la liste des animau
    def liste_animaux_affichage(self, animal : Elephant):
        if len.liste_animaux > 1:
            texte = ""
            for animal in self._liste_animaux_responsable:
                texte += f"- {animal}\n"
            return texte