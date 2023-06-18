from turtle import Turtle
FONT = ('arial', 20, 'bold')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.score=0
        self.lives=3
        self.penup()
        self.color("white")
        self.goto(x=-50,y=215)
        self.write(f"Score:{self.score}\nLives:{self.lives}",font=FONT)
        self.hideturtle()

    def update_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score:{self.score}\nLives:{self.lives}",font=FONT)

    def remaining_lives(self):
        self.lives-=1
        self.clear()
        self.write(f"Score:{self.score}\nLives:{self.lives}",font=FONT)


    def reset_scoreboard(self):
        self.clear()
        self.score = 0
        self.lives = 3
        self.write(f"Score:{self.score}\nLives:{self.lives}",font=FONT)
