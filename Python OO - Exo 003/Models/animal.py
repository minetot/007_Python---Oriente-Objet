from Models import Soigneur
from abc import ABC, abstractmethod

class Animal(ABC):
    # def definir(self, nom, appetit = 50, satisfaction = 50, en_vie = True, soigneur = None):
    #     if not isinstance(self._en_vie , bool):
    #         raise TypeError ("Le parametre en_vie, doit être une bolean")
        
    #     self._nom = nom
    #     self._appetit = appetit
    #     self._satisfaction = satisfaction
    #     self._en_vie = en_vie
    #     self._soigneur = soigneur

    #@abstractmethod
    def __init__(self:str, nom:str, appetit:int, satisfaction:int, en_vie:bool, soigneur:Soigneur):
        self._nom = nom
        self._appetit = appetit
        self._satisfaction = satisfaction
        self._en_vie = en_vie
        self._soigneur = soigneur

    #@abstractmethod
    @property
    def animal_data_display(self):
        if self._en_vie == True:
            return f"Animal - Nom : {self._nom}\n Appetit : {self._appetit}/100 \n Satfaction : {self._satisfaction}/100 \n En Vie : {self._en_vie} \n Soigneur {self._soigneur} \n"
        return f"L'animal {self._nom} est mort"
    
    
    @property
    def nom(self):
        return self._nom
    
    
    @nom.setter
    def nom(self, value):
        if not isinstance(value,str):
            raise TypeError("Le nom doit être une chaine") 
        self._nom = value
    
    
    @property
    def appetit(self):
        return self._appetit
    
    
    @property
    def satisfaction(self):
        return self._satisfaction
    
    
    @property
    def en_vie(self):
        return self._en_vie
    
    
    @property
    def soigneur(self):
        return self._soigneur.nom
    @soigneur.getter
    def soigneur(self, value):
        self._soigneur = value
    
    #@abstractmethod
    # def probabilite_deces(self):
    #     proba = 10
    #     return 
    
    @abstractmethod
    def observer_environement(self):
        pass
    
    @abstractmethod
    def faire_bruit(self):
        pass