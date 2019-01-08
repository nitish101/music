from django.db import models

class Albums(models.Model):
    artist = models.CharField(max_length=200)
    album_title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.album_title + ' - ' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Albums, on_delete=models.CASCADE)
    file_key = models.CharField(max_length=100)
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title
