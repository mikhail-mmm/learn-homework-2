"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    file_name = 'referat.txt'
    with open(file_name, 'r', encoding='utf-8') as f:
        text_from_file = f.read()
    print(len(text_from_file))
    words_list = text_from_file.split(' ')
    print(len(words_list))
    text_in_file = text_from_file.replace('.', '!')
    with open('referat2.txt', 'w', encoding='utf-8') as f2:
        f2.write(text_in_file)
    
if __name__ == "__main__":
    main()
    