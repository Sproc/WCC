import random
# Get the user's guess
# Params: None
# Returns: Integer
#
def get_guess():

    # Get initial guess
    guess = raw_input('Enter your guess: ')

    # Assume it's not valid, until it's proven otherwise
    valid = False

    while valid != True:

        try:
            # Try and convert this number to an integer
            # If it fails, the exception will occur
            guess = int(guess)
        except Exception:
            # Exception was thrown when trying to convert to number,
            # Report the issue and ask again
            print('Invalid input; please enter a whole number.')
            valid = False
            guess = get_guess()

        # If they get here, it means the number must have been valid
        # Set valid to be true to break out of the while loop
        valid = True

    return guess
            #12
# Test get_guess
#print get_guess() # Expected: Keeps prompting until user enters a valid number

def compare(guess, secret_number):
    if guess > secret_number :
        return 'high'
    elif guess < secret_number :
        return 'low'
    else :
        return 'win'
# Test compare
assert compare(100,1) == 'high'
assert compare(1,100) == 'low'
assert compare(100, 100) == 'win'

#
#
#
def play():

    # Pick a secret numbers
    secret_number = random.randint(1, 100)
        #32
    # When building your program, the following line will tell you what
    # the secret_number is; this will make it easier to test the game.
    # When done, remove or comment-out this line.
    #print('TEMPORARY DEBUGGING HELPER -> The secret number is: ' + str(secret_number))

    # Print message at the start the game
    print("\nI'm thinking of a number between 1 and 100. I will give you 5 chances to figure it out. What do you think it is?")

    # Get the players initial guess
                              #low
    for guess_count in [4, 3, 2, 1, 0]:
        guess = get_guess()
        if compare(guess, secret_number) == 'win':
            print('You got it! The number was ' + str(secret_number) + '. Thanks for playing!')
            break
        elif guess_count == 0 :
            print('That was your last chance! Sorry. You lost!')
        else:
            print 'Too ' + str(compare(guess,secret_number)) + '. ' + str(guess_count) + ' Guesses left.  Guess again.'





# Run the game
play()
