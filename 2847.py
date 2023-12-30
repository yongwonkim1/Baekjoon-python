import sys
read = sys.stdin.readline
arr = []
for _ in range(int(read())):
    arr.append(int(read()))
cur = arr[-1]
count = 0
for i in range(len(arr)-2,-1,-1):
    if arr[i] >= cur:
        count += arr[i]-cur +1
        cur = cur-1
    else:
        cur = arr[i]
print(count)