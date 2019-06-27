# Generated by Django 2.2 on 2019-05-28 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estado', '0002_auto_20190528_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estado',
            name='nome',
            field=models.CharField(max_length=200, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='estado',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pais.Pais', verbose_name='País'),
        ),
    ]
