from tkinter import *
from tkinter.scrolledtext import ScrolledText as st
from packages import Tkinter_Layouts, Functions
from .Factor import factor
b = None


def sleep(a):
    pass


class solvef:
    def __init__(self):
        self.a1 = None
        self.answer = None
        self.lcm1 = None
        self.greater = None
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
        self.a.title('fraction')
        self.a.geometry("500x500")
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
        self.solve(str(e0))

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
        self.l1 = Label(where, text="enter equation as y/x (+, -, *, %) y/x  \n If negative write as -x/y + -x/y")
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
            self.b.relwidget(self.l1, 0.1, 0.9, 0.0, 0.450)
            self.b.relwidget(self.e0, 0.07, 0.7, 0.1, 0.530)
            self.b.relwidget(self.b1, 0.07, 0.1, 0.450, 0.560)
        elif mode == 2:
            self.b.relwidget(self.l1, 0.07, 0.5, 0.5, 0.450)
            self.b.relwidget(self.e0, 0.05, 0.5, 0.5, 0.520)
            self.b.relwidget(self.b1, 0.07, 0.1, 0.450, 0.580)

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

    def solve(self, q):
        if True:
            al = ['(+)', "(-)", "(*)", "(%)"]
            eq = q
            if al[0] in eq:
                try:
                    self.print('using addition')
                    a0, b0 = eq.split(al[0])
                    self.print(f'splitting equation up')
                    self.print(f'Fraction number 1 = {a0[0]}/{a0[1]}')
                    self.print(f'Fraction number 2 = {b0[0]}/{b0[1]}')
                    a1 = a0.split('/')
                    b1 = b0.split('/')
                    self.print('breaking down fractions into individual numbers')
                    self.print(a1)
                    self.print(b1)
                    self.lcm1 = self.lcm(int(a1[1]), int(b1[1]))
                    lcm1 = int(self.lcm1)
                    if int(a1[1] > b1[1]):
                        a2 = b1
                        b2 = a1
                        self.print(f'bigger number = {b2}')
                        # self.print(a2, b2)
                        sleep(1)
                        m = int(a2[1]) / int(b2[1])
                        self.print(f'{str(a2[1])} / {str(b2[1])}')
                        sleep(1)
                        if int(m) == m and isinstance(m, float):
                            m = int(m)
                            self.print(f"m = {m}")
                            sleep(1)
                            self.print(f"{b2[1]} * m for nominator and {b2[1]} * m for denominator")
                            sleep(1)
                            frac1 = [int(b2[0]) * m, int(b2[1]) * m]
                            sleep(1)
                            self.print(f"fraction number one = {frac1}")
                            sleep(1)
                            top = int(frac1[0]) + int(a2[0])
                            sleep(1)
                            self.print(f"{str(frac1[0])}/{str(frac1[1])} + {str(a2[0])}/{str(a2[1])}")
                            sleep(1)
                            bottom = int(frac1[1])
                            sleep(1)
                            self.print(f"denominator  = {bottom}")
                            sleep(1)
                            answer = f'answer = {str(top)} / {str(bottom)}'
                            self.print(f"answer = {answer}")
                        else:
                            m = int(lcm1)
                            sleep(1)
                            self.print(f'getting lowest common multiple {lcm1}')
                            d = int(lcm1) / int(b2[1])
                            d1 = int(lcm1) / int(a2[1])
                            sleep(1)
                            self.print(f"{str(a2[0])} * {str(d1)} / {str(a2[1])} * {str(d1)}")
                            frac1 = [int(a2[0]) * int(d1), int(a2[1]) * int(d1)]
                            self.print(f"{str(frac1[0])} / {str(frac1[1])}")
                            sleep(1)
                            self.print(f"{str(b2[0])} * {str(d)} / {str(b2[1])} * {str(d)}")
                            frac2 = [int(b2[0]) * int(d), int(b2[1]) * int(d)]
                            sleep(1)
                            self.print(f"{str(frac2[0])} / {str(frac2[1])}")
                            top = int(frac1[0]) + int(frac2[0])
                            sleep(1)
                            self.print(f'top = {str(frac1[0])} + {str(frac2[0])}')
                            sleep(1)
                            bottom = m
                            self.print(f'whole fraction = {str(top)}/{str(bottom)}')
                            answer = f'answer = {str(top)} / {str(bottom)}'
                            sleep(1)
                            rem = int(top) - int(bottom)
                            self.print(answer, rem)
                    else:
                        a2 = a1
                        b2 = b1
                        self.print(a2, b2)
                        m = int(a2[1]) / int(b2[1])
                        if int(m) == m and isinstance(m, float):
                            m = int(m)
                            self.print(f"m = {m}")
                            sleep(1)
                            self.print(f"{a2[1]} * {str(m)} for nominator and {a2[1]} * {str(m)} for denominator")
                            sleep(1)
                            frac1 = [int(b2[0]) * m, int(b2[1]) * m]
                            self.print(f"fraction number one = {frac1}")
                            sleep(1)
                            top = int(frac1[0]) + int(a2[0])
                            self.print(f"{str(frac1[0])}/{str(frac1[1])} + {str(a2[0])}/{str(a2[1])}")
                            sleep(1)
                            bottom = int(frac1[1])
                            self.print(f"denominator  = {bottom}")
                            sleep(1)
                            answer = f'answer = {str(top)} / {str(bottom)}'
                            rem = int(top) - int(bottom)
                            self.print(answer, rem)
                        else:
                            m = int(lcm1)
                            self.print(f'getting lowest common multiple {lcm1}')
                            sleep(1)
                            d = int(lcm1) / int(b2[1])
                            d1 = int(lcm1) / int(a2[1])
                            self.print(f"{str(a2[0])} * {str(d1)} / {str(a2[1])} * {str(d1)}")
                            frac1 = [int(a2[0]) * int(d1), int(a2[1]) * int(d1)]
                            self.print(f"{str(frac1[0])} / {str(frac1[1])}")
                            sleep(1)
                            self.print(f"{str(b2[0])} * {str(d)} / {str(b2[1])} * {str(d)}")
                            frac2 = [int(b2[0]) * int(d), int(b2[1]) * int(d)]
                            self.print(f"{str(frac2[0])} / {str(frac2[1])}")
                            sleep(1)
                            top = int(frac1[0]) + int(frac2[0])
                            self.print(f'top = {str(frac1[0])} + {str(frac2[0])}')
                            sleep(1)
                            bottom = m
                            self.print(f'whole fraction = {str(top)}/{str(bottom)}')
                            sleep(1)
                            answer = f'answer = {str(top)} / {str(bottom)}'
                            rem = int(top) - int(bottom)
                            self.print(answer, rem)
                except TypeError and ValueError as e:
                    self.print(e)
            elif al[1] in eq:
                try:
                    self.print('using subtraction')
                    a0, b0 = eq.split(al[1])
                    a1 = a0.split('/')
                    b1 = b0.split('/')
                    lcm1 = self.lcm(int(a1[1]), int(b1[1]))
                    self.print('finding bigger number')
                    if int(a1[1] < b1[1]):
                        a2 = b1
                        b2 = a1
                        self.print(a2, b2)
                        m = int(a2[1]) / int(b2[1])
                        if m == m and isinstance(m, float):
                            m = int(m)
                            self.print(f"m = {m}, variable = {m}")
                            sleep(1)
                            self.print(f"{b2[0]} * {m} for nominator and {b2[1]} * {m} for denominator")
                            frac1 = [int(b2[0]) * m, int(b2[1]) * m]
                            self.print(f"fraction number one = {frac1}")
                            sleep(1)
                            top = int(frac1[0]) - int(a2[0])
                            self.print(f"{str(frac1[0])}/{str(frac1[1])} - {str(a2[0])}/{str(a2[1])}")
                            sleep(1)
                            bottom = int(frac1[1])
                            self.print(f"denominator  = {bottom}")
                            sleep(1)
                            answer = f'answer = {str(top)} / {str(bottom)}'
                            rem = int(top) - int(bottom)
                            self.print(answer, rem)
                        else:
                            m = int(self.lcm1)
                            self.print(f'getting lowest common multiple {lcm1}')
                            d = int(lcm1) / int(b2[1])
                            d1 = int(lcm1) / int(a2[1])
                            frac1 = [int(a2[0]) * int(d1), int(a2[1]) * int(d1)]
                            sleep(1)
                            self.print(f"{str(frac1[0])} / {str(frac1[1])}")
                            frac2 = [int(b2[0]) * int(d), int(b2[1]) * int(d)]
                            sleep(1)
                            self.print(f"{str(frac2[0])} / {str(frac2[1])}")
                            top = int(frac1[0]) - int(frac2[0])
                            self.print(f'top = {str(frac1[0])} - {str(frac2[0])}')
                            sleep(1)
                            bottom = m
                            self.print(f'whole fraction = {str(top)}/{str(bottom)}')
                            answer = f'answer = {str(top)} / {str(bottom)}'
                            sleep(1)
                            rem = int(top) - int(bottom)
                            self.print(answer, rem)
                    else:
                        a2 = a1
                        b2 = b1
                        self.print(a2, b2)
                        m = int(a2[1]) / int(b2[1])
                        if int(m) == m and isinstance(m, float):
                            m = int(m)
                            self.print(f"m = {m}")
                            sleep(1)
                            self.print(f"{b2[0]} * {m} for nominator and {b2[1]} * {m} for denominator")
                            frac1 = [int(b2[0]) * m, int(b2[1]) * m]
                            self.print(f"fraction number one = {frac1}")
                            sleep(1)
                            top = int(frac1[0]) - int(a2[0])
                            self.print(f"{str(frac1[0])}/{str(frac1[1])} - {str(a2[0])}/{str(a2[1])}")
                            sleep(1)
                            bottom = int(frac1[1])
                            self.print(f"denominator  = {bottom}")
                            sleep(1)
                            answer = f'answer = {str(top)} / {str(bottom)}'
                            rem = int(top) - int(bottom)
                            self.print(answer, rem)
                        else:
                            m = int(lcm1)
                            self.print(f'getting lowest common multiple {lcm1}')
                            sleep(1)
                            d = int(lcm1) / int(b2[1])
                            d1 = int(lcm1) / int(a2[1])
                            self.print(f"{str(a2[0])} * {str(d1)} / {str(a2[1])} * {str(d1)}")
                            frac1 = [int(a2[0]) * int(d1), int(a2[1]) * int(d1)]
                            sleep(1)
                            self.print(f"{str(frac1[0])} / {str(frac1[1])}")
                            sleep(1)
                            self.print(f"{str(b2[0])} * {str(d)} / {str(b2[1])} * {str(d)}")
                            frac2 = [int(b2[0]) * int(d), int(b2[1]) * int(d)]
                            sleep(1)
                            self.print(f"{str(frac2[0])} / {str(frac2[1])}")
                            top = int(frac1[0]) - int(frac2[0])
                            sleep(1)
                            self.print(f'top = {str(frac1[0])} - {str(frac2[0])}')
                            bottom = m
                            sleep(1)
                            self.print(f'whole fraction = {str(top)}/{str(bottom)}')
                            # reduce if possible
                            answer = f'answer = {str(top)} / {str(bottom)}'
                            rem = int(top) - int(bottom)
                            return f"{answer} with remainder {str(rem)}"
                except TypeError and ValueError as e:
                    self.print(e)
            elif al[2] in eq:
                try:
                    a0, b0 = eq.split(al[2])
                    a1 = a0.split('/')
                    b1 = b0.split('/')
                    self.print('using Multiplying Fractions Formula: a/b * c/d = a*c / b*d')
                    sleep(.5)
                    step3 = a1
                    step3a = b1
                    step3c = int(step3[0]) * int(step3a[0])
                    self.print(f'{str(step3[0])} * {str(step3a[0])}')
                    step3d = int(step3[1]) * int(step3a[1])
                    self.print(f'{str(step3[1])} * {str(step3a[1])}')
                    self.print(f'{step3c}/{step3d}')
                    step4 = step3c / step3d
                    step4a = step3c % step3d
                    self.answer = f"{step4a} / {step3d} with a remainder of {int(step4)} "
                    self.print(f"answer = {self.answer}")
                except ValueError and TypeError as e:
                    self.print(e)
            elif al[3] in eq:
                try:
                    self.print("Division Detected")
                    self.print('using Dividing Fractions Formula: a/b % c/d = a*d / b*c')
                    a0, b0 = eq.split(al[3])
                    self.print('splitting Equation')
                    a1 = a0.split('/')
                    b1 = b0.split('/')
                    self.print('using Multiplying Fractions Formula: a/b * c/d = a*c / b*d')
                    step4 = a1
                    step4a = b1
                    self.print(step4, step4a)
                    step5 = int(step4[0]) * int(step4a[1])
                    self.print(f'{str(step4[0])} * {str(step4a[1])} = {str(step5)}')
                    step5a = int(step4[1]) * int(step4a[0])
                    self.print(f'{str(step4[1])} * {str(step4a[0])} = {str(step5a)}')
                    a1 = factor()
                    a1 = a1.factor(int(step5), 1)
                    a2 = factor()
                    a2 = a2.factor(int(step5a), 1)
                    self.print(f'getting factors for {step5}')
                    self.print(f'Factors for {str(step5)} = {str(a1)}')
                    self.print(f'Factors for {str(step5a)} = {str(a2)}')
                    self.print('comparing factors')
                    # print(a1)
                    # print(a2)
                    a3 = set(a1) & set(a2)
                    self.print(f'common factors = {str(a3)}')
                    a4 = int(max(a3))
                    self.print(f'using {a4} to reduce fraction')
                    step6 = int(step5) / a4
                    self.print(f'{int(step5)}/{str(a4)}')
                    step7 = int(step5a) / a4
                    self.print(f'{int(step5a)}/{str(a4)}')
                    self.answer = f'answer = {str(int(step6))}/{str(int(step7))}'
                    self.print(self.answer)
                except ValueError and TypeError as e:
                    self.print(e)
