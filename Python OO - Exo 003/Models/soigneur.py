import datetime
from Models import Elephant

class Soigneur:
    def __init__(self, nom:str, date_naissance:int, experience:int = 0 , liste_animaux_responsable = set()):
        if not isinstance(liste_animaux_responsable, set): # Ici on s'assure que la liste est un set
            raise TypeError("La liste des animaux doit être un set")
        self._nom = nom
        self._date_naissance = date_naissance
        self._experience = experience
        self._liste_animaux_responsable = liste_animaux_responsable
    
    def liste_animaux_responsable_ajout(self, animal : Elephant):
        self._liste_animaux_responsable.add(animal)
        texte = ""
        for animal in self._liste_animaux_responsable:
            texte += f"- {animal}\n"
        return f"L'animal {animal._nom} est bien sous la charger du dr.{self._nom}\n {texte}\n" 
        
    def liste_animaux_responsable_remove(self, animal : Elephant):
        if animal in self._liste_animaux_responsable:
            self._liste_animaux_responsable.remove(animal)
            return f"L'animal n'est gérer par dr.{self._nom}"
        texte = ""
        for animal in self._liste_animaux_responsable:
            texte += f"- {animal}\n"

        return f"L'animal n'est pas dans la liste \n {texte}\n"
    
    # Defini la méthode pour vérifier les data du GOAT qui soignera l'animal
    @property
    def soigneur_data_display(self):
        return f"Le(a) docteur s'apelle {self._nom}.\n Date de naissance : {self._date_naissance}\n Nombre d'année d'experiance : {self._experience} \n Il est en charge de {len(self._nb_animaux_responsable)} animaux.\n"
    
    # Afficher le nom et le Modifier
    @property
    def nom(self):
        return self._nom
    @nom.setter
    def nom(self, value):
        if not isinstance(value,str):
            raise TypeError("Le nom doit être une chaine")

    @property
    def date_naissance(self):
        return self._date_naissance

    @property
    def experience(self):
        return self._experience
    
    @property
    def age(self):
        if not hasattr(self, '_date_naissance'):
            return 0
        try:
            date_naissance_recup = datetime.strptime(self._date_naissance, "%d/%m/%y")
            date_du_jour = datetime.today()
            age = date_du_jour.year - date_naissance_recup.year - ((date_du_jour.mouth, date_du_jour.day) < (date_naissance_recup.month, date_naissance_recup.day))
        except ValueError:
            return "Date de naissance invalide (format attendu : JJ/MM/AAAA)"

    def nombre_animaux_responsable(self):
        return len(self._liste_animaux_responsable)

    # Action de norir l'animal | On vérifie si il est en vie | si il a faim | l'animal mange
    def nourir(self, animal : Elephant):
        if self != animal._soigneur:
            return f"Le soigneur n'est pas abilité à nourir cet animal"
        elif animal._en_vie == False: # On vérifie que l'animal est en vie
            return f"L'animal {animal._nom} est décédé 🪦\n"
        elif animal._appetit > 100 or animal._satisfaction > 100: # On vérifie que l'animal à faim
            return f"L'animal {animal._nom} est déjà plein et n'a plus envie de manger.\n"
        else: # L'animal mange
            animal._appetit += 30
            animal._satisfaction += 30
            if animal._satisfaction > 100:
                animal._satisfaction = 100
            if animal._appetit > 100:
                animal._appetit = 100
            return f"L'animal {animal._nom} à bien manger et sa satifaction a augumentée.\n"
    
    # Action d'entretenir l'animal ↑ Même chose qu'au dessus   
    def entretenir(self, animal : Elephant):
        if self != animal._soigneur:
            return f"Le soigneur n'est pas abilité à entretenir cet animal"
        elif animal._en_vie == False: # On vérifie que l'animal est en vie
            return f"L'animal {animal._nom} est décédé 🪦\n"
        elif animal._satisfaction >= 100: # On vérifie qu'il ne soit pas déjà satisfait
            return f"L'animal {animal._nom} est déjà satisfait\n"
        else:
            animal._satisfaction +=40
            if animal._satisfaction > 100:
                animal._satisfaction = 100
            return f"l'animal {animal._nom} est bien content"