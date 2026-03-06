from datetime import date

def get_number():
    """
    Gets from user the date.
    Validates the user input.
    Prints result to console.
    """
    print("\n----------Calendar calculator----------")

    while True:
        try:
            user_date = input("Enter date (yyyy.mm.dd): ").split(".")
            year, month, day = int(user_date[0]), int(user_date[1]), int(user_date[2])
        except ValueError:
            print("Invalid date. Enter date in format 'yyyy.mm.dd'.")
            continue

        if month < 1 or month > 12:
            print("Invalid date. Enter date in format 'yyyy.mm.dd'.")
            continue
        elif year < 1 or year > 9999:
            print("Invalid date. Enter date in format 'yyyy.mm.dd'.")
            continue

        break

    print(f"In this day the weekday was: {calendar_calculate(year, month, day)}\n")

def calendar_calculate(year, month, day):
    """
    Calculates the day of week which was on entered date by the user.
    Takes into leap year.

    Parameters:
        year (int): The year entered by the user.
        month (int): The month entered by the user.
        day (int): The day entered by the user.

    Returns:
        days_of_week[i] (str): The day of the week which was on entered date.
    """
    all_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    all_month_leap = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_leap(year):
        if day > all_month_leap[month]:
            print(f"This month doesn't have {day} days. Please, try again.")
            get_number()
    else:
        if day > all_month[month]:
            print(f"This month doesn't have {day} days. Please, try again.")
            get_number()

    current_date = str(date.today()).split("-")
    current_year, current_month, current_day = int(current_date[0]), int(current_date[1]), int(current_date[2])

    days = 0
    if year <= current_year:
        for i in range(year, current_year):
            if is_leap(i):
                days += 366
            else:
                days += 365
    else:
        for i in range(current_year, year):
            if is_leap(i):
                days -= 366
            else:
                days -= 365

    for i in range(0, current_month):
        if is_leap(current_year):
            days += all_month_leap[i]
        else:
            days += all_month[i]

    for i in range(0, month):
        if is_leap(year):
            days -= all_month_leap[i]
        else:
            days -= all_month[i]

    days += current_day
    days -= day

    today_weekday = (date.today().weekday())
    day_of_week = (today_weekday - days) % 7

    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    return days_of_week[day_of_week]

def is_leap(year):
    """
    Calculates if the year is a leap year.

    Parameters:
        year (int): The year.

    Returns:
        bool: True if the year is a leap year, otherwise False.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)