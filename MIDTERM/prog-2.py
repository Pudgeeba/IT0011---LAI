# Task 2: Convert Date Format
from datetime import datetime

def convert_date():
    user_input = input("Enter the date (mm/dd/yyyy): ")
    try:
        date_obj = datetime.strptime(user_input, "%m/%d/%Y")
        formatted_date = date_obj.strftime("%B %d, %Y")
        print(f"Date Output: {formatted_date}")
    except ValueError:
        print("Invalid date format. Please use mm/dd/yyyy.")

convert_date()