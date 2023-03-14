s = input()
count = 0
for i in range(len(s)):
    if s[i] in ['a', 'e', 'i', 'o', 'u']:
        count += 1
print(count)
