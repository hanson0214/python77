a=(input("輸入月及日為:"))
w=int(a.split(" ")[0])
w1=int(a.split(" ")[1])
if (w==1 and w1>=21)or(w==2 and w1<=18):
    print("星座為"+"Aquarius") 
elif(w==2 and w1>=19)or(w==3 and w1<=20):
    print("星座為"+"Pisces")
elif(w==3 and w1>=21)or(w==4 and w1<=20):
    print("星座為"+"Aries")
elif(w==4 and w1>=21)or(w==5 and w1<=21):
    print("星座為"+"Taurus")
elif(w==5 and w1>=22)or(w==6 and w1<=21):
    print("星座為"+"Gemini") 
elif(w==6 and w1>=22)or(w==7 and w1<=22):
    print("星座為"+"Cancer") 
elif(w==7 and w1>=23)or(w==8 and w1<=23):
    print("星座為"+"Leo") 
elif(w==8 and w1>=24)or(w==9 and w1<=23):
    print("星座為"+"Virgo") 
elif(w==9 and w1>=24)or(w==10 and w1<=23):
    print("星座為"+"Libra") 
elif(w==10 and w1>=24)or(w==11 and w1<=22):
    print("星座為"+"Scorpio") 
elif(w==11 and w1>=23)or(w==12 and w1<=21):
    print("星座為"+"Sagittarius") 
elif(w==12 and w1>=22)or(w==1 and w1<=20):
    print("星座為"+"Capricorn") 