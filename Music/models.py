from django.db import models
from django.urls import reverse


class Albums(models.Model):
    artist = models.CharField(max_length=200)
    album_title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()

    def get_absolute_url(self):
        return reverse('Music:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.album_title + ' - ' + self.artist


class Playlist(models.Model):





class Song(models.Model):
    album = models.ForeignKey(Albums, on_delete=models.CASCADE)
    file_key = models.CharField(max_length=100)
    song_title = models.CharField(max_length=250)


    def __str__(self):
        return self.song_title
