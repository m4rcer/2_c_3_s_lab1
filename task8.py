from random import randrange

n = randrange(0, 10000)


def findNearestPowerOfTwo(n):
    power = 0
    while True:
        if (2 ** power >= n):
            break
        power += 1

    return power

power = findNearestPowerOfTwo(n)

dif = 2 ** power - n

result = [randrange(0, 10000) for i in range(n)] + [0 for i in range(dif)]

print(result)