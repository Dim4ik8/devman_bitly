# Программа для работы с короткими ссылками
___
## Данный скрипт умеет делать следующее:
- создавать короткие ссылки (bitlink) из обычных
- подчситывать количество кликов по bitlink
- проверять, является ли ссылка bitlink или нет
___
## Необходимые для установки библиотеки
```angular2html
requests==2.28.1
python-dotenv==0.21.0
```
___
## Запуск скрипта
> python main.py
___
## Пример работы скрипта 
Скрипт при попытке создания bitlink из ссылки (на примере http://mail.ru) выдает JSON файл с различными ключами, одним из которых (link) и является короткая ссылка.
```angular2html
{'archived': False,
 'created_at': '2022-09-25T10:58:03+0000',
 'custom_bitlinks': [],
 'deeplinks': [],
 'id': 'bit.ly/3rp1TcV',
 'link': 'https://bit.ly/3rp1TcV',
 'long_url': 'http://mail.ru/',
 'references': {'group': 'https://api-ssl.bitly.com/v4/groups/Bm9p9XyRAWV'},
 'tags': []}

```