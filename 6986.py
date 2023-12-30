import sys
import decimal
read = sys.stdin.readline
n, k = map(int,read().split())
arr = []
for _ in range(n):
    arr.append(float(read()))
arr.sort()
if k == 0:
    print(f'{round(sum(arr)/n+0.00000001,2):.2f}')
    print(f'{round(sum(arr)/n+0.00000001,2):.2f}')
else:
    print(f'{round(sum(arr[k:-k])/(n-2*k)+0.00000001,2):.2f}')
    print(f'{round((sum(arr[k:-k])+k*arr[k]+k*arr[-k-1])/n+0.00000001,2):.2f}')
    


