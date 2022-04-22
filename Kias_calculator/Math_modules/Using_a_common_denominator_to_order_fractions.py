from tkinter import *
from tkinter.scrolledtext import ScrolledText as st
from packages import Tkinter_Layouts, Functions
from .lcm import Lcm as lcm


class Orderfractions:
    def __init__(self):
        self.answer = None
        self.b = None
        self.f = None
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

    def start(self):
        self.a = Tk()
        self.a.title('factor')
        width = self.a.winfo_screenwidth()
        height = self.a.winfo_screenheight()
        self.a.geometry(f'{str(width)}x{str(height)}')
        self.frames(self.a)
        f = self.f
        self.b = Tkinter_Layouts(f)
        self.label(f)
        self.buttons(f)
        self.entry(f)
        self.Input(1, None, self.submit)
        self.b.textarea(self.textarea, 0.3, 1.0)
        self.b.relwidget(self.l, 0.03, 1.0, 0.0, 0.890)
        self.b.relwidget(self.b1, 0.07, 0.2, 0.4, 0.700)
        self.b.relwidget(self.b2, 0.07, 0.2, 0.0, 0.700)
        self.a.mainloop()

    def end(self):
        end = Functions()
        end.tk_end(self.a)

    def submit(self):
        e0 = self.e0.get()
        self.order_fractions(e0)
        self.enter(str(self.answer))

    def frames(self, where):
        self.f = Frame(where)
        pass

    def buttons(self, where):
        self.b1 = Button(where, text='submit', command=self.submit)
        self.b2 = Button(where, text="exit", command=self.end)
        pass

    def entry(self, where):
        self.e0 = Entry(where, textvariable=self.input)
        self.e1 = Entry(where, textvariable=self.input1)
        self.textarea = st(where)
        pass

    def label(self, where):
        self.l = Label(where, text="Author Donald Ford")
        self.l1 = Label(where, text="enter fractions to check")
        self.l2 = Label(where, text="enter second number")
        pass

    def enter(self, a):
        self.textarea.config(state='normal')
        self.textarea.insert(END, str(a) + "\n")
        self.textarea.config(state='disabled')

        # code for input make in to package later

    def Input(self, mode: int, cmd, text):
        if mode == 0:  # compare two numbers or take multiple inputs
            self.b.relwidget(self.l2, 0.07, 0.5, 0.500, 0.450)
            self.b.relwidget(self.l1, 0.07, 0.5, 0.0, 0.450)
            self.b.relwidget(self.e1, 0.05, 0.5, 0.50, 0.500)
            self.b.relwidget(self.e0, 0.05, 0.5, 0.0, 0.500)
            self.b.relwidget(self.b1, 0.07, 0.1, 0.450, 0.600)
        elif mode == 1:  # enter equation
            self.b.relwidget(self.l1, 0.09, 0.9, 0.0, 0.450)
            self.b.relwidget(self.e0, 0.07, 0.7, 0.1, 0.530)
            self.b.relwidget(self.b1, 0.07, 0.1, 0.450, 0.560)
        elif mode == 2:
            self.l1 = Label(text=text)
            self.b1 = Button(text='submit', command=cmd)
            self.b.relwidget(self.l1, 0.07, 0.5, 0.5, 0.450)
            self.b.relwidget(self.e0, 0.05, 0.5, 0.5, 0.520)
            self.b.relwidget(self.b1, 0.07, 0.1, 0.450, 0.580)

    def order_fractions(self, a9):
        if True:
            try:
                e, q = a9.split()
                e1 = e.split('/')
                q1 = q.split('/')
                print(e1, q1)
                a1 = lcm()
                a1 = a1.start(0, int(e1[1]), int(q1[1]))
                a0 = int(int(a1) / int(e1[1]))
                a1 = int(int(a1) / int(q1[1]))
                b = int(int(a1) * int(q1[0]))
                c = int(int(a0) * int(e1[0]))
                if int(c) > int(b):
                    self.answer = f'{str(c)}/{str(a1)} > {str(b)}/{str(a1)}'
                    self.enter(self.answer)
                else:
                    self.answer = f'{str(c)}/{str(a1)} < {str(b)}/{str(a1)}'
                    self.enter(self.answer)
            except TypeError and ValueError as e:
                self.enter(e)
