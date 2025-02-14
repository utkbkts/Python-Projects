from turtle import Screen
from snake import Snake
from food import Food
import time


SCREEN_SIZE = 600
LIMIT = SCREEN_SIZE // 2
#Ekranı oluşturmak

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Yılan Oyunu")
screen.tracer(0)

#Yılanı oluşturmak
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #yılan yiyecek yapısı

    if snake.head.distance(food) < 15:
        food.refresh() # yeni yiyecek konumunu belirliyoruz
        snake.grow() # yılan büyüsün
    
    if (snake.head.xcor() > LIMIT or snake.head.xcor() < -LIMIT or snake.head.ycor() > LIMIT or snake.head.ycor()<-LIMIT):
        game_on = False
        print("Oyun bitti yılan sınır dışına çıktı")

screen.exitonclick()