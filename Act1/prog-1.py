#find the highest number among three inputs
# Getting input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))


# Check for the highest number by using nested if..elif..else
if num1 >= num2:
    if num1 >= num3:
        highest = num1
    else:
        highest = num3
else:
    if num2 >= num3:
        highest = num2
    else:
        highest = num3


# For displaying the highest number
print(f"The highest number is: {highest}")