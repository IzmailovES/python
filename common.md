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


