for t in range(int(input())):
    n, m = map(int,input().split())
    arr = []
    answer = 0
    for i in range(n):
        arr.append(list(map(int,input().split())))
        for j in range(1,n):
            arr[i][j] +=arr[i][j-1]
    for i in range(n-m+1):
        for j in range(n-m+1):
            res = 0
            for k in range(m):
                if j==0:
                    res+=arr[i+k][m-1]
                else:
                    res += arr[i+k][m-1+j]-arr[i+k][j-1]
            answer = max(answer,res)
    print(f'#{t+1} {answer}')