## Author. Jorge Lopez
## Miniproject 4
## PONG Game

import simplegui

# Initialize globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

ball_pos = [WIDTH / 2, HEIGHT / 2]

vel = [-40.0 / 6.0,  5.0 / 6.0] ## the largest the denominator the slowest the ball


# define event handlers
def draw(canvas):
    global WIDTH, HEIGHT
    # Update ball position
    ball_pos[0] += vel[0]
    ball_pos[1] += vel[1]
    
    print "ball_pos[0,1]=", ball_pos[0], ball_pos[1]
    
    # collide and reflect off of left hand side of canvas
    if (ball_pos[0] <= BALL_RADIUS):
       vel[0] = - vel[0]
       print "LEFT WALL"
    elif ball_pos[0] >= (WIDTH - BALL_RADIUS):
        print "RIGHT WALL!"
        vel[0] = - vel[0]
    
    if ball_pos[1] <= BALL_RADIUS:
        print "UPPER BALL! %%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
        vel[1] = - vel[1]
    elif ball_pos[1] >= HEIGHT - BALL_RADIUS:
        print "LOWER BALL!#########################"       
        vel[1] = - vel[1]
##   else:
##        if ball_pos[1] >= (HEIGHT - BALL_RADIUS):
##           vel[1] = - vel[1]
           
    
   

    
    # Draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

# create frame
frame = simplegui.create_frame("Ball physics", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)

# start frame
frame.start()
