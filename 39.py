n=int(input())
for i in range(int((n+1)/2)):
        print(' '*(n-i)+'*'*(2*i-1))
for i in range(int((n+1)/2),0,-1):
        print(' '*(n-i)+'*'*(2*i-1))