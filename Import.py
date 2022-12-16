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
