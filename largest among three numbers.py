num1=int(input("enter a number 1:"))
num2=int(input("enter a number 2:"))
num3=int(input("enter a number 3:"))

if(num1>num2) and (num1>num3):
    print(num1, "is a greater number")
elif(num2>num1) and (num2>num3):
    print(num2,"is a greater number")
else:
    print(num3, "is a greater number among all")
