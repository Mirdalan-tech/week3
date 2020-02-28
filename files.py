"""
Задание
Скачайте файл по ссылке
Прочитайте содержимое файла в переменную, подсчитайте длину получившейся строки
Подсчитайте количество слов в тексте
Замените точки в тексте на восклицательные знаки
Сохраните результат в файл referat2.txt
"""

with open('referat.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print('"Длина строки":', len(content))
    print('Количество слов в тексте:', (len(content.split())))
    referat2 = (content.replace('.', '!'))
    new_file = open("referat2.txt", "w")
    new_file.write(referat2)
    new_file.close()



    
