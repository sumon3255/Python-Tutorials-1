f=open("sumon.txt")
#print(f.tell())

f.seek(10)#reading will be start from 10th no charecter
#print(f.tell())
print(f.readline())
#print(f.tell())

#print(f.tell())
f.close()