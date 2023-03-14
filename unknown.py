import sys
input = sys.stdin.readline

t = int(input())

stack = []
run = ['push', 'pop', 'top', 'size', 'empty']

for _ in range(t):
    s = list(input().split())
    if s[0] == run[0]:
        stack.append(s[1])
    if s[0] == run[1]:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    if s[0] == run[2]:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack)-1])
    if s[0] == run[3]:
        print(len(stack))
    if s[0] == run[4]:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
