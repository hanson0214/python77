a = list((input("輸入一組四位數字為:")))
for i in range(len(a)):
    a[i]=(int(a[i])+7)%10
n=0
n=a[0]
a[0]=a[2]
a[2]=n
n=a[1]
a[1]=a[3]
a[3]=n
t=""
for i in range(len(a)):
    t+=str(a[i])
print("輸出加密後的數字為:"+t)