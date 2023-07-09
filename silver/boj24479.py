import sys
sys.setrecursionlimit(400000)

def dfs(graph, start, vis):
    global cnt
    vis[start] = cnt
    for i in graph[start]:
        if not vis[i]:
            cnt += 1
            dfs(graph, i, vis)


n, m, r = map(int, input().split())
graph = [[]for _ in range(n+1)]
vis = [False]*(n+1)
cnt = 1

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n+1):
    graph[i].sort()

dfs(graph, r, vis)

for i in range(1, n+1):
    if vis[i]:
        print(vis[i])
    else:
        print(0)
