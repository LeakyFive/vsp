guess_word = 'апельсин'
guess_count = 3
guess = ''

while guess_count != 0:
    guess = input('Попробуй угадать слово!\n')
    if guess != guess_word:
        guess_count -= 1
        print('Вы не угадали, у вас осталось попыток: ' + str(guess_count))
    elif guess_word == guess:
        print('Вы выиграли!')
        break
if guess_count == 0:
    print('Вы проиграли!')

