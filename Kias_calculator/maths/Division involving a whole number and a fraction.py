def factor():
    while True:
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        print("enter number to be factored")
        a0 = int(input().strip('\n'))
        for i in range(1, a0 + 1):
            if a0 % i == 0:
                print(i)

		
factor()
