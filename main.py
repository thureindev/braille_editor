import turtle
import ui_settings as ui

from braille_grapher import BrailleGrapher
from braille_chars import get_braille_chars

brailles = get_braille_chars()


def main():
    grapher = BrailleGrapher(text="abcde fghij klmno pqrst")

    grapher.write_emboss()

    user_text = input('Enter Text to Translate to Braille: ')
    # default line break is 30 chars
    text_to_braille(user_text)


def text_to_braille(txt, line_break=30):
    text = [*txt.lower()]
    top_line = []
    mid_line = []
    bot_line = []
    for c in text:
        split_brailles = brailles[c].split('_')
        top_line.append(split_brailles[0])
        mid_line.append(split_brailles[1])
        bot_line.append(split_brailles[2])

    #    # NORMAL Braille print
    print("\nBraille Format: \n")
    index = 0
    line_len = len(top_line)
    while index < line_len:
        # index create terminal index for line break
        if index + line_break < line_len:
            terminal = index + line_break
        else:
            terminal = line_len

        for i in range(index, terminal):
            print(top_line[i], end=" ")
        print('')  # line break
        for ii in range(index, terminal):
            print(mid_line[ii], end=" ")
        print('')  # line break
        for iii in range(index, terminal):
            print(bot_line[iii], end=" ")
        print('\n')  # line break
        index = terminal

    #    # MIRRORED Braille print
    print("MIRRORED (Useful for punching out braille dots): \n")
    index = 0
    line_len = len(top_line)
    while index < line_len:
        # index create terminal index for line break
        if index + line_break < line_len:
            terminal = index + line_break - 1
        else:
            terminal = line_len

        for i in range(terminal - 1, index - 1, -1):
            print(top_line[i], end=" ")
        print('')  # line break
        for ii in range(terminal - 1, index - 1, -1):
            print(mid_line[ii], end=" ")
        print('')  # line break
        for iii in range(terminal - 1, index - 1, -1):
            print(bot_line[iii], end=" ")
        print('\n')  # line break
        index = terminal


if __name__ == '__main__':
    screen = turtle.Screen()
    # screen.tracer(0)
    # time.sleep(gs.CLOCK_TICK)
    # screen.update()

    screen.title("Braille")
    screen.bgcolor("#F0F0F0")

    screen.setup(ui.SCREEN_WIDTH, ui.SCREEN_HEIGHT)
    main()
    screen.exitonclick()
