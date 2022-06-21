a=(input("輸入N及M為:"))
y=[]
u=""
if (a.split(" ")[0]==0)and a.split(" ")[1]==0:
    exit
else:
    for i in range(int(a.split(" ")[0])):
        b=input("輸入矩陣數值第"+str(i+1)+"列為:")
        y.append(b.split(" "))
    for o in range(int(a.split(" ")[1])):
        for i in range(int(a.split(" ")[0])):
            u+=y[i][o]+" "
        print("輸出矩陣數值第"+str(o+1)+"列為:"+str(u))
        u=""