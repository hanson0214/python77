a=input("輸入月租費形式及通話時間為:")
s=0
if a.split(",")[0]=="186":
    s=round(int(a.split(",")[1])*0.09)
    if s>186:
        s=round(s*0.8)
    else:
        s=round(s*0.9)
if a.split(",")[0]=="386":
    s=round(int(a.split(",")[1])*0.08)
    if s>386:
        s=round(s*0.7)
    else:
        s=round(s*0.8)
if a.split(",")[0]=="586":
    s=round(int(a.split(",")[1])*0.07)
    if s>586:
        s=round(s*0.6)
    else:
        s=round(s*0.7)
if a.split(",")[0]=="986":
    s=round(int(a.split(",")[1])*0.06)
    if s>986:
        s=round(s*0.5)
    else:
        s=round(s*0.6)
print("通話費為:"+str(s))
