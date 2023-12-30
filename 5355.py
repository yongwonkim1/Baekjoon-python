for _ in range(int(input())):
    arr = list(input().split())
    res = float(arr[0])
    for i in arr[1:]:
        if i == '@':
            res*=3
        elif i == '%':
            res+=5
        else:
            res-=7
    print(f'{res:.2f}')
