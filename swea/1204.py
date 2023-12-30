for n in range(int(input())):
    input()
    answer = 0
    arr=list(map(int,input().split()))
    for i in range(101):
        if arr.count(i) >= arr.count(answer):
            answer = i
    print(f'#{n+1} {answer}')