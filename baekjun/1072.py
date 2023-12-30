import math
x,y = map(int,input().split())

k=0

if x==y:
    print(-1)
    exit()
while(1):
    v = (y+k)*100//(x+k)+1
    k = v*x//100-y
    print(v,k)
    if (y+k)*100//(k+x)>=v:
        break
print(k)