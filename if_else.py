#Python program to demonstrate the use of if statement by pring the grades of students from their marks

marks = float(input("Enter the marks :"))
if marks>90:
    print("Excellent! you have got A+ grades")

elif marks>80:
    print("Congratulations you have got A grades")

elif marks>70:
    print("Great! you have got B+ grades")

elif marks>60:
    print("Nice you have got B grades")

elif marks>50:
    print(" You have got C grades")

elif marks>40:
    print("You have got D grades")

else:
    print("Sorry! you have Faile. Better luck next time!")

