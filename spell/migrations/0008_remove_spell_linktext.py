# Generated by Django 3.0.3 on 2020-02-19 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spell', '0007_auto_20200219_1826'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spell',
            name='linktext',
        ),
    ]
