from proj.word import getWord
word = getWord() #function defined in imported file

failed = 0
guesses = "_" * len(word)


def startGame(failed,guesses,word):
    wrong = 7
    print("Guess this " + str(len(word)) + " letter word.")
    guess = input("Try to guess! " + guesses + " Guess letter: ")

    while guess in word: #while loop will ensure that multiple letters in one word are both indexed
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        guesses = guesses[:index] + guess + guesses[index +1:]

    else:
        failed += 1
        if failed < wrong:
            print("Wrong guess. " + str(wrong - failed) + " failed attempts remaining." )

        elif failed == wrong: #if the number of failed attempts equals them total allowed attempts loss
            print("You lose. The letters you missed were " + word)


    if word == "_" * len(word):
        print("Yay! You win!")
    elif wrong != failed:
        startGame(failed,guesses,word)
startGame(failed,guesses,word)


#sources
# use find in python https://www.programiz.com/python-programming/methods/string/find
# indexing in python https://www.pythonlikeyoumeanit.com/Module3_IntroducingNumpy/BasicIndexing.html
#specific index stack overflow https://stackoverflow.com/questions/41752946/replacing-a-character-from-a-certain-index
# stackOverflow how to use relative imports https://stackoverflow.com/questions/48931254/relative-import-in-python-3-6
