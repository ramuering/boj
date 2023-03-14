t = int(input())
for i in range(t):
    n = int(input())
    d = dict()
    for j in range(n):
        key, value = map(str, input().split())
        d[key] = int(value)
    print(max(d, key=d.get))
