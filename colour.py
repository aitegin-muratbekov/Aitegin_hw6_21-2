import re

def add_colour_content():
    with open('MOCK_DATA.txt', 'r', encoding='utf-8') as file:
        content = file.read()
    with open('colour.txt', 'w', encoding='utf-8') as file:
        file.write("\n".join(re.findall(r'#[\w]{6}', content)))

