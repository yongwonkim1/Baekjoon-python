import sys
read = sys.stdin.readline
n = int(read())
arr = sorted(list(map(int,read().split())))
if n%2 == 0:
    print(arr[n//2-1])
else:
    print(arr[n//2])
