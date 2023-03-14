import math

t, w, h = map(int, input().split())
for _ in range(t):
    n = int(input())
    if n <= w or n <= h or n <= math.sqrt((w*w)+(h*h)):
        print("DA")
    else:
        print("NE")
