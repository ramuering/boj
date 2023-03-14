num = int(input())
result = []
for i in range(1, num):
    tmp = num-i
    arr = list(str(tmp))
    for n in arr:
        tmp += int(n)
    if tmp == num:
        result.append(num-i)

if len(result) == 0:
    print(0)
else:
    print(min(result))
