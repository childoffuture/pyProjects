from django.db import models


class PerevalAdded(models.Model):
    date_added = models.DateTimeField(blank=True, null=True)
    raw_data = models.TextField(blank=True, null=True)  # This field type is a guess.
    images = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        db_table = 'pereval_added'


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