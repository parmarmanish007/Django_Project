# Generated by Django 3.2.3 on 2022-01-05 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hadmin', '0020_remove_contact1_contacts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='area_id',
        ),
    ]
