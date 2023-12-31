from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from bricks import Bricks, bricks_list
from scoreboard import Scoreboard
import time

status=Turtle()
screen=Screen()
scoreboard=Scoreboard()
ball=Ball()
paddle=Paddle()
bricks=Bricks()

FONT = ('arial', 80, 'bold')

# screen setup
screen.tracer(0)
screen.title("Breakout Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)

def input():
    restart_input = screen.textinput("Restart Game", "Do you want to restart the game?\n YES or NO")
    if restart_input == "yes":
        screen.update()
        status.clear()
        scoreboard.reset_scoreboard()
        restart_game()

    elif restart_input == "no" :
        status.clear()
        scoreboard.reset_scoreboard()
        status.color("white")
        status.goto(x=-200, y=100)
        status.write("Good bye!",font=FONT)
        time.sleep(1)
        screen.clear()

    else:
        screen.reset()


def restart_game():
    bricks.brick_wall()
    screen.onkeypress(paddle.move_right, 'Right')
    screen.onkeypress(paddle.move_left, 'Left')
    screen.listen()
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.08)
        ball.move()
        check_collision_with_walls()
        check_collision_with_bricks()
        check_collision_with_paddle()
        if len(bricks_list) == 0 and scoreboard.lives >= 0:
            status.color("white")
            status.goto(x=-200, y=0)
            status.write("you won", font=FONT)

        elif scoreboard.lives < 0:
            status.color("white")
            status.goto(x=-200, y=100)
            status.write("you lose", font=FONT)
            status.hideturtle()
            input()





def check_collision_with_walls():
    if ball.xcor() > 380:
       ball.bounce_back()

    elif ball.xcor() < -380:
        ball.bounce_back()

    elif ball.xcor()==400:
        ball.goto(x=350,y=ball.ycor())

    elif ball.ycor() > 280 :
         ball.bounce_down()

    elif ball.ycor() < -220:
         ball.ball_reset()
         paddle.paddle_reset()
         ball.move()
         scoreboard.remaining_lives()
def check_collision_with_bricks():
    for brk in bricks_list:

        if ball.distance(brk) <30 :
           ball.bounce_brick()
           brk.hideturtle()
           scoreboard.update_score()
           bricks_list.remove(brk)
def check_collision_with_paddle():
    if ball.distance(paddle)<40 and ball.ycor()<-180:
       ball.bounce_up()


restart_game()

screen.exitonclick()
