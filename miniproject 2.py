#  Author. Jorge Lopez miniproject#2

# "Guess the number" mini-project

import math
import simplegui
import random


# define event handlers for control panel
def range100():
    global attempts, range, secret_number 
    range = 100
    print "at range100"
    # button that changes the range to [0,100) and starts a new game    
    attempts = int(math.ceil(math.log(100,2)))
    print "NEW GAME, RANGE IS 0, 100"
    print "NUMBER OF REMAINING GUESSES IS ", attempts
    secret_number = random.randrange(0,range)
    print "secret number 100 =", secret_number


def range1000():
    global attempts, range, secret_number
    range = 1000
    print "at range 1000"
    # button that changes the range to [0,1000) and starts a new game     
    attempts = int(math.ceil(math.log(1000,2))) 
    print "NEW GAME!, RANGE IS 0, 1000"
    print "NUMBER OF REMAINING GUESSES IS ", attempts
    secret_number = random.randrange(0,range)
    print "secret number 1000 =", secret_number
    

     
def input_guess(guess):
       global attempts, range, secret_number
       guess=int(guess) ## converts to integer input_guess
       print "GUESS WAS ", guess
       if guess > (range - 1) :
          print "YOU NEED TO ENTER A NUMBER < ", range
       else:
         if attempts >= 1:
            ## print "at input guess, secret_number=", secret_number
            if secret_number == guess:
               print "**************"
               print "** CORRECT! **"
               print "**************"
               ##sound = simplegui.load_sound('http://commondatastorage.googleapis.com/codeskulptor-assets/Epoq-Lepidoptera.ogg')
               ##sound.play()
               new_game()
            else:
               if secret_number < guess:
                  
                  attempts = attempts - 1
                  if attempts > 0:
                     print "LOWER!"      
                     print "NUMBER OF REMAINING GUESSES = ", attempts
                  else:
                    print " * SORRY THE SECRET NUMBER WAS:", secret_number
                    new_game()
               else:
                  if secret_number > guess:
                     
                     attempts = attempts - 1
                     if attempts > 0:
                        print "HIGHER!"   
                        print "NUMBER OF REMAINING GUESSES = ", attempts
                     else:
                        print " * SORRY THE SECRET NUMBER WAS:", secret_number
                        new_game()   
                        ## print "NUMBER OF REMAINING GUESSES = ", attempts
               
                         
         else:
             print " 1 SORRY THE SECRET NUMBER WAS:", secret_number
             new_game()
  

# helper function to start and restart the game
def new_game():
    global attempts, range, guess, secret_number
    # initialize global variables used in your code here
    range = 100
    attempts = int(math.ceil(math.log(100,2)))
    secret_number = random.randrange(0,range)
    print "NEW GAME!, RANGE IS 0, 100"
    print "NUMBER OF REMAINING GUESSES IS ", attempts
    ## print "secret number =", secret_number
   
f = simplegui.create_frame("GUESS THE NUMBER",200,200)

f.add_button("Range is [0,100)", range100,200)
f.add_button("Range is [0,1000)", range1000,200)
f.add_input("Enter Guess", input_guess, 200)  

f.start()

# register event handlers for control elements and start frame

new_game()