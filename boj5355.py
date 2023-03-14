t = int(input())
for i in range(t):
    array = list(map(str, input().split()))
    num = float(array[0])
    for j in range(1, len(array)):
        if array[j] == '@':
            num *= 3
        if array[j] == '%':
            num += 5
        if array[j] == '#':
            num -= 7
    print(round(num, 2))
