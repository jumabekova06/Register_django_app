

Первое, что нужно сделать, это cклонировать репозиторий:
```sh
$ git clone https://github.com/jumabekova06/project.git
$ cd project

```

Создайте виртуальную среду для установки зависимостей и активируйте ее:

```sh
$ virtualenv venv
$ source venv/bin/activate
```

Затем установите зависимости:

```sh
(venv)$ pip install -r requirements.txt
```
Запускаем сервер:
```sh

(venv)$ python manage.py runserver
```
навигация для API `http://127.0.0.1:8000/api/v1/register`.



