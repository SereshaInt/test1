### Cоздать скрипт, который через параметр запуска получает имя исполняемого файла
### И запускает этот файл через библиотеку subprocess
### Обработку ошибок сделать через исключения

from sys import argv
import subprocess as s

if len(argv) == 1:
    print('Скрипт запущен без параметров')
else:
    try:
        s.run(argv[1])
    except FileNotFoundError:
        print("Файл не найден")
    except PermissionError:
        print("Недостаточно прав для запуска")
    except Exception as err:
        print("Ошибка: ", err)

### Написать функцию, которая распечатает все файлы в каталоге
### В функцию добавить вывод отладочной информации через библиотеку logging
### Указать, какой каталог обрабатывается и сколько файлов в каталоге было распечатано

import logging as l, os, sys

#l.basicConfig(stream=sys.stdout, level=l.DEBUG)

def myDir1(path):
    if os.path.isdir(path):
        d = os.listdir(path)
        l.debug('path: {}'.format(path))
        l.debug('count: {}'.format(len(d)))
        print("Список файлов: {}".format(d))
    else: print("неверный путь")
    return

myDir1("c:/123456")

### Создать функцию, которая в фоновом потоке скачает содержимое сайта https://epam.com, сохранить в файл

import subprocess as s, requests, threading

def saveURL(url, filename):
    try:
        u = requests.get(url)
        if u.status_code == 200:
            with open(filename, 'w', encoding="utf-8") as f:
                f.write(u.text)
            print("Данные сохранены")
        else: print("Ошибка, код {}".format(u.status_code))
    except Exception as err:
        print("Ошибка: ", err)

a = threading.Thread(target=saveURL, args=("https://epam.com", "c:/1.txt",))
a.daemon = True
a.start()
print(100500)

saveURL("https://epam.com", "c:/11.txt")