# find the highest number and display numbers in descending order3

# Getting input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Determine the order using nested if..elif..else
if num1 >= num2 and num1 >= num3:
    if num2 >= num3:
        highest, middle, lowest = num1, num2, num3
    else:
        highest, middle, lowest = num1, num3, num2
elif num2 >= num1 and num2 >= num3:
    if num1 >= num3:
        highest, middle, lowest = num2, num1, num3
    else:
        highest, middle, lowest = num2, num3, num1
else:
    if num1 >= num2:
        highest, middle, lowest = num3, num1, num2
    else:
        highest, middle, lowest = num3, num2, num1

# Display the numbers (descending order)
print(f"Numbers in descending order: {highest}, {middle}, {lowest}")