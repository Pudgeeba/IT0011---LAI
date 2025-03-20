def divide(a, b):
    if b == 0:
        print("Error: Denominator must not be zero.")
        return None
    return a / b

def exponentiation(a, b):
    return a ** b

def remainder(a, b):
    if b == 0:
        print("Error: Denominator must not be zero.")
        return None
    return a % b

def summation(a, b):
    if b <= a:
        print("Error: The second number must be greater than the first number.")
        return None
    return sum(range(a, b + 1))

def main():
    print("\n---- MENU ----")
    print("[D] - Divide")
    print("[E] - Exponentiation")
    print("[R] - Remainder")
    print("[F] - Summation")

    choice = input("Enter your choice: ").upper()

    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    if choice == 'D':
        result = divide(num1, num2)
    elif choice == 'E':
        result = exponentiation(num1, num2)
    elif choice == 'R':
        result = remainder(num1, num2)
    elif choice == 'F':
        result = summation(num1, num2)
    else:
        print("Invalid choice. Please select from the menu.")
        return

    if result is not None:
        print(f"Result: {result}")

if __name__ == "__main__":
    main()
