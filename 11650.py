import sys
arr = []
for _ in range(int(input())):
    arr.append(list(map(int,sys.stdin.readline().split())))
arr.sort()
for i in arr:
    print(i[0],i[1])