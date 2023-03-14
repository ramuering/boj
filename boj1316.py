def checker(word):
    chk = set()
    for i in range(len(word)):
        if word[i] not in chk:
            chk.add(word[i])
            s = 1
        else:
            if word[i] == word[i-1]:
                continue
            else:
                s = 0
                break
    if s == 1:
        return 1


t = int(input())
result = 0
for _ in range(t):
    word = list(input())
    if checker(word):
        result += 1

print(result)
