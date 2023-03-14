t = int(input())
for j in range(t):
    a, b = 0, 0
    for i in range(9):
        x, y = map(int, input().split())
        a += x
        b += y
    if a > b:
        print("Yonsei")
    if b > a:
        print("Korea")
    if a == b:
        print("Draw")
