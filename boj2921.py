n = int(input())
sum = 0
for i in range(1, n+1):
    for j in range(i, i+i+1):
        sum += j
print(sum)
