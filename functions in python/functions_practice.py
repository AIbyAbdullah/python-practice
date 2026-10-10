# write a program using function to find the greatest of three numbers
a=int(input("Enter first number a: "))
b=int(input("Enter second number b: "))
c=int(input("Enter third number c: "))

def greatest(a,b,c):
    if a>b and a>c:
        return f"{a} a is greatest"
    elif b>a and b>c:
        return f"{b} b is greatest"
    else:
        return f"{c} c is greatest"

greatest1=greatest(a,b,c)
print("The greatest of three numbers is: ",greatest1)


# write a program using function to convert fahrenheit to celsius

def F_to_C(F):
    return 5*(F-32)/9

F=int(input("Enter temperature in Fahrenheit: "))
C=F_to_C(F)
print(f"{round(C,2)} Celsius")

# write a program using function to convert celsius to fahrenheit

def C_to_F(C):
    return (C*9/5)+32
c=float(input("Enter temperature in Celsius: "))
f=C_to_F(c)
print(f"{round(f,2)} Fahrenheit")

# write a python program which converts inches to cm.

def inches_to_cm(inches):
    return inches * 2.54
inches=float(input("Enter length in inches: "))
print(f"the coresponding length in cm is: {round(inches_to_cm(inches),2)} cm")