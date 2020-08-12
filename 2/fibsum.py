num = 0
tot = 0
n = 3


def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


while num < 4e6:
    num = fib(n)
    if num % 2 == 0:
        tot += num
    n += 1

print(tot)
