# Generated by Django 3.2.8 on 2021-11-28 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20211122_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
