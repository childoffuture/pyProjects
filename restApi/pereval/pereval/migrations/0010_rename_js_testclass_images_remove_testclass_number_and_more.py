# Generated by Django 4.0.2 on 2022-02-28 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pereval', '0009_testclass_js'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testclass',
            old_name='js',
            new_name='images',
        ),
        migrations.RemoveField(
            model_name='testclass',
            name='number',
        ),
        migrations.RemoveField(
            model_name='testclass',
            name='title',
        ),
        migrations.AddField(
            model_name='testclass',
            name='date_added',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='testclass',
            name='raw_data',
            field=models.JSONField(blank=True, default={}),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testclass',
            name='status',
            field=models.TextField(default='new', max_length=20),
        ),
    ]
