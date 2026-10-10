    # This program prints the multiplication table of a given number in order.
n=int(input("Enter a number: "))
for i in range(1,11):
    print(f"{n} x {i} = {n*i}")
    
    
    
     # This program prints the multiplication table of a given number in reverse order.
n=int(input("Enter a number: "))
for i in range(1,11):
    print(f"{n} x {11-i} = {n*(11-i)}")