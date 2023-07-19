chk = ['(', ')', '[', ']']
while True:
    arr = list(input())
    ans = True
    if arr[0] == '.':
        break
    stack = []
    for i in arr:
        if i in chk:
            if i == chk[0] or i == chk[2]:
                stack.append(i)
            elif i == chk[1] and stack:
                if chk[0] == stack[-1]:
                    stack.pop()
                elif stack[-1] == chk[2]:
                    ans = False
            elif i == chk[3] and stack:
                if chk[2] == stack[-1]:
                    stack.pop()
                elif stack[-1] == chk[0]:
                    ans = False
            elif i == chk[1] or i == chk[3] and not stack:
                ans = False
        else:
            continue
    if len(stack) == 0 and ans:
        print('yes')
    else:
        print('no')
