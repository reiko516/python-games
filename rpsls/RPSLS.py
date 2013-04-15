# Rock-paper-scissors-lizard-Spock 

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

def name_to_number(name):
    # convert name to number using if/elif/else
    
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    else:
        return 4
     
def number_to_name(num):
    # convert number to a name using if/elif/else
    
    if num == 0:
        return "rock"
    elif num == 1:
        return "Spock"
    elif num == 2:
        return "paper"
    elif num == 3:
        return "lizard"
    else:
        return "scissors"

import random

def rpsls(name): 
    # convert guess to player_number using name_to_number
    print "Player chooses", name
    player_number = name_to_number(name)
    
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)
    print "Computer chooses", number_to_name(comp_number)
    
    # compute difference of player_number and comp_number modulo five
    result = (player_number - comp_number) % 5
    
    # use if/elif/else to determine winner and print to console
    if result == 0:
        print "It's a tie!\n"
    elif result > 2:
        print "Computer wins!\n"
    else:
        print "Player wins!\n"
    
    print "-----------------\n"

name = raw_input("Choose between rock, paper, scissors, lizard, or Spock. (Case sensitive)")
rpsls(name)