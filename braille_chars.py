

def get_braille_chars(emboss_char='O', flat_char=' '):
    e = f'{emboss_char}'
    f = f'{flat_char}'
    return {
        'a': f"{e}{f}{f}_{f}{f}{f}",

        'b': f"{e}{e}{f}_{f}{f}{f}",

        'c': f"{e}{f}{e}_{f}{f}{f}",

        'c': f"{e}{e}{f}_{f}{f}{f}",

        'd': f"{e}{e}{e}_{f}{f}{f}",

        'e': f"{e}{f}{e}_{f}{f}{f}",

        'f': f"{e}{f}{e}_{f}{e}{f}",

        'g': f"{e}{e}{e}_{f}{e}{f}",

        'h': f"{e}{e}{f}_{f}{e}{f}",

        'i': f"{f}{f}{e}_{f}{e}{f}",

        'j': f"{f}{e}{e}_{f}{e}{f}",

        'k': f"{e}{f}{f}_{e}{f}{f}",

        'l': f"{e}{f}{f}_{e}{e}{f}",

        'm': f"{e}{f}{e}_{f}{e}{f}",

        'n': f"{e}{e}{e}_{f}{e}{f}",

        'o': f"{e}{e}{f}_{e}{f}{f}",

        'p': f"{e}{f}{e}_{e}{e}{f}",

        'q': f"{e}{e}{e}_{e}{e}{f}",

        'r': f"{e}{e}{f}_{e}{e}{f}",

        's': f"{f}{f}{e}_{e}{e}{f}",

        't': f"{f}{e}{e}_{e}{e}{f}",

        'u': f"{e}{f}{f}_{e}{f}{e}",

        'v': f"{e}{f}{f}_{e}{e}{e}",

        'w': f"{f}{e}{e}_{f}{e}{e}",

        'x': f"{e}{f}{e}_{e}{f}{e}",

        'y': f"{e}{e}{e}_{e}{f}{e}",

        'z': f"{e}{e}{f}_{e}{f}{e}",

        'cap': f"{f}{f}{f}_{f}{f}{e}",

        'num': f"{f}{f}{e}_{e}{e}{e}",

        ' ': f"{f}{f}{f}_{f}{f}{f}",

        '.': f"{f}{f}{f}_{f}{f}{f}",

        ',': f"{f}{f}{f}_{f}{f}{f}",

        "'": f"{f}{f}{f}_{f}{f}{f}",

        '!': f"{f}{e}{f}_{e}{e}{f}",
    }

