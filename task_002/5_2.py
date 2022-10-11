# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные хранятся в отдельных текстовых файлах.

# in
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'

# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ

# out in file
# 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ

# 'text_code_words.txt'
# 5a29v4s3D3d2F4g2O3i2a1
# 1v2b2w2P3u2T1Y1y2W2Q

import itertools
import os

def encode(data_list: list):
    for line in data_list:
        res = [f'{len(list(num))}{char}' for char, num in itertools.groupby(line)]
        res = ''.join(res)
        
        path_code = 'task_002/text_code_words.txt'
        with open(path_code, 'a', encoding='utf-8') as data:
            data.write(''.join(res))
            data.write('\n')

def decode(data_list: list):
    num =''
    for line in data_list:
        temp = []
        line = line.strip()
        for i in line:
            if i.isdigit():
                num += i
            else:
                temp.append([int(num), i])
                num = ''
            line = itertools.starmap(lambda x, y: x * y, temp)
            line = ''.join(line)
        print('decode')
        print(line)
        

def get_data(path):
    if os.path.exists(path):  
        with open(path, 'r', encoding='utf-8') as data:
            data_list = data.read()
            data_list = data_list.strip().split(sep='\n')
        return data_list
    else: print("Файл не существует")
    

data_list = get_data('task_002/text_words.txt')
encode(data_list)
data_list_code = get_data('task_002/text_code_words.txt')
decode(data_list_code)

 
