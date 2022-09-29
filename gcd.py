a = int(input("Give a number a ."))
b = int(input("Give a number b ."))

def gcd (a,b):
    i = min(a,b)

    while i > 0:
        if (a%i) == 0 and (b%i) == 0:
            return(i)
        else :
            i=i-1    
    print(i)

print(gcd (a,b))
