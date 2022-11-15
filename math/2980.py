import sys
read = sys.stdin.readline
light = []
cnt = 0
cur = 0
N, L = map(int, read().split())
for i in range(N):
    d, r, g = map(int, read().split())
    cnt += d - cur
    cur = d
    c = cnt % (r + g)
    if c > r:
        continue
    else:
        cnt += r-c

print(cnt + L - cur)
