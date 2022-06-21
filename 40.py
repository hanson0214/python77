a=int(input())
s=""
for t in range(1,a,2):
    print(" "*int(a/2)+str(t))
    s+=str(t)
print(s+str(a)+s[::-1])
for t in range(a-2,0,-2):
    print(" "*int(a/2)+str(t))