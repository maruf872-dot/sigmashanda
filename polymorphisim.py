class Cricket:
    def __init__(self, player, score):
      self.__player = player
      self.__score = score
    def info(self):
       print(f"Cricket - Player: {self.__player}, Score: {self.__score}")
    def play(self):
       print(f"{self.__player} hits a six!")
    def get_score(self):
       return self.__score
    def set_score(self, new_score):
       if  new_score > 0:
          self.__score = new_score
          print(f"Score Updated to {self.__score}")
       else:
          print("Score must be positive, not negative.")
class Football:
    def __init__(self, player, score):
       self.__player = player
       self.__score = score
    def info(self):
       print(f"Football - player: {self.__player}, Score {self.__score}")
    def play(self):
       print(f"{self.__player} scores a goal!")
    def get_score(self):
         return self.__score
    def set_score(self, new_score):
         if new_score > 0:
            self.__score = new_score
            print(f"Score Updated to {self.__score}")
         else:
            print("Score must be positive, not negative.")
cricket = Cricket("Kabirnath", 46)
football = Football("Rahimnath", 3)

print("=== Cricket Scoreboard === \n")
for sport in (cricket, football):
   sport.info()
   sport.play()

print(" --- Direct Change Attemp --- ")
cricket.__score = 999
print(f"get_score() still shows: {cricket.get_score} ")

print(" \n--- Updating Scores --- ")
cricket.set_score(123)
football.set_score(10)

