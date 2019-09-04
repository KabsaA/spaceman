word = "beyonce" # length is 7
guess = "" # length is 0
#print(len(guess))
while len(guess) < len(word):
    guessing = input("Guess a letter: ")
    for i in word:
        if i == guessing:
            guess += i
            print(guess)
    if len(guess) >= len(word):
        break
