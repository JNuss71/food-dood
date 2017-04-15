from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
from getreqtest import search_calls
from logos import getlogo

class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Example")
        self.master.rowconfigure(5, weight=1)
        self.master.columnconfigure(5, weight=1)
        self.grid(sticky=W+E+N+S)

        self.button = Button(self, text="Browse", command=self.load_file, width=10)
        self.button.grid(row=1, column=0, sticky=W)

    def load_file(self):
        fname = askopenfilename()
        print(search_calls(getlogo(fname)))


if __name__ == "__main__":
    MyFrame().mainloop()