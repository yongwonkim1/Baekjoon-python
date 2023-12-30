a,b = input().split()
arr = []
count = 0
rarr = []
for _ in range(int(a)):
    arr.append(list(map(int,input().split())))
    if arr[-1][0] == int(b):
        rarr = arr[-1]
for i in range(len(arr)):
    if arr[i][1] > rarr[1]:
        count +=1
        continue
    elif arr[i][1] == rarr[1]:
        if arr[i][2] > rarr[2]:
            count+=1
            continue
        elif arr[i][2] == rarr[2]:
            if arr[i][3] > rarr[3]:
                count +=1
print(count+1)