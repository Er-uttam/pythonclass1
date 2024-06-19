while True:
    num1=int(input("Enter the 1st number:"))
    num2=int(input("Enter the 2nd nummber:"))

    operation=input("Enter the Operation You want:")

    if(operation=="add"):
        print("The sum of",num1,"and",num2,"is:",num1+num2)
    elif(operation=="subtract"):
        print("The difference  of",num1,"and",num2,"is:",num1-num2)
    elif(operation=="product"):
        print("The product of",num1,"and",num2,"is:",num1*num2)
    elif(operation=="division"):
        print("The division of",num1,"and",num2,"is:",num1/num2)
        
    user_option=input("Enter y for quit and n for continue.")
    if(user_option=="y"):
        break
        
        