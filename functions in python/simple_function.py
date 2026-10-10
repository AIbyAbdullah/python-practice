# find the average of three numbers using function
def avg():  # function definition
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    c=int(input("Enter third number: "))
    average=(a+b+c)/3
    print("The average of three numbers is: ", average)
    print("thank you for using the program")

avg()  # function call


# functions with parameters and arguments
print("Functions with parameters and arguments")

def goodDay(name,ending):
    print("Good day ," ,name)
    print(ending)

goodDay("jonn","Thanks you")
goodDay("umer","Thanks you")
goodDay("Ali","Thanks you")


# function with return value

def goodDay(name,ending):
    print("Good day ," ,name)
    print(ending)
    return "OK"

goodDay1=goodDay("jonn","Thanks you")
print(goodDay1)

