def modeInArray(arr):
    frequency = {}
    for i in arr:
        frequency[i] = frequency.get(i,0) + 1
    mode = max(frequency, key = frequency.get)
    return mode

array = [1, 2, 2, 3, 3, 3, 4, 4]
print(modeInArray(array)) 