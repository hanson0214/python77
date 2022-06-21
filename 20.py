a=int(input("組數為:"))
for i in range(a):
    n=input("第"+str(i+1)+"組").split(" ")
    print("第"+str(i+1)+"組應收費用:"+str((250*int(n[0])+175*int(n[1]))))