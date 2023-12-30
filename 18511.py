n, p = map(str,input().split())
arr = sorted(list(map(int,input().split())))
res = ''
br = False
def findVal(val):
    for k in range(1,len(arr)):
        if val <= arr[k]:
            return str(arr[k-1])
    return str(arr[-1])
if int(n[0]) < arr[0]:
    print(str(arr[-1])*(len(n)-1))
    exit()
for i in range(len(n)):
    if int(n[i]) in arr:
        res += n[i]
    else:
        if int(n[i]) > arr[0]:
            res+=findVal(int(n[i]))
            break
        else:
            for j in range(1,i):
                res = res[:-1]
                if int(n[i-j]) > arr[0]:
                    res+=findVal(int(n[i-j]))
                    br = True
                    break
            if br:
                break
if int(res + str(arr[-1])*(len(n)-len(res)))>int(n):
    print(str(arr[-1])*(len(n)-1))
else:
    print(res + str(arr[-1])*(len(n)-len(res)))



            

