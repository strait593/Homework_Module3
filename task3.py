import re

phone_numbers = ["    +38(050)123-32-34", "     0503451234","(050)8889900","38050-111-22-22","38050 111 22 11   "]

def normalize_phone(phone_number:str):
    normalize_number = phone_number.strip().replace("(", "").replace(")","").replace("+","").replace(" ","").replace("-","").replace("380","").removeprefix("0")
    
    return "+380" + normalize_number

print(normalize_phone("    +38(050)123-32-34"))