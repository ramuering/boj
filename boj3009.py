x = [0]*1001
y = [0]*1001
rx, ry = 0, 0
for i in range(3):
    a, b = map(int, input().split())
    x[a] += 1
    y[b] += 1

for i in range(1, 1001):
    if x[i] == 1:
        rx = i
    if y[i] == 1:
        ry = i
    if rx != 0 and ry != 0:
        break
print(rx, ry)
