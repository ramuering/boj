def Rev(num):
    num = list(str(num))
    num.reverse()
    return ''.join(num).lstrip('0')


a, b = map(str, input().split())

print(Rev(int(Rev(a))+int(Rev(b))))
