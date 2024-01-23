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
