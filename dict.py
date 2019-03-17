favourite_langs = {
    'Толя': 'C#',
    'Дима': 'Ruby',
    'Кирилл': 'Kotlin',
    'Ваня': 'JavaScript',
    'Аркадий': 'Scala'   
}

friends = ['Толя', 'Дима']

for name in sorted(favourite_langs):
    hello = 'Привет, ' + name + '!'
    if name in friends:
        hello_mate = hello + ' Я смотрю, ты любишь ' + favourite_langs[name]
        print(hello_mate)
    else:
        print(hello)

fruits = {}

for number in range(4):
    key = input('Введи имя фрукта: ')
    value = input('\nВведи цвет фрукта: ')
    fruits[key] = value
print(fruits)
