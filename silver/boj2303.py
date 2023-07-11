from itertools import combinations

n=int(input())
game=[[] for _ in range(n)]
result=[[] for _ in range(n)]
for i in range(n):
  tmp=list(map(int,input().split()))
  temp=list(combinations(tmp,3))
  for j in range(len(temp)):
    game[i].append(sum(temp[j]))
    result[i].append(sum(temp[j])%10)
ans=0
m=0
for i in range(len(result[i])):
  for j in range(n):
    if m<=result[j][i]:
      if m==result[j][i]:
        ans=max(ans,j)
      else:
          m=result[j][i]
          ans=j

print(ans+1)
    
  

