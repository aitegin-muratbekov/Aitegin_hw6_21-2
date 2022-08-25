import re
from colour import add_colour_content
from files import add_files_content
from emails import add_emails_content
from names import add_names_content


while True:
    funct = input('Эта программа парсит файл MOCK_DATA.TXT \n '
                  'выберите что вы хотите извлечь и введите число(1,5)\n'
                  '1: name and surname \n'
                  '2: email\n'
                  '3: files\n'
                  '4 color\n'
                  '5 выйти     ')

    if funct == '1':
        add_names_content()
    elif funct == '2':
        add_emails_content()
    elif funct == '3':
        add_files_content()
    elif funct == '4':
        add_colour_content()
    elif funct == '5':
        print('Программа завершена')
        break
    print("Успешно добавлено в файл")










