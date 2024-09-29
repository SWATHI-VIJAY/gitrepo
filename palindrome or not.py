def check_palindrome(n):
    return n==n[::-1]

t=(input("enter a word:"))
if check_palindrome(t):
    print("it is a palindrome")
else:
    print("not a palindrome")


