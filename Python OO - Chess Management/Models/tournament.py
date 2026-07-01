import uuid
from datetime import date
from enum import Enum
from .player import Player

class Category(Enum):
    JUNIOR = "Junior"
    SENIOR = "Senior"
    VETERAN = "Veterant"

class Status(Enum):
    WAITING_FOR_PLAYERS = "Waiting for players"
    IN_PROGRESS = "In progress"
    COMPLETED = "Completed"

class Tournament:
# region Contrusteur
    def __init__(self, name: str, location: str, category: str, registration_deadline : date, nb_players_min: int = 2, nb_players_max: int = 64 , bool_woman_only: bool = False,):
        
        #parametre avec comportement
        self.__status = Status.WAITING_FOR_PLAYERS
        self.__tournament_id = str(uuid.uuid4())
        self.__list_player = set()
        self.__current_round_number = 0
        
        # parametre du constructeur
        self.name = name
        self.location = location
        self.category = category
        self.registration_deadline = registration_deadline
        self.nb_players_min = nb_players_min
        self.nb_players_max = nb_players_max
        self.__elo_min = int
        self.__elo_max = int
        self.__bool_woman_only = bool_woman_only
# endregion

# region Getter Setter
    #NAME
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        if self.__status != Status.WAITING_FOR_PLAYERS:
            raise ValueError("Il est impossible de modifier le nom du tournois si il a commencé")
        self.__name = value
    #LOCATION
    @property
    def location(self):
        return self.__location
    @location.setter
    def location(self, value):
        if self.__status != Status.WAITING_FOR_PLAYERS:
            raise ValueError("Il est impossible de changer la localistion du tounois si il a commencé.")
        self.__location = value
    #CATEGORY
    @property
    def category(self):
        return self.__category
    @category.setter
    def category(self, value):
        if self.__status != Status.WAITING_FOR_PLAYERS:
            raise ValueError("Il est impossible de changer la catégorie du tounois si il a commencé.")
        try:
            self.__category = Category(value)
        except ValueError:
            raise ValueError("Category = Junior, Senior, Veteran")
    #STATUS
    @property
    def status(self):
        return self.__status

    #registration_deadline
    @property
    def registration_deadline(self):
        return self.__registration_deadline
    @registration_deadline.setter
    def registration_deadline(self, value):
        if not isinstance(value, date):
            raise TypeError("La date doit être un objet date")
        if value < date.today():
            raise ValueError("La date limite ne doit pas être dans le passé")
        self.__registration_deadline = value

    @property
    def nb_players_min(self):
        return self.__nb_players_min
    @nb_players_min.setter
    def nb_players_min(self, value):
        
        if not value >= 2 and value <= 64 :
            raise ValueError("Valeur entre 2 et 64")
        if self.__status != Status.WAITING_FOR_PLAYERS:
            raise ValueError("Il est impossible de changer le nb_player du tounois si il a commencé.")
        
        self.__nb_players_min = value

    @property
    def nb_players_max(self):
        return self.__nb_players_max
    @nb_players_max.setter
    def nb_players_max(self, value):
        if not value >= 2 and value <= 64 :
            raise ValueError("Valeur entre 2 et 64")
        if self.__status != Status.WAITING_FOR_PLAYERS:
            raise ValueError("Il est impossible de changer le nb_player du tounois si il a commencé.")
        if value < self.__nb_players_min:
            raise ValueError("Joueur max doit être plus grand que Joueur min")
        self.__nb_players_max = value
        
    @property
    def elo_min(self):
        return self.__elo_min
    @elo_min.setter
    def elo_min(self, value):
        if value < 0 or value > 3000:
            raise ValueError("Le elo doit se trouver entre 0 et 3000")
        if not self.__current_round_number == 0:
            raise ValueError("Il est impossible de changer le elo_min du tounois si il a commencé.")
        self.__elo_min = value
    
    @property
    def elo_max(self):
        return self.__elo_max
    @elo_max.setter
    def elo_max(self, value):
        if not value in range(1,3000):
            raise ValueError("Le elo doit se trouver entre 0 et 3000")
        if not self.__current_round_number == 0:
            raise ValueError("Il est impossible de changer le elo_max du tounois si il a commencé.")
        if value < self.__elo_min:
            raise ValueError("ELO max doit être plus grand que ELO min")
        self.__elo_max = value

    @property
    def bool_woman_only(self):
        return self.__bool_woman_only
    
    @property
    def tournament_id(self):
        return self.__tournament_id
    
    @property
    def list_player(self):
        return self.__list_player
    
# endregion
    @staticmethod
    def __check_age(player, category):
        age = player.get_age()  # on calcule l'âge du joueur
        
        if category == Category.JUNIOR and age >= 18:
            raise ValueError("Joueur trop âgé pour la catégorie Junior")
        if category == Category.SENIOR and not (18 <= age < 60):
            raise ValueError("Joueur doit avoir entre 18 et 60 ans pour Senior")
        if category == Category.VETERAN and age < 60:
            raise ValueError("Joueur trop jeune pour la catégorie Veteran")

    # Adding player to my player list 
    def add_player(self, player : Player):
        
        self.__check_age(player, self.__category)
        
        if self.__nb_players_max < len(self.__list_player):
            raise ValueError("Nombre maximum de participant atteint")
        if self.__registration_deadline < date.today():
            raise ValueError("La deadline d'inscription est passée")
        if not self.__status == "Waiting for players":
            raise ValueError("On ne peux plus inscrire de personne car le tournois à commencer ou est fini.")
        if self.__bool_woman_only == True and player.gender.value == "Male":
            raise ValueError("Seul les femmes peuvent être ajouter à ce tournois")
        if not self.__elo_min < player.elo:
            raise ValueError("Score Elo : trop bas")
        if not self.__elo_max > player.elo:
            raise ValueError("Score Elo : trop haut")

        self.__list_player.add(player)

    # Remove player to my player list 
    def remove_player(self, player : Player):
        if self.__registration_deadline < date.today():
            raise ValueError("La deadline d'inscription est passée")
        if not self.__status == "Waiting for players":
            raise ValueError("On ne peux supprimer de player car le tournois à commencer ou est fini.")
        self.__list_player.remove(player)