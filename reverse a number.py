#To reverse any giver number or string.
n=int(input("Type a number and get its reverse.\n"))
r=10

while n>0:
    t=n%(r)
    t=int(t)
    print(t,end="")
    n=(n-t)/10
    
