t = int(input())
array = [0]*t
i, cnt = 0, 0
while cnt < t:
    array[i] = int(input())
    cnt += 1
    if array[i] == 0:
        array[i-1] = 0
        i -= 1
    else:
        i += 1

print(sum(array))
