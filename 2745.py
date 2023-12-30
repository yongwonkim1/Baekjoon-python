a, b = input().split()
result = 0
b=int(b)
for i in range(1,len(a)+1):
    if a[-i].isdigit() :
        result+= int(a[-i])*b**(i-1)
    else:
        result += (ord(a[-i])-ord("A")+10) * b**(i-1)
print(result)