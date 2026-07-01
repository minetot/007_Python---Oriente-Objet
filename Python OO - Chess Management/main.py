from datetime import date
from Models import Player, Gender, Match, Tournament, Tournament_list, Ranking_scores

def main():
    player1 = Player("Mineto", "compasanthony@gmail.com", date(1999, 7, 6), "Male")
    player2 = Player("Kirito", "alessio@gmail.com", date(2000, 6, 26),"Male",1400)

# region test player
    print(player1.username)
    print(player1.email)
    print(player1.date_of_birth)
    print(player1.gender.value)
    print(player1.elo)
    print(date.today())
# endregion
    tournament1 = Tournament("WorldWarChess","Tubize","Senior",date(2027, 1, 1))
    manager1 = Tournament_list()
    manager1.add_tounament(tournament1)
    manager1.displayTournament()
if __name__ == "__main__":
    main()