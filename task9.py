banknotes = {"5000": 5, "2000": 22, "1000": 43, "500": 59,
             "200": 102, "100": 2325, "50": 12323, "10": 6454}

sum = int(input())

result = dict()

for note in banknotes.keys():
    banknotesCount = sum // int(note)

    if (banknotesCount == 0):
        continue

    if (banknotesCount > banknotes[note]):
        sum -= int(note) * banknotes[note]
        result[note] = banknotes[note]
        continue

    sum -= int(note) * banknotesCount
    result[note] = banknotesCount

if (sum != 0):
    print("Операция не может быть выполнена!")
    exit()

print(' + '.join(f'{key} * {result[key]}' for key in result.keys()))
