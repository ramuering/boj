import sys
sys.setrecursionlimit(100000)

def dfs(x):
  vis[x]=True
  for i in graph[x]:
    if vis[i]==False:
      dfs(i)

n,m=map(int,sys.stdin.readline().split())

graph=[[] for _ in range(n+1)]
vis=[False]*(n+1)

for i in range(m):
  x,y=map(int,sys.stdin.readline().split())
  graph[x].append(y)
  graph[y].append(x)
  
ans=0 
for i in range(1,n+1):
  if not vis[i]:
    dfs(i)
    ans+=1
print(ans)