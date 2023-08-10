s=input()
chk=input()

cnt=0
start=0
while True:
  idx=s.find(chk,start)
  if idx==-1:
    break
  else:
    if chk in s[start:]:
      cnt+=1
      start=idx+len(chk)
print(cnt)
