biggest = 0
for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        pal = str(i*j)
        if pal == pal[::-1] and i * j > biggest:
            biggest = i * j

print(biggest)
