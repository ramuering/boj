from collections import deque


def bfs(x, y):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1 and visited[nx][ny] == False:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx, ny))
                visited[nx][ny] = True
    return graph[n-1][m-1]


n, m = map(int, input().split())
graph = []
visited = [[False for _ in range(m)] for _ in range(n)]
for i in range(n):
    graph.append(list(map(int, input())))

print(bfs(0, 0))
