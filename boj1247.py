i = 0
while i < 3:
    s = (int)(input())
    j = 0
    sum = 0
    while j < s:
        num = (int)(input())
        sum = (int)(sum+num)
        j += 1
    if sum == 0:
        print('0')
    elif sum < 0:
        print('-')
    elif sum > 0:
        print('+')
    i += 1
