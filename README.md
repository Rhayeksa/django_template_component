# Django Template Component

Project yang akan digunakan sebagai template ketika pembuatan project web app dan rest api menggunakan Django framework

## Teknologi

- Python 3.11.7
- Python 3.11.7-venv
- Django 5.0.1
- db.sqlite3

## Membuat Project Dan Virtual Env

```console
mkdir my_first_django_project && # membuat project folder
cd ./my_first_django_project # masuk directory folder
```

```console
python3.11 -m venv .venv && # membuat virtual env
. ./.venv/bin/active && # masuk ke mode virtual env
pip install --upgrade pip && # upgrade version package manager pada virtual env
pip install -r ./requirements.txt # masuk ke mode virtual env
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
    label = "api"

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
```
