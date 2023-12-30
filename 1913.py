n = int(input())
k = int(input())
arr = [[0]*n for _ in range(n)]
ver =  n//2
hor = n//2
cur = 1
arr[ver][hor] = cur
for i in range(1,n+1):
    if i&2==1:
        for _ in range(i):
            
            

