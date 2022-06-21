a=int(input("小明身上有多少錢:"))
b=int(input("販賣機有幾種飲料:"))
c=0
f=[]
for t in range(b):
    f.append(int(input()))
for y in f:
    if a>=y:
        c+=1
print(c)
