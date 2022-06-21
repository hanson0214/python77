a=(input("輸入一整數序列為:"))
c=a.split(" ")
p=0
for i in c:
    if c.count(i)>(len(c)/2):
        p=1
if(p==1):
    print("過半元素為:"+i)
else:
    print("過半元素為:NO")
