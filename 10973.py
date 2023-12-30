n = int(input())
arr = list(map(int,input().split()))
stack = []
last = 0
if arr == list(range(1,n+1)):
    print(-1)
    exit()
stack.append(arr.pop())
for i in range(len(arr)):
    print(arr,stack)
    if arr[-1] < stack[-1]:
        stack.append(arr.pop())
    else:
        last = stack.pop()
        stack.append(arr.pop())
        break
print(' '.join(map(str,arr)),str(last),' '.join(map(str,sorted(stack))))