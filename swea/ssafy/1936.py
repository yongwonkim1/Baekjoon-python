a,b = map(int,input().split())
a = 4 if b==3 and a==1 else a
b = 4 if a==3 and b==1 else b
print('A' if a > b else 'B')

