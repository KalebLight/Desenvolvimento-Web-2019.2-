# Generated by Django 2.2.5 on 2019-12-08 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_notes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Notes',
            new_name='Note',
        ),
    ]
