import string
a=list("紅豆生南國,春來發幾枝,願君多采擷,此物最相思。")
b=list("春眠不覺曉,處處聞啼鳥,夜來風雨聲,花落知多少?")
c=set()
d=set()
for word in a:
    for letter in word:
        if letter in string.punctuation:
            word = word.replace(letter,"")   
    c.add(word)
for word in b:
    for letter in word:
        if letter in string.punctuation:
            word = word.replace(letter,"")   
    d.add(word)
c.remove("")
d.remove("")
print(c&d)