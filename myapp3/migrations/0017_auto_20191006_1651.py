# Generated by Django 2.1.7 on 2019-10-06 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp3', '0016_auto_20191006_1124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentmarksheetdata',
            name='degree',
        ),
        migrations.RemoveField(
            model_name='studentmarksheetdata',
            name='gender',
        ),
        migrations.AlterField(
            model_name='studentmarksheetdata',
            name='branch_cse',
            field=models.CharField(default='', max_length=100, null=True),
        ),
    ]