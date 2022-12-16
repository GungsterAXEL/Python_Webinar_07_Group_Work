import os
import Logger

os.chdir(os.path.dirname(__file__))


def remover():
    try:
        word = input("Введи искомое значение -> ")
        with open('PhoneBook.txt', 'r', encoding='utf-8') as file:
            content = list(map(str, file.read().split('\n')))
        print(content)
        content = [i for i in content if word not in i]
        print(content)
        with open('PhoneBook.txt', 'w', encoding='utf-8') as file:
            file.write(content)

        Logger.log_logger('Remover', True)
    except:
        Logger.log_logger('Remover', False)


remover()


quit()
def remover():
    try:
        word = input("Введи искомое значение -> ")
        with open('PhoneBook.txt', 'r', encoding='utf-8') as file:
            content = list(map(str, file.read().split('\n')))
        print(content)
        temp = []
        # for i, v in enumerate(content):
        #     if word.lower() in v.lower():
        #         temp.append(v)
        # if len(temp) == 0:
        #     print("Нечего удалять!")
        # else:
        #     for i in temp:
        #         print(i)
        temp.append(v for v in content if word not in v)
        temp = list(map(str, temp))
        print(temp)
        with open('PhoneBook.txt', 'w', encoding='utf-8') as file:
            file.write(temp)

        Logger.log_logger('Remover', True)
    except:
        Logger.log_logger('Remover', False)
