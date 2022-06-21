a=int(input())
b=int(input())
c=int(input())
if b*b-(4*a*c)<0:
    print(0)
elif b*b-(4*a*c)>0:
    print((-b+((b*b-(4*a*c))**(1/2)))/(2*a))
    print((-b-((b*b-(4*a*c))**(1/2)))/(2*a))
else:
    print(((-b+((b*b-(4*a*c))**(1/2)))/(2*a)))