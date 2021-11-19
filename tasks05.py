### Скачать содержимое https://epam.com, посчитать кол-во тэгов div
from bs4 import BeautifulSoup
import requests

u = requests.get('https://epam.com', stream=True)
if u.status_code == requests.codes.ok:
    soup = BeautifulSoup (u.text, 'html.parser')
    print('кол-во div =', len(soup.find_all('div')))

### Базы данных
### sqlite, создать таблицу с 2мя столбцами (номер и имя)
### добавить 3 строки, получить их и распечатать

import sqlite3

conn = sqlite3.connect(':memory:')
conn.execute('CREATE TABLE table1(number int, name text)')
conn.execute('INSERT INTO table1(number, name) SELECT 1, "row 1"')
conn.execute('INSERT INTO table1(number, name) SELECT 2, "row 2"')
conn.commit()

c = conn.execute('SELECT number, name FROM table1')
#print(c.fetchall())
for r in c:
    print(r)

conn.close()
