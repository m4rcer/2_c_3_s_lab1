from random import randrange
import datetime

def generateGroups(teams):
    groups = []
    teams = list(teams)

    for i in range(4):
        group = []

        for j in range(4):
            index = randrange(0, len(teams))
            group.append(teams[index])
            del teams[index]

        groups.append(group)

    return groups

def generateGamesDates(startDate, delta, count):
    return [(startDate + delta * i).strftime(("%d/%m/%Y, %H:%M")) for i in range(count)]


teams = ["Unbroken", "Мерч", "Гулливер", "Альфа", "Band", "Sila", "Wise", "Toads",
         "Lodge", "Bulls", "Реал",  "Интер", "Атлетико",  "Сити", "Бойз",  "FootBoys"]

groups = generateGroups(teams)

dateStart = datetime.datetime(2023, 9, 14, 22, 45)
twoWeeks = datetime.timedelta(14)

dates= generateGamesDates(dateStart, twoWeeks, len(teams) - 1)

for i in range(len(groups)):
    print(groups[i])

print(dates)