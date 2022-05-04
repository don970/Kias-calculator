from time import sleep


class Simplifying_a_ratio:
    def __init__(self):
        self.answer = None
        self.ls = None
        self.simplifying_a_ratio_of_univariate_monomials()

    def factor(self, a0):
        ls = []
        self.ls = ls
        for i in range(1, a0 + 1):
            if a0 % i == 0:
                ls.append(i)
        return ls

    def simplifying_a_ratio_of_univariate_monomials(self):
        a = input('enter equation as 45 w**7/15 w**2 \n')
        a0, b = a.split('/')
        a1 = a0.split()
        b0 = b.split()
        a2 = a1[1].split('**')
        b1 = b0[1].split('**')
        a3 = [a1[0], str(a2[0]), str(a2[1])]
        b2 = [b0[0], str(b1[0]), str(b1[1])]
        # find the factors
        print(f'finding common factors')
        a4 = self.factor(int(a3[0]))
        a5 = self.factor(int(b2[0]))
        sleep(1)
        print(f'''
    factors for {str((a3[0]))} = {str(a4)}
    factors for {str(b2[0])} = {str(a5)}    
        ''')
        sleep(1)
        # compare both and return matches
        a6 = set(a4) and set(a5)
        print(f'matching factors are {str(a6)}')
        sleep(1)
        # return largest factor
        a7 = int(max(a6))
        print(f'largest factor is {str(a7)}')
        print("")
        sleep(1)
        # divide by factor
        print('dividing by largest factor and calculating exponents ')
        a10 = int(a3[2]) - int(b2[2])
        if int(a7) > int(a3[0]) and int(a7) > int(b2[0]):
            print(f'{str(a7)} % {str(a3[0])}')
            print("")
            a8 = int(a7) / int(a3[0])
            sleep(1)
            print(f'{str(a7)} % {str(a3[0])}')
            a9 = int(a7) / int(b2[0])
            sleep(1)
            self.answer = f'{str(a8)}{a3[1]}/{str(a9)}**{str(a10)}'
            print(f'{str(a8)}{a3[1]}/{str(a9)}**{str(a10)}')
        else:
            a = int(a7)
            b = int(a3[0])
            c = int(b2[0])
            a8 = b / a
            print(f'{str(b)} % {str(a)} = {str(int(a8))}')
            print('')
            sleep(1)
            a9 = c / a
            print(f'{str(c)} % {str(int(a))} = {str(int(a9))}')
            sleep(1)
            print('')
            if int(a9) == 1:
                a9 = 0
                print(f'answer = {str(int(a8))}{a3[1]}**{str(int(a10))}')
                self.answer = f'{str(a8)}{a3[1]}/{str(a9)}**{str(a10)}'
                sleep(10)
            else:
                self.answer = f'{str(a8)}{a3[1]}/{str(a9)}**{str(a10)}'
                print(f'answer = {str(int(a8))}{a3[1]}/{str(int(a9))}**{str(int(a10))}')
                sleep(10)



