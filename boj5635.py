n = int(input())
array = []
for i in range(n):
    name, d, m, y = map(str, input().split())
    array.append([name, int(d), int(m), int(y)])
maxx = 2010
minn = 1990
for i in range(n):
    if array[i][3] < maxx:
        max_i = i
        maxx = array[i][3]
    if array[i][3] == maxx:
        if array[i][2] < array[max_i][2]:
            max_i = i
        if array[i][2] == array[max_i][2]:
            if array[i][1] < array[max_i][1]:
                max_i = i
for i in range(n):
    if array[i][3] > minn:
        min_i = i
        minn = array[i][3]
    if array[i][3] == minn:
        if array[i][2] > array[min_i][2]:
            min_i = i
        if array[i][2] == array[min_i][2]:
            if array[i][1] > array[min_i][1]:
                min_i = i
print(array[min_i][0])
print(array[max_i][0])
