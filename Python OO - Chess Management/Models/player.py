import re 
from datetime import date
from enum import Enum
# region Enum gender
class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"
# endregion

class Player:

# region Constructor
    def __init__(self, username: str, email: str, date_of_birth: date, gender: Gender, elo: int = 1200):
        
        self.username = username
        self.email = email
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.elo = elo
# endregion

# region Getter Setter Parametre
    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, value):
        self.__username = value

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, value):
        if not re.match(r"[^@]+@[^@]+\.[^@]+",value):
            raise ValueError("Email invalide")
        self.__email = value

    @property
    def date_of_birth(self):
        return self.__date_of_birth
    @date_of_birth.setter
    def date_of_birth(self, value):
        if not isinstance(value, date):
            raise ValueError("Date invalide\nDD/MM/YYYY")
        self.__date_of_birth = value
    
    @property
    def gender(self):
        return self.__gender
    @gender.setter
    def gender(self, value):
        try:
            self.__gender = Gender(value)
        except ValueError:
            raise ValueError("Genre invalide\nMale\nFemale\nOther")

    @property
    def elo(self):
        return self.__elo
    @elo.setter
    def elo(self, value):
        if not isinstance(value, int):
            raise TypeError("Elo : Entier positif")
        if value < 0 and value > 3000:
            raise ValueError("Elo entre 0 et 3000")
        self.__elo = value
# endregion

# region methode
    def get_age(self):
        today = date.today()
        age = today.year - self.__date_of_birth.year
        if today < date(today.year, self.__date_of_birth.month,self.__date_of_birth.day):
            age -= 1 # Anniveraire pas encore passé
        return age
# endregion