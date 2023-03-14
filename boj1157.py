from copy import copy

str = input()
str = str.upper()
s = set(str)
li = list(s)


n = str.count(li[0])
a = {li[0]: n}
i = 1
while i < len(li):
    n = str.count(li[i])
    a[li[i]] = n
    i += 1
result_k = list(a.keys())
result_v = list(a.values())

m = (int)(max(result_v))

k = 0
c = 0
while k < (int)(len(result_v)):
    if result_v[k] == m:
        c += 1
    k += 1

if c == 1:
    r = result_v.index(m)
    print(result_k[r])
else:
    print('?')
