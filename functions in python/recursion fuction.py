 # recursion funtion is a function that calls itself in order to solve a problem. It is used to
 # break down a problem into smaller sub-problems. Recursion is a powerful tool in programming,
 # but it can also be tricky to understand and implement correctly.
 
    #example of recursion function to calculate factorial of a number
'''
n(1)=1
n(2)=1 * 2
n(3)=1 * 2 * 3
n(4)=1 * 2 * 3 * 4
n(5)=1 * 2 * 3 * 4 * 5
n(n)=1 * 2 * 3 * 4 * 5 * ...* (n-1) * n

sum(n)= n * sum(n-1)
'''
n=int(input("Enter a number: "))
def factorial(n):
    if n==0 or n==1:
       return 1
    return n * factorial(n-1)

print(f"The factorial of {n} is {factorial(n)}")

# write a program using recursion function to find the sum of first n natural numbers

'''
sum(1)=1
sum(2)=1 + 2
sum(3)=1 + 2 + 3
sum(4)=1 + 2 + 3 + 4
sum(5)=1 + 2 + 3 + 4 + 5
sum(n)=1 + 2 + 3 + 4 + 5 + ...+ (n-1) + n

sum(n)=n + sum(n-1)
'''
def sum(n):
    if n==1:
        return 1
    return n + sum(n-1)

n=int(input("Enter a number: "))
print(f"The sum of first {n} natural numbers is {sum(n)}")

# write a program using recursion function to print first n lines of the following patterns

'''
***
**    for n=3
*

'''

def pattern(n):
    if n==0:
        return
    print("*" * n)
    pattern(n-1)

pattern(int(input("Enter a number: ")))
