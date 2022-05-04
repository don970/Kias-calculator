class MSolve:
    def __init__(self, mode):
        self.answer = None
        self.complete = False
        if mode == 0:
            self.solve(str('none'))

    def solve(self, i: str):
        from time import sleep
        while True:
            if i == "none":
                print('enter mixed number to be writen as an improper fraction as "x x/x"')
                mixed_number: str = input()
            else:
                mixed_number = i
            print(mixed_number)
            sleep(1)
            print('splitting mixed number to number and fraction')
            mix_number_split = mixed_number.split()
            print(mix_number_split)
            sleep(1)
            print('preparing fraction for addition')
            fraction = mix_number_split[1].split('/')
            print(fraction)
            sleep(1)
            answer = int(int(mix_number_split[0]) * int(fraction[1]) + int(fraction[0]))
            answer = f"{str(answer)}/{fraction[1]}"
            self.answer = answer
            if mixed_number == i:
                return answer
            else:
                print(f"answer = {answer}")
                sleep(10)