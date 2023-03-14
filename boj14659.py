t = int(input())
arr = list(map(int, input().split()))
result = []

for i in arr:
    start = i
    cnt = 0
    for j in range(arr.index(start)+1, len(arr)):
        if start > arr[j]:
            cnt += 1
        else:
            break
    result.append(cnt)

print(max(result))
