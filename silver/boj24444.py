from collections import deque


def bfs(graph, start, vis, cnt):
    queue = deque([start])
    vis[start] = cnt
    cnt += 1
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not vis[i]:
                queue.append(i)
                vis[i] = cnt
                cnt += 1


n, m, r = map(int, input().split())

graph = [[] for _ in range(n+1)]
vis = [False]*(n+1)
result = []
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in range(len(graph)):
    graph[i].sort()
bfs(graph, r, vis, 1)

for i in range(1, n+1):
    if vis[i]:
        print(vis[i])
    else:
        print(0)
