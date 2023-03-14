def ROT13(s):
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr(ord(s[i])+13)
            if ord(s[i]) > 90:
                s[i] = chr(ord(s[i])-26)
        if s[i].islower():
            s[i] = chr(ord(s[i])+13)
            if ord(s[i]) > 122:
                s[i] = chr(ord(s[i])-26)
    return s


s = list(input())
print(''.join(ROT13(s)))
