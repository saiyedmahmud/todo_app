# Generated by Django 4.0.3 on 2022-03-21 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_task_completed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='on_date',
            new_name='created_on',
        ),
    ]
