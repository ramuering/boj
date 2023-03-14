n = int(input())
nums = list(map(int, input().split()))
cnt = 0
for num in nums:
    if num == 1:
        continue
    ox = 0
    for i in range(2, num):
        if num % i == 0:
            ox += 1
            break
    if ox == 0:
        cnt += 1
print(cnt)
