from datetime import datetime


def get_days_from_today(date: str) -> int:
    
    given_date = datetime.strptime(date, "%Y-%m-%d").date()
    today = datetime.now().date()
    delta = today - given_date
    return delta.days

days_difference = get_days_from_today("2026-10-09")
print(days_difference," days")