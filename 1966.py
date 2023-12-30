import sys
from collections import deque
read= sys.stdin.readline

for _ in range(int(read())):
    n, m = map(int,read().split())
    arr= deque(list(map(int,read().split())))
    i = 0
    while(arr):
        if max(arr) == arr[0]:
            i+=1
            arr.popleft()
            if m==0:
                print(i)
                break
        else:
            arr.append(arr.popleft())
        if m==0:
            m=len(arr)-1
        else:
            m-=1
    
