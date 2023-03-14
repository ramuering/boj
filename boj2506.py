t = int(input())
score = list(map(str, input().split()))
count = 0
temp = 0

for i in range(len(score)):
    if score[i] == '1':
        temp += 1
        count += temp
    if score[i] == '0':
        temp = 0

print(count)
