t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    arr = []
    for _ in range(a):
        arr.append(int(input()))
    brr = set(arr)
    print(len(arr)-len(brr))
