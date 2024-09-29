def sum_natural(n):
    return n*(n+1)//2
n=int(input("enter a positive number:"))
result=sum_natural(n)
print(f"the sum of natural number of {n} is",result)