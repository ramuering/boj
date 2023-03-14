n = int(input())
f = int(input())

cnt = 1
n = (n//100)*100

while True:
    if n % f == 0:
        break
    n += cnt

print('{0:02d}'.format(n % 100))
