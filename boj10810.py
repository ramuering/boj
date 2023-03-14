n, m = map(int, input().split())

array = [0]*n
for cnt in range(m):
    i, j, k = map(int, input().split())
    for a in range(i-1, j):
        array[a] = k

for k in array:
    print(k, end=' ')
