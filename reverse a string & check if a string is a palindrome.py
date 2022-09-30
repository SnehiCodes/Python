#program to reverse a string
n=(input("Give me a word."))
lenStr=len(n)
#print(lenStr)
j= lenStr
while j>=1:
    print(n[j-1],end="")
    j=j-1


#program to check whether a given string is a palindrome.  
n=(input("Give me a word."))  
lenStr=len(n)
j= lenStr
i=0
while i<=(j/2) :
    if n[i]!=n[lenStr- 1]:
        print(n+ " is not a palindrome")
        break    
        i=i+1
    else:  
        print(n+ " is a palindrome")
        break
#print(n[i])
#print(type(lenStr))
#print(n[lenStr- 1])