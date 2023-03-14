n, m = map(int, input().split())
result = []
i = 0
while True:
    i += 1
    for cnt in range(i):
        result.append(i)
        if len(result) == m:
            break
    if len(result) == m:
        break
print(sum(result[n-1:]))
