a=int(input("請輸入階乘值M:"))
r=0
i=1
while i<a:
    i=1
    for e in range(1,r+1):
      i=i*e  
    r+=1
print("超過M為"+str(a)+"的最小階層N值為:"+str(r-1))