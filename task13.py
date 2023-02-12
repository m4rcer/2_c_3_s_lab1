from functools import reduce


def extra_enumerate(seq, start=0):
    sum = reduce(lambda x, y: x + y, seq)
    cum = 0

    for i in range(len(seq)):
        cum += seq[i]

        yield (start + i, seq[i], cum, cum/sum)

    return


x = [1, 3, 4, 2]

for i, elem, cum, frac in extra_enumerate(x):
    print(elem, cum, frac)
