from .lcm import lcm


class Using_a_common_denominator_to_order_fractions:
    def __init__(self):
        self.answer = None
        self.using_a_common_denominator_to_order_fractions()

    def using_a_common_denominator_to_order_fractions(self):
        while True:
            e, q = input('enter fractions to check').split()
            e1 = e.split('/')
            q1 = q.split('/')
            a = lcm(int(e1[1]), int(q1[1]))
            a0 = int(int(a) / int(e1[1]))
            a1 = int(int(a) / int(q1[1]))
            b = int(int(a1) * int(q1[0]))
            c = int(int(a0) * int(e1[0]))
            if int(c) > int(b):
                self.answer = f'{str(c)}/{str(a)} > {str(b)}/{str(a)}'
                print(self.answer)
            else:
                self.answer = f'{str(c)}/{str(a)} < {str(b)}/{str(a)}'
                print(self.answer)
