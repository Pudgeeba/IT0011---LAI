# Program to check if a number is prime

# Getting input from the user
num = int(input("Enter a number: "))

# Prime numbers are greater than 1
if num <= 1:
    print(f"{num} is not a prime number (Prime numbers are greater than 1).")
else:
    is_prime = True  # Flag to check if the number is prime
    
    # Loop from 2 to the square root of num (optimization)
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False  # Found a divisor, so it's not prime
            print(f"{num} is divisible by {i}, so it is not a prime number.")
            break  # Exit loop early

    # Display result
    if is_prime:
        print(f"{num} is a prime number!")