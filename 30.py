a=""
y="1234"
while(a!='0000'):
    A=0
    B=0
    a=(input())
    if a!="0000":
        for u in range(len(a)):
            if a[u]==y[u]:
                A+=1
            if a[u]!=y[u] and y.count(a[u])>0:
                B+=1
        print(str(A)+"A"+str(B)+"B")
        
    