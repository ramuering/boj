import sys


t=int(sys.stdin.readline())
result=[]

for _ in range(t):
    oper=list(sys.stdin.readline().split())
    if oper[0]=='push':
        oper[1]=int(oper[1])
        result.append((oper[1]))
    elif oper[0]=='pop':
        if len(result)==0:
            print('-1')
        else:
          print(result[0])
          del result[0]
    elif oper[0]=='size':
      print(len(result))
    elif oper[0]=='empty':
      if len(result)==0:
        print(1)
      else:
        print(0)  
    elif oper[0]=='front':
      if len(result)>0:
        print(result[0])
      else:
        print(-1)
    elif oper[0]=='back':
      if len(result)>0:
        print(result[-1])
      else:
        print(-1)
      
