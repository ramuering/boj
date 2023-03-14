
t = int(input())
nums = list(map(int, input().split()))

if t == 1:
    print(nums[0]*nums[0])
else:
    print(min(nums)*max(nums))
