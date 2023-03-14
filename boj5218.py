t = int(input())

for _ in range(t):
    d = []
    a, b = map(str, input().split())
    for i in range(len(a)):
        if (ord(b[i])-64)-(ord(a[i])-64) < 0:
            d.append((ord(b[i])-64)-(ord(a[i])-64)+26)
        else:
            d.append((ord(b[i])-64)-(ord(a[i])-64))
    print("Distances: ", end='')
    for i in d:
        print(i, end=' ')
    print()
