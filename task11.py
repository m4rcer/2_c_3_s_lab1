def frange(start, stop, step):
    count = int((stop - start) / step)

    if (count <= 0):
        return []

    for i in range(count):
        yield start + step * i

    


for x in frange(1, 5, 0.1):
    print(x)
