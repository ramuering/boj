s = input()
if s.count('-') > 0:
    s = s[:s.index('-'):]+s[s.index('-'):].replace('+', '-')
tmp = [str(i) for i in range(10)]
num = []
temp = []

for i in range(len(s)):
    if s[i] in tmp:
        temp.append(s[i])
        if i == len(s)-1:
            num.append(int(''.join(temp)))
    if s[i] not in tmp:
        if temp:
            num.append(int(''.join(temp)))
            temp = []
            num.append(s[i])

result = num.pop(0)
for i in range(len(num)):
    if num[i] == '+':
        result += num[i+1]
    elif num[i] == '-':
        result -= num[i+1]
    elif type[num[i]] is int:
        continue

print(result)
