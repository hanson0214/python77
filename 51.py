import string
a=list(input())
b=set()
c = []
for word in a:
    for letter in word:
        if letter in string.punctuation:
            word = word.replace(letter,"")   
    c.append(word)
for r in c:
    if c.count(r)>1 and r!="":
        b.add(r)
print(b)
