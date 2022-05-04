from time import sleep
from factor import Factor


def A():  # finding the price of a disconted item when given the percent
    while True:
        p = input('enter percent disconted \n')
        a = input('enter orginal amount \n')
        n = float(p) / 100
        c = float(n) * float(a)
        d = float(a) + float(c)
        print(float(d))


def B():  # finding the percent a item is discounted
    while True:
        p = input('enter new amount \n')
        a = input('enter orginal amount \n')
        b = input('add or sub \n')
        d = float(p) - float(a)
        d = float(d) / float(a)
        e = float(d) * 100.0
        if b.strip("\n") == 'sub':
            print(f'decrease in price by {str(float(abs(e)))}%')
        else:
            print(f'increase in price by {str(float(abs(e)))}%')


def C():  # Multiplicative property of equality with fractions
    while True:
        print("equation = a/b*x=c")
        a = input('enter a')
        b = input('enter b')
        c = input("enter c")
        d = input("enter d")
        if len(d) == 0:
            d = 1
        print('x = c*b/a*d')
        x = float(int(c) * int(b))
        x1 = float(int(a) * int(d))
        e = Factor(1, int(x))
        e1 = Factor(1, int(x1))
        e = e.factor(int(x), 0)
        e1 = e1.factor(int(x1), 0)
        e2 = set(e1) & set(e)
        e3 = float(max(e2))
        e4 = float(int(x) / int(e3))
        e5 = float(int(x1) / int(e3))
        if int(e5) == 1:
            print(e4)
        else:
            print(f"answer = {str(e4)}/{e5}")


def D():  # Multiplicative property of equality with decimals
    while True:
        l = ["/"]
        print('equation = c=a.a/b.b or c=a*b')
        a = input("enter equation")
        if l[0] in a:
            a1 = a.split('=')
            a2 = str(a1[1]).split('/')
            answer = f"answer = {str(a2[0])} = {str(float(float(a2[1])) * float(a1[0]))}"
            print(answer)
        else:
            a1 = a.split('=')
            a2 = str(a1[1]).split('*')
            if float(a2[0]) > float(a1[0]):
                answer = f"answer = {str(a2[1])} = {str(round(float(float(a2[0]) / float(a1[0])), len(a1[0])))}"
                print(answer)
            else:
                answer = f"answer = {str(a2[1])} = {str(round(float(float(a1[0]) / float(a2[0])), len(a1[0])))}"
                print(answer)


def E():  # Solving a two-step equation with signed decimals
    while True:
        print('equation = a+-b/c=d or a+b*c=d')
        eq = input("enter equation \n")
        a = ['*', '/', '+', '-', "="]
        if a[1] in eq:
            print(1)
            s1 = eq.split(a[1])
            if a[2] in s1[0]:
                s2 = str(s1[0]).split(a[2])
                s2a = str(s1[1]).split(a[4])
                print(s2, s2a)
                e = float(s2[0])
                b = str(s2[1])
                c = float(s2a[0])
                d = float(s2a[1])
                e1 = list(str(e))
                if a[3] in e1:
                    e = abs(e)
                    answer = float(float(e) + float(d))
                    answer = answer * float(c)
                    print(round(answer, len(str(c))))
                else:
                    e = e - e * 2
                    answer = float(float(e) + float(d))
                    answer = answer * float(c)
                    print(round(answer, len(str(c))))
        elif a[0] in eq:
            print(2)
            s1 = eq.split(a[0])
            print(s1)
            if a[2] in s1[0]:
                s2 = str(s1[0]).split(a[2])
                s2a = str(s1[1]).split(a[4])
                print(s2, s2a)
                e = float(s2[0])
                b = float(s2[1])
                c = str(s2a[0])
                d = float(s2a[1])
                e1 = list(str(e))
                print(e, b, c, d)
                print(e1)
                if a[3] in e1[0].strip('\n'):
                    print(1)
                    e = abs(e)
                    print(f'{str(d)} + {str(e)}')
                    answer = float(float(d) + float(e))
                    print(f'{str(answer)} / {str(b)}')
                    answer = answer / float(b)
                    print(round(answer, len(str(d))))
                else:
                    print(2)
                    e = e - e * 2
                    print(f'{str(d)} + {str(e)}')
                    answer = float(float(d) + float(e))
                    print(f'{str(answer)} / {str(b)}')
                    answer = answer / float(b)
                    print(round(answer, len(str(d))))


def F(a, b, mode):  # Identifying solutions to a linear equation in two variables
    # a, b are the values in the question example would be y=2x+8 a would be 2, b is 8
    while True:
        c = input()
        d = input()
        if mode == 0:
            answer = int(c) * int(a) - int(d) * int(b)
            print(answer)
        else:
            answer = int(c) * int(a) + int(b)
            print(answer)


def G():  # Graphing a linear equation of the form y = mx
    def factor(a0, mode):
        ii = []
        if mode == 0:
            a0 = int(a0)
            for i in range(1, 4):
                b = a0 * i
                ii.append(b)
            return ii

    rule = input('Enter Rule --example "y=2*x or y=1/2 * x" \n')
    if '/' in rule:
        b = rule.split('=')
        b1 = b[1].split('/')
        b2 = b1[1].split("*")
        x = factor(b2[0], 0)
        print('x=0, y=0')
        print('')
        print('')
        for items in x:
            b3 = float(b1[0]) / float(b2[0])
            y = float(b3) * int(items)
            answer = f'x={str(items)}, y={str(int(y))}'
            print(answer)
            print('')
            print('')
    else:
        x = 0
        while x < 4:
            a = ['/', '*']
            b = rule.split('=')
            c = b[1].split(a[1])
            y = int(c[0]) * x
            answer = f'x={str(x)}, y={str(y)}'
            x += 1
            print(answer)


def h():  # graphing a line when given its equation in slope intercept form:intger slope
    while True:
        def factor(a0, mode):
            ii = []
            if mode == 0:
                a0 = int(a0)
                for i in range(1, 4):
                    b = a0 * i
                    ii.append(b)
                return ii

        rule = input('Enter Rule --example "y=2*x+6 or y=1/2*x+6" \n')
        if '/' in rule:
            b = rule.split('=')
            b1 = b[1].split('/')
            b2 = b1[1].split("*")
            b4 = b2[1].split('+')
            x = factor(b2[0], 0)
            print('')
            print('')
            for items in x:
                b3 = float(b1[0]) / float(str(b2[0]))
                y = float(b3) * float(items)
                y = int(y) + int(b4[1])
                answer = f'x={str(items)}, y={str(int(y))}'
                print(answer)
                print('')
                print('')
        else:
            x = 0
            while x < 4:
                a = ['/', '*']
                b = rule.split('=')
                c = b[1].split(a[1])
                d = c[1].split('+')
                y = int(c[0]) * x + int(d[1])
                answer = f'x={str(x)}, y={str(y)}'
                x += 1
                print(answer)


def i():  # Writing an equation in slope-intercept form given the slope and a point
    while True:
        a = input('enter slope \n')  # 1 or 1/2 example
        b = input('enter point as x,y \n')  # 0,1 example
        if '/' in a.strip('\n'):
            a = a.split('/')
            print(a)
            a1 = int(a[0]) / int(a[1])
            b = b.split(',')
            print(b)
            x = int(b[0])
            y = int(b[1])
            m = float(a1)
            c = m * float(x)
            print(c)
            for i in range(-100, 100):
                print(f'using {str(i)}')
                print(f'checking if {str(c)} + {str(i)}')
                if c + i == y:
                    if int(i) < 0:
                        print()
                        print("answer below")
                        print(f'y={a[0]}/{a[1]}(x){str(i)}')
                        print(f'b={str(i)}')
                        break
                    else:
                        print()
                        print("answer below")
                        print(f'y={a[0]}/{a[1]}(x)+{str(i)}')
                        print(f'b={str(i)}')
                        break
        else:
            b = b.split(',')
            print(b)
            x = int(b[0])
            y = int(b[1])
            m = float(a)
            c = m * float(x)
            print(c)
            for i in range(-100, 100):
                print(f'using {str(i)}')
                print(f'checking if {str(c)} + {str(i)}')
                if c + i == y:
                    if int(i) < 0:
                        print()
                        print("answer below")
                        print(f'y={str(a)}(x){str(i)}')
                        print(f'b={str(i)}')
                        break
                    else:
                        print()
                        print("answer below")
                        print(f'y={str(a)}(x)+{str(i)}')
                        print(f'b={str(i)}')
                        break

G()
