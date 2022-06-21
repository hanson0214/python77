from re import L


a=[]
a.append((input("國文:")))
a.append(input("英文:"))
a.append(input("微積分:"))
a.append(input("體育:"))
a.append(input("程式設計:"))
a=list(map(float,a))
g=0
for y in a:
    g+=y
print("平均分數:"+str(float(round(g/5,2))))
h=""
if a.index(max(a))==0:
    h="國文"
elif a.index(max(a))==1:
    h="英文"
elif a.index(max(a))==2:
    h="微積分"
elif a.index(max(a))==3:
    h="體育"
elif a.index(max(a))==4:
    h="程式設計"
print("最高分科目:"+h+str(int(max(a)))+"分")
l=""
if a.index(min(a))==0:
    l="國文"
elif a.index(min(a))==1:
    l="英文"
elif a.index(min(a))==2:
    l="微積分"
elif a.index(min(a))==3:
    l="體育"
elif a.index(min(a))==4:
    l="程式設計"
print("最低分科目:"+l+str(int(min(a)))+"分")