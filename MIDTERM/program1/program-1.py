file_path = r"C:\Users\klain\IT0011---LAI\MIDTERM\program1\numbers.txt" 

def process_numbers_file():
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            for idx, line in enumerate(lines, start=1):
                numbers = list(map(int, line.strip().split(",")))
                total = sum(numbers)
                result = "Palindrome" if str(total) == str(total)[::-1] else "Not a palindrome"
                print(f"Line {idx}: {', '.join(map(str, numbers))} (sum {total}) - {result}")
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")

process_numbers_file()
