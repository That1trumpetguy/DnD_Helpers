from datetime import datetime

# Define the custom calendar structure
custom_calendar = {
    "months": ["Ada", "Turing", "Namor", "Neumann", "Maeve", "Syfarth", "Fulquist", "Olba"],
    "days_per_month": 32,
    "days_per_year": 256,
    "weekdays": ["Al", "Hissier", "Bet", "Ulma"],
}

# Function to convert a real-world date to the custom calendar
def convert_to_custom_calendar(real_date):
    # Get day of the year (1-based index)
    day_of_year = real_date.timetuple().tm_yday  # 1 = Jan 1st
    
    # Convert real-world day to custom calendar cycle (modulo 256)
    custom_day = (day_of_year - 1) % custom_calendar["days_per_year"]
    
    # Find the month and day in the custom calendar
    month_index = custom_day // custom_calendar["days_per_month"]
    day_in_month = (custom_day % custom_calendar["days_per_month"]) + 1

    # Get month name
    month_name = custom_calendar["months"][month_index]

    return f"{month_name} {day_in_month}, 971"  # Assuming year 971

# Example usage
real_date_1 = datetime(1836, 3, 6)  # March 10, 2025
#real_date_2 = datetime(2025, 3, 11)  # March 11, 2025

print(convert_to_custom_calendar(real_date_1))  # Output: Namor 5, 971
#print(convert_to_custom_calendar(real_date_2))  # Output: Namor 6, 971
