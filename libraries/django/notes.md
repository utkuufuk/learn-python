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

    # equivalent to toString() in Java
    def __str__(self):
        return self.album_title + " - " + self.artist

# each song is linked to an album
class Song(models.Model):
    # whenever the album is deleted, this song is also deleted (CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=150)
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

## Migrating models for the app
```sh
python manage.py makemigrations music
python manage.py migrate
```

## Using the server shell
Run the server shelll
```sh
python manage.py shell
```

Create and insert an object to the database:
```python
from music.models import Album, Song

# create a new album object and save it to the database
a = Album(artist="Taylor Swift", album_title="Red", genre="Country", album_logo="https://github.com/utkuufuk/alpha-beta-chess/blob/master/chess.png")
a.save()

# check the new object's primary key in database
a.id

# retrieve Album objects from database
Album.objects.all()
Album.objects.filter(id=1)
Album.objects.filter(artist__startswith="Taylor")

# exit shell
exit()
```

## Creating an admin user
```sh
python manage.py createsuperuser
```

## Managing databases from admin page
### music/admin.py
```python
from django.contrib import admin
from .models import Album

admin.site.register(Album)
```







<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>



























