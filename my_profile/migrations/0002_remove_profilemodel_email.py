# Generated by Django 4.1.1 on 2022-11-21 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_profile', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilemodel',
            name='email',
        ),
    ]
