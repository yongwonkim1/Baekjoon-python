for i in range(int(input())):
    arr = list(map(int,input().split()))
    answer = 0
    for ele in arr:
        if ele %2 == 1:
            answer+=ele
    print(f'#{i+1} {answer}')