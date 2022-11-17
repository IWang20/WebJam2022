from django.db import models

# Create your models here.

class Song(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    region = models.TextField(max_length=20)
    genre = models.TextField(max_length=20)
    duration = models.CharField(max_length=10)
    audio_file = models.FileField(blank=True, null=True)
    image_file = models.ImageField(blank=True, null=True)
    
    paginate = 2 # if you are going to implement next/previous song requests


    def __str__(self):
        return self.title