import random

word_list = ["apple", "mango", "grape", "avocado", "blueberry"]

# for fruit in word_list:
#     print(fruit)

word = random.choice(word_list)
#print(word)

guess = input("Enter a single letter: ")
if len(guess) == 1 and guess.isalpha():
    print("Good guess")
else:
    print("Opps! That is not a valid input")


