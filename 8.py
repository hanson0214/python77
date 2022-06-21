a=int(input("輸入第一行正整數為:"))
b=input("第二行中數列中的數字為:")
c=[]
c=b.split(" ")
v=0
o=""
for i in c:
    if c.count(i)>1 and v<c.count(i):
        v=c.count(i)
        o=i
if v>1:
    print("最大出現次數的數字為:"+o)
    print("出現次數為:"+str(v))
else:
    print("每個次數剛好只出現1次")

    