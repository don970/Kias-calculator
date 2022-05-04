# add and subtract
from time import sleep


def factor(a0):
    ls = []
    for i in range(1, a0 + 1):
        if a0 % i == 0:
            ls.append(i)
    return ls


class mixed_numbers:
    def __init__(self):
        self.answer = None
        self.MultiplactionAndDevision()

    def MultiplactionAndDevision(self):
        symbols = ["*", '%', '/']
        equation = input('enter equation as 1 3/4*2 5/7 or a a/b*a c/d \n')
        if symbols[0] in str(equation.strip('\n')):
            print("Multiplication Detected")
            print('splitting Equation')
            step1, step1a = equation.split(symbols[0])
            print(step1, step1a)
            print('using Multiplying Fractions Formula: a/b * c/d = a*c / b*d')
            sleep(.5)
            try:
                from write_mixed_number_as_improper_fraction import MSolve
                a = f"{str(step1)}"
                b = f"{str(step1a)}"
                c = MSolve(1)
                c = c.solve(str(a))
                d = MSolve(1)
                d = d.solve(str(b))
                step3 = d.split(symbols[2])
                step3a = c.split(symbols[2])
                step3c = int(step3[0]) * int(step3a[0])
                print(f'{str(step3[0])} * {str(step3a[0])}')
                step3d = int(step3[1]) * int(step3a[1])
                print(f'{str(step3[1])} * {str(step3a[1])}')
                print(f'{step3c}/{step3d}')
                step4 = step3c / step3d
                step4a = step3c % step3d
                self.answer = f"{int(step4)} {step4a} / {step3d}"
                print(f"{int(step4)} {step4a} / {step3d}")
            except ValueError and TypeError as e:
                print(e)
        else:
            print("Division Detected")
            print('splitting Equation')
            step1, step1a = equation.split(symbols[1])
            print(step1, step1a)
            print('using Dividing Fractions Formula: a/b % c/d = a*d / b*c')
            sleep(.5)
            step2 = step1.split()
            step2a = step1a.split()
            print(step2, step2a)
            from write_mixed_number_as_improper_fraction import MSolve
            a = MSolve(1)
            b = f'{str(step2[0])} {str(step2[1])}'
            c = f'{str(step2a[0])} {str(step2a[1])}'
            step3 = a.solve(str(b))
            step3a = a.solve(str(c))
            step4 = step3.split(symbols[2])
            step4a = step3a.split(symbols[2])
            print(step4, step4a)
            step5 = int(step4[0]) * int(step4a[1])
            print(f'{str(step4[0])} * {str(step4a[1])} = {str(step5)}')
            step5a = int(step4[1]) * int(step4a[0])
            print(f'{str(step4[1])} * {str(step4a[0])} = {str(step5a)}')
            a1 = factor(int(step5))
            a2 = factor(int(step5a))
            print(a1)
            print(a2)
            a3 = set(a1) & set(a2)
            a4 = int(max(a3))
            step6 = int(step5) / a4
            step7 = int(step5a) / a4
            answer = f'answer = {str(int(step6))}/{str(int(step7))}'
            print(answer)

    def AdditionandSubtraction(self):
        pass

mixed_numbers()
