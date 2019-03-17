import random

current_slot = random.randint(1, 6)
slot_with_bullet = random.randint(1 ,6)

print('Пуля в слоте номер ' + str(slot_with_bullet))
while current_slot is not slot_with_bullet:
    input()
    print('Крутите барабан')
    current_slot = random.randint(1, 6)
    print('Сектор ' + str(current_slot) + ' на барабане')

print('Гейм овер(')

# a = input('Введите номер карты: \n')
# stars = '****'
# new_a = a.replace(a[-4:], stars)
# print(new_a)

# a = input('Введите номер карты: \n')

# new_a = '*' * (len(a) - 4)
# print(new_a + a[-4:])