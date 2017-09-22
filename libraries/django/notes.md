# Django
## Creating a Project
```sh
django-admin startproject mywebsite
```

## Starting the Server
```sh
python manage.py runserver
```

## Creating an App
```sh
python manage.py startapp music
cd music
vim urls.py
```

### music/urls.py
```python
from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),                  # index/home page for the app
]
```

## Creating a View for the Home Page
### music/views.py
```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>This is the music app home page</h1>")
```

## Handling Requests from the App
### mywebsite/urls.py
```python
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^music/', include('music.urls')),
]
```
Go to `localhost:8000/music`

## Synchronizing the Source Code with the Database
```sh
python manage.py migrate
```

## Create Models for the App
### music/models.py
```python
from django.db import models

class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=300)
    genre = models.CharField(max_length=40)
    album_logo = models.CharField(max_length=1000) 

# each song is linked to an album
class Song(models.Model):
    # whenever the album is deleted, this song is also deleted (CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
```

## Updating the Settings File
### music/apps.py
```python
from django.apps import AppConfig

class MusicConfig(AppConfig):
    name = 'music'
```
### mywebsite/settings.py
```python
# ...
INSTALLED_APPS = [
    'music.apps.MusicConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
# ...
```

### migrate models for the app
```sh
python manage.py makemigrations music
python manage.py migrate
```




























