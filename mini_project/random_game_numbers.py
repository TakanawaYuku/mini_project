import random

print('Добро пожаловать в числовую угадайку. Прежде чем мы начнем давайте определимcя с диапозоном:')

num_1, num_2 = int(input('Введите с какого числа будем начинать: ')), int(input('Введите каким числом будем заканчивать: '))

num_random = random.randint(num_1, num_2)


def is_valid(num):

    if num.isdigit() and num_1 <= int(num) <= num_2:
        return True
    else:
        return False


def game_randon():
    count = 0
    while True:
        count += 1
        n = input(f'Введите Ваше число от {num_1} до {num_2}: ')
        if not is_valid(n):
            print(f'А может быть все-таки введем целое число от {num_1} до {num_2}?')

        if is_valid(n):
            n = int(n)
            if n < num_random:

                print('Ваше число меньше загаданного, попробуйте еще разок')

            if n > num_random:

                print('Ваше число больше загаданного, попробуйте еще разок')

            if n == num_random:
                print('Вы угадали, поздравляем!')
                print(f'Количество затраченных попыток {count}')
                break

    continue_game = input('Хотите сыграть еще раз Y/N:').upper()
    if continue_game == 'Y':
        print('Продолжим...')
        game_randon()
    else:
        if continue_game == 'N':
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')


game_randon()