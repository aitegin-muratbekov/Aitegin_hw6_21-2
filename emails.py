import re

def add_emails_content():
    with open('MOCK_DATA.txt', 'r', encoding='utf-8') as file:
        content = file.read()
    with open('emails.txt', 'w', encoding='utf-8') as file:
        file.write("\n".join(re.findall(r'\b[a-z@0-9-]+\.(?:(?:[a-z]{1,3}\.[a-z]{2})|[a-z]+)', content)))