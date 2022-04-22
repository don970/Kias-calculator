from tkinter.scrolledtext import ScrolledText as st
from tkinter import *
from Math_modules import Lcm, factor, solve, solvef, Orderfractions, Graphing


class layout:
    def __init__(self):
        self.b5 = None
        self.b4 = None
        self.complete = None
        self.textarea = None
        self.b3 = None
        self.b2 = None
        self.b0 = None
        self.b1 = None
        self.l1 = None
        self.l2 = None
        self.e0 = None
        self.e1 = None
        self.input1 = StringVar()
        self.input = StringVar()
        self.l = None
        self.a = None
        self.f = None

    def mainWindow(self, master):
        self.frames(master)
        self.label(self.f)
        self.buttons(self.f)
        self.entry(self.f)
        from packages.TkinterLayouts import Tkinter_Layouts
        self.a = Tkinter_Layouts(self.f)
        a = self.a
        a.relwidget(self.l, 0.03, 1.0, 0.0, 0.890)
        a.relwidget(self.b0, 0.05, 0.3, 0.0, 0.340)
        a.relwidget(self.b1, 0.05, 0.3, 0.3, 0.390)
        a.relwidget(self.b2, 0.05, 0.3, 0.3, 0.340)
        a.relwidget(self.b3, 0.05, 0.3, 0.0, 0.390)
        a.relwidget(self.b4, 0.05, 0.3, 0.6, 0.340)
        a.relwidget(self.b5, 0.05, 0.3, 0.6, 0.390)
        a.textarea(self.textarea, 0.3, 1.0)
        self.textarea.config(state='disabled')
        pass

    def solveforx(self):
        a = solve()
        a.start()
        self.complete = True
        pass

    def lcm(self):
        a = Lcm()
        a.start(1, 1, 1)
        self.complete = True
        pass

    def factor(self):
        a = factor()
        a.start()
        self.complete = True
        pass

    def fractions(self):
        a = solvef()
        a.start()
        self.complete = True
        pass

    def orderfractions(self):
        a = Orderfractions()
        a.start()
        self.complete = True
        pass

    def linear_equations(self):
        a = Graphing()
        a.start()
        self.complete = True

    def frames(self, where):
        self.f = Frame(where)
        pass

    def buttons(self, where):
        self.b0 = Button(where, text='Least common multiple', command=self.lcm)
        self.b1 = Button(where, text='fractions', command=self.fractions)
        self.b2 = Button(where, text='factor', command=self.factor)
        self.b3 = Button(where, text='solve for x', command=self.solveforx)
        self.b4 = Button(where, text='order fractions', command=self.orderfractions)
        self.b5 = Button(where, text="linear equation", command=self.linear_equations)
        pass

    def entry(self, where):
        self.e0 = Entry(where, textvariable=self.input)
        self.e1 = Entry(where, textvariable=self.input1)
        self.textarea = st(where)
        pass

    def label(self, where):
        self.l = Label(where, text="Author Donald Ford")
        self.l1 = Label(where, text="enter first number")
        self.l2 = Label(where, text="enter second number")
        pass

    def enter(self, a):
        self.textarea.config(state='normal')
        self.textarea.insert(END, str(a) + "\n")
        self.textarea.config(state='disabled')

    # code for input make in to package later
    def Input(self, mode: int, cmd, text):
        if mode == 0:  # compare two numbers or take multiple inputs
            self.a.relwidget(self.l2, 0.07, 0.5, 0.500, 0.450)
            self.a.relwidget(self.l1, 0.07, 0.5, 0.0, 0.450)
            self.a.relwidget(self.e1, 0.05, 0.5, 0.50, 0.500)
            self.a.relwidget(self.e0, 0.05, 0.5, 0.0, 0.500)
            self.a.relwidget(self.b1, 0.07, 0.1, 0.450, 0.560)
        elif mode == 1:  # enter equation
            self.b1 = Button(text='submit', command=cmd)
            self.a.relwidget(self.l1, 0.07, 0.5, 0.5, 0.450)
            self.a.relwidget(self.e0, 0.05, 0.5, 0.5, 0.500)
            self.a.relwidget(self.b1, 0.07, 0.1, 0.450, 0.560)
        elif mode == 2:
            self.l1 = Label(text=text)
            self.b1 = Button(text='submit', command=cmd)
            self.a.relwidget(self.l1, 0.07, 0.5, 0.5, 0.450)
            self.a.relwidget(self.e0, 0.05, 0.5, 0.5, 0.520)
            self.a.relwidget(self.b1, 0.07, 0.1, 0.450, 0.580)
