# Generated by Django 2.1.7 on 2019-10-11 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp3', '0022_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='subject_title',
            field=models.CharField(choices=[(1, 'graph_theor'), (2, 'autometa_theor'), (3, 'data_minin'), (4, 'ds'), (5, 'networkin'), (6, 'computer_graphic')], default='1', max_length=100),
        ),
    ]