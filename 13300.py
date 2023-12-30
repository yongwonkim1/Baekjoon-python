import math
n, k = map(int,input().split())
room = 0
arr = [[0 for _ in range(2)] for _ in range(6)]
for i in range(n):
    a, b = map(int, input().split())
    arr[b-1][a]+=1
for i in range(2):
    for j in range(6):
        if arr[j][i]==0:
            continue
        room += math.ceil(arr[j][i]/k)
print(room)