x=input()
if x=='1000':
  x='999'
ans=99
if len(x)<=2:
  ans=x
else:
  ans=ans+((int(x[0])-1)*5)
  if int(x[1])%2!=0:
    start=int(x[0])//2+1
  else:
    start=int(x[0])//2
  for i in range(start,10):
    if int(x[0])>i and int(x[0])-i>=0 and (int(x[0])-i)==(i-(int(x[0])-i)):
      ans+=1
      continue
    if int(x[0])<i and i-int(x[0])>=0 and (i-int(x[0]))==i+(i-int(x[0])):
      ans+=1
      continue
    if int(x[0])==i:
      ans+=1
print(ans)
  
