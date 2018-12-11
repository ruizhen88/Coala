fibo = list()

num = int(input("몇번째까지 출력할까요? "))

while len(fibo) != num:
    for n in range(0, num):
        if n == 0 or n == 1:
            fibo.append(1)
        else:
            n = fibo[n-2] + fibo[n-1]
            fibo.append(n)
    for n in fibo:
        print("{0}".format(n))

# fibo = [1, 1, 2, 3, 5, 8, 13]

