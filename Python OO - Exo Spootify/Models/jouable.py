from abc import ABC, abstractmethod

class Jouable(ABC):

    @abstractmethod
    def jouer(self):
        pass