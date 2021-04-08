n=int(input())
p=n//2
for i in range(p):
    print ((p-1-i)*" ",end="")
    print((2*i+n-1)*"*",end="")
    print (2*(p-1-i)*" ",end="")
    print((2*i+n-1)*"*",end="")
    print('\n')    
for i in range(n):
    s=n-2-i
    print(2*i*" ",end="")
    print(2*s*"*",end="")
    print(2*s*"*",end="")
    print(2*i*" ",end="")
    print('\n')