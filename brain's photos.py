s =input()
n=int(s[0])
k=0
for i in range(n):
    l=input()
    print(l)
    print(l.find('C'))
    if l.find("C") !=-1 | l.find("M") !=-1 | l.find("Y") !=-1 :
        k = k+1
        print(k)
    break

print(k)
if k>0:
    print("#Color")
else:
    print("#Black&White")