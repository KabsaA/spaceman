word = "bad" # length is 7
guess = "" # length is 0
failed = 0
#print(len(guess))
while len(guess) < len(word):
    guessing = input("Guess a letter: ")
    for i in word:
        for j in guessing:
            if i == j:
                guess += i
            else:
                failed += 1
    print(guess)
    if failed == 4 :
        print("No more guesses")
        #break
    elif len(guess) >= len(word):
        break
# need to create a counter for FAILED ATTEMPTS
