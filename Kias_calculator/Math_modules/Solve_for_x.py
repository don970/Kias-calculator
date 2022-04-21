from tkinter import *
from tkinter.scrolledtext import ScrolledText as st
from packages import Tkinter_Layouts, Functions


class solve:
    def __init__(self):
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
        self.a.title('Solve for x')
        self.a.geometry("450x480")
        self.frames(self.a)
        f = self.f
        self.b = Tkinter_Layouts(f)
        self.label(f)
        self.buttons(f)
        self.entry(f)
        self.Input(1)
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
        self.solve_for_x(str(e0))

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
        self.l1 = Label(where, text="enter equation as 2 x(+)21/5=3")
        self.l2 = Label(where, text="enter second number")
        pass

    def enter(self, a):
        self.textarea.config(state='normal')
        self.textarea.insert(END, str(a) + "\n")
        self.textarea.config(state='disabled')

        # code for input make in to package later

    def Input(self, mode):
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
            self.b.relwidget(self.l1, 0.07, 0.5, 0.5, 0.450)
            self.b.relwidget(self.e0, 0.05, 0.5, 0.5, 0.520)
            self.b.relwidget(self.b1, 0.07, 0.1, 0.450, 0.580)

    def solve_for_x(self, aa):
        try:
            eq = aa
            eq1 = eq.split()  # split first number from rest
            l = ['(+)', '(-)']
            if l[0] in eq1[1].strip('\n'):
                eq2 = eq1[1].split(l[0])
                self.enter('finding type of equation:' + str(eq2))
                eq3 = eq2[1].split('=')
                self.enter('splitting equation up' + str(eq2))
                eq4 = eq3[0].split('/')
                self.enter("further splitting equation")
                a = int(int(eq3[1]) * int(eq4[1]))
                self.enter(f'multiplying {str(eq3[1])} and {str(eq4[1])} = {str(a)}')
                self.enter(f'subtracting {str(a)} and {str(eq4[0])} = {int(a) - int(eq4[0])}')
                a = a - int(eq4[0])
                v = 1
                self.enter('finding bigger number')
                d = int(a) / int(eq1[0])
                if int(a) > int(eq1[0]):
                    d = int(eq1[0]) / int(a)
                    v = 0
                if v == 0:
                    self.enter(f'dividing {str(eq1[0])} and {str(a)}')
                    answer = f'{str(eq2[0])} = {str(int(d))}'
                    self.enter(answer)
                else:
                    d = int(a) / int(eq1[0])
                    self.enter(f'dividing {str(a)} and {str(eq1[0])}')
                    answer = f'{str(eq2[0])} = {str(int(d))}'
                    self.enter(answer)
        except ValueError and TypeError as e:
            self.enter(e)
