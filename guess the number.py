import random
class NumberGuessingGame:
    def __init__(self):
        self.LOWER = 1
        self.HIGHER = 100
    def get_random_number(self):
        return random.randint(self.LOWER, self.HIGHER)
    def start(self):
        random_number = self.get_random_number()
        print(
            f"Guess the randomly generated number from {self.LOWER} to {self.HIGHER}")
        chances = 0
        while True:
            user_number = int(input("\n\n\n\n\n\n\n\nEnter your guess: "))
            if user_number == random_number:
                print(
                    f"Well done, You got it in {chances + 1} guess{'es' if chances > 1 else''}!")
                break
            elif user_number < random_number:
                print(f"Your number is LESS than the random number ({user_number} < the random number)")
            else:
                print(f"Your number is GREATER than the random number ({user_number} > the random number)")
            chances += 1
numberGuessingGame = NumberGuessingGame()
numberGuessingGame.start()