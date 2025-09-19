#find the greatest number among 2 given numbers

a=10
b=20

if a>=b:
    print("A is greater",a)
else:
    print("B is greater",b)


#find the greatest number among 3 given numbers
a=20
b=30
c=40

if (a>=b and a>=c):
    print("A is greater",a)
elif (b>=c):
    print("B is greater",b)
else:
    print("C is greater",c)



#write a program to find a number is even or odd
num=int(input("Enter a number"))
if num%2==0:
    print("You need to join in Team A")
else:
    print("You need to join in Team B")


#write a program to find if an year is Leap.
amount=20000
year=2025

if (year%4==0 and year%100!=0) or (year %400 ==0):
    print("Leap Year You got 20% discount",int(amount*20/100))
else:
    print("Leap Year you got 10% discout,",int(amount*10/100))
    
    
    















