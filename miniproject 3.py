# miniproject 3
# template for "Stopwatch: The Game"
import simplegui

# define global variables
message="this is just a test"

a = 0
b = 0
c = 0
d = 0
bc = 0
Stop=False


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D

def start_button_handler():
    timer.start()

def stop_button_handler():
    global Stop
    timer.stop()
    Stop=True
 
def reset_button_handler():
    global a, bc, d, Stop
    a = 0
    bc = 0
    d = 0
    t="0000"
    timer = simplegui.create_timer(100, timer_handler)
    if Stop:
       Stop=False 
       timer.start()
     
    
# define event handlers for buttons; "Start", "Stop", "Reset"


# define event handler for timer with 0.1 sec interval


# define draw handler
def draw(canvas):
    canvas.draw_text(format(t), [15, 120], 50, "Green", "monospace")

def format(t):
   t=str(t[:1]+":"+t[1:3]+"."+t[3:4])
   print "t en format=", "["+t+"]"
   return t

def timer_handler():
   global position, a,b,c,d, bc, t
   ## bc = int(str(b) + str(c))
   position=[50, 50]
   d+=1
   ## print "in timer handler", d
   

   ## print "b,c=", b, c, "and bc=", bc
   if d%10 == 0:
      d = 0
      bc+=1
      print "bc=", bc
      if bc%60 == 0:
         print "bc is module 60!"
         bc = 0
         if a < 58:
            a+=1
         else:
            print "THIS TIMER ONLY COUNTS UNTIL 59:59.9!"
         
   print "a=", a, "bc=", bc, "d=", d
   if bc<=9:
      Sbc="0"+str(bc)
      t=str(a)+Sbc+str(d)
   else:
      t=str(a)+str(bc)+str(d)
   ## format(t)
   frame.set_draw_handler(draw)


# create frame
frame = simplegui.create_frame("Home", 200, 200)
frame.add_button("START", start_button_handler)
frame.add_button("STOP", stop_button_handler)
frame.add_button("RESET", reset_button_handler)

# register event handlers
timer = simplegui.create_timer(100, timer_handler)

# start frame
t="0000"
frame.start()
frame.set_draw_handler(draw)
# Please remember to review the grading rubric
