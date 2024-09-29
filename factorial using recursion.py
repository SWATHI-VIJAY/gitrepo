def factorial(num):
    if num==1:
        return 1
    else:
        return num*factorial(num-1)
    
x=int(input("enter a number:"))
result=factorial(x)
print(f"the factorial of {x} is: {result}")