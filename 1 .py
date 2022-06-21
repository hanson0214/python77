a=(input("請輸入正整數"))
s=""
d=[]
r=0
u=0
for i in range(1,len(list(a))+1):
    for f in range(1,len(list(a))+1):
        r=int(a[f-1:f+i-1])
        u=0
        for t in range(1,r+1):
            if(r%t)==0:u+=1
        if (u==2):d.append(r)
d.sort()
if d==[]:
    print("NO PRIME FOUND")
else:
    print("子字串中最大的質數為"+d[len(d)-1])
