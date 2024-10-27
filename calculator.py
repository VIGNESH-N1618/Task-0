def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def moddivision(a,b):
    return a%b
def division(a,b):
    return a/b
while(True):
    print("menu:\n1.Addition\n2.Subtraction\n3.Multiplication\n4.ModDivision\n5.Division\n")
    choice=int(input("enter your choice(1-5):\n"))
    a=int(input("enter value of a:\n"))
    b=int(input("enter value of b:\n"))     
    if(choice==1):
        print("addition of a and b:",addition(a,b))
    elif(choice==2):
        print("subtraction of a and b:",subtraction(a,b))
    elif(choice==3):
        print("multiplication of a and b:",multiplication(a,b))
    elif(choice==4):
        print("moddivision of a and b:",moddivision(a,b))
    elif(choice==5):
        print("division of a and b:",division(a,b))
    else:
        print("invalid choice")
        break
    
          
