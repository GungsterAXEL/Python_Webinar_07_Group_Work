import Menu
import Add
import Import
import Export_xlsx
import View
import Print_Format

number = Menu.menu_choice()

def choose(number):
    if number == 1:
        Add.new_entry_saver()
    if number == 2:
        View.phonebook_view()
    if number == 3:
        Import.read_import_file()
    if number == 4:
        Export_xlsx.xlsx_export()
    if number == 5:
        Print_Format.find_finder()

choose()
