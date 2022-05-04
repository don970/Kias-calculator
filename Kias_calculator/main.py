from tkinter import *
from layout import layout
from layout import os_check

a = Tk()
c = os_check(a, '600x650')
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
