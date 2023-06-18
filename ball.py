from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.goto(x=0,y=-185)
        self.x_move=-10*random.choice([-1,1])
        self.speed(10)
        self.y_move=10


    def move(self):
        new_x=self.xcor()+self.x_move
        new_y=self.ycor()+self.y_move
        self.goto(x=new_x,y=new_y)
    # when ball hits the brick
    def bounce_brick(self):
        self.x_move*=1*random.choice([-1,1])
        self.y_move*=-1

    # when ball hits the paddle
    def bounce_up(self):
        self.y_move*=-1
    #when ball hits the side walls
    def bounce_back(self):
        self.x_move*=-1

#     when ball hits the top wall
    def bounce_down(self):
        self.y_move-=20

# when ball misses the paddle
    def ball_reset(self):
        self.goto(x=0,y=-180)


