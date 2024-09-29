def factor(n):
    print("factor of",n,"are:")
    for i in range(1,n+1):
        if n%i==0:
            print(i)

num=570
result=factor(num)
print(result)
