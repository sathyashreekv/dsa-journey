marks=int(input("Enter the marks obtained in the exam:"))
if marks>=90 and marks<=100:
    print("Grade A")
elif marks>=80 and marks<90:
    print("Grade B")
elif marks<80 and marks>=70:
    print("Grade C")
elif marks<70 and marks>=60:
    print("Grade D")
elif marks<60:
    print("Grade F")