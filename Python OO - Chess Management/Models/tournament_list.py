from .tournament import Tournament

class Tournament_list:
    def __init__(self):
        self.__tournamentList = set()
    
    @property
    def tournamentList(self):
        return self.__tournamentList
    
    def add_tounament(self, tournament : Tournament):
        print (f"{tournament.name} Est ajouter à la liste.")
        self.__tournamentList.add(tournament)
        
    def displayTournament(self):
        for tournament in self.__tournamentList:
            print(f"Name : {tournament.name}\n Location : {tournament.location} \n Number of registrant : {len(tournament.list_player)}\n Categories : {tournament.category}\n Status : {tournament.status.value}\n Registration Deadline : {tournament.registration_deadline}")
