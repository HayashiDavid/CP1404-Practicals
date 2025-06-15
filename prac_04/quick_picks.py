import random

MINIMUM_VALUE = 1
MAXIMUM_VALUE = 45
QUICK_PICK_THRESHOLD = 6

number_pick = int(input("How many quick pick?>>> "))
for i in range(number_pick):
    number_list = []
    for j in range(QUICK_PICK_THRESHOLD):
        number = random.randint(MINIMUM_VALUE, MAXIMUM_VALUE)
        while number in number_list:
            number = random.randint(MINIMUM_VALUE, MAXIMUM_VALUE)
        number_list.append(number)
    number_list.sort()
    print(" ".join(f"{number:>{len(str(MAXIMUM_VALUE))}}" for number in number_list))

