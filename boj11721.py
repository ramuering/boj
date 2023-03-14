s = list(input())
count = 0
for w in s:
    count += 1
    print(w, end='')
    if count % 10 == 0:
        print()
