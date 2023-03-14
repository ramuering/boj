t = int(input())
for i in range(t):
    n = int(input())
    credit = []
    grade = 0
    for j in range(n):
        c, g = input().split()
        credit.append(int(c))
        grade += float(g)*int(c)
    avg = grade/sum(credit)
    print(sum(credit), "{0:.1f}".format(avg))
