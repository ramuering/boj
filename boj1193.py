n = int(input())
cnt = 0
r = 1
chk = True
for i in range(1, 10000001):
    a, b = i, 1
    while a >= 1 and b <= i:
        if r % 2 != 0:
            x, y = a, b
        else:
            x, y = b, a
        cnt += 1
        print(x, y)
        if cnt == n:
            print("{}/{}".format(x, y))
            chk = False
            break
        a -= 1
        b += 1
    if chk == False:
        break
    r += 1
