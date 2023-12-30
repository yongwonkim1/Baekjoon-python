n = int(input())
for i in range(n):
    result = 0
    arr = list(map(int,input().split()))
    for ele in arr:
        if ele%2!=0:
            result+=ele
    print("#",i+1," ",result,sep="")
    