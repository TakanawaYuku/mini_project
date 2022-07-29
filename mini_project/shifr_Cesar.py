# s = 'To be, or not to be, that is the question!'
# new_s = ''
# eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
# eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#
# for i in range(len(s)):
#     if s[i].isupper():
#         ind = eng_upper_alphabet.find(s[i])
#         while not ind + 17 < len(eng_upper_alphabet):
#             eng_upper_alphabet += eng_upper_alphabet
#         new_s += eng_upper_alphabet[ind + 17]
#     elif s[i].islower():
#         ind = eng_lower_alphabet.find(s[i])
#         while not ind + 17 < len(eng_lower_alphabet):
#             eng_lower_alphabet += eng_lower_alphabet
#         new_s += eng_lower_alphabet[ind + 17]
#     else:
#         new_s += s[i]
# print(new_s)


# for i in input():
#     if i.isalpha():
#         print(chr((ord(i) - 7) % ord('я')), end='')
#     else:
#         print(i, end='')

# s = 'Шсъцхр щмчжмщ йшм, нмтзж йшм лхшщзщг.'
# m = ''
# for i in s:
#     if i.isalpha():
#         m += chr(ord(i) - 7)
#     else:
#         m += i
#     m = m.lower()
# print(m.capitalize())




# n, s = -25, 'Sgd fqzrr hr zkvzxr fqddmdq nm sgd nsgdq rhcd ne sgd edmbd.'
# for i in s:
#     if i.isalpha():
#         c = ('a', 'A')[i.isupper()]
#         print(chr(ord(c) + (ord(i) + n - ord(c)) % 26), end='')
#     else:
#         print(i, end='')


# s = 'Hawnj pk swhg xabkna ukq nqj.'
# new_s = ''
# eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz' * 2
# eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * 2
#
# for j in range(1, 26):
#     for i in range(len(s)):
#         if s[i].isupper():
#             ind = eng_upper_alphabet.rfind(s[i])
#             new_s += eng_upper_alphabet[ind - j]
#         elif s[i].islower():
#             ind = eng_lower_alphabet.rfind(s[i])
#             new_s += eng_lower_alphabet[ind - j]
#         else:
#             new_s += s[i]
#
#     print(new_s)
#     new_s = ''


n = input()
# ищем длину слов переводим в словарь в виде чисел
s = n
for j in n:
    if j in '*,.!@"-':
        s = s.replace(j, '')
g = [len(i) for i in s.split()]

# объявляем переменную счетчик, когда попадается пробел переходим на след ячейку в словаре
count = 0
word_new = ''
for d in n:
    number = ord(d)
    if d == ' ':
        count += 1
        word_new += chr(number)
    elif 65 <= number <= 90:
        number += g[count]
        if number > 90:
            number = number - 26
            word_new += chr(number)
        else:
            word_new += chr(number)
    elif 97 <= number <= 122:
        number += g[count]
        if number > 122:
            number = number - 26
            word_new += chr(number)
        else:
            word_new += chr(number)
    else:
        word_new += chr(number)

print(word_new)