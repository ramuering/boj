import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


def dfs(graph, v, vis, cnt):
    vis[v] = True
    for i in graph[v]:
        if i == y:
            print(cnt+1)
            exit()
        if not vis[i]:
            dfs(graph, i, vis, cnt+1)


n = int(input())
x, y = map(int, input().split())
m = int(input())


vis = [False]*(n+1)
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(graph, x, vis, 0)
print(-1)
