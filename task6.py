text = input()

chars = dict()

for char in text:
    chars[char] = 0

for char in text:
    chars[char] += 1

oneEntryChars = dict(filter(
    lambda char: char[1] == 1, chars.items()))

print(list(oneEntryChars.keys()))
