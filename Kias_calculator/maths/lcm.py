from tkinter import *
from tkinter.scrolledtext import ScrolledText
from time import sleep


class lcm:
    def __init__(self):
        self.complete = False

    def lcm(self, x, y):
        # choose the greater number
        if x > y:
            greater = x
        else:
            greater = y

        while True:
            if (greater % x == 0) and (greater % y == 0):
                lcm1 = greater
                lcm1 = lcm1
                lmc2 = f"lowest common multiple = {str(lcm1)} \n"
                return lmc2
            greater += 1
