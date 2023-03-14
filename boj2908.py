a, b = input().split()
reverse_a = list(a)
reverse_b = list(b)

reverse_a.reverse()
reverse_b.reverse()

for i in range(3):
    if int(reverse_a[i]) > int(reverse_b[i]):
        result = reverse_a
        break
    elif int(reverse_a[i]) < int(reverse_b[i]):
        result = reverse_b
        break
print(''.join(result))
