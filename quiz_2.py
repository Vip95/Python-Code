# Guess the number game

import random

targetNumber = random.randrange ( 1,10,1)
no_of_guesses_left = 3

while ( no_of_guesses_left > 0 ) : 
    number_guessed = int ( input ( " Enter a number ") ) 
    no_of_guesses_left -= 1

    if ( number_guessed == targetNumber ) :
        print ("Gotcha you got it right!")
        break
    elif ( number_guessed > targetNumber ) :
        print ("Required number is lesser than your choice")
        print ("Chances left", no_of_guesses_left)
    else :
        print ("Required number is greater than the number you guessed!")
        print ("Chances left", no_of_guesses_left)
else :
    print ("Game Over!")          


    


