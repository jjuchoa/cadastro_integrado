# Generated by Django 2.2 on 2019-05-16 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NomeLogradouro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeLogradouro', models.CharField(max_length=200, verbose_name='Nome do logradouro')),
            ],
        ),
    ]