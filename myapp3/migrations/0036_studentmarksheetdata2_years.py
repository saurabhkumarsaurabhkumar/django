# Generated by Django 2.1.7 on 2019-10-12 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp3', '0035_auto_20191012_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentmarksheetdata2',
            name='years',
            field=models.IntegerField(choices=[(1, '2016-2020'), (2, '2017-2021'), (3, '2018-2024'), (4, '2019-2025')], default='1'),
        ),
    ]
