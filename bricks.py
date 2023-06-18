from turtle import Turtle
color=["red","red","orange","orange","green","green","yellow","yellow"]
bricks_list = []

class Bricks():

            x1 = -365
            y1 = 200
            for y in range(8):
                for x in range(15):

                    brick = Turtle()
                    brick.speed(0)

                    brick.penup()
                    brick.shape("square")
                    brick.shapesize(stretch_wid=1, stretch_len=2)
                    brick.color(color[y])
                    brick.penup()
                    brick.goto(x1, y1)
                    brick.pendown()
                    bricks_list.append(brick)

                    x1 += 55

                y1-=30
                x1=-365
                brick.hideturtle()


