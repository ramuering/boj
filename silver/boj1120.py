a, b = input().split()
n = len(b)-len(a)
m = 51

for i in range(n+1):
    cnt = 0
    for j in range(len(a)):
        if b[i+j] != a[j]:
            cnt += 1
    if m > cnt:
        m = cnt

print(m)
