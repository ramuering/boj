n, m = map(int, input().split())
arr = [str(i) for i in range(n+1)]

for _ in range(m):
    i, j = map(int, input().split())
    temp = arr[i:j+1]
    temp.reverse()
    arr[i:j+1] = temp
arr.pop(0)
print(' '.join(arr))
