arr =[]
n = int(input())
result = ''
for _ in range(n):
    arr.append(input())
for i in range(len(arr[0])):
    word = arr[0][i]
    for j in range(1,n):
        if arr[j][i] != word:
            word = '?'
            break
    result+=word
print(result)
