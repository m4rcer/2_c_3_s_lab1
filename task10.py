import re

password = input()

def isPasswordStrong(password):
    if(len(password) < 8):
        return False

    lowwerLetters = re.search(r"[a-z]", password)
    upperLetters = re.search(r"[a-z]", password)
    digits = re.search(r"[0-9]", password)
    specials = re.search(r"\W", password)

    return all([lowwerLetters, upperLetters, digits, specials])
    
print("Strong!" if isPasswordStrong(password) else "Weak!")