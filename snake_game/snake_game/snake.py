from turtle import Turtle
#Başlangıç pozisyonu
START_POSITIONS = [(0,0),(-20,0),(-40,0)]
#Yılanın ilerleyeceği mesafe
MOVE_DISTANCE = 20

#Yönleri derece cinsinden tanımlıyoruz
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = [] # yılan segmentlerini tutan liste
        self.create_snake() # yılan oluştur
        self.head = self.segments[0] # yılanın baş kısmı
    
    def create_snake(self):
        for position in START_POSITIONS:
            self.add_segment(position)
    
    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup() # iz bırakmaması için
        new_segment.goto(position) # segmenti belirli bir pozisyona yerleştirir.
        self.segments.append(new_segment) # yeni oluşturduğumuz segmenti ekle
    
    def move(self):
        for seg_num in range(len(self.segments)- 1,0,-1):
            # her segmenti bir öncekinin konumuna taşıyacağız
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        
        self.head.forward(MOVE_DISTANCE) # yılanın başını ileri doğru hareket ettirir.
    
    def grow(self):
        last_segment = self.segments[-1]
        self.add_segment(last_segment.position())
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

