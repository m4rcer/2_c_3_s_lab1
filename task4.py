text = input()

words = text.split()

for word in filter(lambda el: len(el) > 7,words):
    print(word)

for word in filter(lambda el: len(el) >= 4 and len(el) <= 7,words):
    print(word)

for word in filter(lambda el: len(el) < 4,words):
    print(word)

