t = int(input())
for i in range(t):
    n, s = map(str, input().split())
    s = list(s)
    s.pop(int(n)-1)
    print(''.join(s))
