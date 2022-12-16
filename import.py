
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