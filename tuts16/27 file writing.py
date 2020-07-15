#f= open("Islam.txt","w")
#a=f.write("Sumon is Very Smart\n")
#print(a)
#f.close()


#f= open("Islam.txt","w")
#a=f.write("Sumon is Very Smart\n")
#print(a)
#f.close()

#Handle Read and write both
#f=open("Islam.txt","r+")

#.write("Thank you!")
import datetime
def gettime():
    return datetime.datetime.now()

value = input("type here\n")
with open("harry-ex.txt", "a") as op:
    op.write(str([str(gettime())]) + ": " + value  +"\n")
