def isAscedingSequence(list):
    if(len(list) == 0):
        return False

    for i in range(1, len(list)):
        if(list[i] < list[i-1]):
            return False
    return True

list = [1,2,3,4,5,6,7]

print(isAscedingSequence(list))

