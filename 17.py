a=(input(""))
y=[]
for i in range(int(a.split(" ")[0])):
        b=input()
        y.append(b.split(" "))
a1=(input(""))
y1=[]
t=""
for i in range(int(a1.split(" ")[0])):
        b1=input()
        y1.append(b1.split(" "))
for o in range(int(a.split(" ")[1])):
        for i in range(int(a.split(" ")[0])):
            y[i][o]=int(y[i][o])
            y1[i][o]=int(y1[i][o])
            (y[i][o])+=y1[i][o]
            t+=str(y[i][o])+" "
        print(t)
        t=""