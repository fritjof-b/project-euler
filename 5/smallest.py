smallest = 0
i = 20
numbers = [i for i in range(10, 21)]

# bogus solution; will update with prime factorization


def isDivisible(n, numbers):
    for number in numbers:
        if n % number != 0:
            return False
    return True


while smallest == 0:
    if isDivisible(i, numbers):
        smallest = i
    i += 20

print(smallest)
