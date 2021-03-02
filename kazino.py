import random

guess_number = int(input("Выберите любое число..."))
limit = int(input("Выберите преде рандома: "))
random_number = random.randint(0, limit)
if random_number == guess_number:
    print("Вы выйграли! Поздравляю! ")
else:
    print("Было загадно число", random_number)


