n=int(input())
if n<100:
  print(n)
else:
  ans=99
  for i in range(100,n+1):
    tmp=tuple(map(int,str(i)))
    if tmp[0]-tmp[1]==tmp[1]-tmp[2]:
      ans+=1
  print(ans)