import sys
from collections import deque

queue = deque()
n = int(sys.stdin.readline())
for _ in range(n):
    run = list(sys.stdin.readline().split())
    if run[0] == 'push_back':
        queue.append(run[1])
    if run[0] == 'push_front':
        queue.insert(0, run[1])
    if run[0] == 'pop_front':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    if run[0] == 'pop_back':
        if queue:
            print(queue.pop())
        else:
            print(-1)
    if run[0] == 'size':
        print(len(queue))
    if run[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    if run[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    if run[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
