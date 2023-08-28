a = int(input("Enter the a value = "))
b = int(input("Enter the b value = "))
c = int(input("Enter the c value = "))
if a>b:
    if a>c:
        print("Greatest value is: ",a)
    elif a<c:
        print("Greatest value is: ",c)
    else:
        print("a and c are equal")
elif a<b:
    if b<c:
        print("Greatest value is c ",c)
    elif b>c:
        print("Greatest value is b ",b)
    else:
        print("b and c are equal")
else:
    if a==c:
        print("a,b,c are equal")
    elif a<c:
        print("a,b are equal and c is greater")
    else:
        print("a,b are equal and greater")
    
        
    
       
    

