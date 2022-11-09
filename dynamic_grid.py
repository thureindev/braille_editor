import tkinter as tk


class DynamicGrid(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        self.columns = None
        self.bind('<Configure>', self.regrid)

    def regrid(self, event=None):
        width = self.winfo_width()
        slaves = self.grid_slaves()
        max_width = max(slave.winfo_width() for slave in slaves)
        cols = width // max_width
        if cols == self.columns:  # if the column number has not changed, abort
            return
        for i, slave in enumerate(slaves):
            slave.grid_forget()
            slave.grid(row=i // cols, column=i % cols)
        self.columns = cols


class BrailleBlock(tk.Frame):
    def __init__(self, master=None,  txt="...", **kwargs):
        tk.Frame.__init__(self, master, bd=5, relief=tk.RAISED, **kwargs)

        tk.Label(self, text=txt).pack(pady=10)

        # tk.Label(self, text="name").pack(pady=10)
        # tk.Label(self, text=" info ........ info ").pack(pady=10)
        # tk.Label(self, text="data\n" * 5).pack(pady=10)


def start_grid(root, text_list):
    # add frame
    frame = DynamicGrid(root)
    frame.pack(fill=tk.BOTH, expand=True)

    # BrailleBlock(frame).grid()  # use normal grid parameters to set up initial layout
    # BrailleBlock(frame).grid(column=1)
    # BrailleBlock(frame).grid(column=2)
    # BrailleBlock(frame).grid()
    # BrailleBlock(frame).grid()
    # BrailleBlock(frame).grid()

    len_text_list = len(text_list)

    for txt in text_list:
        BrailleBlock(frame, txt=txt).grid()

    root.mainloop()


# if __name__ == '__main__':
#     start_grid()
