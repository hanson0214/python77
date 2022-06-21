a=int(input())
t=[]
for u in range(a):
    t.append(int(input()))
t.sort()
print(t[len(t)-1])