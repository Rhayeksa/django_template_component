# Django Template Component

Project yang akan digunakan sebagai template ketika pembuatan project web app dan rest api menggunakan Django framework

## Teknologi

- Python 3.11.7
- Python 3.11.7-venv
- Django 5.0.1
- db.sqlite3

## Konsep maintenance project

```
MVC - Web
Model => apps.app_name.models.model_name
View => template
Controller => apps.app_name.views.view_name && (apps.app_name.urls.py && core.urls.py)
```

```
MVC - API
Model => apps.app_name.models.model_name
Controller => apps.app_name.views.view_name && (apps.app_name.urls.py && core.urls.py)
```

## Membuat Project Dan Virtual Env

```console
mkdir my_first_django_project && # membuat project folder
cd ./my_first_django_project # masuk directory folder
```

```console
python3.11 -m venv .venv && # membuat virtual env
. ./.venv/bin/active && # masuk ke mode virtual env
pip install --upgrade pip && # upgrade version package manager pada virtual env
```

membuat file requirements.txt

```console
printf \
"\
Django==5.0.1 # Framewok Python dalam pembuatan Web dan API\
\ndjangorestframework==3.14.0 # Library untuk development API\
\nmarkdown==3.5.2 # Markdown support for the browsable API.\
\ndjango-filter==23.5 # Filtering support\
\nautopep8==2.0.4 # Drive untuk merapikan format kode(coding)\
\nPillow==10.2.0 # Drive untuk management Images\
\n\
"\
> requirements.txt
```

```console
pip install -r ./requirements.txt # install driver dan library pada virtual env
```

```console
python ./manage.py startproject core . # membuat core project
```

## Membuat App Dan mendaftarkannya pada setting.py

```console
mkdir apps && # membuat folder apps sebagai package apps, jika belum ada
cd ./apps/ &&
python ./manage.py startapp my_apps && # membuat app
cd ../
```

Tambahkan apps pada file ./apps/my_apps/apps.py

```python
from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.my_apps' # Here
    label = "my_apps"

```

Daftarkan apps pada file ./core/settings.py

```python
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "apps.my_apps", # Here
]

```

## Membuat templates Dan mendaftarkannya pada setting.py

```console
mkdir templates && # membuat folder templates sebagai package templates, jika belum ada
```

struktur folder pada templates

```
...
templates
|--- components
|    |--- navbar.html
|    |--- card.html
|    |--- icon_1.html
|    |--- icon_2.html
|    |--- icon_3.html
|--- pages
|    |--- auth
|    |    |--- login.html
|    |    |--- register.html
|    |--- page1
|    |    |--- detail_by_id.html
|    |    |--- index.html
|    |    |--- insert.html
|    |    |--- update_by_id.html
|    |    |--- update_many_data_by_id_selected.html
|    |--- home.html
|--- 404.html
|--- 500.html
|--- base.html
...
```

## Membuat Model pada Django dan Table pada Database

```
...
apps
|--- app_name
    |--- admin.py
    |--- models
         |--- model_1.py
    ...
...
```

admin.py digunakan untuk mendaftarkan model yang nanti akan jadi table pada database

models digunakan sebagai package dari model-model

```python
#table1.py
from django.db import models


class Table1(models.Model):
    GENDER = (
        ("Pria", "Pria"),
        ("Wanita", "Wanita"),
    )

    char_field = models.CharField(max_length=45)
    email_field = models.EmailField(max_length=225, unique=True)
    choice_field = models.CharField(max_length=9, choices=GENDER)
    text_field = models.TextField(null=True, blank=True)

    class Meta:
        db_table = "table_1"

```

```python
#admin.py
from django.contrib import admin

from .models.table1 import Table1

# Register your models here.
admin.site.register(Table1)

```

## Membuat view dan mendaftarkannya pada urls sebagai controller pada konsep MVC

```
...
apps
|--- app_name
    |--- forms
    |    |--- form_1.py
    |--- views
    |    |--- view_1
    |         |--- get_all.py
    |         |--- get_by_id.py
    |         |--- insert_many.py
    |         |--- insert_one.py
    |         |--- update_by_id.py
    |         |--- update_many_by_id.py
    |         |--- delete_by_id.py
    |         |--- delete_many_by_id.py
    |--- urls.py
    ...
core
|--- urls.py
    ...
template
|--- pages
     |--- pages_1
          |--- get_all.html
          |--- get_by_id.html
          |--- insert_many.html
          |--- insert_one.html
          |--- update_by_id.html
          |--- update_many_by_id_selected.html
    ...
...
```

folder apps.app_name.forms merupakan package dari kumpulan form dan akan digunakan pada apps.app_name.views sebagai object pada saat insert dan update

forlder apps.app_name.views merupakan package dari kumpulan view dan digunakan sebagai logic querying data dan tempat penyimpanan variable dan tempat me-managemen html

urls.py merupakan file peng-combine apps.app_name.views dan path url pada browser. Dan selanjutnya di daftarkan juga ke urls.py utama pada core.urls.py

template merupakan package folder untuk file2 html dan tempat penerapan variable dari apps.app_name.views

## ORM vs Raw Query

### ORM

```
apps
|--- app_name
    |--- forms    # digunakan sebagai attribute html dari field input, seperti class dll
    |--- models   # digunakan sebagai object model
    |--- views    # digunakan sebagai aplikator logic crud
    |--- urls.py  # digunakan sebagai controller penghubung views dan template
template
|--- page         # digunakan sebagai package html
...
```

### Raw Query

```
apps
|--- app_name
    |--- views    # digunakan sebagai aplikator logic crud
    |--- urls.py  # digunakan sebagai controller penghubung views dan template
template
|--- page         # digunakan sebagai package html
...
```

## API Django menggunakan Django REST framework

### directory

```
apps
|--- api
    |--- views    # digunakan sebagai aplikator logic crud dan response Jsons
    |--- urls.py  # digunakan sebagai controller path url ketika di request http
...
```

### register app to setting

```python
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "rest_framework", # here
    "apps.api",
    "apps.web",
]
```

## deploy image to openshift sandbox

rhayeksa/dockerhubx:dtc
username/image_name:tag

## create project/repo di gitlab

## Docker

### membuat project menjadi image
```

```