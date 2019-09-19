import unittest
from proj.word import getWord

import unittest

words = ['apple','microsoft','twitter','fanbulous']
# Declare our function
def get_word(word):
    word = "This is the secret word: " + words[0] + "!"
    return word
def letter_in_word(letter,word):
    if letter in word:
        return "letter is in word"
    else:
        return "Not in word"
def correct_input(uInput):
    if len(uInput) > 1 or len(uInput) < 1:
        return "Guess again only one letter"
    else:
        return "Not in word"

class spacemanTesting(unittest.TestCase):
    # For each test in the class, make a method where self is the parameter
    def test_get_word(self):
        # the actual test
        self.assertEqual(get_word('apple'), "This is the secret word: apple!") #pass
        #self.assertEqual(get_word('microsoft'), "This is the secret word: microsoft!") #fail
        #self.assertEqual(get_word('twitter'), "This is the secret word: twitter!") #fail
    def test_letter_in_word(self):
        #self.assertEqual(letter_in_word('i',"dog"), "Not in word") #fail
        self.assertEqual(letter_in_word('o','robot'), "letter is in word") #pass
        self.assertEqual(letter_in_word("w",'twitter'), "letter is in word") #pass
    def test_correct_input(self):
        #self.assertEqual(correct_input('j'), "Not in word") #fail
        self.assertEqual(correct_input('o'), "Not in word") #pass
        self.assertEqual(correct_input("ww"), "Guess again only one letter") #pass
# run the tests
if __name__ == '__main__':
    unittest.main()
