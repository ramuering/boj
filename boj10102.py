t = int(input())
a, b = 0, 0
score = list(map(str, input()))
for i in range(t):
    if score[i] == 'A':
        a += 1
    if score[i] == 'B':
        b += 1
if a > b:
    print('A')
if a < b:
    print('B')
if a == b:
    print("Tie")
