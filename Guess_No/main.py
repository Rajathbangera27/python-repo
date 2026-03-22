import random

class GuessANumber:
    
    def play_game(self):
        system_number = random.randint(1, 10)
        
        user_guess = int(input("Guess a number between 1 and 10: "))
        
        if user_guess == system_number:
            print("User guess is right")
        else:
            print("User guess is wrong")
            print("The correct number was:", system_number)

game = GuessANumber()
game.play_game()
#PR