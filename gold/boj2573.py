import sys
from collections import deque


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def melting(): 
    new_board = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                continue
            melt_cnt = 0
            for d in range(4):
                ax = i + dx[d]
                ay = j + dy[d]
                if 0 <= ax < N and 0 <= ay < M and board[ax][ay] == 0:
                    melt_cnt += 1
            new_board[i][j] = max(0, board[i][j]-melt_cnt)
    return new_board


N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = 0
while True:
    answer += 1
    board = melting()
    cnt = 0
    visited = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0 and visited[i][j] == 0:
                if cnt == 1:
                    print(answer)
                    exit()
                visited[i][j] = -1
                queue = deque()
                queue.append([i, j])
                while queue:
                    x, y = queue.popleft()
                    for d in range(4):
                        ax = x + dx[d]
                        ay = y + dy[d]
                        if 0 <= ax < N and 0 <= ay < M and visited[ax][ay] == 0 and board[ax][ay] != 0:
                            queue.append([ax, ay])
                            visited[ax][ay] = -1
                cnt += 1
    if cnt == 0:
        print(0)
        exit()
