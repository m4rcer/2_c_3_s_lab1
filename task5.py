import re;

text = input()

def capitalizeWords(words):
    for i in range(len(words)):
        if(len(words[i]) and words[i][0].isupper()):
            words[i] = words[i].upper()

words = re.split("( |,)", text)

capitalizeWords(words)

result = ''.join(words)

print(result)
