t = int(input())
y, f = 0, 0
for i in range(t):
    a, b = map(int, input().split())
    y, f = divmod(a, b)

    print("You get {} piece(s) and your dad gets {} piece(s).".format(y, f))
