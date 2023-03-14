t = int(input())
for _ in range(t):
    array = list(map(int, input().split()))
    array.sort()
    array.pop(0)
    array.pop(-1)
    if (max(array)-min(array)) >= 4:
        print("KIN")
    else:
        print(sum(array))
