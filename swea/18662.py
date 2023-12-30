for n in range(int(input())):
    arr = list(map(int,input().split()))
    a = abs(2*arr[1]-arr[0]-arr[2])
    b = abs((arr[0]+arr[2])/2-arr[1])
    c = abs(2*arr[1]- arr[2]-arr[0])
    print(f'#{n+1} {min(a,b,c):.1f}')