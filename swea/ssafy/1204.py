for tc in range(int(input())):
    cur = 0
    count = 0
    input()
    arr = list(map(int,input().split()))
    arr_s = set(arr)
    for s in arr_s:
        cur_count = arr.count(s)
        if count<cur_count:
            cur =s
            count = cur_count
    print(f'#{tc+1} {cur}')