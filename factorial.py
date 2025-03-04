# Python Program to calculate factorial of a given number using while loop
factorial = 1
num = int(input("Enter an positive integer : "))
if num<0:
    print("Kindly try again with a positive interger value")


elif num==0:
    print(f"THe factorial of {num} is : {factorial}")

else:
    i=1
    while i <= num:
        factorial = factorial * i
        i = i+1  

    print(f"THe factorial of {num} is : {factorial}")

