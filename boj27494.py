num = int(input())
count = 0
for i in range(2023, num+1):
    array = list(str(i))
    temp = []
    for j in range(len(array)):
        t = array.pop(0)
        if (t == '2') and (len(temp) == 0):
            temp.append(t)
        if t == '0' and len(temp) == 1:
            temp.append(t)
        if t == '2' and len(temp) == 2:
            temp.append(t)
        if t == '3' and len(temp) == 3:
            count += 1
            break
print(count)
