class Player:
    def play(self):
        print("(Inside Player class): ")
        print("The player is playing cricket.")

class Batsman(Player):
    def play(self):
      print("(Inside Batsman class): ")  
      print("The batsman is batting. \n")

class Bowler(Player):
    def play(self):
        print("(Inside Bowler class): ")
        print("The bowler is bowling. \n")

#main
batsman = Batsman()
bowler = Bowler()
batsman.play()
bowler.play()
