from turtle import Turtle
from braille_chars import get_braille_chars

EMBOSS = "O"
FLAT = "-"

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

        braille_emboss_blocks = []

        for c in self.text:
            try:
                if c.isupper():
                    braille_text = f"{brailles['cap']}_{brailles[c.lower()]}"
                elif c.isdigit():
                    num = int(c)
                    chars = "jabcdefghi"
                    braille_text = f"{brailles['num']}_{brailles[chars[num]]}"
                else:
                    braille_text = brailles[c]
            except:
                braille_text = brailles[" "]
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
            for line in range(0, len(braille_lines), 2):
                self.grapher.setpos(self.grapher.xcor() + 20, pos_y)

                line_char = ""

                for i in range(0, 3):
                    line_char += f"{braille_lines[line][i]}{braille_lines[line + 1][i]}\n"

                # for letter in braille_lines[line]:
                #     line_char += f"{letter}\n"

                braille_emboss_blocks.append(line_char)

        print("done")
        return braille_emboss_blocks
