# Generated by Django 2.2 on 2019-05-28 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pais', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pais',
            old_name='pais',
            new_name='nome',
        ),
    ]
