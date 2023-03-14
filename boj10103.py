t = int(input())
a, b = 100, 100
for i in range(t):
    A, B = map(int, input().split())
    if A > B:
        b -= A
    if B > A:
        a -= B
print(a)
print(b)
