import random

def get_numbers_ticket(min,max,quantity):

    if min < 0 or max < 0 or quantity < 0:
        return []
    if min > max:
        return []
    if (max - min) < quantity:
        return []

    numbers = []

    for i in range(min,max):
        numbers.append(i)

    winning_numbers_list = []

    winning_numbers = random.sample(numbers, k=quantity)
    winning_numbers_list.append(winning_numbers)

    return f"The winning numbers are: {sorted(winning_numbers)}"

print(get_numbers_ticket(10,4, 5))