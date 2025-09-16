a=int(input("Enter the first side of the triangle:"))
b=int(input("Enter the second side of the triangle:"))
c=int(input("Enter the third side of the triangle:"))
if a+b>c or a+c>b or b+c>a:
    print("The triangle is valid")
    if a==b==c:
        print("The triangle is Equilateral")
    elif a==b and a!=c or b==c and b!=a or a==c and a!=b:
        print("The triangle is Isosceles")
    if a!=b and b!=c and c!=a:
        print("The triangle is Scalene")
else:
    print("The triangle is not valid")