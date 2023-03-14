s = int(input())
result = 0
for i in range(1, s+1):
    result += i
    if result > s:
        result = i-1
        break
print(result)
