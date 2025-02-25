from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()


    def  __str__(self):
        return f'{self.pk} - {self.title}'


class Area(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField()


    def __str__(self):
        return f'{self.name}'