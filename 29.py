a=list(input("甲方的數字:"))
b=list(input("乙方的數字:"))
g=""
for u in range(len(a)):
    if a[u]=="1" and b[u]=="5":
        g+="贏"
    elif a[u]=="1" and b[u]=="2":
        g+="輸"
    elif a[u]=="2" and b[u]=="1":
        g+="贏"
    elif a[u]=="2" and b[u]=="3":
        g+="輸"
    elif a[u]=="3" and b[u]=="2":
        g+="贏"
    elif a[u]=="3" and b[u]=="4":
        g+="輸"
    elif a[u]=="4" and b[u]=="3":
        g+="贏"
    elif a[u]=="4" and b[u]=="5":
        g+="輸"
    elif a[u]=="5" and b[u]=="4":
        g+="贏"
    elif a[u]=="5" and b[u]=="1":
        g+="輸"
    else:
        g+="和"    
print("洗刷刷結果:"+g)