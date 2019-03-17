age = int(input('Введи свой возраст...\n'))

if age < 4:
    price = 0
elif age <= 18:
    price = 50
else:
    price = 100

print('Твой возраст - ' + str(age) + '. ' + 'Ты заплатишь за участие ' + str(price) + ' рублей.')
