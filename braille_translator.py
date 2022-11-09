from braille_chars import get_braille_chars

EMBOSS = "O"
FLAT = "-"

brailles = get_braille_chars(emboss_char=EMBOSS, flat_char=FLAT)


class TextToBrailleTranslator:
    """Class to handle braille translation. language check and translation all packed in this class"""
    def __init__(self, emboss=EMBOSS, flat=FLAT, text="", lang="eng"):
        self.braille_chars = brailles
        self.emboss = emboss
        self.flat = flat

        self.text = text
        self.lang = lang

    def translate(self):
        """Return a list of braille blocks translated from text"""

        # list to return
        braille_emboss_blocks = []

        # since brailles fro numbers 1, 2, 3, ... are equal to a, b, c, ...
        alpha_to_num = "jabcdefghi"

        for ch in self.text:
            try:
                # insert prefix for CAPITAL letters
                if ch.isupper():
                    braille_text = f"{brailles['cap']}_{brailles[ch.lower()]}"

                # insert prefix for Numerical
                elif ch.isdigit():
                    num = int(ch)
                    braille_text = f"{brailles['num']}_{brailles[alpha_to_num[num]]}"

                # registered brailles
                else:
                    braille_text = brailles[ch]

            # if text char is not yet registered in braille dictionary. insert a 'space' braille
            except:
                braille_text = brailles[" "]

            # Handling prefixes DONE ------ ------

            # split into lists
            try:
                braille_lines = braille_text.split("_")

                # normal braille lines = 2, prefixed braille lines = 4
                for line in range(0, len(braille_lines), 2):

                    line_char = ""

                    # 2 braille lines put in frame block together
                    for i in range(0, 3):
                        line_char += f"{braille_lines[line][i]}{braille_lines[line + 1][i]}\n"

                    # append to blocks list
                    braille_emboss_blocks.append(line_char)

            except:
                print("Error! Invalid format in braille dict!")

        return braille_emboss_blocks
