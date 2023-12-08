def find_paragraphs(file_path, word):
    with open(file_path, 'r', encoding = 'utf-8') as file:
        content = file.read()
        paragraphs = content.split('\n\n')
        find = False
        for paragraph in paragraphs:
            lower_paragraph = paragraph.lower()
            if word in lower_paragraph:
                print(paragraph)
                find = True
        if not find:
            print('Такого слова в тексті немає, спроубуйте пошукати інше слово.')

while True:
    word = input('Введіть слово для пошуку: ')
    find_paragraphs('text.txt', word)
    if input('Продовжити пошук? (так/ні) ').lower() == 'ні':
        break
