def number_pattern():
    rows = 5
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "".join(str(num) for num in range(1, i + 1)))

# Example usage
number_pattern()



def odd_number_pattern():
    num = 1
    row = 1

    while row <= 5:
        print(str(num) * num)
        num += 2
        row += 1

# Example usage
odd_number_pattern()
