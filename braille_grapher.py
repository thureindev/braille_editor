from turtle import Turtle
from braille_chars import get_braille_chars

EMBOSS = "O"
FLAT = " "

brailles = get_braille_chars(emboss_char=EMBOSS, flat_char=FLAT)


class BrailleGrapher:
    def __init__(self, emboss=EMBOSS, flat=FLAT, text=""):
        self.braille_chars = brailles
        self.emboss = emboss
        self.flat = flat

        self.text = text

        self.grapher = Turtle()
        self.grapher.hideturtle()
        self.grapher.penup()
        self.grapher.color("black")
        self.grapher.pencolor("black")
        self.grapher.setpos(-600, 400)
        # self.grapher.pendown()
        # self.grapher.goto(-400, 300)

        self.grapher.speed(0)

    def write_emboss(self):
        for c in self.text:

            try:
                braille_text = brailles[c]
            except:
                print("Error")
            else:
                pass
            finally:
                pass

            try:
                braille_lines = braille_text.split("_")
            except:
                print("Error")

            pos_y = 300
            self.grapher.setx(self.grapher.xcor() + 10)
            for line in braille_lines:
                self.grapher.setpos(self.grapher.xcor() + 20, pos_y)
                for letter in line:
                    if letter == self.emboss:
                        self.grapher.pendown()
                        self.grapher.pencolor('black')
                        self.grapher.circle(5)
                        self.grapher.penup()
                        print(letter)
                    else:
                        self.grapher.pendown()
                        self.grapher.pencolor('red')
                        self.grapher.circle(1)
                        self.grapher.penup()
                        print(letter)

                    self.grapher.sety(self.grapher.ycor() - 20)
