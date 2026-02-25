import random

def get_numbers_ticket(min,max,quantity):
    #figuring out whether the variables entered are correct
    if min < 0 or max < 0 or quantity < 0:
        return []
    if min > max:
        return []
    if (max - min) < quantity:
        return []
    #store randomly generated numbers in order to pick random quantity of winning tickets
    numbers = []

    for i in range(min,max):
        numbers.append(i)

    winning_numbers_list = []

    winning_numbers = random.sample(numbers, k=quantity)
    for i in winning_numbers:
        winning_numbers_list.append(i)

    return winning_numbers_list

lottery_numbers = get_numbers_ticket(1000,1200,3)  #get_numbers_ticket(minimal_number, maximum_number, quantity_of_tickets)
print(f"Your winning lottery numbers are: {sorted(lottery_numbers)}")