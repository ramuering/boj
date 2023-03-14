result = 0
temp = 0
for i in range(10):
    i, o = map(int, input().split())
    temp -= i
    if result < temp:
        result = temp
    temp += o
    if result < temp:
        result = temp
print(result)
