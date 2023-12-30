for tc in range(int(input())):
    n,m = map(int,input().split())
    arr = [[0] * n for _ in range(n)]
    for i in range(n):
        arr[i] = list(map(int,input().split()))
    