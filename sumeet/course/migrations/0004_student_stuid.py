# Generated by Django 5.0.6 on 2024-09-18 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_remove_student_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='stuid',
            field=models.IntegerField(null=True),
        ),
    ]
