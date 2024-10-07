# argparse
Прасер аргументов командной строки
#
```
import argparse

parser = argparse.ArgumentParser(description="Some description")
parser.add_argument(...)
parser.add_argument(....)
parser.add_argument(......)

args = parser.parse_args()
```
## Парсинг аргументов
```
parser.add_argument('-a',       # короткий именованный аргумент 
                    '--aaaa',   # длинный именованный аргумент
                    'aaaaa'     # позиционный аргумент
                    help=,      # подпись для хелпа
                    dest=,      # имя поля объекта
                    type=,      # тип (для преобразования из сторки)
                    action=,    # 'store'(по умолчанию), 'store_true/false' - собирается флаг, 'append' - список, 'count' - подсчет вхождения
                    default=,   # значение по умолчанию
                    choices=,   # значения из списка
                    nargs = ,   # сколько аргументов может быть передано. '?', '*', '+' - как в регулярках
                    required,   # необходимость аргумента
)
```
## Взаимоисключающие аргументы



