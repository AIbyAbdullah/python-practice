 # recursion funtion is a function that calls itself in order to solve a problem. It is used to
 # break down a problem into smaller sub-problems. Recursion is a powerful tool in programming,
 # but it can also be tricky to understand and implement correctly.
 
    #example of recursion function to calculate factorial of a number
n=int(input("Enter a number: "))
def factorial(n):
    if n==0 or n==1:
        return 1
    return n * factorial(n-1)

print(f"The factorial of {n} is {factorial(n)}")
    