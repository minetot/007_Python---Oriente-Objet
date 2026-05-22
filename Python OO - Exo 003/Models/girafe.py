from Models import Animal

class Girafe(Animal):
    
    def definir(self, nom, appetit , satisfaction , en_vie , soigneur , longueur_cou):
        # self._nom = nom
        # self._appetit = appetit
        # self._satisfaction = satisfaction
        # self._en_vie = en_vie
        # self._soigneur = soigneur
        super().definir(nom, appetit, satisfaction, en_vie, soigneur,)
        self._longueur_cou = longueur_cou
        
    # @property
    # def girafe_data_display(self):
    #     if self._en_vie == True:
    #         return f"L'girafe {self._nom} est en vie et son Soigneur est {self._soigneur}. \n Son appetit est à {self._appetit} \n Sa satisaction est à {self._satisfaction}"
    #     return f"L'girafe {self._nom} est mort"
    Animal.animal_data_display()

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
        return f"Le soigneur du girafe est {self._soigneur}"    
    @soigneur.setter
    def soigneur(self, value):
        self._soigneur = value

    def manger_feuilles(self):
        self.appetit += 10
        return f"La girafe à manger des feuilles et son appétit à diminuer"
    
    def boire_eau(self):
        self.satisfaction += 20
        return f"La girafe a bu de l'eau et sa satifaction à augumentée"