word = "table"

failed = 0
guesses = "_" * len(word)


def startGame(failed,guesses,word):
    wrong = 7
    print("Guess a letter in this 5 letter word")
    guess = input("Try to guess! " + guesses + " Guess letter: ")

    if guess in word:
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        guesses = guesses[:index] + guess + guesses[index +1:]

    else:
        failed += 1
        if failed < wrong:
            print("Wrong guess. " + str(wrong - failed) + " failed attempts remaining." )

        elif failed == wrong:
            print("You lose. The letters you missed were " + word)

    if word == "_" * len(word):
        print("Yay! You win!")
    elif wrong != failed:
        startGame(failed,guesses,word)

startGame(failed,guesses,word)

# use find in python https://www.programiz.com/python-programming/methods/string/find
# indexing in python https://www.pythonlikeyoumeanit.com/Module3_IntroducingNumpy/BasicIndexing.html
#specific index stack overflow https://stackoverflow.com/questions/41752946/replacing-a-character-from-a-certain-index
