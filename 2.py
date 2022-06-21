import math
a=int(input())
s=0
ns=0
if a>120:
    s+=2.10*120
    ns+=2.10*120
    a-=120
else:
    s+=2.10*a
    ns+=2.10*a
    print("summer months"+str(round(s,2)))
    print("non-summer months"+str(round(ns,2)))
    a-=a
if a>210:
    s+=3.02*210
    ns+=2.68*210
    a-=210
else:
    s+=3.02*a
    ns+=2.68*a
    print("summer months"+str(round(s,2)))
    print("non-summer months"+str(round(ns,2)))
    a-=a
if a>170:
    s+=4.39*170
    ns+=3.61*170
    a-=170
else:
    s+=4.39*a
    ns+=3.61*a
    print("summer months"+str(round(s,2)))
    print("non-summer months"+str(round(ns,2)))
    a-=a
if a>200:
    s+=4.97*200
    ns+=4.01*200
    a-=200
else:
    s+=4.97*a
    ns+=4.01*a
    print("summer months"+str(round(s,2)))
    print("non-summer months"+str(round(ns,2)))
    a-=a
if a>0:
    s+=5.63*a
    ns+=4.50*a
    print("summer months"+str(round(s,2)))
    print("non-summer months"+str(round(ns,2)))
    a-=a



