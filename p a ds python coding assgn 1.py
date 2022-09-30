def intreverse(n):
    ans = 0
    while n > 0:
        (d,n) = (n%10,n//10)
        ans = 10*ans + d
    return(ans)


def matched (s):
    nested = 0
    for i in range (0,len(s)):
        if s[i] == "(" :
            nested = nested + 1  
        elif s[i] == ")" :
            nested = nested - 1
            if nested < 0 :
                return(False)
        return (nested == 0)


def factors(n):
    factorlist = []
    for i in range(1,n+1):
        if n%i == 0 :
            factorlist = factorlist + [i]
    return(factorlist)


def isprime(n):
    return(factors(n)==[1,n])

def sumprime(n) :
    sum = 0
    for i in range(0,len(l)) :
        if isprime(l(i)):
            sum = sum + l[i]
    return (sum)