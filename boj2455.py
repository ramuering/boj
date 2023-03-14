now = 0
m = 0
for i in range(4):
    a, b = map(int, input().split())
    now += b
    now -= a
    if m < now:
        m = now
print(m)
