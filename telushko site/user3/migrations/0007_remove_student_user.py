# Generated by Django 3.2.3 on 2021-12-03 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_student_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='user',
        ),
    ]
