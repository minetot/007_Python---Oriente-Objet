from Models import Animal

class Elephant(Animal):
    
    def definir(self, nom, appetit, satisfaction, en_vie, soigneur, longueur_defense):
        # self._nom = nom
        # self._appetit = appetit
        # self._satisfaction = satisfaction
        # self._en_vie = en_vie
        # self._soigneur = soigneur
        super().definir(nom, appetit, satisfaction, en_vie, soigneur,)
        self._longueur_defense = longueur_defense
    
    @property
    def elephant_data_display(self):
        if self._en_vie == True:
            return f"L'éléphant {self._nom} est en vie et son Soigneur est {self._soigneur}. \n Son appetit est à {self._appetit} \n Sa satisaction est à {self._satisfaction}"
        return f"L'éléphant {self._nom} est mort"
    
    # Affiche du nom
    @property
    def nom(self):
        return f"Le nom de l'animal est : {self.nom}\n"
    # Setter sur le nom
    @nom.setter
    def nom(self, value):
        if not isinstance(value,str):
            raise TypeError("Le nom doit être une chaine") 

    # Affichage appétit avec un getter
    @property
    def appetit(self):
        """
        L'appétit sur 100.
        Si l'appétit atteint 0 : l'éléphant meurt.
        """
        if self._appetit > 100:
            self._appetit = 100
        elif self._appetit < 1:
            self._appetit = 1
            self._en_vie = False
        return f"Appétit de {self._nom} : {self._appetit}"
    
    # Affichage satisfaction avec un getter
    @property
    def satisfaction(self):
        """
        L'satisfaction sur 100.
        Si l'satisfaction atteint 0 : l'éléphant meurt.
        """
        if self._satisfaction > 100:
            self._satisfaction = 100
        elif self._satisfaction < 1:
            self._satisfaction = 1
            self._en_vie = False
        return f"Satisfaction de {self._nom} : {self._satisfaction}"
    
    # Afficher si l'animal est en vie
    @property
    def en_vie(self):
        if not isinstance(self._en_vie , bool):
            raise TypeError ("Le parametre en_vie, doit être une bolean")
        elif self._en_vie == True: return f"{self._nom} est en vie."
        return f"{self._nom} est décédé."

    # Etablire le soigneur
    @property
    def soigneur(self):
        return f"Le soigneur de l'éléphant est {self._soigneur}"
    @soigneur.setter
    def soigneur(self, value):
        self._soigneur = value
    
    # Afficher la longueur des défense
    @property
    def longueur_defense(self):
        return self._longueur_defense
    @longueur_defense.setter
    def longueur_defense(self, value):
        self._longueur_defense = value

    # Capaciter à manger (se lance automatiquement) | vérifie si l'animal est en vie | si il a faim ou pas | mange augumenter son appétit et sa satifaction
    def manger(self):
        if self._en_vie == False:
            return f"L'éléphant {self._nom} est mort"
        
        elif self._appetit >= 100:
            return f"{self._nom} refuse de manger car il est plein. \n"
        
        elif self._appetit < 50:
            self._appetit += 10
            self._satisfaction += 10
            return f"{self._nom} à un peu manger au arbre \n Appetit : {self._appetit} \n Satisfaction : {self._satisfaction}\n"
        return f"L'éléphant n'a rien fait."
    
    def prendre_bain_de_boue(self):
        self.satisfaction += 20
        return f"L'éléphant à jouer dans la boue et sa satisfaction à augumenter"

    def aspirer_eau(self):
        self.satisfaction += 20
        return f"L'éléphant à aspirer de l'eau et sa satisfaction à augumenter"