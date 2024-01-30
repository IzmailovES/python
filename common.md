# venv
create venv:   
```shell
python3 -m venv venvdir
```
activate venv:   
```shell
cd venvdir
source bin/activate
```
deactivate:
```shell
deactivate
```

# pip
list of installed pkgs:
```shell
pip list
```
seach package:   
pip no longer has search function, but we can use pip_search:
```shell
pip install pip_search
python -m pip_search pkg_name
```
install package:
```shell
pip install pkg==version
```

# type annotation
func definition
```python
def somefunc_ret_none_or_int(strvar:str, list_with_int_or_float:list[int|float]) -> None|int :
  pass
```
use in class
```python
class Some:
  strvar : str
  default_none_intvar : int = None
```
typing module
```python
import typing
typing.Any # any value at all
typing.Optional # type or None
typing.Union # union, Union[int,float] ~ int | float
typing.Literal # fixed values, for example user : dict[Literal['name'] | Literal['second_name'] | Literal['username'], str] means dict with fixed three keys and string value
...
```
I can auto generate simple \_\_init\_\_() method with dataclasses.dataclass
```python
fom dataclasses import dataclass
@dataclass
class User:
  id: int
  name: str
  email: str = None
#usage:
user = User(1,'Vasya') # at all
```
where they live?
in \_\_annotations\_\_ attribute in dict

# logging
tooll for logging
```python
import logging

logging.basicConfig(level=logging.DEBUG) ## set log level
# methods:
logging.debug('Это лог уровня DEBUG')
logging.info('Это лог уровня INFO')
logging.warning('Это лог уровня WARNING')
logging.error('Это лог уровня ERROR')
logging.critical('Это лог уровня CRITICAL')
```
```ptyhon
import logging

logger = logging.getLogger(__name__) # create logger with name same as module name
logger.parent # logger always has parent
```
log format
    %(asctime)s - время создания лога в виде, понятном человеку. По умолчанию выглядит так - 2023-12-31 11:29:31,689   
    %(filename)s - имя модуля, в котором сработал вызов лога   
    %(funcName)s - имя функции, в которой произошел вызов лога   
    %(levelname)s - уровень, на котором был вызван данный лог (DEBUG, INFO и т.п.)   
    %(lineno)d - номер строки кода, на которой произошел вызов лога   
    %(name)s - имя логгера   
    %(message)s - сообщение, которое должно быть выведено вместе с логом   

example
```python
import logging

logging.basicConfig(
  level = logging.DEBUG
  format = '[%(asctime)s] #%(levelname)-8s %(filename)s:'
           '%(lineno)d - %(name)s - %(message)s'
}
## or
logging.basicConfig(
    level=logging.DEBUG,
    format='[{asctime}] #{levelname:8} {filename}:'
       '{lineno} - {name} - {message}'
    style = '{'
)

```
## Handlers
You can add handler for your logger to do something when event happens: send email, write to file...
```python
import logging
import sys

# Определяем первый вид форматирования
format_1 = '#%(levelname)-8s [%(asctime)s] - %(filename)s:'\
           '%(lineno)d - %(name)s - %(message)s'
# Определяем второй вид форматирования
format_2 = '[{asctime}] #{levelname:8} {filename}:'\
           '{lineno} - {name} - {message}'

# Инициализируем первый форматтер
formatter_1 = logging.Formatter(fmt=format_1)
# Инициализируем второй форматтер
formatter_2 = logging.Formatter(
    fmt=format_2,
    style='{'
)

# Создаем логгер
logger = logging.getLogger(__name__)

# Инициализируем хэндлер, который будет перенаправлять логи в stderr
stderr_handler = logging.StreamHandler()
# Инициализируем хэндлер, который будет перенаправлять логи в stdout
stdout_handler = logging.StreamHandler(sys.stdout)

file_handler = logging.FileHandler('logs.log', mode = 'a', encodind = 'utf-8')

# Устанавливаем форматтеры для хэндлеров
stderr_handler.setFormatter(formatter_1)
stdout_handler.setFormatter(formatter_2)
file_handler.setFormatter(formatter_1)
# Добавляем хэндлеры логгеру
logger.addHandler(stdout_handler)
logger.addHandler(stderr_handler)
logger.addHandler(file_handler)

# Создаем лог
logger.warning('Это лог с предупреждением!')
```
## logging filters
```python
import logging


# Определяем свой фильтр, наследуюясь от класса Filter библиотеки logging
class ErrorLogFilter(logging.Filter):
    # Переопределяем метод filter, который принимает `self` и `record`
    # Переменная рекорд будет ссылаться на объект класса LogRecord
    def filter(self, record):
        return record.levelname == 'ERROR' and 'важно' in record.msg.lower()


# Инициализируем логгер
logger = logging.getLogger(__name__)

# Создаем хэндлер, который будет направлять логи в stderr
stderr_handler = logging.StreamHandler()

# Подключаем фильтр к хэндлеру
stderr_handler.addFilter(ErrorLogFilter())

# Подключаем хэндлер к логгеру
logger.addHandler(stderr_handler)

logger.warning('Важно! Это лог с предупреждением!')
logger.error('Важно! Это лог с ошибкой!')
logger.info('Важно! Это лог с уровня INFO!')
logger.error('Это лог с ошибкой!')
```
```python
import logging


# Определяем свой фильтр, наследуюясь от класса Filter библиотеки logging
class EvenLogFilter(logging.Filter):
    def filter(self, record):
        return not record.i % 2


# Инициализируем логгер
logger = logging.getLogger(__name__)

# Создаем хэндлер, который будет направлять логи в stderr
stderr_handler = logging.StreamHandler()

# Подключаем фильтр к хэндлеру
stderr_handler.addFilter(EvenLogFilter())

# Подключаем хэндлер к логгеру
logger.addHandler(stderr_handler)

for i in range(1, 5):
    logger.warning('Важно! Это лог с предупреждением! %d', i, extra={'i': i})
```
in exceptions
```python
import logging

logger = logging.getLogger(__name__)

try:
    print(4 / 2)
    print(2 / 0)
except ZeroDivisionError:
    logger.error('Тут было исключение', exc_info=True)
```
```python
import logging

logger = logging.getLogger(__name__)

try:
    print(4 / 2)
    print(2 / 0)
except ZeroDivisionError:
    logger.exception('Тут было исключение')
```

