array = [str(input()) for _ in range(3)]
a = int(array[0])
b = int(array[2])
if array[1] == '+':
    result = a+b
if array[1] == '*':
    result = a*b
print(result)
