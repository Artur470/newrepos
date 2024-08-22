from django.db import models




class Blog(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()