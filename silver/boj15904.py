s=input()
chk=['U',"C","P",'C']
i=0
start=0
while True:
  if i>3:
    print('I love UCPC')
    break
  idx=s.find(chk[i],start)
  if idx==-1:
    print('I hate UCPC')
    break
  else:
    start=idx+1
    i+=1
    

    