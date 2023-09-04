n = int(input())

cnt = 0
sing = 1
while n > 0:
    if sing > n:
        sing = 1
    n -= sing
    cnt += 1
    sing += 1
print(cnt)
