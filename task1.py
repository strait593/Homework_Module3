from datetime import datetime


def validate_format(required_date):
    try:
        parsed_date = datetime.strptime(required_date, "%Y.%m.%d")
        return parsed_date.strftime("%Y-%m-%d")
    except ValueError as e:
        raise ValueError("Incorrect date format, expected YYYY.MM.DD")


def get_days_from_today(user_date):
    current_date = datetime.now().date()

    normalized = validate_format(user_date)
    date_obj = datetime.strptime(normalized, "%Y-%m-%d").date()

    if date_obj > current_date:
        return "I can't see the future boss"

    days_left = current_date - date_obj

    return f"The {user_date} was {days_left.days} days ago"

print(get_days_from_today("2023.01.01"))