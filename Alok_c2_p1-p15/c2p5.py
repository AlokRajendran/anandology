# Problem 5: Write a function factorial to compute factorial of a number. Can you use the product 
# function defined in the previous example to compute factorial?

# import math

# print(math.factorial(4))


def factorial(a):
    for i in range(a):
        i=1
        a= a*i
        return a
factorial(4)



def fact(x):
    x+=1
    f =1
    for i in range (x):
        if i == 0:
            continue
        else:
            f = f * i
    
         
    print(f)

fact(4)