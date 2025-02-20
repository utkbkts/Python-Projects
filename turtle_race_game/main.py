from turtle import Turtle, Screen
import time
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0) 
class TurtlePy(Turtle):
    def __init__(self, color, x, y, position):
        super().__init__()
        self.shape("turtle")
        self.color(color)
        self.penup()
        self.goto(x, y)
        self.right(position)

    def go_up(self):
        if self.ycor() < 280:
            self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        if self.ycor() > -280:
            self.goto(self.xcor(), self.ycor() - 20)

    def go_right(self):
        if self.xcor() < 280:
            self.goto(self.xcor() + 20, self.ycor())

    def go_left(self):
        if self.xcor() > -280:
            self.goto(self.xcor() - 20, self.ycor())

turtle = TurtlePy("red", 0, -280, -90)

screen.listen()
screen.onkey(turtle.go_up, "Up")
screen.onkey(turtle.go_down, "Down")
screen.onkey(turtle.go_right, "Right")
screen.onkey(turtle.go_left, "Left")

class Bar(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.goto(position)

    def move(self):
        new_x = self.xcor() + 5  
        if new_x > 300: 
            new_x = -300
        self.goto(new_x, self.ycor())

class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 280)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))

class Timer(Turtle):
    def __init__(self, level):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.time_left = 30 
        self.level = level
        self.update_timer()

    def update_timer(self):
        self.clear()
        self.goto(100, 250)
        self.write(f"Time: {self.time_left}", align="center", font=("Courier", 24, "normal"))
        self.goto(100, 220) 
        self.write(f"Level: {self.level}", align="center", font=("Courier", 24, "normal"))

    def countdown(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.update_timer()

score = Score_board()
level = 1
timer = Timer(level)

bars = []
def create_bars():
    global level
    bars.clear()  
    for _ in range(level * 5): 
        x = random.randint(-220, 220)
        y = random.randint(-220, 220)
        bar = Bar((x, y))
        bars.append(bar)

create_bars()

def check_collision():
    for bar in bars:
        if turtle.distance(bar) < 20: 
            return True
    return False

def game_wind():
        if turtle.ycor() >= 280:
           return True
        return False


# **Oyun Döngüsü**
game_on = True
while game_on:
    timer.countdown()  
    
    if timer.time_left == 0:
        level += 1
        timer.level = level  
        create_bars()
        timer.time_left = 30 
    
    for bar in bars:
        bar.move()

    if check_collision():
        turtle.goto(0, 0)
        turtle.write("Game Over!", align="center", font=("Arial", 16, "bold"))
        game_on = False

    if game_wind():
        turtle.goto(0,0)
        turtle.write("YESSSSSSS HEYY YOOOO WINNING!", align="center", font=("Arial", 16, "bold"))
        game_on = False
    screen.update()
    
    time.sleep(0.1)

screen.exitonclick()
