import random


letters_guessed = []

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns:
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''

    for i in secret_word:
        #(alternative)if letters_guessed not in secret_word:
        if i not in letters_guessed:
            return False
        else:
            return True

    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    pass

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    string = ""
    word = list(secret_word)

    for i in word:
        if i in letters_guessed:
            string += i
        else:
            string += "_"

    print(string)

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet

    pass


def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''

    if guess in secret_word:
        print('Letter is in word!')
        return True
    else:
        return False

    #TODO: check if the letter guess is in the secret word

    pass




def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''

    print("Welcome to Spaceman")
    print('The secret word contains: _ amount of letters')
    print('You have 7 incorrect guesses, Please enter one letter only per round')

    num_guess = True
    guess_count = 0

    while num_guess:
        user_guess = input('Enter guess here:')

        #Is guess in word
        if len(user_guess) <= 1:
            letters_guessed.append(user_guess)
            guess = is_guess_in_word(user_guess, secret_word)
            if guess == True:
                get_guessed_word(secret_word, letters_guessed)
            else:
                print('Letter not in word:(')
                guess_count += 1
        elif user_guess in letters_guessed:
            print('Already guessed letter')
            guess_count += 1
        won = is_word_guessed(secret_word, letters_guessed)

        if guess_count >= 7:
            print('Sorry! You lost! The word was: ' + secret_word)
            num_guess = False
        else:
            num_guess_left = 7 - guess_count
            print('You have ' + str(num_guess_left) + " guesses remaining!")

        #What happens when user wins
        if won == True:
            print('Congrats! You won!')
            num_guess = False
        else:
            num_guess = True
















        # user_guess = input('Enter guess: ')
        # is_letter_guessed = is_guess_in_word(user_guess, secret_word)
        # #If guessed letter is in secret word, fill the letter in necessary blank
        # if is_letter_guessed == True:
        #     get_guessed_word(user_guess, secret_word)
        # #If user guessed a letter again, game will tell you that you used the letter and try again
        # if user_guess in letters_guessed:
        #     print('Already guessed. Try another letter')
        # elif len(user_guess) <= 1:
        #     letters_guessed.append(user_guess)
        # #More than 7 guesses, program will stop
        # if guess_count >= 7:
        #     print('Sorry! You lost:(')
        #     num_guess = False
        # #Tell user how many guesses he/she has
        # else:
        #     guesses_left = 7 - guess_count
        #     print('You have ' + str(guesses_left) + 'guesses remaining.')











    #TODO: show the player information about the game according to the project spec

    #TODO: Ask the player to guess one letter per round and check that it is only one letter

    #TODO: Check if the guessed letter is in the secret or not and give the player feedback

    #TODO: show the guessed word so far

    #TODO: check if the game has been won or lost






#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)

'[/;lp]'
