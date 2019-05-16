# Generated by Django 2.2 on 2019-05-16 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logradouro', '0001_initial'),
        ('estado', '0001_initial'),
        ('endereco', '0005_auto_20190516_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='endereco',
            name='estado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='estado.Estado', verbose_name='estado'),
        ),
        migrations.AddField(
            model_name='endereco',
            name='logradouro',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='logradouro.Logradouro', verbose_name='logradouro'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='numero',
            field=models.IntegerField(verbose_name='numero'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pais.Pais', verbose_name='pais'),
        ),
    ]
