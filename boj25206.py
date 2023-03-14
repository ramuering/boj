stu = [input().split() for _ in range(20)]
total = 0
score = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0,
         'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}
avg = 0
for i in range(20):
    if stu[i][2] != 'P':
        total += (score[stu[i][2]]*float(stu[i][1]))
        avg += float(stu[i][1])
print(format(round(total/avg, 6), ".6f"))
