raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone(phone_number:str):
    normalize_number = phone_number.strip().replace("(", "").replace(")","").replace("+","").replace(" ","").replace("-","").replace("380","").removeprefix("0").replace("\\", "").replace('n', '').replace('t', '')
    
    return "+380 " + normalize_number

print(normalize_phone("067\\t123 4567"))
print(normalize_phone("(095) 234-5678\\n"))