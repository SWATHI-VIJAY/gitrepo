def fibbonacci(n):
    if n<=1:
        return n
    else:
        return fibbonacci(n-1)+fibbonacci(n-2)
t=int(input("enter a number:"))
if t<=0:
    print("enter a positive number")
else:
    for i in range(t):
        result=fibbonacci(i)
    
        print(f"the fibbonacci sequence is:",result)