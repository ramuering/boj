n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
m, k = map(int, input().split())
b = []
for i in range(m):
    b.append(list(map(int, input().split())))

for i in range(n):
    for j in range(k):
        ans = 0
        for r in range(m):
            ans = ans + a[i][r]*b[r][j]
        print(ans, end=' ')
    print()
