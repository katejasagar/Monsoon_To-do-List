# Generated by Django 3.2.9 on 2021-12-04 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0002_alter_todo_list_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo_list',
            name='description',
        ),
    ]
