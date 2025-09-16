weight=float(input("Enter your weight in kg:"))
height=float(input("Enter the height in meters:"))
bmi=weight/height**2
print("Your BMI :",bmi)
if bmi<18.5:
    print("Underweight")
elif bmi>=18.5 and bmi<=24.9:
    print("Normal Weight")
elif bmi>=25.0 and bmi<=29.9:
    print("Overweight")
elif bmi>=30.0:
    print("Obesity")