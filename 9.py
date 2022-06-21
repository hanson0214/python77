a=(input("輸入s1為:"))
b=input("輸入s2為:")
p=0
if len(a)!=len(b):
    for i in range(len(b)-len(a)):
        if b[i:i+len(a)]==a:
            p=1
    if p==1:
        print("YES")
    else:
        print("NO")        
else:
    if b==a:
        print("YES")
    else:
        print("NO")
