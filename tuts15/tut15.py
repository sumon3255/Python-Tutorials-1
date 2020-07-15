#Exercise2 Faulty calculator


print("Enter Your first Num")
a = input()
print("Enter an Operator")
operator = input()
print("enter yor 2nd Number")
b=input()

if  operator=="+":
    if a == 56 and b == 9:
        print("sum is 77")
else:


    sum = float(a)+float(b)
    print("sum is",sum)

elif operator == "-":
        sub = float(a) - float(b)
        print("sub is", sub)

elif operator == "*":
        mul = float(a) * float(b)
        print("mult is", mul)


elif operator == "/":
        div = float(a) / float(b)
        print("division is", div)
 else:
        mod = float(a) % float(b)
        print("MODLUS is", mod)











