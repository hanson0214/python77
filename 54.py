a=float(input("請輸入路程公里數(km)"))
if a<=1.5:
    print("所需車資為:75")
else:
    print("所需車資為:"+str(5*int((a-1.5+0.24)/0.25)+75))