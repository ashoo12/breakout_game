from turtle import Turtle
class Paddle(Turtle):
      def __init__(self):
          super().__init__()
          self.penup()
          self.shape("square")
          self.color("white")
          self.shapesize(stretch_wid=1, stretch_len=5)
          self.goto(x=0, y=-200)


      def move_right(self):

          new_x=self.xcor()+20
          self.goto(x=new_x,y=self.ycor())
          if self.xcor()>380:
              self.goto(x=new_x*-1, y=self.ycor())

      def move_left(self):
          new_x=self.xcor()-20
          self.goto(x=new_x,y=self.ycor())
          if self.xcor()<-380:
              self.goto(x=new_x*-1, y=self.ycor())


      def paddle_reset(self):
          self.goto(x=0, y=-200)