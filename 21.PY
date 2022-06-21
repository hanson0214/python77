a=[[123,"Tom",'DTGD'],[456,'Cat','CSIE'],[789,'Nama','ASIE'],[321,'Lim','DBA'],[654,'Wen','FDD']]
r=int(input("輸入查詢學號為:"))
for y in range(len(a)):
    if a[y][0]==r:
        print("學生資料為:"+str(a[y][0])+a[y][1]+a[y][2])