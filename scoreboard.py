from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")
HIGH_SCORE_FILE_LOCATION = "high_score.txt"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open(HIGH_SCORE_FILE_LOCATION) as high_score:
            self.high_score = int(high_score.read())
        # self.high_score=0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setposition(0, 270)
        self.update_scoreboard()

    def ate_food(self):
        self.score += 1

        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score}            High score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.high_score < self.score:
            self.high_score = self.score
            with open(HIGH_SCORE_FILE_LOCATION, mode="w")as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.color("black")
        self.write("GAME OVER", align=ALIGNMENT, font=("Arial", 36, "normal"))
