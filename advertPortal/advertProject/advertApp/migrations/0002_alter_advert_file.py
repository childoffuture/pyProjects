# Generated by Django 4.0.1 on 2022-02-05 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='file',
            field=models.FileField(blank=True, upload_to='uploads/'),
        ),
    ]
