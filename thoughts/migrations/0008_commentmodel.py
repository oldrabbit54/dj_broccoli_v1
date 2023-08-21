# Generated by Django 4.1.6 on 2023-02-20 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_profile', '0011_alter_profilemodel_date'),
        ('thoughts', '0007_alter_notemodel_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=200)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='authors', to='my_profile.profilemodel')),
                ('note', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='notes', to='thoughts.notemodel')),
            ],
        ),
    ]
