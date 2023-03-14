n = int(input())
result = 1
for i in range(n, 0, -1):
    result *= i

result = list(str(result))
result.reverse()
cnt = 0
for i in range(len(result)):
    if result[i] != '0':
        break
    cnt += 1

print(cnt)
