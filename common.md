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

``


