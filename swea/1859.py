for n in range(int(input())):
    input()
    arr = list(map(int,input().split()))
    arr_2 = []
    res = 0
    for i in range(len(arr)):
        if(arr_2):
            if arr_2[-1]<arr[i]:
                if arr[i] == max(arr):
                    for j in range(len(arr_2)):
                        if arr_2[-1] < arr[i]:
                            res += arr[i] - arr_2.pop()
        arr_2.append(arr[i])
        arr[i] = 0
        arr_2.sort(reverse=True)
    print("#",n+1," ",res,sep="")


