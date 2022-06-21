a=""
while(a!="end"):
    y=""
    h=0
    h1=0
    a=(input("輸入整數數列(end結束)"))
    if(a!="end"):
        for t  in range(len(a)):
            for o  in range(len(a)):
                c=a[t:o]
                for r in a[t:o]:
                    h1+=int(r)
                if a[t:o] == c[::-1] and c!="" and len(y)<=len(a[t:o]):
                    if len(y)==len(a[t:o]):
                        for r in y:
                            h+=int(r)
                        if h1<h:
                            y=a[t:o]

                    else:
                        y=a[t:o]
                h=0
                h1=0
        print("最長迴文數字子數列為:"+y)
print("結束")
