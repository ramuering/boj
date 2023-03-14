array = [list(input()) for _ in range(5)]

length = []
for i in range(len(array)):
    length.append(len(array[i]))

for j in range(max(length)):
    for i in range(5):
        if len(array[i]) <= j:
            continue
        if array[i][j].isspace():
            continue
        print(array[i][j], end='')
