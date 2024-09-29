n=int(input("enter a number:"))
if n<=0:
    print("enter a positive number")
else:
    total=0
    while(n>0):
        total+=n
        n-=1
    print(f"the sum of natural number {n} is",total)