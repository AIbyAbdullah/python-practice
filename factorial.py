# using while loop to find factorial of a number
n=int(input("Enter a number: "))
i=1
sum=1
while i<=n:
    sum*=i
    i+=1
print("The factorial of", n, "is", sum)

# using for loop to find factorial of a number
n=int(input("Enter a number: "))
product=1
for i in range (1, n+1):
    product=product*i
print(f"The factorial of {n} is {product}")