class Elephant:
    
    def elephant_data(self, nom, appetit = 50, satisfaction = 50, en_vie = True, soigneur = None):
        self._nom = nom
        self._appetit = appetit
        self._satisfaction = satisfaction
        self._en_vie = en_vie
        self._soigneur = soigneur
    
    @property
    def elephant_data_display(self):
        if self._en_vie == True:
            return f"L'éléphant {self._nom} est en vie et son Soigneur est {self._soigneur}. \n Son appetit est à {self._appetit} \n Sa satisaction est à {self._satisfaction}"
        return f"L'éléphant {self._nom} est mort"
    
    # Affichage appétit avec un getter
    @property
    def appetit(self):
        """
        L'appétit sur 100.
        Si l'appétit atteint 0 : l'éléphant meurt.
        """
        return f"Appétit de {self._nom} : {self._appetit}"
    
    # Affichage satisfaction avec un getter
    @property
    def satisfaction(self):
        """
        L'satisfaction sur 100.
        Si l'satisfaction atteint 0 : l'éléphant meurt.
        """
        return f"Satisfaction de {self._nom} : {self._satisfaction}"
    
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