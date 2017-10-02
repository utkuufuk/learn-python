from django.db import models

class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=300)
    genre = models.CharField(max_length=40)
    album_logo = models.CharField(max_length=1000) 

    def __str__(self):
        return self.album_title + " - " + self.artist

# each song is linked to an album
class Song(models.Model):
    # whenever the album is deleted, this song is also deleted (CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=150)
