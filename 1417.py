arr = []
for _ in range(int(input())):
    arr.append(int(input()))
count = 0
while(max(arr)>arr[0]): 
    arr[arr.index(max(arr))]-=1
    arr[0] += 1
    count +=1
if arr.count(arr[0]) >1:
    print(count+1)
else:
    print(count)


