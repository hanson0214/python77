a=""
while(a!=["e","n","d"]):
    a=list(input("檢測的字串(end結束)"))
    if a!=["e","n","d"]:
        c=input("檢測的單一字元:")
        print("字元"+c+"出現次數為:"+str(a.count(c)))
print("檢測結束")