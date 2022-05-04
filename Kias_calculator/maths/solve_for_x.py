from time import sleep
from tkinter import *
from tkinter.scrolledtext import ScrolledText

# Solving a multi-step equation given in fractional form

class solve:
    def __init__(self, tkobject):
        self.answer = None
        self.equation = None
        self.e = tkobject

    def solve_for_x(self, A):
        while True:
            eq = A
            eq1 = eq.split()  # split first number from rest
            l = ['(+)', '(-)']
            if l[0] in eq1[1].strip('\n'):
                eq2 = eq1[1].split(l[0])
                print('finding type of equation:' + str(eq2))
                sleep(1)
                eq3 = eq2[1].split('=')
                print('splitting equation up' + str(eq2))
                sleep(1)
                eq4 = eq3[0].split('/')
                print("further splitting equation")
                a = int(int(eq3[1]) * int(eq4[1]))
                print(f'multiplying {str(eq3[1])} and {str(eq4[1])} = {str(a)}')
                sleep(1)
                print(f'subtracting {str(a)} and {str(eq4[0])} = {int(a) - int(eq4[0])}')
                a = a - int(eq4[0])
                v = 1
                print('finding bigger number')
                if int(a) > int(eq1[0]):
                    b = int(eq1[0]) / int(a)
                    v = 0
                if v == 0:
                    print(f'dividing {str(eq1[0])} and {str(a)}')
                    answer = f'{str(eq2[0])} = {str(int(b))}'
                    print(answer, tkobject)
                    return answer
                else:
                    b = int(a) / int(eq1[0])
                    self.print(f'dividing {str(a)} and {str(eq1[0])}')
                    answer = f'{str(eq2[0])} = {str(int(b))}'
                    print(answer)
                    return answer
