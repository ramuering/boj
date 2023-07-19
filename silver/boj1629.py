def power(a, b):
    if b == 1:
        return a % c
    if b % 2:
        return (power(a, b-1)*a) % c
    tmp = power(a, b//2) % c
    return tmp**2 % c


a, b, c = map(int, input().split())

print(power(a, b))
