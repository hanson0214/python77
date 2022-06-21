a=int(input("輸入筆數:"))
t=[]
for u in range(a):
    b=input().split(" ")
    t.append(b[0])
    t.append(b[1])
for u in range(0,len(t),2):
    print(t[u]+"牌得到"+t[u+1]+"面")