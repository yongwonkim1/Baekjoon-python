s = input()
arr = ['c=','c-','dz=','d-','lj','nj','s=','z=']
skip = 0
count = 0
for i in range(len(s)):
    if skip >0:
        skip -= 1
        continue
    if s[i:i+3] in arr:
        skip = 2
    elif s[i:i+2] in arr:
        skip = 1
    count+=1
print(count)
