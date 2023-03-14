
t = int(input())

for _ in range(t):
    string = list(input())
    left, right = 0, 0
    for i in range(len(string)):
        check = string[i]
        if check == '(':
            left += 1
        if check == ')':
            right += 1
            if right > left:
                break
    if left == right:
        print("YES")
    else:
        print("NO")
