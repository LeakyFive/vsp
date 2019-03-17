trigger = True
while trigger:
    number_a = int(input('Введите число а:\n'))
    operator = input('Введите математический оператор:\n')
    number_b = int(input('Введите число b:\n'))
    if operator == '+':
        print(number_a + number_b)
    elif operator == '-':
        print(number_a - number_b)
    elif operator == '/':
        print(number_a / number_b)
    elif operator == '*':
        print(number_a * number_b)
    else:
        print('Указан неверный оператор!')
    print('Вы хотите выйти из программы?')
    answer = input()
    if answer == 'да':
        trigger = False
