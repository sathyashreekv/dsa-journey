name=input("Enter your name :")
age=int(input("Enter your age:"))
ticket_price=0
if age<5:
    ticket_price=0
    print("Name :",name)
    print("Your ticket is free")
elif age >5 and age<=12:
    ticket_price=10
    print("Name :",name)
    print("Your ticket price is $",ticket_price)
elif age>=13 and age<=60:
    ticket_price=20
    print("Name :",name)
    print("Your ticket price is $",ticket_price)
elif age>60:
    ticket_price=15
    print("Name :",name)
    print("your ticket price is $",ticket_price)
    