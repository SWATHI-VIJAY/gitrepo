num=int(input("enter a number:"))
factorial=1
if(num<0):
    print("not possible")
elif num==0:
    print("factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial*=i
print(f"factorial of a given number :{num} is {factorial}")