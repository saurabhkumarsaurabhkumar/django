# Generated by Django 2.1.7 on 2019-10-12 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp3', '0027_code_grade_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='code',
            name='roll_no',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='code',
            name='student_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
