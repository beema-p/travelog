from django.db import models


# Create your models here.
class Place(models.Model):
    nam = models.CharField(max_length=150)
    img = models.ImageField(upload_to='gallery')
    desc = models.TextField()

    def __str__(self):
        return self.nam


class People(models.Model):
    name = models.CharField(max_length=100)
    imag = models.ImageField(upload_to='pics')
    des = models.TextField()

    def __str__(self):
        return self.name
