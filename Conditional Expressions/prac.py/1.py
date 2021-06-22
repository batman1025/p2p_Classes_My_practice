n=int(input("enter number 1: "))
m=int(input("enter number 2: "))
o=int(input("enter number 3: "))
p=int(input("enter number 4: "))


if (n>m and n>o and n>p):
    print("first number is the greatest")
elif(m>o and m>p):
    print("second number is the greatest")
elif(o>p):
    print("third number is the greatest")
else:
    print("forth number is the greatest")