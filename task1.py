from datetime import datetime

def get_days_from_today(date_string: str) -> int:
    today = datetime.today()
    parsed = None

    #Checking for a correct format
    for fmt in ("%Y-%m-%d", "%d.%m.%Y"):
        try:
            parsed = datetime.strptime(date_string, fmt)
            break
        except ValueError:
            continue
            
    if parsed is None:
        raise ValueError(f"date '{date_string}' is not in a supported format")

    difference = today - parsed

    return difference.days

days_difference = get_days_from_today("13.01.2027")
print(f"{days_difference} days")