import math
sqrt = math.sqrt

t = int(input())
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if (x1 == x2) and (y1 == y2):
        if r1 != r2:
            print(0)
        else:
            print(-1)
    else:
        chk = sqrt(pow(x1-x2, 2)+pow(y1-y2, 2))
        if (chk == r1+r2) or (chk == abs(r1-r2)):
            print(1)
        elif abs(r1-r2) < chk < r1+r2:
            print(2)
        else:
            print(0)
