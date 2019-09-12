word = "table"

failed = 0
guesses = "_" * len(word)


def startGame(failed,guesses,word):
    wrong = 7
    print("Guess a letter in this 5 letter word")
    guess = input("Try to guess! " + guesses + " Guess letter: ")

    while len(guess) <= len(word):
        letter = input("Guess a letter: ")
        for i in word:
            for j in guess:
                if j == i:
                    guess.append(j)
                if failed >= 3:
                    print(guess)
                    break
                    print("no more guesses")
                elif len(guess) >= len(word):
                    print("you lose!")
                    break
                    for j in word:
                        if letter != j:
                            failed += 1 #where does this go?
                            print(failed)
                            print(guess)
                elif j == letter:
                    guess += j
                else:
                    counters += 1
                    print(counters)
startGame()
# something is wrong with the for loop when it loops it is comparing j to all letters which prints
# out each letter multiple times
    #print(guess)
# need to create a counter for FAILED ATTEMPTS
