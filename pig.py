import random

print("Lets Play PIG! ")
print("Ready, its your turn. ")
print("type roll to begin, and type stay to stop turn. ")

class Game:
    def __init__(self):
        self.command = ""
        self.turns = 0
        self.total_score = 0
        self.turn_score = 0
    def play_game(self): 
        while self.total_score <= 100:
            print("turn: {} score: {} in {} turns.".format(self.turn_score, self.total_score, self.turns))
            command = input("command> ").lower()

            if command == "roll":
                roll = random.randint (1,6)
                if roll == 1:
                    print("you rolled a pig! no points haha." )
                    self.turn_score = 0 
                    self.turns = self.turns + 1
                else: 
                    self.turn_score = self.turn_score + roll 
            elif command == "stay":
                print ("your turn is over.")
                self.total_score = self.total_score + self.turn_score
                self.turn_score = 0 
                self.turns = self.turns + 1
            elif command == "quit":
                print ("better luck next time!")
        print ("final score: {} in {} turns ({})".format(self.total_score, self.turns, self.total_score/self.turns))
        
        if self.total_score >= 100:
            winner = input("YOU WIN!")
            with open("scoreboard.txt", "W") as f:
                f.write("{}//{}//{}\n".format(winner, self.turns, self.total_score))
game = Game()
game.play_game()


