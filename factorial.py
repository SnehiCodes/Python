# This is a programme to find factorial of a number.
a = int(input("Give me a positive number."))

def factorial(a) :
    y=1
    while (a>0):
        y = y*a
        a= a-1
    return y    


print(factorial(a))        
