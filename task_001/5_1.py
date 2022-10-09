# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10

# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

# in
# Number of words: 6

# out
# ваб вба абв ваб бва абв
# ваб вба ваб бва

# in
# Number of words: -1

# out
# The data is incorrect
 
import random

def create_str(size, str):
    size = size if size > 0 else -size
    if not len(str) == 3: return -1

    str_list = []

    for i in range(size):
        str_list.append(''. join(random.sample(str, k = 3)))
        str1 = ' '.join(str_list)

    return str1

def filter_str(str, substr):
    string = str.replace(substr, '')
    string = ' '.join(string.split())
    if not len(str) == len(string): return string
    return -1

num = int(input("Размер: "))
str = input("Строка из 3-х символов: ")
substring = input("Подстрока (3 символа): ")

string = create_str(num, str)
if string == -1:
    print('The data is incorrect')
else:
    print(string)
    print(filter_str(string, substring))