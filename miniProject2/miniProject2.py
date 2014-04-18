# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# initialize global variables
num_range = 100
secret_num = 0
num_guesses = 0


# helper function to start and restart the game
def new_game():
    if(num_range == 100):
        range100()
    else:
        range1000()


# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global secret_num, num_range, num_guesses
    num_range = 100
    num_guesses = 7
    secret_num = random.randrange(0, 100)
    print "New game. Range is from 0 to 100."
    print "Number of remaining guesses is ", num_guesses
    print ""


def range1000():
    # button that changes range to range [0,1000) and restarts
    global secret_num, num_range, num_guesses
    num_range = 1000
    num_guesses = 10
    secret_num = random.randrange(0, 1000)
    print "New game. Range is from 0 to 1000."
    print "Number of remaining guesses is ", num_guesses
    print ""

def input_guess(guess):
    # main game logic
    global num_guesses
    num_guesses = num_guesses - 1
    print "Guess was ", guess
    print "Number of remaining guesses is ", num_guesses
    if(secret_num == int(guess)):
        print "Correct!\n"
        new_game()
    else:
        if(num_guesses == 0):
            print "You ran out of guesses. The number was ", secret_num
            print ""
            new_game()
        elif(secret_num < int(guess)):
            print "Lower\n"
        else:
            print "Higher\n"


# create frame
f = simplegui.create_frame("Guess the number", 200, 200)


# register event handlers for control elements
f.add_button("Range is [0,100)", range100, 200)
f.add_button("Range is [0,1000)", range1000, 200)
f.add_input("Enter a guess", input_guess, 200)


# call new_game and start frame
new_game()
f.start()
