# Import (считывает импортируемый файл и добавляет все записи оттуда в БД)
import Export_xlsx

def read_import_file():
    # name = Export_xlsx. #######TODO имя резервной копии, вводимой пользователем
    with open (f'GROUP_TASK/{name}.txt', 'r', encoding = 'utf-8') as file:
        file = list(map(str, file))
        print(file)
    
    with open ('GROUP_TASK/PhoneBook.txt', 'a', encoding = 'utf-8') as send:
        send.writelines(file)


read_import_file()



# формат
# devide = input('Введите разделяющий знак')

# def format_file(text_file, devide):
#     text_file.split(f'{devide}')
#     print(text_file)
    

# format_file()
#__________________________________________________________________________________

import os

os.chdir(os.path.dirname(__file__))

def import_from_file():
    with open("PhoneBook.txt", "r", encoding='utf-8') as phonebook:
        phone = phonebook.readlines()
        for i in range(len(phone)):
            wrds = phone[i].replace(';', '').split(', ')
            for j in range(len(wrds)):
                wrds[j].replace('; ', ' ')
                print(wrds[j])


import_from_file()
