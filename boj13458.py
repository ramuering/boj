n = int(input())
arr = list(map(int, input().split()))
b, c = map(int, input().split())
result = 0

for num in arr:
    if num-b > 0:
        result += ((num-b)//c)+1
        if (num-b) % c != 0:
            result += 1
    else:
        result += 1
print(result)
