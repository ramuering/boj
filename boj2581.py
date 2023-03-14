m = int(input())
n = int(input())
result = []
for i in range(m, n+1):
    if i == 1:
        continue
    ox = 0
    for j in range(2, i):
        if i % j == 0:
            ox = 1
            break
    if ox == 0:
        result.append(i)
if len(result) != 0:
    print(sum(result))
    print(min(result))
else:
    print(-1)
