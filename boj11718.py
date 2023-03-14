arr = []
while True:
    try:
        x = input()
    except EOFError:
        break
    arr.append(x)
for i in arr:
    print(i)
