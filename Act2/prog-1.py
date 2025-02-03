# Compute the sum of numbers from first term to last term

# Getting input from the user
first_term = int(input("Enter first term number: "))
last_term = int(input("Enter last term number: "))

# Variable to store the sum
total = 0

# Use loop to calculate the sum
for num in range(first_term, last_term + 1):
    total += num

# Display the result
print(f"The sum of the numbers from {first_term} to {last_term} is {total}")