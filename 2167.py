import sys
read = sys.stdin.readline
n, m = map(int,read().split())
arr = []
for _ in range(n):
    arr.append(list(map(int,read().split())))
for _ in range(int(read())):
    i, j, x, y = map(int,read().split())
    res = 0
    for k in range(i-1,x):
        for z in range(j-1,y):
            res += arr[k][z]
    print(res)