from View import phonebook_view
from New_Entry import new_entry_saver

menu = ['1. �������� ����� ������.',
'2. ����������� ��� ������.',
'3. ������������ �� �����.',
'4. �������������� � ����.',
'5. ����� ��������.',
'6. �������� ��������.']

menu_dict = {1: new_entry_saver(*input('������� ���, �������, ����� � ������� ����� ������: ').split()),
             2: phonebook_view(),
             3: import_from_format_choice(),
             4: export_format_choice(),
             5: finding_function(),
             6: deleting_function()}

