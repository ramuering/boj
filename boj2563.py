test = int(input())

arr = []
for i in range(test):
    x, y = map(int, input().split())
    for a in range(y, y+10):
        for b in range(x, x+10):
            arr.append(a*100+b)

print(len((set(arr))))
