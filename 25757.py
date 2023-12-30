import sys
read = sys.stdin.readline
n,a = read().split()
if a == 'Y':
    a=2
elif a=='F':
    a = 3
else:
    a=4
visited = set()
for _ in range(int(n)):
    visited.add(read())

print(len(visited)//(a-1))
