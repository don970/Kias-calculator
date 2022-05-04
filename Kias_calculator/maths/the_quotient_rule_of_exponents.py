class QSolve:
    def __init__(self):
        self.answer = None
        self.the_quotient_rule_of_exponents()

    def the_quotient_rule_of_exponents(self):
        while True:
            print('enter equation as y**x / y**x where y = your place holder and x is the value example y**5 / y**4')
            a0 = input()
            a00 = a0.split('/')
            a1 = str(a00[0]).split('**')
            a2 = str(a00[1]).split('**')
            answer = int(a1[1]) - int(a2[1])
            self.answer = answer
            if int(a1[1]) < int(a2[1]):
                print(f'answer = 1/{str(a1[0])}**{str(abs(answer))}')
            else:
                print(f'answer = {str(a1[0])}**{str(answer)}')

