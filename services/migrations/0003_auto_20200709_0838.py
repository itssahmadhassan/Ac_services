# Generated by Django 3.0.7 on 2020-07-09 03:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20200708_2337'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='massage',
            new_name='message',
        ),
    ]
