from datetime import datetime, date

def calculate_age():
    """Calculate age based on birth date"""
    
    print("=== Age Calculator ===")
    print("Enter your birth date:")
    
    try:
        # Get birth date input
        birth_year = int(input("Enter birth year (YYYY): "))
        birth_month = int(input("Enter birth month (1-12): "))
        birth_day = int(input("Enter birth day (1-31): "))
        
        # Create birth date object
        birth_date = date(birth_year, birth_month, birth_day)
        
        # Get current date
        today = date.today()
        
        # Check if birth date is in the future
        if birth_date > today:
            print("Error: Birth date cannot be in the future!")
            return
        
        # Calculate age
        age_years = today.year - birth_date.year
        age_months = today.month - birth_date.month
        age_days = today.day - birth_date.day
        
        # Adjust for cases where birthday hasn't occurred this year
        if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
            age_years -= 1
            age_months += 12
        
        # Adjust for negative days
        if age_days < 0:
            age_months -= 1
            # Get days in previous month
            if today.month == 1:
                prev_month = 12
                prev_year = today.year - 1
            else:
                prev_month = today.month - 1
                prev_year = today.year
            
            days_in_prev_month = (date(prev_year, prev_month + 1, 1) - date(prev_year, prev_month, 1)).days
            age_days += days_in_prev_month
        
        # Adjust for negative months
        if age_months < 0:
            age_months += 12
        
        # Calculate total days lived
        total_days = (today - birth_date).days
        
        # Calculate other time units
        total_weeks = total_days // 7
        total_hours = total_days * 24
        total_minutes = total_hours * 60
        total_seconds = total_minutes * 60
        
        # Display results
        print("\n" + "="*50)
        print("YOUR AGE CALCULATION RESULTS")
        print("="*50)
        
        print(f"Birth Date: {birth_date.strftime('%B %d, %Y')}")
        print(f"Today's Date: {today.strftime('%B %d, %Y')}")
        print()
        
        print("EXACT AGE:")
        print(f"  {age_years} years, {age_months} months, and {age_days} days")
        print()
        
        print("AGE IN DIFFERENT UNITS:")
        print(f"  Years: {age_years}")
        print(f"  Total Months: {age_years * 12 + age_months}")
        print(f"  Total Weeks: {total_weeks}")
        print(f"  Total Days: {total_days}")
        print(f"  Total Hours: {total_hours:,}")
        print(f"  Total Minutes: {total_minutes:,}")
        print(f"  Total Seconds: {total_seconds:,}")
        print()
        
        # Next birthday calculation
        next_birthday = date(today.year, birth_date.month, birth_date.day)
        if next_birthday <= today:
            next_birthday = date(today.year + 1, birth_date.month, birth_date.day)
        
        days_to_birthday = (next_birthday - today).days
        print(f"NEXT BIRTHDAY: {next_birthday.strftime('%B %d, %Y')}")
        print(f"Days until next birthday: {days_to_birthday}")
        
        # Fun facts
        print("\n" + "="*30)
        print("FUN FACTS:")
        print("="*30)
        
        if age_years >= 18:
            print("✓ You are an adult!")
        else:
            years_to_adult = 18 - age_years
            print(f"• You will be an adult in {years_to_adult} years")
        
        if age_years >= 65:
            print("✓ You are a senior citizen!")
        
        # Zodiac sign (simplified)
        zodiac_signs = {
            (3, 21, 4, 19): "Aries", (4, 20, 5, 20): "Taurus",
            (5, 21, 6, 20): "Gemini", (6, 21, 7, 22): "Cancer",
            (7, 23, 8, 22): "Leo", (8, 23, 9, 22): "Virgo",
            (9, 23, 10, 22): "Libra", (10, 23, 11, 21): "Scorpio",
            (11, 22, 12, 21): "Sagittarius", (12, 22, 12, 31): "Capricorn",
            (1, 1, 1, 19): "Capricorn", (1, 20, 2, 18): "Aquarius",
            (2, 19, 3, 20): "Pisces"
        }
        
        user_zodiac = "Unknown"
        for (start_month, start_day, end_month, end_day), sign in zodiac_signs.items():
            if ((birth_month == start_month and birth_day >= start_day) or 
                (birth_month == end_month and birth_day <= end_day)):
                user_zodiac = sign
                break
        
        print(f"• Your zodiac sign: {user_zodiac}")
        
        # Day of week born
        day_of_week = birth_date.strftime('%A')
        print(f"• You were born on a {day_of_week}")
        
    except ValueError:
        print("Error: Please enter valid numbers for the date.")
    except Exception as e:
        print(f"Error: {e}")

def calculate_age_difference():
    """Calculate age difference between two people"""
    
    print("\n=== Age Difference Calculator ===")
    
    try:
        print("Enter first person's birth date:")
        year1 = int(input("Year: "))
        month1 = int(input("Month: "))
        day1 = int(input("Day: "))
        
        print("Enter second person's birth date:")
        year2 = int(input("Year: "))
        month2 = int(input("Month: "))
        day2 = int(input("Day: "))
        
        date1 = date(year1, month1, day1)
        date2 = date(year2, month2, day2)
        
        # Calculate difference
        if date1 > date2:
            older_date = date2
            younger_date = date1
            older_person = "Second person"
            younger_person = "First person"
        else:
            older_date = date1
            younger_date = date2
            older_person = "First person"
            younger_person = "Second person"
        
        difference = younger_date - older_date
        years_diff = difference.days / 365.25
        
        print(f"\nAge Difference: {difference.days} days")
        print(f"That's approximately {years_diff:.1f} years")
        print(f"{older_person} is older than {younger_person}")
        
    except ValueError:
        print("Error: Please enter valid numbers for the dates.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    """Main program menu"""
    
    while True:
        print("\n" + "="*40)
        print("AGE CALCULATOR MENU")
        print("="*40)
        print("1. Calculate your age")
        print("2. Calculate age difference between two people")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == '1':
            calculate_age()
        elif choice == '2':
            calculate_age_difference()
        elif choice == '3':
            print("Thank you for using the Age Calculator!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Run the program
if __name__ == "__main__":
    main()