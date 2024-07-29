# tree-menu
 Django приложение для создания древовидного меню.
# tree-menu-django

--- 

### Описание
Приложение Django, в котором с помощью tamplate tag 
реализовано древовидное меню, редактируемое в админке Django. Меню по 
названию можно отрисовать на любой странице Приложения, 
используя следующие теги:
```
{% load draw_menu %}
{% draw_menu 'main_menu' %}
```


### Запуск проекта
Для Windows:

```shell
git clone https://github.com/pasha-danilevich/tree-menu.git
python -m venv venv
venv/Scripts/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
```

Для корректной работы приложения необходимо:
 * создать суперпользователя
```shell
python manage.py createsuperuser
```
 * либо войти в админ панель: admin - 1234
 * создать меню и его элементы через административную панель.

Запустить сервер разработки
```shell
python manage.py runserver
```