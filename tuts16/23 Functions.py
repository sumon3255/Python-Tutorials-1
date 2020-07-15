#a=5
#b=7
#c=sum((a,b))#build in fuction
#print(c)

#Userdefine Function

#def function1(a,b):
     #print("Hellow You Are In Function",a+b)

#function1(5,7)
def function2(a,b):
    """This Is Function Whice Is Calculate Average Of Two Numbers
    This is not for Three numbers"""
    Average=(a+b)/2
    #print(Average)
    return Average
v=function2(5,7)
print(function2.__doc__)

