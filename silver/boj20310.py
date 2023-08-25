import sys

s = list(sys.stdin.readline().strip())
zero = s.count('0')//2
one = s.count('1')//2

i = 0
while one > 0:
    if s[i] == '1':
        s[i] = '_'
        one -= 1
    i += 1

j = -1
while zero > 0:
    if s[j] == '0':
        s[j] = '_'
        zero -= 1
    j -= 1
s = ''.join(s)
s = s.replace('_', '')
print(s)
