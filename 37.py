n=int(input("整數n:"))
t=[]
while (n!=1):
    t.append(int(n))
    if n%2==0:
        n=(n/2)
    elif n%2==1 and n!=1:
        n=3*n+1
s=""
for r in t:
    s+=str(r)+" "
print("數列:"+s+"1")