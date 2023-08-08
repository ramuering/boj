import sys
sys.setrecursionlimit(10000)

def dfs(graph,x, vis):
  if vis[x]:
    return False
  vis[x]=True
  for i in graph[x]:
    if not vis[i]:
      dfs(graph,i,vis)
    return True
  return False

n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
vis=[False]*(n+1)
vis[0]=True

for i in range(m):
  a,b=map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

cnt=0
for i in range(1,n+1):
  if dfs(graph,i,vis):
    cnt+=1
print(cnt)


