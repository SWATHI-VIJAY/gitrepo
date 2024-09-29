def is_prime(num):
    if num==1:
        return False
    for i in range(2,(num//2)+1):
        if num%i==0:
            return False
    return True
number=int(input("enter a number:"))
result=is_prime(number)
print(f"{number}is a prime number:{result}")

    