print("Enter marks of following subjects..")
m1=int(input("Marks of eng out of 100 : "))
m2=int(input("Marks of computers out of 100 : "))
m3=int(input("Marks of math out of 100 : "))

m=m1+m2+m3
p=m/3
if(m1<33 or m2<33 or m3<33):
    print("you are failed due to less marks in one of the subjects")
elif(p<40):
    print("you are fail due to less total percentage")
else:
    print("you are passed")