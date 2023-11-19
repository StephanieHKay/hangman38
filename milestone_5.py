import random

class Hangman:
    def __init__(self,word_list, num_lives=5):
        #list of words that word will be randomly selected
        self.word_list = word_list
        #numof lives a player has
        self.num_lives = num_lives
        #chose a random word to play game with
        self.word =random.choice(self.word_list)
        #list of letters guessed(letter) and not guessed(_)
        self.word_guessed = ["_" for item in self.word]
        # unique letters in word
        self.unique_letters_in_word = set(self.word)
        self.num_letters = len(self.unique_letters_in_word)
        #list of guesses made so far
        self.list_of_guesses = []

    #check whether guess is in word
    def check_guess(self,guess):
        guess = guess.lower()        
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            #if guess in word, change _ to letter, and reduce list no of unique letter letters yet to be guessed
            for letter in self.word:
                if guess== letter:
                    count= self.word.count(guess)
                    #add correctly guessed letter to word list one or more times
                    guess_word_pos = self.word.index(letter)
                    self.word_guessed[guess_word_pos] = guess                    
                    for i in range(count-1):
                        guess_word_pos = self.word.index(letter, guess_word_pos+1)
                        self.word_guessed[guess_word_pos] = guess

            self.unique_letters_in_word.remove(guess)
            self.num_letters= len(self.unique_letters_in_word)
            print(self.word_guessed)            
        #if guess not in word, reduce lives left and tell player        
        else:
            self.num_lives-=1
            print(f"Sorry {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
    
    #get guess from user, make sure guess is valid
    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break
    #win or lose, play again?
    def play_again(self):
         while True:
                 replay = input("Play again? Y/N ").upper()      
                 if replay == "Y":
                     play_game (self.word_list)
                 elif replay == "N":
                     exit()
                 else:
                     print("Invalid answer, replay? ")
                

def play_game(word_list):
    game = Hangman(word_list, num_lives=5)

    while True:
        if game.num_lives >0 and game.num_letters ==0:
            print("Congratulations. You won the game!")
            game.play_again()
           
        elif game.num_lives >0:
            game.ask_for_input()
        elif game.num_lives == 0:
            print("Sorry, you have lost! ")
            game.play_again()
                

game_fruit_list = ["apple", "mango", "grape", "avocado", "blueberry"]         
    
play_game (game_fruit_list)
