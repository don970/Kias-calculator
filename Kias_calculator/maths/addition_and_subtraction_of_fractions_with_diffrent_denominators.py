from time import sleep


def lcm(x, y):
    # choose the greater number
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm1 = greater
            lcm1 = lcm1
            return int(lcm1)
        greater += 1


class FDMSolve:

    def __init__(self):
        self.lcm1 = None
        self.addition_or_subtraction_of_fractions_with_different_denominators()

    def addition_or_subtraction_of_fractions_with_different_denominators(self):
        while True:
            print('enter equation as y/x (+, -) y/x where y = numerator and x denominator 7/8 (-) 5/6')
            al = ['(+)', '(-)']
            eq = input()
            if al[0] in eq:
                a0, b0 = eq.split(al[0])
                a1 = a0.split('/')
                b1 = b0.split('/')
                self.lcm1 = lcm(int(a1[1]), int(b1[1]))
                lcm1 = int(self.lcm1)
                if int(a1[1] > b1[1]):
                    a2 = b1
                    b2 = a1
                    print(a2, b2)
                    sleep(1)
                    m = int(a2[1]) / int(b2[1])
                    print(f'{str(a2[1])} / {str(b2[1])}')
                    sleep(1)
                    if int(m) == m and isinstance(m, float):
                        m = int(m)
                        print(f"m = {m}")
                        sleep(1)
                        print(f"{b2[1]} * m for nominator and {b2[1]} * m for denominator")
                        sleep(1)
                        frac1 = [int(b2[0]) * m, int(b2[1]) * m]
                        sleep(1)
                        print(f"fraction number one = {frac1}")
                        sleep(1)
                        top = int(frac1[0]) + int(a2[0])
                        sleep(1)
                        print(f"{str(frac1[0])}/{str(frac1[1])} + {str(a2[0])}/{str(a2[1])}")
                        sleep(1)
                        bottom = int(frac1[1])
                        sleep(1)
                        print(f"denominator  = {bottom}")
                        sleep(1)
                        answer = f'answer = {str(top)} / {str(bottom)}'
                        print(f"answer = {answer}")
                    else:
                        m = int(lcm1)
                        sleep(1)
                        print(f'getting lowest common multiple {lcm1}')
                        d = int(lcm1) / int(b2[1])
                        d1 = int(lcm1) / int(a2[1])
                        sleep(1)
                        print(f"{str(a2[0])} * {str(d1)} / {str(a2[1])} * {str(d1)}")
                        frac1 = [int(a2[0]) * int(d1), int(a2[1]) * int(d1)]
                        print(f"{str(frac1[0])} / {str(frac1[1])}")
                        sleep(1)
                        print(f"{str(b2[0])} * {str(d)} / {str(b2[1])} * {str(d)}")
                        frac2 = [int(b2[0]) * int(d), int(b2[1]) * int(d)]
                        sleep(1)
                        print(f"{str(frac2[0])} / {str(frac2[1])}")
                        top = int(frac1[0]) + int(frac2[0])
                        sleep(1)
                        print(f'top = {str(frac1[0])} + {str(frac2[0])}')
                        sleep(1)
                        bottom = m
                        print(f'whole fraction = {str(top)}/{str(bottom)}')
                        answer = f'answer = {str(top)} / {str(bottom)}'
                        sleep(1)
                        rem = int(top) - int(bottom)
                        print(answer, rem)
                else:
                    a2 = a1
                    b2 = b1
                    print(a2, b2)
                    m = int(a2[1]) / int(b2[1])
                    if int(m) == m and isinstance(m, float):
                        m = int(m)
                        print(f"m = {m}")
                        sleep(1)
                        print(f"{a2[1]} * {str(m)} for nominator and {a2[1]} * {str(m)} for denominator")
                        sleep(1)
                        frac1 = [int(b2[0]) * m, int(b2[1]) * m]
                        print(f"fraction number one = {frac1}")
                        sleep(1)
                        top = int(frac1[0]) + int(a2[0])
                        print(f"{str(frac1[0])}/{str(frac1[1])} + {str(a2[0])}/{str(a2[1])}")
                        sleep(1)
                        bottom = int(frac1[1])
                        print(f"denominator  = {bottom}")
                        sleep(1)
                        answer = f'answer = {str(top)} / {str(bottom)}'
                        rem = int(top) - int(bottom)
                        print(answer, rem)
                    else:
                        m = int(lcm1)
                        print(f'getting lowest common multiple {lcm1}')
                        sleep(1)
                        d = int(lcm1) / int(b2[1])
                        d1 = int(lcm1) / int(a2[1])
                        print(f"{str(a2[0])} * {str(d1)} / {str(a2[1])} * {str(d1)}")
                        frac1 = [int(a2[0]) * int(d1), int(a2[1]) * int(d1)]
                        print(f"{str(frac1[0])} / {str(frac1[1])}")
                        sleep(1)
                        print(f"{str(b2[0])} * {str(d)} / {str(b2[1])} * {str(d)}")
                        frac2 = [int(b2[0]) * int(d), int(b2[1]) * int(d)]
                        print(f"{str(frac2[0])} / {str(frac2[1])}")
                        sleep(1)
                        top = int(frac1[0]) + int(frac2[0])
                        print(f'top = {str(frac1[0])} + {str(frac2[0])}')
                        sleep(1)
                        bottom = m
                        print(f'whole fraction = {str(top)}/{str(bottom)}')
                        sleep(1)
                        answer = f'answer = {str(top)} / {str(bottom)}'
                        rem = int(top) - int(bottom)
                        print(answer, rem)
            else:
                a0, b0 = eq.split(al[1])
                a1 = a0.split('/')
                b1 = b0.split('/')
                lcm1 = lcm(int(a1[1]), int(b1[1]))
                print('finding bigger number')
                if int(a1[1] < b1[1]):
                    a2 = b1
                    b2 = a1
                    print(a2, b2)
                    m = int(a2[1]) / int(b2[1])
                    if m == m and isinstance(m, float):
                        m = int(m)
                        print(f"m = {m}")
                        sleep(1)
                        print(f"{b2[0]} * {m} for nominator and {b2[1]} * {m} for denominator")
                        frac1 = [int(b2[0]) * m, int(b2[1]) * m]
                        print(f"fraction number one = {frac1}")
                        sleep(1)
                        top = int(frac1[0]) - int(a2[0])
                        print(f"{str(frac1[0])}/{str(frac1[1])} - {str(a2[0])}/{str(a2[1])}")
                        sleep(1)
                        bottom = int(frac1[1])
                        print(f"denominator  = {bottom}")
                        sleep(1)
                        answer = f'answer = {str(top)} / {str(bottom)}'
                        rem = int(top) - int(bottom)
                        print(answer, rem)
                    else:
                        m = int(self.lcm1)
                        print(f'getting lowest common multiple {lcm1}')
                        d = int(lcm1) / int(b2[1])
                        d1 = int(lcm1) / int(a2[1])
                        frac1 = [int(a2[0]) * int(d1), int(a2[1]) * int(d1)]
                        sleep(1)
                        print(f"{str(frac1[0])} / {str(frac1[1])}")
                        frac2 = [int(b2[0]) * int(d), int(b2[1]) * int(d)]
                        sleep(1)
                        print(f"{str(frac2[0])} / {str(frac2[1])}")
                        top = int(frac1[0]) - int(frac2[0])
                        print(f'top = {str(frac1[0])} - {str(frac2[0])}')
                        sleep(1)
                        bottom = m
                        print(f'whole fraction = {str(top)}/{str(bottom)}')
                        answer = f'answer = {str(top)} / {str(bottom)}'
                        sleep(1)
                        rem = int(top) - int(bottom)
                        print(answer, rem)
                else:
                    a2 = a1
                    b2 = b1
                    print(a2, b2)
                    m = int(a2[1]) / int(b2[1])
                    if int(m) == m and isinstance(m, float):
                        m = int(m)
                        print(f"m = {m}")
                        sleep(1)
                        print(f"{b2[0]} * {m} for nominator and {b2[1]} * {m} for denominator")
                        frac1 = [int(b2[0]) * m, int(b2[1]) * m]
                        print(f"fraction number one = {frac1}")
                        sleep(1)
                        top = int(frac1[0]) - int(a2[0])
                        print(f"{str(frac1[0])}/{str(frac1[1])} - {str(a2[0])}/{str(a2[1])}")
                        sleep(1)
                        bottom = int(frac1[1])
                        print(f"denominator  = {bottom}")
                        sleep(1)
                        answer = f'answer = {str(top)} / {str(bottom)}'
                        rem = int(top) - int(bottom)
                        print(answer, rem)
                    else:
                        m = int(lcm1)
                        print(f'getting lowest common multiple {lcm1}')
                        sleep(1)
                        d = int(lcm1) / int(b2[1])
                        d1 = int(lcm1) / int(a2[1])
                        print(f"{str(a2[0])} * {str(d1)} / {str(a2[1])} * {str(d1)}")
                        frac1 = [int(a2[0]) * int(d1), int(a2[1]) * int(d1)]
                        sleep(1)
                        print(f"{str(frac1[0])} / {str(frac1[1])}")
                        sleep(1)
                        print(f"{str(b2[0])} * {str(d)} / {str(b2[1])} * {str(d)}")
                        frac2 = [int(b2[0]) * int(d), int(b2[1]) * int(d)]
                        sleep(1)
                        print(f"{str(frac2[0])} / {str(frac2[1])}")
                        top = int(frac1[0]) - int(frac2[0])
                        sleep(1)
                        print(f'top = {str(frac1[0])} - {str(frac2[0])}')
                        bottom = m
                        sleep(1)
                        print(f'whole fraction = {str(top)}/{str(bottom)}')
                        # reduce if possible
                        answer = f'answer = {str(top)} / {str(bottom)}'
                        rem = int(top) - int(bottom)
                        print(answer, rem)



a = FDMSolve()
a.self.addition_or_subtraction_of_fractions_with_different_denominators()
