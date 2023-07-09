def next_permutation(arr):
    i, j = len(arr)-1, len(arr)-1
    while i > 0 and arr[i-1] >= arr[i]:
        i -= 1
    if i == 0:
        return False
    while arr[i-1] >= arr[j]:
        j -= 1
    arr[i-1], arr[j] = arr[j], arr[i-1]
    k = len(arr)-1
    while i < k:
        arr[i], arr[k] = arr[k], arr[i]
        i += 1
        k -= 1
    return arr


s = list(input())
result = sorted(s)
cnt = 0

while result:
    flag = True
    for i in range(1, len(result)):
        if result[i] == result[i-1]:
            flag = False
            break
    if flag:
        cnt += 1
    result = next_permutation(result)
print(cnt)
