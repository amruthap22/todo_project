# Generated by Django 5.1.1 on 2024-09-27 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='title_requried',
            new_name='time_requried',
        ),
    ]