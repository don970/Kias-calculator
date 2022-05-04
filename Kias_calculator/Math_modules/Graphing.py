from tkinter import *
from tkinter.scrolledtext import ScrolledText as st
from packages import Tkinter_Layouts, Functions
from layout.os_dep import os_check
b = None


class Graphing:
    def __init__(self):
        self.complete = False
        self.data = None
        self.int2 = None
        self.int1 = None
        self.a1 = None
        self.answer = None
        self.lcm1 = None
        self.greater = None
        self.place = None
        self.b = []
        self.f = None
        self.textarea = None
        self.e0 = None
        self.e1 = None
        self.input1 = StringVar()
        self.input = StringVar()
        self.l = []
        self.a = None
        self.f = None

    def start(self):
        # create tk window
        self.a = Tk()
        # name the window
        self.a.title('Graphing')
        # custom code that sets the window size
        c = os_check(self.a, '600x650')
        # create a frame and place it in the root tkinter object
        self.frames(self.a)
        # place frame on window
        self.place = Tkinter_Layouts(self.f)
        # create the labels, buttons and entry objects and places them
        self.Input(1, None, None)

    def end(self, a):
        end = Functions()
        end.tk_end(a)
        self.complete = True

    def submit(self, a):
        self.place.relwidget(self.e0, 0.07, 0.7, 0.1, 0.530)
        if a == 1:
            self.solve(1, self.e0.get())
        else:
            self.Input(0, 'submit', self.f)

    def frames(self, where):
        self.f = Frame(where)
        pass

    def buttons(self, where, text: list, cmd: list):
        x = 0
        self.b = []
        while x < len(text) and x < len(cmd):
            for i in range(0, len(cmd)):
                try:
                    self.b.append(Button(where, text=text[x], command=lambda: self.submit(x + 1)))
                    if x <= len(cmd) and x <= len(text):
                        x += 1
                except IndexError:
                    return self.b
            return self.b

    def entry(self, where):
        self.e0 = Entry(where, textvariable=self.input)
        self.e1 = Entry(where, textvariable=self.input1)
        self.textarea = st(where)
        pass

    def label(self, where, text: list):
        x = 0
        for i in text:
            self.l.append(Label(where, text=text[x]))
            x += 1
        return self.l
        pass

    def enter(self, a):
        self.textarea.config(state='normal')
        self.textarea.insert(END, str(a) + "\n")
        self.textarea.config(state='disabled')

        # code for input make in to package later

    def Input(self, mode, text, where):
        # if the mode is equal to 0 we want to display the buttons, labels and entry files
        # create entrys
        self.entry(self.f)
        if mode == 0:
            buttons = []
            labels = []
            # create labels and saves in a list
            labels.append(self.label(self.f, ['enter equation as y=2x(+)-1', 'enter (x,y) from chart']))
            # create buttons
            buttons.append(self.buttons(self.f, ['submit', None], [0, 0]))
            # set some variables for so we can munipulate each of them with math
            h = 0.07
            w = 0.5
            rx = 0.0
            ry = 0.44
            # for the number of items in the list labels
            x = 0
            for i in labels:
                # place labels
                self.place.relwidget(str(labels[x]), h, w, rx, ry)
                x += 1
                rx += 0.5

            x = 0
            for i in buttons:
                self.place.relwidget(buttons[x], 0.05, 0.1, 0.450, 0.7)
                x += 1

        elif mode == 1:  # enter equation  + 8 on last
            buttons = self.buttons(self.f, ['Identifying solutions to a linear equation in two variables', 'Graphing a linear equation of the form y = mx'], [0, 0])
            x = 0
            xy = 0.0
            for i in buttons:
                try:
                    self.place.relwidget(buttons[x], 0.07, 1.0, 0.0, xy)
                    x += 1
                    xy += 0.07
                except IndexError:
                    pass

    def lcm(self, x, y):
        # choose the greater number
        if x > y:
            greater = x
            self.greater = greater
        else:
            greater = y
            self.greater = greater

        while True:
            if (greater % x == 0) and (greater % y == 0):
                lcm1 = greater
                lcm1 = lcm1
                return int(lcm1)
            greater += 1

    def print(self, *a):
        self.textarea.insert(END, str(a) + '\n')
        pass

    def solve(self, mode, a):
        modes = [1, 2, 3]
        # modes
        # 1 = Using y=mx+place with a table. Example would be like having the slope intercept of a line y=-2x-1
        # with a table like
        #                    |x|   y=-2x-1   (x,y)
        #                   | 0 | y=-2(0)-1 | (0,-1) |
        #                   | 1 | y=-2(1)-1 | (1,-1) |
        #                   | 2 | y=-2(2)-1 | (2,-1) |
        #                   | 3 | y=-2(3)-1 | (3,-1) |
        #
        if mode in modes:
            if mode == 1:
                data = self.Input(0, 'enter (x,y) from chart', self.f)
                # answer = int(c) * int(a) - int(d) * int(place)
                print(self.data)
