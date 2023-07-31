n,m=map(int,input().split())
chess=[]
chk=[]
for _ in range(n):
  chess.append(list(input()))
  
for i in range(n-7):
  for j in range(m-7):
    white,black=0,0
    for x in range(i,i+8):
      for y in range(j,j+8):
        if (x+y)%2==0:
          if chess[x][y]!='B':
            black+=1
          else:
            white+=1
        else:
          if chess[x][y]!='W':
            black+=1
          else:
            white+=1
    chk.append(white)
    chk.append(black)

print(min(chk))
        