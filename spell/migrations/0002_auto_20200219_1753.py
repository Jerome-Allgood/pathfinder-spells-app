# Generated by Django 3.0.3 on 2020-02-19 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spell', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spell',
            old_name='subcshools',
            new_name='subcshool',
        ),
    ]
