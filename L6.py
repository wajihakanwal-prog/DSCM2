class Cricket:
    def __init__(self, player,score):
        self.__player = player
        self.__score = score
    def info(self):
        print(f"Player name is :{self.player},score:{self.score}")

    def play(self):
        print(f"{self.player} is playing cricket")        
    def get_score(self):
        return self.__score
    def set_score(self,new_score):
        if new_score>=0:
            self.__score = new_score
        else:
            print("Invalid score")
class Football:
    def __init__(self, player,goals):
        self.__player = player
        self.__goals = goals
    def info(self):
        print(f"Player name is :{self.player},goals:{self.goals}")
    def play(self):
        print(f"{self.player} is playing football")
    def get_goals(self):
        return self.__goals
    def set_score(self,new_goals):
        if new_goals>=0:
            self.__goals = new_goals
        else:
            print("Invalid goals")

cricket=Cricket("Virat",100)
football=Football("Messi",50)

for sports in (cricket,football):
    sports.play()
    sports.info()
cricket.__score(100)
football.__goals(50)
    