num = int(input())

fibo = [0]*91
fibo[0] = 0
fibo[1] = 1

for i in range(2, num+1):
    fibo[i] = fibo[i-1]+fibo[i-2]
    print(fibo[i])

print(fibo[num])
