#palindrome number
s= input ("enter the value :")
reverse=s[::-1]
if (s==reverse):
    print("it is a palindrome")
else:
    print("it is not a palindrome")