 
def greatest(a, b, c): 
    if a > b and a > c:
        return a 
    elif b > c: 
        return b  
    else:
        return c
 
num1 = float(input("Enter first number: ")) 
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: ")) 
print(f"The greatest number is: {greatest(num1, num2, num3)}")