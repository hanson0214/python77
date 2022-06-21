a={'John','Mary','Tina','Fiona','Claire','Eva','Ben','Bill','Bert'}
b={'John','Mary','Fiona','Claire','Ben','Bill'}
c={'Mary','Fiona','Claire','Eva','Ben'}
print("數學跟英文都及格"+str(c&b))
print("數學不及格"+str(a-c))
print("英文及格且數學不及格"+str(b&(a-c)))