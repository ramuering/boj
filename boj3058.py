t = int(input())
for _ in range(t):
    array = list(map(int, input().split()))
    result = []
    for i in range(len(array)):
        if array[i] % 2 == 0:
            result.append(array[i])
    print(sum(result), min(result))
