## Miniproject 1
## Author. Jorge Lopez
##
## 
##   0 — rock
##   1 — Spock
##   2 — paper
##   3 — lizard
##   4 — scissors

import random

def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return 9
    
def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return "Name Unknown"
    
def rpsls(player_choice):
 
    print
    print 'player chooses', player_choice
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0,4)
    computer_choice=number_to_name(comp_number)
    print 'Computer chooses',computer_choice
    ## Determine winner
    
    winop = (comp_number - player_number)%5
    if winop in [1,2]:
        print 'Computer wins!' ## winop
    elif winop == 0:
         print 'Computer and Player tie!'
    else:
        print 'Player wins!' ## winop
        
    
## calling function rpsls

rpsls('rock')
rpsls('Spock')
rpsls('paper')
rpsls('lizard')
rpsls('scissors')



    
    
    
