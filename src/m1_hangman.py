"""
Hangman.

Authors: Shengjun Guan and YOUR_PARTNERS_NAME_HERE.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.
def main():
    hangman()

def hangman():
    setting()
    pick_up_word()
    # playing_looping()
    # win_lose()
    # play_again()

def setting():
    print('I will choose a random secret word from a dictionary. You set the INIMUM legth of that word')
    while True:
        word_limit = int(input('What MINIMUM length do you want for the secret word?'))
        if type(word_limit) == int and word_limit > 0:
            print('You set the DIFFICULTY  of the game by setting the number of UNSUCCESSFUL choices you can make before you LOSE the game.'
                  'The traditional form of Hangman sets this number to', word_limit)
            break

def playing_looping():
        input_guess()
        continue_or_not()
        display()

def input_guess():

# TODO: 2. Implement Hangman using your Iterative Enhancement Plan.
main()
####### Do NOT attempt this assignment before class! #######

