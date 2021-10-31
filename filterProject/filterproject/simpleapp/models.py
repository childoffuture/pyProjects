from django.db import models

class News(models.Model):
    title = models.CharField(max_length=128, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

