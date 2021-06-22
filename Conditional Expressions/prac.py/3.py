

n=input("enter spam text to be checked : ")

if ("make a lot of money" in n):
    spam=True
elif( "buy now" in n ):
    spam=True
elif("subscribe this" in n):
    spam=True
elif("click this" in n):
    spam=True
else:
    spam=False

if(spam):
    print("This is a spam text")
else:
    print("This is not a spam text")



