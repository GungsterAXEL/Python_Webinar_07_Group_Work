# Меню

def menu_choice():
    # print(' 0. Вернуться к меню')
    print(' 1. Добавление записи')
    print(' 2. Вывод записи на экран')
    print(' 3. Импорт')
    print(' 4. Экспорт')
    print(' 5. Поиск контакта')
    print(' 6. Удаление контакта')
    access = int(input('Выберите пункт: '))
    return access


choice = menu_choice()
#print(choice)
