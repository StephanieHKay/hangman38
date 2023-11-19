import milestone_2

def ask_for_input():
    while True:
        guess = input("Player, enter a letter: ")
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

    print(milestone_2.random_word)
    check_guess(guess)

def check_guess(guess):
    guess = guess.lower()
    if guess in milestone_2.random_word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")
ask_for_input()