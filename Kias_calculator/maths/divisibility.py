class divisibility:
    def __init__(self):
        self.Divisibility()

    def Divisibility(self):
        while True:
            lst = []
            rule = int(input('enter number to use as divisible rule'))
            num = int(input('How many numbers: '))
            for n in range(num):
                numbers = int(input('Enter number'))
                lst.append(numbers)
                a = sum(lst)
                print(a)
                if a % rule == 0:
                    print(True)
                else:
                    print(False)