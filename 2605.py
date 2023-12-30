arr = list(range(1,int(input())+1))
arr_2 = list(map(int,input().split()))
for i in range(len(arr)):
    for j in range(arr_2[i]):
        arr[i-j],arr[i-j-1] = arr[i-j-1],arr[i-j]
print(" ".join(map(str,arr)))
