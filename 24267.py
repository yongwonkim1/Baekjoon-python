def MenOfPassion(n):
    A = list(range(n))
    sum = 0
    count = 0
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            for k in range(j + 1, n + 1):
                count+=1
                sum += A[i-1] * A[j-1] * A[k-1]
    return count
n = int(input())
print(MenOfPassion(n))
print("3")
