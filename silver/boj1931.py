from sys import stdin

n=int(input())
room=[]

for i in range(n):
  room.append(list(map(int,stdin.readline().split())))

room.sort(key=lambda x:(x[1], x[0]))
chk=room[0]
cnt=1
room.pop(0)
for start,end in room:
  if start>=chk[1]:
    chk=[start,end]
    print(chk)
    cnt+=1

print(cnt)