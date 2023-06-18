from turtle import Turtle
color=["red","red","orange","orange","green","green","yellow","yellow"]
bricks_list = []


class Bricks():
        brick = Turtle(shape="square")
        brick.penup()
        x1 =brick.xcor=-365
        y1 =brick.ycor= 200
        brick.shapesize(stretch_wid=1, stretch_len=2)

        brick.speed(0)
        for y in range(8):
            for x in range(14):
                  brick.color(color[y])
                  brick.goto(x1, y1)
                  brick.stamp()
                  bricks_list.append(brick)
                  x1 += 55
            y1-=30
            x1=-365
for i in range(len(bricks_list)):
              print(bricks_list[i].position())
print(bricks_list)