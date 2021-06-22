username=input("Enter Your Username : ")

l=len(username)

if (l>10):
    print("The entered username contains more than 10 characters")
elif (l==10):
    print("The entered username contains 10 characters")
else:
    print("The entered username contains less than 10 characters")