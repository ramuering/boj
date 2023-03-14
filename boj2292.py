n = int(input())
cal = 6
count = 1
while True:
    if n <= 1:
        break
    n -= cal
    count += 1

    if 1 < n < cal:
        count += 1
        break
    cal += 6

print(count)
