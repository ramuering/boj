import math

n, m = map(int, input().split())

factor = math.gcd(n, m)
multiple = (n*m)//factor
print(factor)
print(multiple)
