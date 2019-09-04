# create word

word = "beyonce"

guess = ""

guessing = input("Guess a letter: ")

for i in word:
    if i == guess:
        guessing += i
