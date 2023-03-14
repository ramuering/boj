array = list(map(str, input()))
a = ''.join(array)
array.reverse()
b = ''.join(array)
if a == b:
    print(1)
else:
    print(0)
