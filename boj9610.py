t = int(input())
array = [0]*5
for i in range(t):
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        array[4] += 1
    if x > 0 and y > 0:
        array[0] += 1
    if x < 0 and y > 0:
        array[1] += 1
    if x < 0 and y < 0:
        array[2] += 1
    if x > 0 and y < 0:
        array[3] += 1

for i in range(5):
    if i == 4:
        print("AXIS:", array[i])
    else:
        print("Q{}:".format(i+1), array[i])
