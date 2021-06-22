print("Enter marks of following subjects..")
m1=int(input("Marks of eng out of 100 : "))
m2=int(input("Marks of computers out of 100 : "))
m3=int(input("Marks of math out of 100 : "))

m= m1+m2+m3
p1= (m1/100)*100
p2= (m2/100)*100
p3= (m3/100)*100

p=(m/300)*100
if (p>=40 and p1>33 and p2>33 and p3>33):
    print("pass")
else:
    print("fail")