# Generated by Django 4.1.6 on 2023-02-10 20:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HelpModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(1)])),
                ('date', models.DateTimeField(null=True)),
                ('note', models.TextField(max_length=1000)),
            ],
        ),
    ]
