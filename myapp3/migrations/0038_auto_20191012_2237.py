# Generated by Django 2.1.7 on 2019-10-12 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp3', '0037_studentmarksheetdata2_degree_of_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmarksheetdata2',
            name='code_title',
            field=models.IntegerField(choices=[(1, 'CS962'), (2, 'CS302'), (3, 'CS303'), (4, 'CS903'), (5, 'CS301'), (6, 'CS304')], default='1'),
        ),
    ]