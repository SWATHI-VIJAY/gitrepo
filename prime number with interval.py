lower=int(input("enter a lower number:"))
upper=int(input("enter a upper limit:"))

for i in range(lower,upper+1):
    if i>1:
        for t in range(2,i):
            if i%t==0:
                break
        else:
             print(i)


