print("Введите число: \n")

try:
    number = float(input())

    if(number < 0):
        raise ValueError("Неверный формат!")

    print(f'{int(number)} руб. {int(number%1 * 100)} коп.')
except ValueError as e:
    print(e)