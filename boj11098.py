n = int(input())
for i in range(n):
    p = int(input())
    d = dict()
    for j in range(p):
        price, name = map(str, input().split())
        d[name] = int(price)
    print(max(d, key=d.get))
