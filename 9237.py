input()
res = 0
s = sorted(list(map(int,input().split())),reverse=True)
for i in range(len(s)):
    res = max(res,i+s[i])
print(res+2)