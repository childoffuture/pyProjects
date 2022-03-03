from django.db import models


class PerevalAreas(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_parent = models.BigIntegerField()
    title = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'pereval_areas'


class PerevalImages(models.Model):
    date_added = models.DateTimeField(blank=True, null=True)
    img = models.BinaryField()

    class Meta:
        db_table = 'pereval_images'


class Pereval(models.Model):
    date_added = models.DateTimeField(blank=True, null=True)
    raw_data = models.JSONField(blank=True)
    images = models.JSONField(blank=True)
    status = models.TextField(max_length=20, default='new')

    class Meta:
        db_table = 'pereval_added'
