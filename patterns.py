  # patterns 1
'''
                  *  
                 *** 
                *****
'''

n=int(input("Enter a number: "))
for i in range(1,n+1):
    print(" " * (n-i), end="")
    print("*" * (2*i-1),end="")
    print(" ")

    # pattern 2
'''
            * 
            ** 
            *** 
            **** 
'''
n=int(input("Enter a number: "))
for i in range(1,n+1):
    print("*" * i, end="")
    print(" ")


    # patter no 3
    '''
    *****
    *   *
    *   *
    *   *
    *****
    '''

n=int(input("Enter a number: "))

for i in range(1,n+1):
        if i==1 or i==n:
            print("*" * n)
        else:
           # print("*" + " " * (n-2) + "*")
                # OR
            print("*" , end="")
            print(" " * (n-2), end="")
            print("*")
            
            
            
            
