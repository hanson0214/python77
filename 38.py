a=int(input())
t=[]
for u in range(a):
    t.append(int(input()))
for y in t:
    if y%9==0 or y%11==0:
        print("第"+str(t.index(y)+1)+"個點"+str(y))