a=[[123,456,9000],[456,789,5000],[789,888,6000],[336,558,10000],[775,666,12000],[566,221,7000]]
u=int(input("輸入查詢組數N為:"))
i=0
for o in range(u):
    n=input().split(" ")
    for y in range(len(a)):
        if str(a[y][0])==str(n[0]) and str(a[y][1])==str(n[1]):
            i=1
            break
    if i==1:
        print(a[y][2])
        i=0
    else:
        print("error")
        i=0
