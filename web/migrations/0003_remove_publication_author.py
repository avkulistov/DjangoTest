# Generated by Django 3.0.5 on 2020-04-16 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20200416_1109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publication',
            name='author',
        ),
    ]
