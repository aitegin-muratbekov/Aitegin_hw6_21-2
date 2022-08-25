import re
def add_names_content():
    with open('MOCK_DATA.txt', 'r', encoding='utf-8') as file:
        content = file.read()
    with open('names.txt', 'w', encoding='utf-8') as file:
        file.write("\n".join(re.findall(r"[A-Z](?:[a-z-']+)\s(?:[A-Z](?:[a-zA-Z-' ]+)|(?:[a-z]+)\s[A-Z](?:[a-z-']+))", content)))