import random
from string import ascii_lowercase, ascii_uppercase

as_lower = ascii_lowercase
as_upper = ascii_uppercase
digit = 1234567890
symbol = '#$%&*+-=?@^_!'

char = ''

password_count = int(input('Сколько паролей вам нужно: '))

len_password = int(input('Укажите длину вашего пароля: '))

digit_password = input('Будем ли включать цифры д/н: ')

upper_password = input('Будем ли включать прописные буквы д/н: ')

lower_password = input('Будем ли включать строчные буквы д/н: ')

symbol_password = input('Будем ли включать символы д/н: ')

symbol_random = input('Будем ли исключать неоднозначные символы д/н: ')


if digit_password == 'д':
    char += str(digit)

if upper_password == 'д':
    char += as_upper

if lower_password == 'д':
    char += as_lower

if symbol_password == 'д':
    char += symbol

if symbol_random == 'д':
    for s in 'il1Lo0O':
        char.replace(s, '')


def generate_password(length, chars):
    chars_random = random.sample(chars, length)

    return ''.join(chars_random)


for _ in range(password_count):
    print(generate_password(len_password, char))