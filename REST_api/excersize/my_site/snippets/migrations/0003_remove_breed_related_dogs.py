# Generated by Django 3.1.1 on 2020-10-10 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_breed_related_dogs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='breed',
            name='related_dogs',
        ),
    ]
