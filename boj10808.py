s = list(input())
cnt = [0]*26

for w in s:
    cnt[ord(w)-97] += 1

for i in cnt:
    print(i, end=' ')
