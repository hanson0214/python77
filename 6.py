a=(input("輸入值為:"))
a.split(",")
s=""
p=""
d=[]
d=a.split(",")
d.sort()
for i in d:
    s+=i
d.reverse()
for i in d:
    p+=i
print("最大值數列與最小值數列差值為"+int(p)-int(s))