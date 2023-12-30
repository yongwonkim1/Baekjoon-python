for tc in range(int(input())):
    arr = [[0] * 9 for _ in range(9)]
    for i in range(9):
        arr[i] = list(map(int,input().split()))
    for i in range(9):
        j = i // 3
        l = i % 3
        if len(set(arr[i]))<9:
            print(f'#{tc+1} 0')
            break
        if len(set(k[i] for k in arr)) < 9:
            print(f'#{tc+1} 0')
            break
        if len(set(sum(list(k[3*l:3*l+3] for k in arr[3*j:3*j+3]),[]))) < 9:
            print(f'#{tc+1} 0')
            break
        if i == 8:
            print(f'#{tc+1} 1')