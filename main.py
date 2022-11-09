import tkinter as tk
import dynamic_grid as dg
from braille_translator import TextToBrailleTranslator

import ui_settings as ui


def main():
    # create Tk windows
    root_window = tk.Tk(className='_Braille Editor')
    # set window size
    root_window.geometry(f"{ui.SCREEN_WIDTH}x{ui.SCREEN_HEIGHT}")

    # Take user input   #   #   #   #   #

    # Initialize a Label to display the User Input
    label = tk.Label(root_window, text="", font=("Courier 12 bold"))
    label.pack()
    label.configure(text="Enter text to translate to Braille")

    # Create an Entry widget to accept User Input
    entry = tk.Entry(root_window, width=40)
    entry.focus_set()
    entry.pack()

    def display_braille():
        user_text = entry.get()

        for widgets in root_window.winfo_children():
            if widgets.widgetName == "frame":
                # print(widgets.widgetName)
                widgets.destroy()

        # create translator instance
        translator = TextToBrailleTranslator(text=user_text)

        # get translated braille to display
        translated_braille = translator.translate()

        # start display in auto grid windows
        dg.start_grid(root_window, translated_braille)

    # Create a Button to validate Entry Widget
    tk.Button(root_window, text="Translate", width=20, command=display_braille).pack(pady=20)

    root_window.mainloop()


if __name__ == '__main__':
    main()
