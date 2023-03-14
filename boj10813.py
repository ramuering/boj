n, m = map(int, input().split())
arr = [i for i in range(0, n+1)]
print(arr)
for _ in range(m):
    a, b = map(int, input().split())
    arr[a], arr[b] = arr[b], arr[a]
    print(arr)

for i in range(1, len(arr)):
    print(arr[i], end=' ')
