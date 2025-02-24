from django.db import models

class index1(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class index2(models.Model):
    home = models.CharField(max_length=100)
    about = models.CharField(max_length=100)
    service = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)

    def __str__(self):
        return self.home

