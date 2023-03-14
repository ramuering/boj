import math
m = int(input())
n = int(input())
result = []
for i in range(m, n+1):
    a = int(math.sqrt(i))
    if a*a == i:
        result.append(i)
if len(result) != 0:
    print(sum(result))
    print(min(result))
else:
    print(-1)
