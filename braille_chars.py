

def get_braille_chars(emboss_char='O', flat_char=' '):
    e = f'{emboss_char}'
    f = f'{flat_char}'
    return {
        'a': f"{e}{f}{f}_{f}{f}{f}",

        'b': f"{e}{e}{f}_{f}{f}{f}",

        'c': f"{e}{f}{f}_{e}{f}{f}",

        'd': f"{e}{f}{f}_{e}{e}{f}",

        'e': f"{e}{f}{f}_{f}{e}{f}",

        'f': f"{e}{e}{f}_{e}{f}{f}",

        'g': f"{e}{e}{f}_{e}{e}{f}",

        'h': f"{e}{e}{f}_{f}{e}{f}",

        'i': f"{f}{e}{f}_{e}{f}{f}",

        'j': f"{f}{e}{f}_{e}{e}{f}",

        'k': f"{e}{f}{e}_{f}{f}{f}",

        'l': f"{e}{e}{e}_{f}{f}{f}",

        'm': f"{e}{f}{e}_{e}{f}{f}",

        'n': f"{e}{f}{e}_{e}{e}{f}",

        'o': f"{e}{f}{e}_{f}{e}{f}",

        'p': f"{e}{e}{e}_{e}{f}{f}",

        'q': f"{e}{e}{e}_{e}{e}{f}",

        'r': f"{e}{e}{e}_{f}{e}{f}",

        's': f"{f}{e}{e}_{e}{f}{f}",

        't': f"{f}{e}{e}_{e}{e}{f}",

        'u': f"{e}{f}{e}_{f}{f}{e}",

        'v': f"{e}{e}{e}_{f}{f}{e}",

        'w': f"{f}{e}{f}_{e}{e}{e}",

        'x': f"{e}{f}{e}_{e}{f}{e}",

        'y': f"{e}{f}{e}_{e}{e}{e}",

        'z': f"{e}{f}{e}_{f}{e}{e}",

        'cap': f"{f}{f}{f}_{f}{f}{e}",

        'num': f"{f}{f}{e}_{e}{e}{e}",

        ' ': f"{f}{f}{f}_{f}{f}{f}",

        '.': f"{f}{e}{f}_{f}{e}{e}",

        ',': f"{f}{e}{f}_{f}{f}{f}",

        '!': f"{f}{e}{e}_{f}{e}{f}",
    }

