from itertools import combinations
import math
nums=list(map(int,input().split()))
ans=[]
if 1 in nums:
  nums = [i for i in nums if i>1]
  for a,b in combinations(nums,3-(5-len(nums))):
    tmp=math.gcd(a,b)
    ans.append(a*b//tmp)
  print(min(ans))
else: 
  for a,b,c in list(combinations(nums,3)):
    tmp1=math.gcd(a,b)
    tmp2=math.gcd(tmp1,c)
    tmp3=a*b//tmp1
    ans.append(tmp3*c//tmp2)
  print(min(ans))  