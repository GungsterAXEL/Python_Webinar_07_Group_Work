import Menu
import Add
import Import_txt
import Export_xlsx
import View
import Finder
import Import_xlsx
import Export_docx
import Remover


# Проверка ввода.
def int_input_checker(message):
    user_input = input(message)
    try:
        user_input = int(user_input)
    except:
        print('Ошибка ввода!')
        user_input = int_input_checker(message)
    finally:
        return user_input


def choose(number):
    if number == 1:
        Add.new_entry_saver(input('Введите Имя, Фамилию, Номер и Заметку через пробел: ').split())
    if number == 2:
        View.phonebook_view()
    if number == 3:
        print('Из какого файла импортировать данные? ')
        print('1. XLSX\n2. TXT')
        answer = int_input_checker('Выберите пункт: ')
        if answer == 1:
            Import_xlsx.xlsx_import()
        else:
            Import_txt.txt_import()
    if number == 4:
        print('В каком формате экспортировать данные? ')
        print('1. XLSX\n2. DOCX')
        answer = int_input_checker('Выберите пункт: ')
        if answer == 1:
            Export_xlsx.xlsx_export()
        else:
            Export_docx.docx_export()
    if number == 5:
        Finder.find_finder()
    if number == 6:
        Remover.remover()

choose(int_input_checker('Выберите пункт меню: '))

