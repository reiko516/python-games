# Try out the game at http://www.codeskulptor.org/#user9_iGAgIHpbEhoQJ0o.py

import simplegui 
import random
import math

# initialize global variables used in the code
num_range = 100
secret_num = random.randrange(0, 100)
guesses = 0
max_guesses = 0

# helper function to initialize game

def init():
    global num_range, guesses, max_guesses
    guesses = 0
    max_guesses = math.ceil(math.log(num_range, 2))
    print "New game. Range is 0 to %d." % num_range
    print "You have", max_guesses, "tries to guess the number.\n"

# define event handlers for control panel
    
def range100():
    # button that changes range to range [0,100) and restarts
    global num_range, secret_num
    num_range = 100
    init()
    secret_num = random.randrange(0, 100)
    return secret_num

def range1000():
    # button that changes range to range [0,1000) and restarts
    global num_range, secret_num
    num_range = 1000
    init()
    secret_num = random.randrange(0, 1000)
    return secret_num
    
def get_input(guess):
    # main game logic goes here
    global secret_num, guesses, max_guesses    
    
    # grabs player guess string and turns into an integer
    player_guess = int(guess)
    
    # keeps track of how many guesses made and guesses left
    guesses += 1
    guess_left = max_guesses - guesses
    
    # print results   
    if guess_left==0:
        print "Sorry, you ran out of guesses. The number was", secret_num, "\n"
        init()
        return            
    
    if player_guess > secret_num:
        print "Your guess was", player_guess
        print "Choose lower!"
        print "You have", guess_left, "guesses left.\n"
    elif player_guess < secret_num:
        print "Your guess was", player_guess
        print "Choose higher!"
        print "You have", guess_left, "guesses left.\n"
    else:
        print "Your guess was", player_guess
        print "You got it right!\n"
        init()
        return
           
# create frame
f = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements
f.add_button("Range is [0, 100]", range100, 200)
f.add_button("Range is [0, 1000]", range1000, 200)
f.add_input("Enter a guess", get_input, 200)

# initialize the game
init()

# start frame
f.start()
