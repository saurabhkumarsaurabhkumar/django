# Generated by Django 2.1.7 on 2019-10-05 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp3', '0005_studentmarksheetdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentmarksheetdata',
            name='degree',
            field=models.CharField(default='0000000', max_length=30, unique=True),
        ),
        migrations.AddField(
            model_name='studentmarksheetdata',
            name='gender',
            field=models.CharField(default='0000000', max_length=30, unique=True),
        ),
    ]
