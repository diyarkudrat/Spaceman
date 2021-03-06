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
    # count = 0
    # for i in secret_word:
    #     if i in letters_guessed:
    #         count += 1
    # if count == len(list(secret_word)):
    #     return True
    # else:
    #     return False

    # return letters_guessed in secret_word

    if secret_word in letters_guessed:
        return True
    else:
        return False




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

    return string



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



def test_is_word_guessed():
     test_word = 'fantasy'
     test_guess = 'q'
     test_function = is_word_guessed(test_word, test_guess)

     assert test_function == False

     # assert test_function == True

def test_get_guessed_word():
    test_word = 'fantasy'
    test_list = ('d','t','x','y','s')
    test_function = get_guessed_word(test_word, test_list)

    assert test_function == '___t_sy'

    # assert test_function == 'f__t__y'

def test_is_guess_in_word():
    test_word = 'fantasy'
    test_guess = 'x'
    test_function = is_guess_in_word(test_word, test_guess)

    assert test_function == False

    # assert test_function == True







def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''

    print('The secret word contains:' + str(len(secret_word)) + ' amount of letters')
    print('You have 7 incorrect guesses to guess the word, Please enter one letter only per round')

    num_guess = True
    guess_count = 0

    while num_guess:
        user_guess = input('Enter guess here:')

        # print(secret_word)

        #Is guess in word
        if user_guess in letters_guessed:
            print('Already guessed letter')
            guess_count = guess_count

        #If user inputs one letter, add to list
        elif len(user_guess) <= 1 and user_guess.isalpha() == True:
            letters_guessed.append(user_guess)
        else:
            print('Only input one letter. Try again')

        #If letter is in word, fill it in
        #If not in  word, add to guess count
        guess = is_guess_in_word(user_guess, secret_word)
        if guess == True:
            print(get_guessed_word(secret_word, letters_guessed))
        else:
            print('Letter not in word')
            print(get_guessed_word(secret_word, letters_guessed))
            guess_count += 1

        #What happens when user wins
        if is_word_guessed(secret_word, letters_guessed) == True:
            print('Congrats! You won!')
            num_guess = False
        else:
            num_guess = True

        #If user has more than 7 incorrect guesses, game over
        if guess_count == 7:
            print('Sorry! You lost! The word was: ' + secret_word)
            num_guess = False
        else:
            #prints how many guesses left for user
            num_guess_left = 7 - guess_count
            print('You have ' + str(num_guess_left) + " guesses remaining!")







#These function calls that will start the game
# secret_word = load_word()
# spaceman(secret_word)
#
# game = True
#
# while game:
#     menu = input('Press P')
#     if menu == 'p':
#         secret_word = load_word()
#         spaceman(secret_word)



def play_game():
    game = True
    #keeps game in loop. After game is over, you can play another game.
    while game:
        print('Welcome to Spaceman!')
        print(' ')
        menu = input('If you wanna play, press P! If you want to quit, press Q')
        letters_guessed.clear()
        if menu == 'p' or menu == 'P':
            secret_word = load_word()
            spaceman(secret_word)
        elif menu == 'q' or menu == 'Q':
            game = False
        else:
            print('Improper input')


test_is_word_guessed()
test_get_guessed_word()
test_is_guess_in_word()

if __name__ == '__main__':
    play_game()


#
# '[/;lp]'
