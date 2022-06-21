a=input().split(" ")
b=0
for i in a:
    if i=="A":
        b+=1
    elif i=="J":
        b+=11
    elif i=="Q":
        b+=12
    elif i=="K":
        b+=13
    else:
        b+=int(i)
print(b)