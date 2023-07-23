n = int(input())
cnt = 0
start = 666
while True:
    if '666' in str(start):
        cnt += 1
    start += 1
    if cnt == n:
        break
print(start-1)
