operations = {
    '+': 'сложение',
    '-': 'вычитание',
    '*': 'умножение',
    '/': 'деление'
}

i_want_to_calculate = True

while i_want_to_calculate:
    a = int(input('Введите первое число\n'))
    operator = input('Введите математическую операцию\n')
    b = int(input('Введите второе число\n'))
    if operator == '+':
        print('Результат операции ' + operations[operator] + ': ' + str(a + b))
    if operator == '-':
        print('Результат операции ' + operations[operator] + ': ' + str(a - b))
    if operator == '*':
        print('Результат операции ' + operations[operator] + ': ' + str(a * b))
    if operator == '/':
        if b != 0:
            print('Результат операции ' + operations[operator] + ': ' + str(a / b))
        else:
            print('Делить на ноль нельзя! Попробуй снова')
    user_input = input('Вы хотите продолжить?')
    if user_input == 'нет':
        i_want_to_calculate = False
    

    