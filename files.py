import re

def add_files_content():
    with open('MOCK_DATA.txt', 'r', encoding='utf-8') as file:
        content = file.read()
    with open('files.txt', 'w', encoding='utf-8') as file:
        file.write("\n".join(re.findall(r'(?:[A-Z](?:[a-zA-Z]+)|[A-Z])\.(?:[a-z1-9]{2,4})', content)))
