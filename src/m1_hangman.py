"""
Hangman.

Authors: Shengjun Guan and YOUR_PARTNERS_NAME_HERE.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    while True:
        word_limit = setting_minimum()

        unsuccessful_choice = unsuccessful_choices()

        word = pick_up_word('words.txt', word_limit)

        secret_word = word

        print(word)

        unsuccessful_choice_present = unsuccessful_choice

        letter_remain = len(word)
        right_guess = []
        while True:
            guess = input_guess()

            consequence = check_letter(guess, secret_word,right_guess) #if consequence = 0, which means there is no cost on life, the guess is right
                                                #if consequence = -1, the guess is wrong
                                                #
            unsuccessful_choice_present = unsuccessful_choice_present + consequence


            if consequence == 0:
                print("Good guess! You still have ",unsuccessful_choice_present,'unsuccessful guesses left before you LOSE the game!')

                # changing the secret_word, need a function to change the secret_word in to the form for gamers
                # at the same time, changing the letter_remain for if continue the game or not!
                (secret_word, letter_remain) = changing_secret_word(secret_word, letter_remain, guess)
                if guess not in right_guess:
                    right_guess = right_guess + [guess,]

            if consequence == -1:
                print('Sorry! There are no',guess, 'letters in the secret word. You have ',unsuccessful_choice_present,' unsuc'
                                                                                                                       'cessful guesses left before you LOSE the game!')
                #TIME to show what is the secret_word for gamers depending on the unsuccessful_choices they still have
            continue_or_done(letter_remain,word, right_guess)
            if letter_remain == 0:
                yes_no_continue = input('Play another game? (y/n)')
                if yes_no_continue == 'n':
                    exit()
                if yes_no_continue == 'y':
                    break
            if unsuccessful_choice_present == 0:
                while True:
                    yes_no_continue = input('Play another game? (y/n)')
                    if yes_no_continue == 'n':
                        exit()
                    if yes_no_continue == 'y':
                        break

def continue_or_done(letter_remain,word, right_guess):
    if letter_remain == 0:
        print('You lose! The secret word was', word)

    gamer_version_secreword = get_gamer_version_secret_word(word, right_guess)


    print('Here is what you currently know about the secret word:')
    print(gamer_version_secreword)

def setting_minimum():
    print('I will choose a random secret word from a dictionary. You set the INIMUM legth of that word')
    while True:
        try:
            word_limit = int(input('What MINIMUM length do you want for the secret word?'))
            if type(word_limit) == int and word_limit > 0:
                return word_limit
        except:
            None

def get_gamer_version_secret_word(word, right_guess):
    str = []

    for n in range(len(word)):
        str = str + ['_']

    #if the letter in right_guess is in the word, show the letter in the gamer_version
    #do not show the letter that is not in the right_guess, which means add the '_' instead

    for i in right_guess:
        for j in range(len(word)):
            if word[j] == i :
### str.append(i)
                str[j] = i

    gamer_version_secreword =''.join(str)
    return gamer_version_secreword

def unsuccessful_choices():
    print('Yuo set the DIFFICULTY of the game by setting the number of UNSUCCESSFUL choices you can make before you LOSE the game '
          '. The traditional form of Hangman sets this number to 5')
    while True:
        unsuccessful_choice = int(input('How many unsuccessful choices do you want to allow yourself?'))
        if type(unsuccessful_choice) == int and unsuccessful_choice >= 0:
            break
    return unsuccessful_choice


def pick_up_word(afile, word_limit):
    import random
    while True:
        lines = open(afile).read().splitlines()
        word = random.choice(lines)
        if len(word) >= word_limit:
            break
    return word


def input_guess():
    while True:
        guess = input('What letter do you want to try?')
        if len(guess) == 1 and guess.islower():
            break
    return guess

def check_letter(guess, secret_word, right_guess):
    consequence = 0
# if consequence = 0, which means there is no cost on life, the guess is right
# if consequence = -1, the guess is wrong
    for i in secret_word:
        if guess == i:
            return consequence
        for item in right_guess:
            if guess == item:
                print('Please other letter!')
                return consequence
    consequence = -1
    return consequence


def changing_secret_word(secret_word, letter_remain, guess):

# changing the secret_word, need a function to change the secret_word in to the form for gamers
# at the same time, changing the letter_remain for if continue the game or not!
    str =[]
    for i in range(len(secret_word)):
        if secret_word[i] == guess:
            letter_remain = letter_remain -1
            str.append('_')
        else:
            str.append(secret_word[i])
    secret_word = ''.join(str)
    return (secret_word, letter_remain)


# DONE: 2. Implement Hangman using your Iterative Enhancement Plan.
main()
####### Do NOT attempt this assignment before class! #######
