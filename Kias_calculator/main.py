from tkinter import *
from layout import layout

a = Tk()
a.geometry('600x600')


class Start:
    def __init__(self, master):
        self.complete = None
        self.onStart(master)

    def onStart(self, master):
        s = layout()
        s.mainWindow(master)
        self.complete = True
        return self.complete


Start(a)
a.title('calculator')
a.mainloop()
