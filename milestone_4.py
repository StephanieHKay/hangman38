import random

class Hangman:
    def __init__(self,word_list, num_lives=5):
        #list of words that word will be randomly selected
        self.word_list = word_list
        #num_of_games
        self.num_lives = num_lives
        #chose a random word to play game with
        self.word =random.choice(self.word_list)
        #list of letters guessed and not guessed
        self.word_guessed = ["_" for item in self.word]
        #number of unique words still not guessed
        self.unique_letters_in_word = set(self.word)
        self.num_letters = len(self.unique_letters_in_word)
        #list of total guesses made so far
        self.list_of_guesses = []

    #check whether guess is in word
    def check_guess(self,guess):
        guess = guess.lower()
        print(self.word)
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            #if guess in word, change _ to letter, and reduce list no of unique letter letters yet to be guessed
            for letter in self.word:
                if letter == guess:
                    guess_word_pos = self.word.index(letter)
                    self.word_guessed[guess_word_pos] = guess
            self.unique_letters_in_word.remove(guess)
            self.num_letters= len(self.unique_letters_in_word)
            print( self.unique_letters_in_word)            
                
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

word_list_fruit = ["apple", "mango", "grape", "avocado", "blueberry"]
game_1 = Hangman(word_list_fruit)
print(game_1.num_letters)
game_1.ask_for_input()
print(game_1.word_guessed)
print(game_1.num_letters)
