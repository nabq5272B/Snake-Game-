import turtle
import time
import random

delay = 0.1

# Scores inittal 
score = 0
high_score = 0

# Window
win = turtle.Screen()
win.title("Snake Game")
win.bgcolor('black')
win.setup(width=700, height=700)
win.tracer(0)

# Head 
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("lime green")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Food
food= turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("yellow")
food.penup()
food.goto(0,150)

segments = []

# Scoreboard
scr = turtle.Turtle()
scr.speed(0)
scr.shape("square")
scr.color("red")
scr.penup()
scr.hideturtle()
scr.goto(0,260)
scr.write("Score: 0 | High score: 0", align = "center", font=("arial",20, "normal"))

#Functions
def up():
    if head.direction != "down":
        head.direction = "up"
def down():
    if head.direction != "up":
        head.direction = "down"
def left():
    if head.direction != "right":
        head.direction = "left"
def right():
    if head.direction != "left":
        head.direction = "right"
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

# Keys
win.listen()
win.onkeypress(up, "Up")
win.onkeypress(down, "Down")
win.onkeypress(left, "Left")
win.onkeypress(right, "Right")

# Main Game Loop
while True:
    win.update()

    # Collision with the borders
    if head.xcor()>340 or head.xcor()<-340 or head.ycor()>340 or head.ycor()<-340:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # Hiding Body Segments
        for x in segments:
            x.goto(1000,1000) #out of range
        
        segments.clear()

        # Reset Score
        score = 0

        # Reset delay
        delay = 0.1

        # Printing New Scores
        scr.clear()
        scr.write(f"Score: {score} | High score: {high_score}", align="center", font=("arial", 20, "normal"))

    # Collision with Food
    if head.distance(food) <20:
        # Placing food on different random spaces of the screen
        x = random.randint(-340,340)
        y = random.randint(-340,340)
        food.goto(x,y)

        # Increasing the body via segments
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("dark green")
        new_segment.penup()
        segments.append(new_segment)

        # Decreasing the delay
        delay -= 0.001

        # Increasing the Score
        score += 10

        if score > high_score:
            high_score = score
        
        # Printing New Scores
        scr.clear()
        scr.write(f"Score: {score} | High score: {high_score}", align="center", font=("center", 20, "normal")) 

    # Moving the segment in reverse order
    for i in range(len(segments)-1,0,-1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x,y)

    # Moving the segment 0 to head
    if len(segments)>0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    # Collision with the body
    for j in segments:
        if j.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            # Hiding body Segments
            for k in segments:
                k.goto(1000,1000)
            
            segments.clear()
            
            # Reset Scores
            score = 0

            # Reset Delay
            delay = 0.1

            # Printing New Scores   
            scr.clear()
            scr.write(f"Score: {score} | High score: {high_score}", align="center", font=("arial", 20, "normal"))
    
    time.sleep(delay)

win.mainloop()   