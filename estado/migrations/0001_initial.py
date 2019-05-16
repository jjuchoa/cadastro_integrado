# Generated by Django 2.2 on 2019-05-16 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pais', '0004_pais'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=200, verbose_name='estado')),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pais.Pais', verbose_name='pais')),
            ],
        ),
    ]
