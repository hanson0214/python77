from tkinter import W


t=int(input("請輸入陣列大小:"))
a=[]
for y in range(t):
    a.append(input().split(" "))
p=0
p1=""
for u in range(t):
    for o in range(t):
        if int(a[u][o])>p:
            p=int(a[u][o])
            a[u][o]=0
            p1="("+str(u+1)+","+str(o+1)+")"
w=0
w1=""
for u in range(t):
    for o in range(t):
        if int(a[u][o])>w:
            w=int(a[u][o])
            a[u][o]=0
            w1="("+str(u+1)+","+str(o+1)+")"
j=0
j1=""
for u in range(t):
    for o in range(t):
        if int(a[u][o])>j:
            j=int(a[u][o])
            a[u][o]=0
            j1="("+str(u+1)+","+str(o+1)+")"
print("最大值為:"+str(p+w+j))
print("位置為"+str(p1)+","+str(w1)+","+str(j1))