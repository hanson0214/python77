d=int(input())
s=""
p=""
for u in range(d):
    for y in range(4):
        s+=((input()))
    if int(s[-3])-int(s[-4])==int(s[-2])-int(s[-3]):
        s+=str(int(s[-1])+(int(s[-3])-int(s[-4])))

        p+="等差數列"+" "
    if int(s[-3])/int(s[-4])==int(s[-2])/int(s[-3]):
        s+=str(int(int(s[-1])*(int(s[-3])/int(s[-4]))))

        p+="等比數列"+" "
    s+=";"
q=s.split(";")
t=p.split(" ")
for w in range(len(q)):
    if w!=len(q)-1:
        print(q[w])
        print("此為"+t[w])

    