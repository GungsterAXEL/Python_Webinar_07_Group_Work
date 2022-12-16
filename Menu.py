from View import phonebook_view
from New_Entry import new_entry_saver

menu = ['1. Добавить новую запись.',
'2. Просмотреть все записи.',
'3. Имортировать из файла.',
'4. Экспортировать в файл.',
'5. Поиск контакта.',
'6. Удаление контакта.']

menu_dict = {1: new_entry_saver(*input('Введите Имя, Фамилию, Номер и Заметку через пробел: ').split()),
             2: phonebook_view(),
             3: import_from_format_choice(),
             4: export_format_choice(),
             5: finding_function(),
             6: deleting_function()}

