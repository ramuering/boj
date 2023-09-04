import sys
s = sys.stdin.read()
ch = [0] * 200
max = -2147000000

for i in s:
    if s.islower():
        ch[ord(i)] += 1

for i in range(len(ch)):
    if ch[i] > max:
        max = ch[i]

for i in range(len(ch)):
    if ch[i] == max:
        print(chr(i), end='')
