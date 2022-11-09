import time
import ui_settings as ui

import dynamic_grid as dg

from braille_grapher import BrailleGrapher
from braille_chars import get_braille_chars

brailles = get_braille_chars()


def main():
    grapher = BrailleGrapher(text="abcde fghij klmno pqrst uvwxy z .,!")

    translated = grapher.write_emboss()

    dg.start_grid(translated)


if __name__ == '__main__':
    main()
