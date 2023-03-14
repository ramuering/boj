n, m = map(int, input().split())
nums = list(map(int, input().split()))
result = []
for i in range(n-2):
    for j in range(i+1, n-1):
        for r in range(j+1, n):
            result.append(nums[i]+nums[j]+nums[r])
min = 100000
for num in result:
    if abs(m-num) < min and m >= num:
        min = abs(m-num)
        absNum = num

print(absNum)
