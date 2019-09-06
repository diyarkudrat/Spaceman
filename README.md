Spaceman Game!

Rules:
The objective of the game is to guess the word.
You guess letter by letter.
If you incorrectly guess 7 letters, game over.
Have to guess a letter, or else it'll tell you that you have to guess a letter and you have one less guess remaining.

Game:
There's a 'welcome page'.
Press P to play or Q to quit.
After a game has been played, it'll go back to the welcome page.
Each guess will display if the letter is in the word or not.
It'll also display how many incorrect guesses remaining.
And it'll display the word with the correct guess letters filled in while the others are blank.
After losing a game, it'll display what word it was.



#Spaceman Pseudocode

    Layout:
        Title/Beginning:
            "Welcome to Spaceman!"
            "The secret word contains: x amount of letters"
            "You have 7 incorrect guesses, Please enter one letter only per round"

        Each input of correct letter layout:
            "Enter a letter: "" "
            "Your guess appears in the word!"
            "Guessed word so far: "_a_ _" "
            "These letters hasn't been guessed: remaining letters in alphabet"

        Each input of incorrect letter layout:
            "Enter a letter: " " "
            "Sorry your guess was not in the word, try again"
            "You have 6 incorrect guesses left"
            "Guessed word so far: "
            "These letters hasn't been guessed: remaining letters in alphabet"

    is_word_guessed function:
        function that checks if all the letters in the secret word have been Guessed
        if letter is not in secret word
            return False
        else
            return True

    get_guessed_word function:
        function that shows the guessed letters in secret word and underscores the letters you have not guessed yet
        if guessed letter is in secret word
            fill that letter in
        elif guessed letter hasn't been Guessed
            display "_"
    is_guess_in_word function:
        function that checks if guessed letter is in secret word
        if guessed letter is in secret word:
            return True
        else:
            return False

    spaceman function:
        While Loop
        if user's guess is in secret word, put word in empty slot
        put user's guess in lettersGuessed list
        if user's guess is already in lettersGuessed list, print 'Letter already guessed. Please try again'
