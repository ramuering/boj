array = list(map(str, input()))

for i in range(len(array)):
    if i == 0:
        start = array[i]
        result = 10
    else:
        if start == array[i]:
            result += 5
            start = array[i]
        else:
            result += 10
            start = array[i]

print(result)
