a=int(input("搭了幾次電梯:"))
o=1
t=0
for u in range(a):
    i=int(input())
    if o>i:
        t+=(o-i)*10
        o=i
    else:
        t+=(i-o)*20
        o=i
print(str(t)+"元")